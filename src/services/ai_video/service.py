"""
Service d'IA pour la génération de vidéos à partir de texte utilisant l'API Hugging Face.
"""
import os
import base64
import tempfile
import logging
from pathlib import Path
import requests
import json
from flask import current_app

# Configuration d'un logger standard 
logger = logging.getLogger(__name__)

class AIVideoService:
    """Service pour la génération de vidéos via Text-to-Video."""
    
    def __init__(self, api_key=None):
        """Initialise le service de génération de vidéo."""
        # Permettre l'injection de la clé API ou la lire depuis l'environnement
        self.api_key = api_key or os.getenv('HUGGING_FACE_API_KEY')
        # Utiliser le nouveau nom de modèle correct
        self.model_name = os.getenv('VIDEO_AI_MODEL', 'damo-vilab/text-to-video-ms-1.7b')
        self.results_dir = os.getenv('RESULTS_PATH', 'D:/Projet/temp/results')
        self.api_url = f"https://api-inference.huggingface.co/models/{self.model_name}"
        
        # Créer les dossiers nécessaires
        Path(self.results_dir).mkdir(parents=True, exist_ok=True)
        
        if not self.api_key:
            logger.warning("HUGGING_FACE_API_KEY is not set")
            if current_app:
                current_app.logger.warning("HUGGING_FACE_API_KEY is not set")
        else:
            logger.info("HUGGING_FACE_API_KEY is configured")
            if current_app:
                current_app.logger.info("HUGGING_FACE_API_KEY is configured")
    
    def generate_video_from_text(self, prompt, num_frames=16, height=256, width=256, fps=8):
        """
        Génère une vidéo à partir d'un texte descriptif en utilisant l'API Hugging Face.
        
        Args:
            prompt: Description textuelle de la vidéo à générer
            num_frames: Nombre de frames à générer
            height: Hauteur de la vidéo
            width: Largeur de la vidéo
            fps: Images par seconde
            
        Returns:
            dict: Contient l'URL de la vidéo générée et d'autres informations
        """
        try:
            if not self.api_key:
                raise ValueError("Hugging Face API key is not configured")

            # Préparer les headers pour l'API
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }

            # Préparer les données pour l'API
            payload = {
                "inputs": prompt,
                "parameters": {
                    "num_frames": num_frames,
                    "height": height,
                    "width": width,
                    "num_inference_steps": 25
                }
            }

            # Appeler l'API
            if current_app:
                current_app.logger.info(f"Calling Hugging Face API for prompt: {prompt}")
            else:
                logger.info(f"Calling Hugging Face API for prompt: {prompt}")

            response = requests.post(self.api_url, headers=headers, json=payload)
            
            if response.status_code != 200:
                error_msg = f"API request failed with status {response.status_code}: {response.text}"
                raise ValueError(error_msg)

            # Sauvegarder la vidéo reçue
            video_path = self._save_video_from_response(response, prompt, fps)
            
            # Créer l'URL relative pour le frontend
            if current_app:
                relative_path = os.path.relpath(video_path, current_app.static_folder)
            else:
                relative_path = os.path.relpath(video_path, "static")
            video_url = f"/static/{relative_path.replace(os.sep, '/')}"
            
            return {
                'success': True,
                'video_url': video_url,
                'message': 'Vidéo générée avec succès',
                'details': {
                    'frames': num_frames,
                    'fps': fps,
                    'resolution': f"{width}x{height}"
                }
            }
            
        except Exception as e:
            if current_app:
                current_app.logger.error(f"Error generating video: {str(e)}")
            else:
                logger.error(f"Error generating video: {str(e)}")
            return {
                'success': False,
                'error': str(e)
            }
    
    def _save_video_from_response(self, response, prompt, fps=8):
        """
        Sauvegarde la vidéo reçue de l'API.
        
        Args:
            response: Réponse de l'API contenant la vidéo
            prompt: Texte utilisé pour générer la vidéo (utilisé pour le nom de fichier)
            fps: Images par seconde
            
        Returns:
            str: Chemin du fichier vidéo sauvegardé
        """
        # Créer un nom de fichier sécurisé basé sur le prompt
        safe_filename = "".join(x for x in prompt if x.isalnum() or x in "._- ")[:50]
        timestamp = tempfile.mktemp(prefix='', suffix='')[1:11]
        video_filename = f"video_{safe_filename}_{timestamp}.mp4"
        video_path = os.path.join(self.results_dir, video_filename)
        
        # Sauvegarder la vidéo
        with open(video_path, 'wb') as f:
            f.write(response.content)
            
        if current_app:
            current_app.logger.info(f"Video saved to {video_path}")
        else:
            logger.info(f"Video saved to {video_path}")
        
        return video_path

# Ne pas créer l'instance ici, mais la créer dans app.py
# video_service = AIVideoService() 