from flask import Blueprint, render_template, request, jsonify, current_app, send_from_directory
from ..services.face_swap_service import FaceSwapService

bp = Blueprint('web', __name__)
face_swap_service = FaceSwapService()

@bp.route('/')
def index():
    """Page d'accueil"""
    return render_template('index.html')

@bp.route('/faceswap')
def faceswap():
    """Page du service Face Swap"""
    return render_template('faceswap.html')

@bp.route('/dashboard')
def dashboard():
    """Page du tableau de bord"""
    return render_template('dashboard.html')

@bp.route('/static/<path:filename>')
def serve_static(filename):
    """Sert les fichiers statiques"""
    return send_from_directory('static', filename)

@bp.route('/create-payment-intent', methods=['POST'])
def create_payment():
    """Endpoint pour création d'intention de paiement"""
    try:
        return jsonify({
            'clientSecret': 'demo_mode'
        })
    except Exception as e:
        return jsonify(error=str(e)), 403

@bp.route('/process-faceswap', methods=['POST'])
def process_faceswap():
    """Endpoint pour traiter le face swap via l'interface web"""
    if 'source_image' not in request.files or 'target_image' not in request.files:
        return jsonify({'error': 'Missing image files'}), 400

    source_image = request.files['source_image']
    target_image = request.files['target_image']

    # Validate file names
    if source_image.filename == '' or target_image.filename == '':
        return jsonify({'error': 'No selected files'}), 400

    # Process the face swap
    result = face_swap_service.swap_faces(source_image, target_image)
    return jsonify(result)

@bp.errorhandler(413)
def request_entity_too_large(error):
    """Erreur quand le fichier est trop grand"""
    return jsonify({'error': 'File too large. Maximum size is 5MB.'}), 413

@bp.errorhandler(500)
def internal_server_error(error):
    """Erreur serveur interne"""
    return jsonify({'error': 'Internal server error. Please try again later.'}), 500 