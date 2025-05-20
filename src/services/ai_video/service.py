"""
Service d'IA pour la génération de vidéos à partir de texte utilisant ModelScope.
"""
import os
import base64
import tempfile
from pathlib import Path
import torch
from diffusers import DiffusionPipeline
import imageio
import numpy as np
from flask import current_app

class AIVideoService:
    """Service pour la génération de vidéos via ModelScope."""
    
    def __init__(self):
        """Initialise le service de génération de vidéo."""
        self.api_key = os.environ.get('HUGGING_FACE_API_KEY')
        self.model_name = os.environ.get('VIDEO_AI_MODEL', 'modelscope/damo-text-to-video-synthesis')
        self.cache_dir = os.environ.get('MODEL_CACHE_PATH', 'D:/Projet/temp/models')
        self.results_dir = os.environ.get('RESULTS_PATH', 'D:/Projet/temp/results')
        
        # Créer les dossiers nécessaires
        Path(self.cache_dir).mkdir(parents=True, exist_ok=True)
        Path(self.results_dir).mkdir(parents=True, exist_ok=True)
        
        if not self.api_key:
            current_app.logger.warning("HUGGING_FACE_API_KEY is not set")
        
        self.pipe = None
    
    def _load_model(self):
        """Charge le modèle de génération de vidéo s'il n'est pas déjà chargé."""
        if self.pipe is None:
            if not self.api_key:
                raise ValueError("Hugging Face API key is not configured")
            
            # Utiliser le cache sur le disque D
            self.pipe = DiffusionPipeline.from_pretrained(
                self.model_name,
                torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
                cache_dir=self.cache_dir,
                trust_remote_code=True,
                use_auth_token=self.api_key
            )
            
            # Déplacer sur GPU si disponible
            if torch.cuda.is_available():
                self.pipe = self.pipe.to("cuda")
                current_app.logger.info("Model loaded on GPU")
            else:
                current_app.logger.info("Model loaded on CPU")
    
    def generate_video_from_text(self, prompt, num_frames=16, height=256, width=256, fps=8):
        """
        Génère une vidéo à partir d'un texte descriptif.
        
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
            # Charger le modèle
            self._load_model()
            
            # Générer la vidéo
            current_app.logger.info(f"Generating video for prompt: {prompt}")
            video_frames = self.pipe(
                prompt,
                num_frames=num_frames,
                height=height,
                width=width,
            ).frames
            
            # Convertir les frames en vidéo
            video_path = self._save_video(video_frames, prompt, fps)
            
            # Créer l'URL relative pour le frontend
            relative_path = os.path.relpath(video_path, current_app.static_folder)
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
            current_app.logger.error(f"Error generating video: {str(e)}")
            return {
                'success': False,
                'error': str(e)
            }
    
    def _save_video(self, frames, prompt, fps=8):
        """
        Sauvegarde les frames en tant que fichier vidéo.
        
        Args:
            frames: Liste des frames de la vidéo
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
        
        # Convertir les frames en format approprié pour imageio
        if isinstance(frames[0], torch.Tensor):
            frames = [frame.cpu().numpy() for frame in frames]
        frames = [frame.astype(np.uint8) for frame in frames]
        
        # Sauvegarder la vidéo
        imageio.mimsave(video_path, frames, fps=fps)
        current_app.logger.info(f"Video saved to {video_path}")
        
        return video_path

# Créer une instance du service
video_service = AIVideoService() 