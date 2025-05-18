"""
Image processor for face swap service
Handles preprocessing and preparation of images
"""

import os
import io
import tempfile
from PIL import Image
from werkzeug.datastructures import FileStorage

class ImageProcessor:
    """Image processor for safely handling and optimizing images"""
    
    @staticmethod
    def process(image_file):
        """
        Process image file for face swap
        
        Args:
            image_file: FileStorage object to process
            
        Returns:
            FileStorage: Processed image file or None if error
        """
        try:
            # Open the image with PIL
            img = Image.open(image_file)
            
            # Convert to RGB if needed (remove transparency)
            if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
                bg = Image.new('RGB', img.size, (255, 255, 255))
                bg.paste(img, mask=img.split()[3] if img.mode == 'RGBA' else None)
                img = bg
            
            # Resize if too large (max 1024px)
            max_size = 1024
            if img.width > max_size or img.height > max_size:
                ratio = min(max_size / img.width, max_size / img.height)
                new_width = int(img.width * ratio)
                new_height = int(img.height * ratio)
                img = img.resize((new_width, new_height), Image.LANCZOS)
            
            # Save optimized image to BytesIO
            img_io = io.BytesIO()
            img.save(img_io, format='JPEG', quality=85, optimize=True)
            img_io.seek(0)
            
            # Create new FileStorage from BytesIO
            processed_file = FileStorage(
                stream=img_io,
                filename=f"processed_{os.path.basename(image_file.filename)}",
                content_type='image/jpeg'
            )
            
            return processed_file
            
        except Exception as e:
            print(f"Image processing error: {str(e)}")
            return None 