import pytest
import io
import tempfile
import os
from PIL import Image
from python.prohibition_web_svc.helpers.pdf_helpers import set_transparency_to_white, create_pdf_with_images


class TestSetTransparencyToWhite:
    """Test cases for set_transparency_to_white function"""

    def test_set_transparency_to_white_with_transparent_image(self):
        """Test converting an image with transparency to white background"""
        # Create a test image with transparency
        img = Image.new("RGBA", (100, 100), (0, 0, 0, 0))  # Fully transparent
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as input_file:
            input_path = input_file.name
            img.save(input_path)
        
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as output_file:
            output_path = output_file.name
        
        try:
            # Call the function
            set_transparency_to_white(input_path, output_path)
            
            # Verify the output image exists
            assert os.path.exists(output_path)
            
            # Load and check the output image
            output_img = Image.open(output_path)
            assert output_img.mode == "RGB"  # Should be RGB without alpha
            
            # Check that the image has a white background where it was transparent
            # Get pixel at (50, 50) - should be blended with white
            pixel = output_img.getpixel((50, 50))
            # Fully transparent (0, 0, 0, 0) over white should give (255, 255, 255)
            assert pixel[0] == 255  # Red channel should be 255 (white)
            assert pixel[1] == 255  # Green channel should be 255 (white)
            assert pixel[2] == 255  # Blue channel should be 255 (white)

        finally:
            # Clean up
            if os.path.exists(input_path):
                os.unlink(input_path)
            if os.path.exists(output_path):
                os.unlink(output_path)

    def test_set_transparency_to_white_with_fully_transparent_image(self):
        """Test converting a fully transparent image to white background"""
        # Create a test image with full transparency
        img = Image.new("RGBA", (100, 100), (0, 0, 0, 0))  # Fully transparent
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as input_file:
            input_path = input_file.name
            img.save(input_path)
        
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as output_file:
            output_path = output_file.name
        
        try:
            # Call the function
            set_transparency_to_white(input_path, output_path)
            
            # Verify the output image exists
            assert os.path.exists(output_path)
            
            # Load and check the output image
            output_img = Image.open(output_path)
            assert output_img.mode == "RGB"  # Should be RGB without alpha
            
            # Check that the image is now white
            pixel = output_img.getpixel((50, 50))
            assert pixel == (255, 255, 255)  # Should be pure white
            
        finally:
            # Clean up
            if os.path.exists(input_path):
                os.unlink(input_path)
            if os.path.exists(output_path):
                os.unlink(output_path)

    def test_set_transparency_to_white_with_opaque_image(self):
        """Test with an already opaque image (no transparency)"""
        # Create a test image without transparency
        img = Image.new("RGB", (100, 100), (254, 0, 0))  # Opaque red
        with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as input_file:
            input_path = input_file.name
            img.save(input_path)
        
        with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as output_file:
            output_path = output_file.name
        
        try:
            # Call the function
            set_transparency_to_white(input_path, output_path)
            
            # Verify the output image exists and is unchanged
            assert os.path.exists(output_path)
            output_img = Image.open(output_path)
            assert output_img.mode == "RGB"
            
            # Check pixel value remains the same
            pixel = output_img.getpixel((50, 50))
            assert pixel == (254, 0, 0)
            
        finally:
            # Clean up
            if os.path.exists(input_path):
                os.unlink(input_path)
            if os.path.exists(output_path):
                os.unlink(output_path)

    def test_set_transparency_to_white_invalid_input_path(self):
        """Test with invalid input path"""
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as output_file:
            output_path = output_file.name
        
        try:
            with pytest.raises(FileNotFoundError):
                set_transparency_to_white("/nonexistent/path.png", output_path)
        finally:
            if os.path.exists(output_path):
                os.unlink(output_path)


