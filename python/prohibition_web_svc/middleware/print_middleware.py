import asyncio
import base64
import copy
import json
import re
from pathlib import Path
from flask import Response
from jinja2 import Environment, FileSystemLoader, select_autoescape
from playwright.async_api import async_playwright
from python.common.enums import ErrorCode
from python.common.logging_utils import get_logger
from python.prohibition_web_svc.middleware import common_middleware
from python.prohibition_web_svc.middleware import collision_middleware
from python.prohibition_web_svc.models.print_request_payload import PrintRequestPayload

logger = get_logger(__name__)

EVENT_TYPE = 'Print - Document Render'

def set_event_type(**kwargs) -> tuple:
    """Set the event type for the print event."""
    logger.verbose('inside set_event_type()')
    kwargs['event_type'] = EVENT_TYPE
    return True, kwargs


def validate_print_payload(**kwargs) -> tuple:
    """Validate the print request payload using PrintRequestPayload model."""
    logger.verbose("inside validate_print_payload()")
    
    request = kwargs.get('request')
    if not request:
        kwargs['error'] = {
            'error_code': ErrorCode.P01,
            'error_details': "No request object found",
            'event_type': EVENT_TYPE,
            'func': validate_print_payload,
        }
        return False, kwargs

    try:
        # Get the JSON payload from the request
        if request.is_json:
            payload = request.get_json()
        else:
            payload = json.loads(request.data.decode('utf-8'))
        
        # Validate using PrintRequestPayload structure
        if not isinstance(payload, dict):
            raise ValueError("Payload must be a JSON object")
            
        # Validate required fields based on PrintRequestPayload model
        if 'template' not in payload or not payload['template']:
            logger.warning("validation error: missing or empty template")
            kwargs['error'] = {
                'error_code': ErrorCode.P01,
                'error_details': "Missing required field: template",
                'event_type': EVENT_TYPE,
                'func': validate_print_payload,
            }
            return False, kwargs
        
        if 'data' not in payload or not payload['data']:
            logger.warning("validation error: missing or empty data")
            kwargs['error'] = {
                'error_code': ErrorCode.P01,
                'error_details': "Missing required field: data",
                'event_type': EVENT_TYPE,
                'func': validate_print_payload,
            }
            return False, kwargs
        
        # Validate data field is a dictionary
        if not isinstance(payload['data'], dict):
            kwargs['error'] = {
                'error_code': ErrorCode.P01,
                'error_details': "Field 'data' must be an object",
                'event_type': EVENT_TYPE,
                'func': validate_print_payload,
            }
            return False, kwargs
        
        # Validate options if present
        if 'options' in payload and not isinstance(payload['options'], dict):
            kwargs['error'] = {
                'error_code': ErrorCode.P01,
                'error_details': "Field 'options' must be an object",
                'event_type': EVENT_TYPE,
                'func': validate_print_payload,
            }
            return False, kwargs
        
        validated_payload: PrintRequestPayload = payload
        kwargs['payload'] = validated_payload
        
        logger.verbose("payload validation successful")
        return True, kwargs
        
    except Exception as e:
        logger.error(e)
        kwargs['error'] = {
            'error_code': ErrorCode.P01,
            'error_details': f"Invalid JSON payload: {str(e)}",
            'event_type': EVENT_TYPE,
            'func': validate_print_payload,
        }
        return False, kwargs

