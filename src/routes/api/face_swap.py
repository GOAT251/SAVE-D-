"""Routes API pour le face swap"""

from flask import Blueprint, request, jsonify
from ...extensions import limiter
from ...services.face_swap import FaceSwapService # New import

# Create API blueprint
face_swap_api_bp = Blueprint('face_swap_api', __name__)
face_swap_service = FaceSwapService()

@face_swap_api_bp.route('/', methods=['POST'])
@limiter.limit("20 per hour")
def swap_faces():
    """
    API endpoint pour échanger les visages
    Requiert deux images en multipart/form-data:
    - source_image: L'image contenant le visage à utiliser
    - target_image: L'image où le visage sera placé
    """
    try:
        # Vérifier que les images sont présentes
        if 'source_image' not in request.files or 'target_image' not in request.files:
            return jsonify({
                'success': False,
                'error': 'Les deux images sont requises (source_image et target_image)'
            }), 400
        
        source_image = request.files['source_image']
        target_image = request.files['target_image']
        
        # Vérifier les noms de fichiers
        if source_image.filename == '' or target_image.filename == '':
            return jsonify({
                'success': False,
                'error': 'Nom de fichier invalide'
            }), 400
        
        # Traiter les images
        result = face_swap_service.swap_faces(source_image, target_image)
        
        # Retourner le résultat
        return jsonify(result)
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@face_swap_api_bp.errorhandler(413)
def request_entity_too_large(error):
    """Gestion des erreurs de taille de fichier"""
    return jsonify({
        'success': False,
        'error': 'Fichier trop volumineux. Taille maximale : 5MB'
    }), 413

@face_swap_api_bp.errorhandler(429)
def ratelimit_handler(error):
    """Gestion des erreurs de rate limiting"""
    return jsonify({
        'success': False,
        'error': 'Trop de requêtes. Veuillez réessayer plus tard.',
        'retry_after': error.description
    }), 429 