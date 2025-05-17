from flask import Blueprint, request, jsonify
from ..services.face_swap_service import FaceSwapService

bp = Blueprint('api', __name__, url_prefix='/api/v1')
face_swap_service = FaceSwapService()

@bp.route('/health', methods=['GET'])
def health_check():
    """Endpoint de vérification de l'état de l'API"""
    return jsonify({"status": "ok", "message": "API is running"})

@bp.route('/face-swap', methods=['POST'])
def process_face_swap():
    """Endpoint pour le face-swap via API"""
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