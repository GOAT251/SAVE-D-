"""Routes web pour la création de vidéos AI"""

from flask import Blueprint, render_template, request, jsonify
from ...extensions import limiter

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

        # TODO: Implement AI video generation service
        # For now, return a placeholder response
        return jsonify({
            'success': True,
            'message': 'Génération de vidéo en cours de développement'
        })

    except Exception as e:
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