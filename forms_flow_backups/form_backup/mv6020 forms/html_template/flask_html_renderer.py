"""
Flask service to render MV6020 HTML content without PDF generation.
- Serves the rendered HTML directly at /api/render endpoint
- Uses the same Playwright-based rendering logic as the PDF renderer
- Ensures HTML is processed exactly the same way as before PDF generation

Requirements:
    pip install flask jinja2 playwright
    playwright install chromium

Run:
    python flask_html_renderer.py
    
Then visit: http://localhost:5000/api/render
"""

import asyncio
from flask import Flask, request, jsonify, send_file, Response
from flask_cors import CORS
import asyncio
import os
from pathlib import Path
import json
from jinja2 import Environment, FileSystemLoader, select_autoescape
from playwright.async_api import async_playwright
import io

app = Flask(__name__)
CORS(app)

# Same data structure as in the original file
DATA = {
    # Top-level toggles/values used on pages
    "scenarios": True,
    "fatal": "na",
    "total_fatals": 0,
    "officer_name": "BAET",
    "badge": "RSI99",
    "detachment": "RSI",
    "status": "Complete",
    "supervisor_reviewed": True,

    "prefix": "R",
    "case_no": "1234567",
    "prime_vjur": "100 Mile House 3303",
    "police_file_no": "2025-1234",

    "collision_date": "2025-04-03",
    "reported_same_day": True,
    "time_unknown": False,
    "collision_time": "13:27",
    "date_reported": "2025-04-03",
    "collision_type": "Fatality Personal Injury Property Damage (reportable over $10k)",
    "hitrun": "no",
    "attend": "yes",

    "agency_type": "RCMP - Southeast District",
    "police_code": "0101 Armstrong Prov",
    "police_zone": "1234",

    # Page 2 location/GPS
    "highway_code": "2 City/Mun",
    "loc_route": "",
    "loc_segment": "",
    "loc_km": "",
    "city": "Victoria",
    "territory": "Organized",
    "street_on": "Yates",
    "street_at": "Quadra",
    "loc_desc": "Intersection",
    "gps_format": "dd",  # or 'dms'
    "lat_ns": "N",
    "lat_deg": "48",
    "lat_min": "0",
    "lat_sec": "0.000",
    "lon_ew": "W",
    "lon_deg": "123",
    "lon_min": "0",
    "lon_sec": "0.000",

    "road_class": "11 One Lane Undivided",
    "traffic_flow": "01 One Way",
    "collision_location": "01 At Intersection",
    "speed_primary": "14 Posted - 40 km/h",
    "speed_secondary": "24 Advisory - 40 km/h",
    "land_usage": "03 Apartment Residential",
    "road_type": "01 Asphalt",
    "traffic_control": "21 Traffic Signal - Red",
    "roadway_character": "11 Straight / Flat",
    "surface": "01 Dry",
    "weather": "01 Clear",
    "lighting": "01 Daylight",
    "pco": "2 Head On",
    "first_contact": "03 Pedestrian",
    "first_contact_loc": "01 On Roadway",

    # Page 3 – Entity 1
    "entity1_type": "Vehicle",
    "entity1_no": "01",
    "entity1_offender": "Yes",
    "entity1_parked": False,
    "entity1_unknown": False,

    "e1_dl": "12345678",
    "e1_dl_prov": "BC British Columbia",
    "e1_dl_exp": "2034",
    "e1_surname": "SMITH",
    "e1_given": "JOHN DAVID",
    "e1_dob": "1985-03-15",
    "e1_gender": "Male",
    "e1_addr": "123 MAIN ST",
    "e1_phone": "250-555-0123",

    "e1_veh_year": "2020",
    "e1_veh_make": "TOYOTA",
    "e1_veh_model": "CAMRY",
    "e1_veh_color": "BLUE",
    "e1_plate": "ABC123",
    "e1_plate_prov": "BC British Columbia",
    "e1_vin": "1HGBH41JXMN109186",
    "e1_style": "SEDAN",
    "e1_insurer": "ICBC",
    "e1_policy": "POL123456",
    "e1_owner_same": True,
    "e1_owner_name": "JOHN DAVID SMITH",
    "e1_owner_addr": "123 MAIN ST",
    "e1_damage_loc": "01 Front End",
    "e1_damage_sev": "04 Severe - Major structural repairs needed",
    "e1_damage_est": "$10,000.00",
    "e1_stolen": "No",
}


