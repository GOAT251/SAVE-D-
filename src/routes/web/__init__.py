from flask import Blueprint, render_template, request, jsonify, current_app, send_from_directory
import os

# Import sub-blueprints
from .face_swap import face_swap_web_bp
from .looks_analysis import looks_analysis_bp
from .ai_video import ai_video_bp

def create_web_blueprint():
    """Crée et configure le blueprint web principal"""
    bp = Blueprint('web', __name__)

    # Register sub-blueprints
    bp.register_blueprint(face_swap_web_bp, url_prefix='/face-swap')  # Explicitly set url_prefix
    bp.register_blueprint(looks_analysis_bp)  # This will be prefixed with /web/looks-analysis
    bp.register_blueprint(ai_video_bp)  # This will be prefixed with /web/ai-video

    @bp.route('/')
    def index():
        """Page d'accueil"""
        return render_template('index.html')

    @bp.route('/dashboard')
    def dashboard():
        """Page du tableau de bord"""
        return render_template('dashboard.html')

    @bp.route('/static/images/<path:filename>')
    def serve_image(filename):
        """Sert les images statiques de manière sécurisée"""
        images_dir = os.path.join(current_app.static_folder, 'images')
        return send_from_directory(images_dir, filename)

    @bp.route('/static/images/assets/<path:filename>')
    def serve_asset(filename):
        """Sert les assets statiques de manière sécurisée"""
        assets_dir = os.path.join(current_app.static_folder, 'images', 'assets')
        return send_from_directory(assets_dir, filename)

    @bp.route('/create-payment-intent', methods=['POST'])
    def create_payment():
        """Endpoint pour création d'intention de paiement"""
        try:
            return jsonify({
                'clientSecret': 'demo_mode'
            })
        except Exception as e:
            return jsonify(error=str(e)), 403

    @bp.errorhandler(413)
    def request_entity_too_large(error):
        """Erreur quand le fichier est trop grand"""
        return jsonify({'error': 'File too large. Maximum size is 5MB.'}), 413

    @bp.errorhandler(500)
    def internal_server_error(error):
        """Erreur serveur interne"""
        return jsonify({'error': 'Internal server error. Please try again later.'}), 500

    return bp 