class TestCreatePdfWithImage:
    """Test cases for create_pdf_with_image function"""

    def test_create_pdf_with_single_image(self):
        """Test creating PDF with a single image"""
        # Create a test image
        img = Image.new("RGB", (200, 200), (255, 0, 0))  # Red square
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as img_file:
            img_path = img_file.name
            img.save(img_path)
        
        try:
            # Call the function
            pdf_bytes = create_pdf_with_images(img_path)
            
            # Verify PDF bytes are returned
            assert isinstance(pdf_bytes, bytes)
            assert len(pdf_bytes) > 0
            
            # Check PDF header
            assert pdf_bytes.startswith(b'%PDF-')
            
        finally:
            # Clean up
            if os.path.exists(img_path):
                os.unlink(img_path)

    def test_create_pdf_with_single_image_landscape(self):
        """Test creating PDF with a single image in landscape mode"""
        # Create a test image
        img = Image.new("RGB", (200, 200), (255, 0, 0))  # Red square
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as img_file:
            img_path = img_file.name
            img.save(img_path)
        
        try:
            # Call the function with landscape=True
            pdf_bytes = create_pdf_with_images(img_path, is_landscape=True)
            
            # Verify PDF bytes are returned
            assert isinstance(pdf_bytes, bytes)
            assert len(pdf_bytes) > 0
            assert pdf_bytes.startswith(b'%PDF-')
            
        finally:
            # Clean up
            if os.path.exists(img_path):
                os.unlink(img_path)

    def test_create_pdf_with_multiple_images(self):
        """Test creating PDF with multiple images"""
        # Create test images
        img1 = Image.new("RGB", (200, 200), (255, 0, 0))  # Red
        img2 = Image.new("RGB", (200, 200), (0, 255, 0))  # Green
        
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as img_file1:
            img_path1 = img_file1.name
            img1.save(img_path1)
        
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as img_file2:
            img_path2 = img_file2.name
            img2.save(img_path2)
        
        try:
            # Call the function
            pdf_bytes = create_pdf_with_images(img_path1, img_path2)
            
            # Verify PDF bytes are returned
            assert isinstance(pdf_bytes, bytes)
            assert len(pdf_bytes) > 0
            assert pdf_bytes.startswith(b'%PDF-')
            
        finally:
            # Clean up
            for path in [img_path1, img_path2]:
                if os.path.exists(path):
                    os.unlink(path)

    def test_create_pdf_with_multiple_images_landscape(self):
        """Test creating PDF with multiple images in landscape mode"""
        # Create test images
        img1 = Image.new("RGB", (200, 200), (255, 0, 0))  # Red
        img2 = Image.new("RGB", (200, 200), (0, 255, 0))  # Green
        
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as img_file1:
            img_path1 = img_file1.name
            img1.save(img_path1)
        
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as img_file2:
            img_path2 = img_file2.name
            img2.save(img_path2)
        
        try:
            # Call the function with landscape=True
            pdf_bytes = create_pdf_with_images(img_path1, img_path2, is_landscape=True)
            
            # Verify PDF bytes are returned
            assert isinstance(pdf_bytes, bytes)
            assert len(pdf_bytes) > 0
            assert pdf_bytes.startswith(b'%PDF-')
            
        finally:
            # Clean up
            for path in [img_path1, img_path2]:
                if os.path.exists(path):
                    os.unlink(path)

    def test_create_pdf_with_transparent_image(self):
        """Test creating PDF with an image that has transparency"""
        # Create a test image with transparency
        img = Image.new("RGBA", (200, 200), (255, 0, 0, 128))  # Semi-transparent red
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as img_file:
            img_path = img_file.name
            img.save(img_path)
        
        try:
            # Call the function
            pdf_bytes = create_pdf_with_images(img_path)
            
            # Verify PDF bytes are returned
            assert isinstance(pdf_bytes, bytes)
            assert len(pdf_bytes) > 0
            assert pdf_bytes.startswith(b'%PDF-')
            
        finally:
            # Clean up
            if os.path.exists(img_path):
                os.unlink(img_path)

    def test_create_pdf_with_transparent_image_landscape(self):
        """Test creating PDF with transparent image in landscape mode"""
        # Create a test image with transparency
        img = Image.new("RGBA", (200, 200), (0, 255, 0, 128))  # Semi-transparent green
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as img_file:
            img_path = img_file.name
            img.save(img_path)
        
        try:
            # Call the function with landscape=True
            pdf_bytes = create_pdf_with_images(img_path, is_landscape=True)
            
            # Verify PDF bytes are returned
            assert isinstance(pdf_bytes, bytes)
            assert len(pdf_bytes) > 0
            assert pdf_bytes.startswith(b'%PDF-')
            
        finally:
            # Clean up
            if os.path.exists(img_path):
                os.unlink(img_path)

    def test_create_pdf_with_no_images(self):
        """Test creating PDF with no images (should raise ValueError)"""
        with pytest.raises(ValueError, match="At least one image path must be provided"):
            create_pdf_with_images()

    def test_create_pdf_default_parameters(self):
        """Test creating PDF with default parameters (portrait mode)"""
        # Create a test image
        img = Image.new("RGB", (200, 200), (255, 0, 0))  # Red square
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as img_file:
            img_path = img_file.name
            img.save(img_path)
        
        try:
            # Call the function without specifying is_landscape (should default to False)
            pdf_bytes = create_pdf_with_images(img_path)
            
            # Verify PDF bytes are returned
            assert isinstance(pdf_bytes, bytes)
            assert len(pdf_bytes) > 0
            assert pdf_bytes.startswith(b'%PDF-')
            
        finally:
            # Clean up
            if os.path.exists(img_path):
                os.unlink(img_path)

    def test_create_pdf_with_invalid_image_path(self):
        """Test creating PDF with invalid image path"""
        with pytest.raises(Exception, match="Error processing image /nonexistent/path.png"):
            create_pdf_with_images("/nonexistent/path.png")

    def test_create_pdf_with_corrupted_image(self):
        """Test creating PDF with a corrupted image file"""
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as img_file:
            img_path = img_file.name
            # Write some invalid data
            with open(img_path, 'wb') as f:
                f.write(b'invalid image data')
        
        try:
            with pytest.raises(Exception, match="Error processing image"):
                create_pdf_with_images(img_path)
        finally:
            if os.path.exists(img_path):
                os.unlink(img_path)

    def test_create_pdf_with_different_image_formats(self):
        """Test creating PDF with different image formats"""
        # Create test images in different formats
        img_png = Image.new("RGB", (100, 100), (255, 0, 0))
        img_jpg = Image.new("RGB", (100, 100), (0, 255, 0))
        
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as png_file:
            png_path = png_file.name
            img_png.save(png_path)
        
        with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as jpg_file:
            jpg_path = jpg_file.name
            img_jpg.save(jpg_path)
        
        try:
            # Call the function with different formats
            pdf_bytes = create_pdf_with_images(png_path, jpg_path)
            
            # Verify PDF is created successfully
            assert isinstance(pdf_bytes, bytes)
            assert len(pdf_bytes) > 0
            assert pdf_bytes.startswith(b'%PDF-')
            
        finally:
            # Clean up
            for path in [png_path, jpg_path]:
                if os.path.exists(path):
                    os.unlink(path)

    def test_create_pdf_with_large_image(self):
        """Test creating PDF with a large image"""
        # Create a large test image
        img = Image.new("RGB", (1000, 1000), (128, 128, 128))  # Large gray square
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as img_file:
            img_path = img_file.name
            img.save(img_path)
        
        try:
            # Call the function
            pdf_bytes = create_pdf_with_images(img_path)
            
            # Verify PDF bytes are returned
            assert isinstance(pdf_bytes, bytes)
            assert len(pdf_bytes) > 0
            assert pdf_bytes.startswith(b'%PDF-')
            
        finally:
            # Clean up
            if os.path.exists(img_path):
                os.unlink(img_path)

    def test_create_pdf_with_small_image(self):
        """Test creating PDF with a very small image"""
        # Create a small test image
        img = Image.new("RGB", (10, 10), (255, 255, 0))  # Small yellow square
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as img_file:
            img_path = img_file.name
            img.save(img_path)
        
        try:
            # Call the function
            pdf_bytes = create_pdf_with_images(img_path)
            
            # Verify PDF bytes are returned
            assert isinstance(pdf_bytes, bytes)
            assert len(pdf_bytes) > 0
            assert pdf_bytes.startswith(b'%PDF-')
            
        finally:
            # Clean up
            if os.path.exists(img_path):
                os.unlink(img_path)

    def test_create_pdf_mixed_transparency_and_opaque(self):
        """Test creating PDF with mix of transparent and opaque images"""
        # Create transparent image
        img_transparent = Image.new("RGBA", (100, 100), (255, 0, 0, 128))
        # Create opaque image
        img_opaque = Image.new("RGB", (100, 100), (0, 255, 0))
        
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as transparent_file:
            transparent_path = transparent_file.name
            img_transparent.save(transparent_path)
        
        with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as opaque_file:
            opaque_path = opaque_file.name
            img_opaque.save(opaque_path)
        
        try:
            # Call the function with mixed image types
            pdf_bytes = create_pdf_with_images(transparent_path, opaque_path)
            
            # Verify PDF is created successfully
            assert isinstance(pdf_bytes, bytes)
            assert len(pdf_bytes) > 0
            assert pdf_bytes.startswith(b'%PDF-')
            
        finally:
            # Clean up
            for path in [transparent_path, opaque_path]:
                if os.path.exists(path):
                    os.unlink(path)