async def render_with_playwright_async(template_path: str = "mv6020.html", data: dict = None, output_type: str = "pdf"):
    """
    Render the Jinja template using Playwright (same logic as PDF renderer).
    - `template_path`: path to the HTML template
    - `data`: dict used by the template (defaults to DATA)
    - `output_type`: "pdf" or "html" - determines return format
    Returns the PDF content as bytes or HTML content as string.
    """
    data = data or DATA
    template_dir = str(Path(template_path).parent) or "."
    template_name = Path(template_path).name

    try:
        # Render the template with Jinja2 (same as original)
        env = Environment(
            loader=FileSystemLoader(template_dir),
            autoescape=select_autoescape(["html", "xml"]),
            trim_blocks=True,
            lstrip_blocks=True,
        )
        tpl = env.get_template(template_name)
        # Add output_type to template data for conditional CSS
        template_data = {**data, 'output_type': output_type}
        html_str = tpl.render(data=template_data)

        # Save rendered HTML temporarily (for debugging, same as original)
        # temp_html = Path("temp_rendered.html")
        # temp_html.write_text(html_str, encoding="utf-8")

        # Use Playwright to process HTML (same logic as PDF renderer, but return HTML instead)
        async with async_playwright() as p:
            # Launch browser (headless by default)
            browser = await p.chromium.launch(
                headless=True,  # Set to False if you want to see the browser
                args=["--disable-dev-shm-usage"]  # Helps with Docker/CI environments
            )
            
            try:
                # Create a new page
                page = await browser.new_page()
                
                # Set content directly (same as original)
                await page.set_content(html_str, wait_until="networkidle")
                
                if output_type.lower() == "html":
                    # Return the final HTML content after Playwright processing
                    final_html = await page.content()
                    return final_html
                else:
                    # Generate PDF with options (same as original)
                    pdf_bytes = await page.pdf(
                        format="Letter",  # US Letter size
                        print_background=True,  # Include background colors/images
                        display_header_footer=True,  # Enable header/footer
                        # header_template="""
                        #     <div style="font-size: 11pt; font-weight: bold; margin-left: 20px;">
                        #         Electronic MV6020 Traffic Accident Report
                        #     </div>
                        # """,
                        # footer_template="""
                        #     <div style="font-size: 8pt; width: 100%; text-align: center; border-top: 1px solid #000; padding-top: 5px;">
                        #         RCMP GRC ED6190 (eMV6020 2024-07 v1.97 PILOT USE ONLY) &nbsp;&nbsp;&nbsp;&nbsp; 
                        #         Page <span class="pageNumber"></span> of <span class="totalPages"></span>
                        #     </div>
                        # """,
                        margin={
                            "top": "0.75in",
                            "bottom": "0.75in", 
                            "left": "0.5in",
                            "right": "0.5in"
                        },
                        prefer_css_page_size=False,  # Use format/margin settings above
                    )
                    
                    return pdf_bytes
                
            finally:
                await browser.close()
                
                # Clean up temp file (optional)
                # if temp_html.exists():
                #     temp_html.unlink()
                    
    except Exception as e:
        # Return error based on output type
        error_html = f"<h1>Error rendering template with Playwright</h1><p>{str(e)}</p>"
        if output_type.lower() == "html":
            return error_html
        else:
            return error_html.encode('utf-8')


def render_with_playwright(template_path: str = "mv6020.html", data: dict = None, output_type: str = "pdf"):
    """
    Synchronous wrapper for the async Playwright render function.
    """
    return asyncio.run(render_with_playwright_async(template_path, data, output_type))


@app.route('/')
def index():
    """Root endpoint with basic info."""
    return jsonify({
        "message": "MV6020 HTML Renderer Service",
        "endpoints": {
            "/api/render": "GET: Renders PDF with defaults, POST: Renders PDF with custom data/template/options",
            "/api/render/<template_name>": "GET: Renders specific template with defaults, POST: with custom data/options",
            "/api/data": "Returns the current data being used",
            "/api/templates": "Lists available templates"
        }
    })