async def render_with_playwright_async(template_path: str, data: dict, output_type: str = "pdf"):
    """Render the Jinja template using Playwright."""
    template_dir = str(Path(template_path).parent) or "."
    template_name = Path(template_path).name

    try:
        # Render the template with Jinja2
        env = Environment(
            loader=FileSystemLoader(template_dir),
            autoescape=select_autoescape(["html", "xml"]),
            trim_blocks=True,
            lstrip_blocks=True,
        )
        tpl = env.get_template(template_name)
        template_data = {**data, 'output_type': output_type}
        html_str = tpl.render(data=template_data)
        
        # Convert relative image paths to base64 data URLs for Playwright
        
        def replace_image_src(match):
            src = match.group(1)
            if not src.startswith(('http://', 'https://', 'data:', 'file://')):
                # Handle relative paths
                image_path = Path(template_dir) / src
                if image_path.exists():
                    try:
                        with open(image_path, 'rb') as img_file:
                            img_data = img_file.read()
                            img_base64 = base64.b64encode(img_data).decode('utf-8')
                            # Determine MIME type based on file extension
                            ext = image_path.suffix.lower()
                            mime_type = {
                                '.png': 'image/png',
                                '.jpg': 'image/jpeg', 
                                '.jpeg': 'image/jpeg',
                                '.gif': 'image/gif',
                                '.svg': 'image/svg+xml'
                            }.get(ext, 'image/png')
                            return f'src="data:{mime_type};base64,{img_base64}"'
                    except Exception as e:
                        print(f"Warning: Could not load image {image_path}: {e}")
                        return match.group(0)  # Return original if failed
            return match.group(0)  # Return original for absolute URLs
        
        # Replace image src attributes
        html_str = re.sub(r'src="([^"]*)"', replace_image_src, html_str)

        # Use Playwright to process HTML
        async with async_playwright() as p:
            browser = await p.chromium.launch(
                headless=True,
                args=["--disable-dev-shm-usage"]
            )
            
            try:
                page = await browser.new_page()
                await page.set_content(html_str, wait_until="networkidle")
                
                if output_type.lower() == "html":
                    final_html = await page.content()
                    return final_html
                else:
                    # Set explicit page dimensions to US Letter (8.5in x 11in) with 0.5in margins on sides, 0.75in top/bottom
                    # This gives a content area of 7.5in x 9.5in
                    await page.set_viewport_size({"width": 816, "height": 1056})  # 8.5in x 11in at 96 DPI
                    
                    # Build dynamic header configuration
                    form_details = template_data.get('form_details')
                    header = {
                        'form_no': form_details.get('form_no', ''),
                        'form_title': form_details.get('form_title', ''),
                        'subtext': form_details.get('subtext', '')
                    }
                    
                    # Create dynamic header template
                    header_template = f"""
                        <div style="display: flex; justify-content: space-between; width: 100%; padding: 10px 20px; font-family: Arial, sans-serif;">
                            <span style="font-size: 11pt; font-weight: bold;">{header['form_title']}{' - ' + header['form_no'] if header['form_no'] else ''}</span>
                            <span style="font-size: 9pt; font-weight: bold;">{header['subtext']}</span>
                        </div>
                    """
                    
                    # Build dynamic footer configuration MV6020E (122025)
                    footer = {
                        'form_version': form_details.get('form_version', '')
                    }
                    
                    # Create dynamic footer template
                    footer_template = f"""
                        <div style="display: flex; justify-content: space-between; width: 100%; padding: 5px 20px; font-family: Arial, sans-serif; font-size: 8pt;">
                            <span>{footer['form_version']}</span>
                            <span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span>
                        </div>
                    """
                    
                    pdf_bytes = await page.pdf(
                        width="8.5in",
                        height="11in",
                        print_background=True,
                        display_header_footer=True,
                        header_template=header_template,
                        footer_template=footer_template,
                        prefer_css_page_size=False,
                    )
                    return pdf_bytes
                
            finally:
                await browser.close()
                    
    except Exception as e:
        error_html = f"<h1>Error rendering template with Playwright</h1><p>{str(e)}</p>"
        if output_type.lower() == "html":
            return error_html
        else:
            return error_html.encode('utf-8')

def render_with_playwright(template_path: str, data: dict, output_type: str = "pdf"):
    """Synchronous wrapper for the async Playwright render function."""
    return asyncio.run(render_with_playwright_async(template_path, data, output_type))

def render_document_with_playwright(**kwargs) -> tuple:
    """Render document using Playwright and store result in kwargs."""
    logger.verbose('inside render_document_with_playwright()')
    
    try:
        payload = kwargs.get('payload', {})
        template_name = payload.get('template')
        data = payload.get('data')
        options = payload.get('options', {})
        output_type = options.get('type', 'pdf').lower()
        
        # Check if template exists in templates folder
        # Get the absolute path to the templates directory
        current_dir = Path(__file__).parent.parent  # Go up to prohibition_web_svc directory
        template_path = current_dir / "templates" / template_name
        if not template_path.exists():
            kwargs['error'] = {
                'error_code': ErrorCode.P01,
                'error_details': f"Template '{template_name}' not found in templates folder",
                'event_type': EVENT_TYPE,
                'func': render_document_with_playwright,
            }
            return False, kwargs
        
        # Render the document
        content = render_with_playwright(str(template_path), data, output_type)
        
        kwargs['rendered_content'] = content
        kwargs['content_type'] = 'text/html' if output_type == 'html' else 'application/pdf'
        kwargs['filename'] = options.get('filename', 
            template_name.replace('.html', '.pdf' if output_type == 'pdf' else '.html'))
        
        return True, kwargs
        
    except Exception as e:
        logger.error(e)
        kwargs['error'] = {
            'error_code': ErrorCode.P02,
            'error_details': str(e),
            'event_type': EVENT_TYPE,
            'func': render_document_with_playwright,
        }
        return False, kwargs

def return_rendered_response(**kwargs) -> tuple:
    """Return the rendered content as Flask Response."""
    logger.verbose('inside return_rendered_response()')
    
    try:
        content = kwargs.get('rendered_content')
        content_type = kwargs.get('content_type', 'application/pdf')
        filename = kwargs.get('filename', 'document.pdf')
        
        response = Response(
            content,
            mimetype=content_type,
            headers={
                'Content-Disposition': f'inline; filename={filename}',
                'Content-Type': content_type + ('; charset=utf-8' if content_type == 'text/html' else '')
            }
        )
        
        kwargs['response'] = response
        return True, kwargs
        
    except Exception as e:
        logger.error(e)
        kwargs['error'] = {
            'error_code': ErrorCode.P02,
            'error_details': str(e),
            'event_type': EVENT_TYPE,
            'func': return_rendered_response,
        }
        return False, kwargs


def log_payload_to_splunk(**kwargs) -> tuple:
    try:
        request = kwargs.get('request')
        payload = request.get_json()
        payload = copy.deepcopy(payload)
        payload_masked = collision_middleware.mask_sensitive_data(payload)
        kwargs['splunk_data'] = {
            'event': 'print request received',
            'request_id': kwargs.get('request_id', ''),
            'user_guid': kwargs.get('user_guid', ''),
            'username': kwargs.get('username', ''),
            'payload': payload_masked
        }
    except Exception as e:
        logger.error(e)
    return True, kwargs