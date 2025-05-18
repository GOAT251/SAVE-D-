"""Utilitaires pour le traitement d'images"""

import os
import cv2
import numpy as np
from PIL import Image
import io
import uuid

def validate_image(file):
    """
    Valide une image
    Args:
        file: FileStorage object
    Returns:
        bool: True si l'image est valide
    """
    try:
        if not file:
            return False
            
        # Vérification du type MIME
        allowed_types = {'image/jpeg', 'image/png', 'image/jpg'}
        if file.content_type not in allowed_types:
            return False
            
        # Vérification de la taille
        file.seek(0, 2)
        size = file.tell()
        file.seek(0)
        if size > 5 * 1024 * 1024:  # 5MB max
            return False
            
        # Vérification que c'est une vraie image
        img = Image.open(file)
        img.verify()
        file.seek(0)
        return True
        
    except Exception:
        return False

def preprocess_image(file):
    """
    Prétraite une image pour le face swap
    Args:
        file: FileStorage object
    Returns:
        numpy.ndarray: Image prétraitée
    """
    try:
        # Lecture de l'image
        image_bytes = file.read()
        file.seek(0)
        
        # Conversion en array numpy
        nparr = np.frombuffer(image_bytes, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        # Redimensionnement si nécessaire
        max_dimension = 1024
        height, width = image.shape[:2]
        
        if height > max_dimension or width > max_dimension:
            scale = max_dimension / max(height, width)
            new_width = int(width * scale)
            new_height = int(height * scale)
            image = cv2.resize(image, (new_width, new_height))
            
        return image
        
    except Exception:
        return None

def encode_base64(image):
    """
    Encode une image en base64
    Args:
        image: Image numpy (OpenCV)
    Returns:
        str: String base64 de l'image
    """
    try:
        # Conversion en format JPEG
        from io import BytesIO
        import base64
        
        # Conversion en RGB si nécessaire
        if len(image.shape) == 3 and image.shape[2] == 3:
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        else:
            image_rgb = image
            
        pil_img = Image.fromarray(image_rgb)
        
        # Sauvegarde en buffer
        buffer = BytesIO()
        pil_img.save(buffer, format="JPEG")
        
        # Encodage en base64
        base64_image = base64.b64encode(buffer.getvalue()).decode('utf-8')
        return base64_image
    
    except Exception:
        return None

def process_image(source_path, target_path):
    """
    Traitement simple d'image pour le face swap
    Args:
        source_path: Chemin de l'image source
        target_path: Chemin de l'image cible
    Returns:
        str: Chemin du résultat
    """
    # Charger les images avec OpenCV
    source_img = cv2.imread(source_path)
    target_img = cv2.imread(target_path)
    
    # Détecter les visages
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    source_gray = cv2.cvtColor(source_img, cv2.COLOR_BGR2GRAY)
    target_gray = cv2.cvtColor(target_img, cv2.COLOR_BGR2GRAY)
    
    source_faces = face_cascade.detectMultiScale(source_gray, 1.1, 4)
    target_faces = face_cascade.detectMultiScale(target_gray, 1.1, 4)
    
    if len(source_faces) == 0 or len(target_faces) == 0:
        raise ValueError("Aucun visage détecté dans une ou les deux images")
    
    # Utiliser le premier visage
    (x1, y1, w1, h1) = source_faces[0]
    (x2, y2, w2, h2) = target_faces[0]
    
    # Extraire le visage source
    face_source = source_img[y1:y1+h1, x1:x1+w1]
    
    # Redimensionner pour correspondre au visage cible
    face_source_resized = cv2.resize(face_source, (w2, h2))
    
    # Créer une copie de l'image cible
    result_img = target_img.copy()
    
    # Superposer le visage
    result_img[y2:y2+h2, x2:x2+w2] = face_source_resized
    
    # Ajouter un watermark
    cv2.putText(
        result_img, 
        'MOG AI DEMO', 
        (10, 30), 
        cv2.FONT_HERSHEY_SIMPLEX, 
        1, 
        (255, 255, 255), 
        2
    )
    
    # Générer un nom de fichier unique pour le résultat
    result_filename = f"result_{uuid.uuid4().hex[:8]}.jpg"
    result_path = os.path.join('static', 'uploads', result_filename)
    
    # Sauvegarder le résultat
    cv2.imwrite(result_path, result_img)
    
    return result_path 