@app.route('/api/render', methods=['GET', 'POST'])
def render_pdf():
    """Render the MV6020 template to PDF using Playwright and return as PDF file.
    
    GET: Uses default data and template auto-detection
    POST: Accepts JSON body with custom data, template, and options
    
    POST Body Example:
    {
        "template": "mv6020_2_ no_header.html",
        "data": {
            "officer_name": "SMITH",
            "case_no": "2025-5678",
            "collision_date": "2025-08-13"
        },
        "options": {
            "filename": "case_2025_5678.pdf",
            "type": "pdf"
        }
    }
    """
    
    if request.method == 'POST':
        try:
            # Parse JSON body
            request_data = request.get_json()
            if not request_data:
                return jsonify({"error": "No JSON data provided"}), 400
            
            # Extract template name
            template_name = request_data.get('template')
            if not template_name:
                # Use default template detection if not specified
                template_options = [
                    "mv6020_2_ no_header.html",
                    "mv6020.html",
                    "mv6020_2_no_header.html"
                ]
                for template_path in template_options:
                    if Path(template_path).exists():
                        template_name = template_path
                        break
                
                if not template_name:
                    return jsonify({
                        "error": "No template specified and no default templates found",
                        "available_templates": template_options
                    }), 404
            
            # Validate template exists
            if not Path(template_name).exists():
                return jsonify({"error": f"Template '{template_name}' not found"}), 404
            
            # Extract custom data (merge with defaults)
            custom_data = request_data.get('data', {})
            merged_data = {**DATA, **custom_data}  # Custom data overrides defaults
            
            # Extract options
            options = request_data.get('options', {})
            output_type = options.get('type', 'pdf').lower()
            filename = options.get('filename', 'MV6020_report.pdf' if output_type == 'pdf' else 'MV6020_report.html')
            
            # Generate content based on type
            content = render_with_playwright(template_name, merged_data, output_type)
            
            # Return response with proper headers based on type
            if output_type == 'html':
                return Response(
                    content,
                    mimetype='text/html',
                    headers={
                        'Content-Disposition': f'inline; filename={filename}',
                        'Content-Type': 'text/html; charset=utf-8'
                    }
                )
            else:
                return Response(
                    content,
                    mimetype='application/pdf',
                    headers={
                        'Content-Disposition': f'inline; filename={filename}',
                        'Content-Type': 'application/pdf'
                    }
                )
            
        except Exception as e:
            return jsonify({"error": f"Failed to process request: {str(e)}"}), 500
    
    else:  # GET request - use original logic
        # Try different possible template names
        template_options = [
            "mv6020_2_ no_header.html",
            "mv6020.html",
            "mv6020_2_no_header.html"
        ]
        
        for template_path in template_options:
            if Path(template_path).exists():
                pdf_content = render_with_playwright(template_path, DATA, "pdf")
                
                # Return PDF as response with proper headers
                return Response(
                    pdf_content,
                    mimetype='application/pdf',
                    headers={
                        'Content-Disposition': 'inline; filename=MV6020_report.pdf',
                        'Content-Type': 'application/pdf'
                    }
                )
        
        # If no template found, return error as JSON
        return jsonify({
            "error": "Template Not Found",
            "message": "Could not find any of the following templates",
            "templates": template_options
        }), 404


@app.route('/api/templates')
def list_templates():
    """List available templates."""
    templates = []
    for file_path in Path('.').glob('*.html'):
        templates.append({
            "name": file_path.name,
            "path": str(file_path),
            "size": file_path.stat().st_size,
            "modified": file_path.stat().st_mtime
        })
    
    return jsonify({
        "templates": templates,
        "count": len(templates)
    })


@app.route('/api/data')
def get_data():
    """Return the current data being used for rendering."""
    return jsonify(DATA)


@app.route('/api/render/<template_name>', methods=['GET', 'POST'])
def render_specific_template(template_name):
    """Render a specific template by name to PDF using Playwright.
    
    GET: Use default data
    POST: Accept JSON body with custom data and options
    """
    if not template_name.endswith('.html'):
        template_name += '.html'
    
    if not Path(template_name).exists():
        return jsonify({"error": f"Template '{template_name}' not found"}), 404
    
    if request.method == 'POST':
        try:
            request_data = request.get_json() or {}
            custom_data = request_data.get('data', {})
            merged_data = {**DATA, **custom_data}
            
            options = request_data.get('options', {})
            output_type = options.get('type', 'pdf').lower()
            filename = options.get('filename', template_name.replace('.html', '.pdf' if output_type == 'pdf' else '.html'))
            
        except Exception as e:
            return jsonify({"error": f"Invalid JSON: {str(e)}"}), 400
    else:
        merged_data = DATA
        output_type = 'pdf'
        filename = template_name.replace('.html', '.pdf')
    
    content = render_with_playwright(template_name, merged_data, output_type)
    
    # Return response with proper headers based on type
    if output_type == 'html':
        return Response(
            content,
            mimetype='text/html',
            headers={
                'Content-Disposition': f'inline; filename={filename}',
                'Content-Type': 'text/html; charset=utf-8'
            }
        )
    else:
        return Response(
            content,
            mimetype='application/pdf',
            headers={
                'Content-Disposition': f'inline; filename={filename}',
                'Content-Type': 'application/pdf'
            }
        )


if __name__ == '__main__':
    print("🚀 Starting MV6020 PDF Renderer Service (with Playwright)...")
    print("📍 Visit http://localhost:5000/api/render to download/view the rendered PDF")
    print("📊 Visit http://localhost:5000/api/data to see the data being used")
    print("🏠 Visit http://localhost:5000/ for service info")
    print("⚠️  Note: First request may be slower due to Playwright browser startup")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
