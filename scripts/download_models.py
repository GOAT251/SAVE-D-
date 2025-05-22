import os
import requests
from pathlib import Path

# URLs des modèles Face-API.js (mise à jour avec CDN fiable)
BASE_URL = "https://cdn.jsdelivr.net/npm/@vladmandic/face-api@1/model/"
MODELS = {
    'tiny_face_detector': {
        'manifest': f"{BASE_URL}tiny_face_detector_model-weights_manifest.json",
        'weights': f"{BASE_URL}tiny_face_detector_model-shard1"
    },
    'face_landmark_68_tiny': {
        'manifest': f"{BASE_URL}face_landmark_68_tiny_model-weights_manifest.json",
        'weights': f"{BASE_URL}face_landmark_68_tiny_model-shard1"
    },
    'face_recognition': {
        'manifest': f"{BASE_URL}face_recognition_model-weights_manifest.json",
        'weights': f"{BASE_URL}face_recognition_model-shard1"
    }
}

# Dossier de destination
MODELS_DIR = Path('static/models')

def download_file(url, dest_path):
    """Télécharge un fichier depuis une URL"""
    response = requests.get(url)
    response.raise_for_status()
    
    with open(dest_path, 'wb') as f:
        f.write(response.content)
    print(f"Téléchargé: {dest_path}")

def main():
    """Télécharge tous les modèles nécessaires"""
    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    
    for model_name, urls in MODELS.items():
        # Télécharger le manifest
        manifest_path = MODELS_DIR / f"{model_name}_model-weights_manifest.json"
        download_file(urls['manifest'], manifest_path)
        
        # Télécharger les weights
        weights_path = MODELS_DIR / f"{model_name}_model-shard1"
        download_file(urls['weights'], weights_path)

if __name__ == '__main__':
    main()
    print("Tous les modèles ont été téléchargés avec succès!") 