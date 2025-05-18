"""Routes web pour la création de vidéos AI"""

from flask import Blueprint, render_template, request, jsonify, current_app
from ...extensions import limiter
from ...services.ai_video.service import video_service

ai_video_bp = Blueprint('ai_video', __name__, url_prefix='/ai-video')

@ai_video_bp.route('/')
def index():
    """Page principale de création de vidéos AI"""
    return render_template('ai_video/index.html')

@ai_video_bp.route('/generate', methods=['POST'])
@limiter.limit("5 per minute")  # More restrictive limit for video generation
def generate_video():
    """Traitement de la requête de génération de vidéo"""
    try:
        data = request.get_json()
        if not data or 'prompt' not in data:
            return jsonify({
                'success': False,
                'error': 'Prompt requis'
            }), 400

        prompt = data['prompt']
        
        # Récupérer les paramètres optionnels
        duration = int(data.get('duration', 3))
        quality = data.get('quality', 'high')
        
        # Vérifier les valeurs
        if duration < 1 or duration > 10:
            duration = 3  # Valeur par défaut sécurisée
        
        if quality not in ['low', 'high', 'ultra']:
            quality = 'high'  # Valeur par défaut sécurisée
            
        # Générer la vidéo avec notre service
        result = video_service.generate_video_from_text(prompt, duration, quality)
        
        if result['success']:
            return jsonify(result)
        else:
            return jsonify(result), 500

    except Exception as e:
        current_app.logger.error(f"Error in generate_video route: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@ai_video_bp.errorhandler(429)
def ratelimit_handler(error):
    """Gestion des erreurs de rate limiting"""
    return jsonify({
        'success': False,
        'error': 'Trop de requêtes. Veuillez réessayer plus tard.'
    }), 429 