#!/usr/bin/env python
"""
Script de nettoyage pour MOG AI
Nettoie les fichiers temporaires et les caches
"""

import os
import shutil
from datetime import datetime, timedelta

def clean_uploads():
    """Nettoie les fichiers uploadés de plus de 1 heure"""
    uploads_dir = os.path.join(os.path.dirname(__file__), 'static', 'uploads')
    if not os.path.exists(uploads_dir):
        os.makedirs(uploads_dir)
        return
        
    now = datetime.now()
    for filename in os.listdir(uploads_dir):
        if filename == '.gitkeep':
            continue
            
        filepath = os.path.join(uploads_dir, filename)
        file_modified = datetime.fromtimestamp(os.path.getmtime(filepath))
        if now - file_modified > timedelta(hours=1):
            try:
                if os.path.isfile(filepath):
                    os.remove(filepath)
                elif os.path.isdir(filepath):
                    shutil.rmtree(filepath)
            except Exception as e:
                print(f"Erreur lors de la suppression de {filepath}: {e}")

def clean_cache():
    """Nettoie les fichiers de cache"""
    cache_dirs = [
        '__pycache__',
        '.pytest_cache',
        '.webassets-cache',
        '.cache'
    ]
    
    for cache_dir in cache_dirs:
        if os.path.exists(cache_dir):
            try:
                shutil.rmtree(cache_dir)
            except Exception as e:
                print(f"Erreur lors de la suppression de {cache_dir}: {e}")

if __name__ == '__main__':
    print("Nettoyage des fichiers temporaires...")
    clean_uploads()
    clean_cache()
    print("Nettoyage terminé.") 