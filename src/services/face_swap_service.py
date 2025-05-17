import os
import requests
from PIL import Image
from io import BytesIO
import base64
from ..extensions import cache
from flask import current_app

class FaceSwapService:
    def __init__(self):
        # Using InsightFace's face swapping model
        self.api_url = "https://api-inference.huggingface.co/models/InstituteForTheStudyOfLearning/face-swap"
        self.api_key = os.environ.get('HUGGINGFACE_API_KEY')
        if not self.api_key:
            raise ValueError("HUGGINGFACE_API_KEY environment variable is not set")
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

    @cache.memoize(timeout=300)
    def swap_faces(self, source_image, target_image):
        """
        Perform face swap using Hugging Face's face-swap model
        Args:
            source_image: BytesIO object of the source image
            target_image: BytesIO object of the target image
        Returns:
            dict: Result containing success status and either the result image or error message
        """
        try:
            # Validate images
            if not self._validate_image(source_image) or not self._validate_image(target_image):
                return {
                    'success': False,
                    'error': 'Invalid image format or size. Please use JPG or PNG files under 5MB.'
                }

            # Read image data
            source_data = source_image.read()
            target_data = target_image.read()

            # Reset file pointers
            source_image.seek(0)
            target_image.seek(0)

            # Convert images to base64
            source_b64 = base64.b64encode(source_data).decode('utf-8')
            target_b64 = base64.b64encode(target_data).decode('utf-8')

            # Prepare the payload
            payload = {
                "inputs": {
                    "source_image": source_b64,
                    "target_image": target_b64
                }
            }

            # Make API request
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json=payload,
                timeout=30  # 30 seconds timeout
            )

            if response.status_code == 200:
                # The response should be a base64 encoded image
                try:
                    result_data = response.json()
                    if isinstance(result_data, dict) and 'image' in result_data:
                        return {
                            'success': True,
                            'result': result_data['image']
                        }
                    else:
                        return {
                            'success': True,
                            'result': base64.b64encode(response.content).decode('utf-8')
                        }
                except Exception as e:
                    # If response is direct image data
                    return {
                        'success': True,
                        'result': base64.b64encode(response.content).decode('utf-8')
                    }
            elif response.status_code == 503:
                return {
                    'success': False,
                    'error': 'Model is loading. Please try again in a few seconds.',
                    'retry': True
                }
            else:
                error_msg = response.text if response.text else f"API Error (Status {response.status_code})"
                current_app.logger.error(f"Face swap API error: {error_msg}")
                return {
                    'success': False,
                    'error': error_msg
                }

        except requests.exceptions.Timeout:
            current_app.logger.error("Face swap API timeout")
            return {
                'success': False,
                'error': 'Request timed out. Please try again.'
            }
        except Exception as e:
            current_app.logger.error(f"Face swap error: {str(e)}")
            return {
                'success': False,
                'error': str(e)
            }

    def _validate_image(self, image):
        """
        Validate image format and size
        Args:
            image: BytesIO object of the image
        Returns:
            bool: True if valid, False otherwise
        """
        try:
            img = Image.open(image)
            # Reset file pointer
            image.seek(0)
            
            # Check file size (max 5MB)
            image.seek(0, 2)  # Seek to end
            size = image.tell()
            image.seek(0)  # Reset pointer
            
            if size > 5 * 1024 * 1024:  # 5MB
                return False
                
            # Check format
            return img.format.lower() in ['jpeg', 'jpg', 'png']
        except Exception:
            return False 