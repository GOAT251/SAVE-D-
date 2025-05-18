"""Face swap service implementation"""

import os
import base64
import logging
import requests
import cv2
import numpy as np
from io import BytesIO
from flask import current_app
from .validator import ImageValidator
from .processor import ImageProcessor
from PIL import Image
from werkzeug.utils import secure_filename
from src.utils.image_utils import process_image
from src.extensions import cache

class FaceSwapService:
    """Service for performing face swaps securely"""

    def __init__(self):
        """Initialize the service with secure configuration"""
        self._api_key = os.environ.get('HUGGINGFACE_API_KEY')
        self._api_url = "https://api-inference.huggingface.co/models/deepinsight/face-swap"
        self.is_available = bool(self._api_key)
        self.upload_folder = os.path.join('static', 'uploads')
        os.makedirs(self.upload_folder, exist_ok=True)

    def swap_faces(self, source_image, target_image):
        """
        Perform face swap securely
        Args:
            source_image: FileStorage object of source image
            target_image: FileStorage object of target image
        Returns:
            dict: Result containing success status and either result image or error
        """
        try:
            # Validate images
            source_valid, source_error = ImageValidator.validate(source_image)
            if not source_valid:
                return {'success': False, 'error': f"Source image error: {source_error}"}

            target_valid, target_error = ImageValidator.validate(target_image)
            if not target_valid:
                return {'success': False, 'error': f"Target image error: {target_error}"}

            # Process images
            source_processed = ImageProcessor.process(source_image)
            target_processed = ImageProcessor.process(target_image)

            if not source_processed or not target_processed:
                return {'success': False, 'error': 'Error processing images'}

            # Check if API is configured
            if self.is_available:
                try:
                    # Convert to base64
                    source_b64 = base64.b64encode(source_processed.read()).decode('utf-8')
                    target_b64 = base64.b64encode(target_processed.read()).decode('utf-8')
                    source_processed.seek(0)
                    target_processed.seek(0)

                    # Make API request
                    response = self._make_api_request(source_b64, target_b64)
                    
                    if response.status_code == 200:
                        return {
                            'success': True,
                            'image': base64.b64encode(response.content).decode('utf-8')
                        }
                    elif response.status_code == 503:
                        # Si l'API est indisponible, on bascule sur le mode démo
                        logging.warning("API unavailable, falling back to demo mode")
                        return self._local_demo_swap(source_processed, target_processed)
                    else:
                        error_msg = response.text if response.text else f"Service error (Status {response.status_code})"
                        logging.error(f"API error: {error_msg}")
                        return {'success': False, 'error': 'Service error. Please try again later.'}
                        
                except Exception as e:
                    logging.error(f"API request error: {str(e)}")
                    # En cas d'erreur, on bascule sur le mode démo
                    return self._local_demo_swap(source_processed, target_processed)
            else:
                # Si pas de clé API, on utilise le mode démo
                return self._local_demo_swap(source_processed, target_processed)

        except Exception as e:
            logging.error(f"Face swap error: {str(e)}")
            return {'success': False, 'error': 'An unexpected error occurred'}

    def _make_api_request(self, source_b64, target_b64):
        """
        Make secure API request to Hugging Face
        Args:
            source_b64: Base64 encoded source image
            target_b64: Base64 encoded target image
        Returns:
            requests.Response: API response
        """
        headers = {
            "Authorization": f"Bearer {self._api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "inputs": {
                "source_image": source_b64,
                "target_image": target_b64
            }
        }

        return requests.post(
            self._api_url,
            headers=headers,
            json=payload,
            timeout=30
        )

    def _local_demo_swap(self, source_image, target_image):
        """
        Perform a simple face swap locally for demo purposes
        Args:
            source_image: Processed source image
            target_image: Processed target image
        Returns:
            dict: Result with base64 image
        """
        try:
            # Convert to OpenCV format
            source_img = Image.open(source_image).convert('RGB')
            target_img = Image.open(target_image).convert('RGB')
            
            source_np = np.array(source_img)
            target_np = np.array(target_img)
            
            # Convert BGR (OpenCV format)
            source_cv = cv2.cvtColor(source_np, cv2.COLOR_RGB2BGR)
            target_cv = cv2.cvtColor(target_np, cv2.COLOR_RGB2BGR)
            
            # Load face detector
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            
            # Detect faces - Ajustement des paramètres pour une meilleure détection
            source_faces = face_cascade.detectMultiScale(
                cv2.cvtColor(source_cv, cv2.COLOR_BGR2GRAY),
                scaleFactor=1.1,  # Réduit de 1.3 à 1.1 pour plus de sensibilité
                minNeighbors=3,   # Réduit de 5 à 3 pour plus de détections
                minSize=(30, 30)  # Taille minimale du visage
            )
            target_faces = face_cascade.detectMultiScale(
                cv2.cvtColor(target_cv, cv2.COLOR_BGR2GRAY),
                scaleFactor=1.1,  # Réduit de 1.3 à 1.1 pour plus de sensibilité
                minNeighbors=3,   # Réduit de 5 à 3 pour plus de détections
                minSize=(30, 30)  # Taille minimale du visage
            )
            
            if len(source_faces) == 0 or len(target_faces) == 0:
                return {
                    'success': False,
                    'error': 'No faces detected in one or both images'
                }
            
            # Use the first face
            x1, y1, w1, h1 = source_faces[0]
            x2, y2, w2, h2 = target_faces[0]
            
            # Simple face swap (demo quality)
            face1 = source_cv[y1:y1+h1, x1:x1+w1]
            face2 = target_cv[y2:y2+h2, x2:x2+w2]
            
            face1_resized = cv2.resize(face1, (w2, h2))
            
            # Create a mask for smooth blending
            mask = np.zeros(target_cv.shape, dtype=target_cv.dtype)
            mask[y2:y2+h2, x2:x2+w2] = face1_resized
            
            # Add watermark for demo mode
            cv2.putText(
                mask, 'DEMO MODE', (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2
            )
            
            # Blend images with smoother transition
            center = (x2 + w2//2, y2 + h2//2)
            output = cv2.seamlessClone(mask, target_cv, mask[:,:,0], center, cv2.NORMAL_CLONE)
            
            # Convert to base64
            _, buffer = cv2.imencode('.jpg', output)
            img_str = base64.b64encode(buffer).decode('utf-8')
            
            return {
                'success': True,
                'image': img_str,
                'note': 'Running in demo mode - API keys not configured'
            }
            
        except Exception as e:
            logging.error(f"Demo swap error: {str(e)}")
            return {
                'success': False,
                'error': 'Error in demo face swap'
            }

    @cache.memoize(timeout=3600)
    def process(self, source_image, target_image):
        """Process face swap request"""
        # Save uploaded files
        source_path = os.path.join(self.upload_folder, secure_filename(source_image.filename))
        target_path = os.path.join(self.upload_folder, secure_filename(target_image.filename))
        
        source_image.save(source_path)
        target_image.save(target_path)
        
        try:
            # Process images
            result_path = process_image(source_path, target_path)
            
            # Return result path relative to static folder
            return os.path.relpath(result_path, 'static')
            
        finally:
            # Cleanup temporary files
            for path in [source_path, target_path]:
                if os.path.exists(path):
                    os.remove(path) 