"""Routes web pour l'analyse de style vestimentaire"""

from flask import Blueprint, render_template, request, jsonify, current_app
from werkzeug.utils import secure_filename
import traceback
from src.services.looks_analysis.service import OptimizedLooksAnalysisService

looks_analysis_bp = Blueprint('looks_analysis', __name__, url_prefix='/looks-analysis')

# Initialize the service
# In a real app, this might be managed by Flask's app context or a dependency injection framework
looks_analyzer = OptimizedLooksAnalysisService()

@looks_analysis_bp.route('/')
def looks_analysis():
    """Page d'analyse de style"""
    return render_template(
        'looks_analysis.html',
        config={
            'maxFileSize': current_app.config.get('MAX_CONTENT_LENGTH', 5 * 1024 * 1024),  # 5MB par défaut
            'supportedFormats': ['image/jpeg', 'image/png', 'image/webp'],
        }
    )

@looks_analysis_bp.route('/analyze', methods=['POST'])
def analyze_look():
    """Traitement de la requête d'analyse de style"""
    try:
        current_app.logger.info("Requête d'analyse de style reçue")
        
        if 'image' not in request.files:
            current_app.logger.warning("Aucune image trouvée dans la requête")
            return jsonify({
                'success': False,
                'error': 'Image requise'
            }), 400

        image_file = request.files['image']
        current_app.logger.info(f"Image reçue: {image_file.filename}")

        if image_file.filename == '':
            current_app.logger.warning("Nom de fichier invalide")
            return jsonify({
                'success': False,
                'error': 'Nom de fichier invalide'
            }), 400

        # Analyse de l'image avec notre service optimisé
        current_app.logger.info("Analyse de l'image en cours...")
        analysis_results = looks_analyzer.analyze_image(image_file)
        current_app.logger.info("Analyse terminée avec succès")
        
        return jsonify({
            'success': True,
            'results': analysis_results
        })

    except Exception as e:
        error_details = traceback.format_exc()
        current_app.logger.error(f"Erreur lors de l'analyse: {str(e)}\n{error_details}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@looks_analysis_bp.errorhandler(413)
def request_entity_too_large(error):
    """Gestion des erreurs de taille de fichier"""
    current_app.logger.warning("Fichier trop volumineux reçu")
    return jsonify({
        'success': False,
        'error': 'Fichier trop volumineux. Taille maximale : 5MB'
    }), 413

@looks_analysis_bp.errorhandler(429)
def ratelimit_handler(error):
    """Gestion des erreurs de rate limiting"""
    current_app.logger.warning("Limite de requêtes atteinte")
    return jsonify({
        'success': False,
        'error': 'Trop de requêtes. Veuillez réessayer plus tard.'
    }), 429