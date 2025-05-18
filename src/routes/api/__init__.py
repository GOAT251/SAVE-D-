"""Routes API pour l'application MOG AI"""

from flask import Blueprint, request, jsonify

# Import API sub-blueprints
from .face_swap import face_swap_api_bp

# Create API blueprint
api_bp = Blueprint('api', __name__, url_prefix='/api/v1')

# Register sub-blueprints
api_bp.register_blueprint(face_swap_api_bp, url_prefix='/face-swap')

@api_bp.route('/health', methods=['GET'])
def health_check():
    """Endpoint de vérification de l'état de l'API"""
    return jsonify({"status": "ok", "message": "API is running"}) 