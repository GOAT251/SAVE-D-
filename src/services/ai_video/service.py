"""
Service d'IA pour la génération de vidéos à partir de texte.
"""
import os
import base64
import tempfile
from urllib.parse import urlparse
import requests
from huggingface_hub import InferenceClient
from flask import current_app

class AIVideoService:
    """Service pour la génération de vidéos via Hugging Face."""
    
    def __init__(self):
        """Initialise le service de génération de vidéo."""
        self.api_key = os.environ.get('HUGGINGFACE_API_KEY')
        if not self.api_key:
            current_app.logger.warning("HUGGINGFACE_API_KEY is not set")
        
        self.client = None
        if self.api_key:
            self.client = InferenceClient(
                provider="fal-ai",
                api_key=self.api_key,
            )
    
    def generate_video_from_text(self, prompt, duration=3, quality="high"):
        """
        Génère une vidéo à partir d'un texte descriptif.
        
        Args:
            prompt: Description textuelle de la vidéo à générer
            duration: Durée de la vidéo en secondes (default: 3)
            quality: Qualité de la vidéo (low, high, ultra)
            
        Returns:
            dict: Contient l'URL ou les données de la vidéo générée et d'autres informations
        """
        if not self.client:
            raise ValueError("Hugging Face API key is not configured")
            
        try:
            # Mapper les niveaux de qualité aux paramètres du modèle
            quality_map = {
                "low": "standard",
                "high": "premium", 
                "ultra": "max"
            }
            quality_param = quality_map.get(quality.lower(), "premium")
            
            # Appel à l'API Hugging Face
            result = self.client.text_to_video(
                prompt,
                model="Lightricks/LTX-Video",
                params={
                    "quality": quality_param,
                    "duration": duration
                }
            )
            
            # Télécharger et encoder la vidéo en base64 si nécessaire
            video_data = None
            if hasattr(result, 'url') and result.url:
                # Si l'API retourne une URL, télécharger la vidéo
                video_url = result.url
                video_data = self._download_video(video_url)
            elif hasattr(result, 'blob') and result.blob:
                # Si l'API retourne des données binaires directement
                video_data = base64.b64encode(result.blob).decode('utf-8')
            
            return {
                'success': True,
                'video_data': video_data,
                'message': 'Vidéo générée avec succès'
            }
            
        except Exception as e:
            current_app.logger.error(f"Error generating video: {str(e)}")
            return {
                'success': False,
                'error': str(e)
            }
    
    def _download_video(self, url):
        """
        Télécharge une vidéo depuis une URL et la convertit en base64.
        
        Args:
            url: URL de la vidéo à télécharger
            
        Returns:
            str: Données de la vidéo encodées en base64
        """
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            
            # Créer un fichier temporaire pour stocker la vidéo
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
                for chunk in response.iter_content(chunk_size=8192):
                    temp_file.write(chunk)
                temp_file_path = temp_file.name
            
            # Lire le fichier et l'encoder en base64
            with open(temp_file_path, 'rb') as f:
                video_bytes = f.read()
                video_base64 = base64.b64encode(video_bytes).decode('utf-8')
            
            # Supprimer le fichier temporaire
            os.unlink(temp_file_path)
            
            return video_base64
            
        except Exception as e:
            current_app.logger.error(f"Error downloading video: {str(e)}")
            raise e

# Créer une instance du service
video_service = AIVideoService() 