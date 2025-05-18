"""
Validator for face swap images
Ensures security and proper formatting
"""

import os
import io
import cv2
import numpy as np
import mimetypes
from PIL import Image
from werkzeug.utils import secure_filename
from flask import current_app

class ImageValidator:
    """Validator for ensuring images are safe and valid"""
    
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB
    
    @staticmethod
    def validate(image_file):
        """
        Validate an image file
        
        Args:
            image_file: FileStorage object to validate
            
        Returns:
            tuple: (is_valid, error_message)
        """
        # Check if file exists
        if not image_file:
            return False, "No image provided"
            
        # Check file size
        image_file.seek(0, os.SEEK_END)
        size = image_file.tell()
        image_file.seek(0)  # Reset file pointer
        
        if size > ImageValidator.MAX_FILE_SIZE:
            return False, "Image size exceeds 5MB limit"
            
        # Check filename
        if image_file.filename == '':
            return False, "No filename provided"
            
        # Check file extension
        if not ImageValidator._allowed_file(image_file.filename):
            return False, "File type not supported"
            
        # Validate using PIL and check for faces
        try:
            image_file.seek(0)
            img = Image.open(image_file)
            img.verify()  # Verify it's a valid image
            image_file.seek(0)  # Reset file pointer
            
            # Convert to OpenCV format for face detection
            img = Image.open(image_file).convert('RGB')
            cv_img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            
            # Load face detector
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            
            # Detect faces
            gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=3,
                minSize=(30, 30)
            )
            
            if len(faces) == 0:
                return False, "No face detected in the image"
            elif len(faces) > 1:
                return False, "Multiple faces detected. Please use an image with a single face"
                
            image_file.seek(0)  # Reset file pointer
            
        except Exception as e:
            return False, f"Invalid image format: {str(e)}"
            
        return True, None
        
    @staticmethod
    def _allowed_file(filename):
        """Check if the file extension is allowed"""
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in ImageValidator.ALLOWED_EXTENSIONS
               
    @staticmethod
    def secure_filename(filename):
        """Generate a secure version of the filename"""
        return secure_filename(filename) 