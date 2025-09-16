import io
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape

import logging

def set_transparency_to_white(image_path, output_image_path):
    """
    Convert an image with transparency to one with a white background.
    
    Args:
        image_path (str): Path to the input image.
        output_image_path (str): Path to save the converted image.
    """
    img = Image.open(image_path).convert("RGBA")
    background = Image.new("RGBA", img.size, (255, 255, 255, 255))  # White background
    combined = Image.alpha_composite(background, img)
    combined = combined.convert("RGB")  # Remove alpha channel
    combined.save(output_image_path)
    logging.debug(f"Image transparency set to white and saved to {output_image_path}")

def create_pdf_with_images(*image_paths, is_landscape=False):
    """
    Creates a PDF file containing the provided images and returns the PDF with pages in letter size as bytes.
    
    Args:
        *image_paths: Variable number of image file paths (strings)
    
    Returns:
        bytes: The PDF content as a bytes array
    
    Raises:
        FileNotFoundError: If any image file is not found
        Exception: For other PDF generation errors
    """
    if not image_paths:
        raise ValueError("At least one image path must be provided")
    
    buffer = io.BytesIO()
    try:
        page_size = letter if not is_landscape else landscape(letter)
        c = canvas.Canvas(buffer, pagesize=page_size, cropMarks=None)
        
        # Add each image to a separate page
        for image_path in image_paths:
            try:
                img = Image.open(image_path).convert("RGBA")
                background = Image.new("RGBA", img.size, (255, 255, 255, 255))  # White background
                combined = Image.alpha_composite(background, img)
                combined = combined.convert("RGB")  # Remove alpha channel
                set_transparency_to_white(image_path, image_path)

                # Draw image on the page (adjust positioning and size as needed)
                width = 612 if not is_landscape else 792
                height = 792 if not is_landscape else 612
                c.drawImage(image_path, 0, 0, width, height,
                            preserveAspectRatio=True,
                            anchor='c', 
                            showBoundary=False)
                c.showPage()  # Start a new page for the next image
            except Exception as e:
                raise Exception(f"Error processing image {image_path}: {str(e)}")
        
        c.save()
        buffer.seek(0)
        return buffer.getvalue()
    
    except Exception as e:
        buffer.close()
        raise e    
    finally:
        buffer.close()
