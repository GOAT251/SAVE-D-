"""Routes web pour l'interface face swap"""

from flask import Blueprint, render_template, request, jsonify
from ...services.face_swap import FaceSwapService 
from ...extensions import limiter

# Définition du blueprint
face_swap_web_bp = Blueprint('face_swap_web', __name__, url_prefix='/face-swap')
face_swap_service = FaceSwapService()

# La route /face-swap sera gérée par le web_bp principal
# Suppression des routes dupliquées qui ont été ajoutées par erreur

@face_swap_web_bp.route('/')
def index():
    """Page principale du face swap"""
    return render_template('face_swap/index.html')

@face_swap_web_bp.route('/process', methods=['POST'])
@limiter.limit("10 per minute")
def process_swap():
    """Traitement de la requête de face swap"""
    try:
        # Vérification des fichiers
        if 'source_image' not in request.files or 'target_image' not in request.files:
            return "Erreur: Les deux images sont requises", 400

        source_image = request.files['source_image']
        target_image = request.files['target_image']

        # Vérification des noms de fichiers
        if source_image.filename == '' or target_image.filename == '':
            return "Erreur: Nom de fichier invalide", 400

        # Traitement des images
        result = face_swap_service.swap_faces(source_image, target_image)

        if not result['success']:
            return f"Erreur: {result['error']}", 400

        # Retourner une page HTML avec l'image en base64
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Résultat Face Swap</title>
            <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
        </head>
        <body class="bg-gray-900 text-white p-8">
            <div class="max-w-4xl mx-auto text-center">
                <h1 class="text-3xl font-bold mb-8">Résultat du Face Swap</h1>
                <div class="rounded-lg overflow-hidden mb-6">
                    <img src="data:image/jpeg;base64,{result['image']}" class="max-w-full mx-auto" alt="Face Swap Result">
                </div>
                <div class="mb-8">
                    <a href="data:image/jpeg;base64,{result['image']}" download="face-swap-result.jpg" class="bg-blue-600 hover:bg-blue-700 px-6 py-3 rounded-lg inline-block">
                        Télécharger l'image
                    </a>
                </div>
                <div>
                    <a href="/web/face-swap/" class="text-blue-400 hover:text-blue-300">
                        Retour au Face Swap
                    </a>
                </div>
            </div>
        </body>
        </html>
        """

    except Exception as e:
        return f"Erreur inattendue: {str(e)}", 500

@face_swap_web_bp.route('/test')
def test():
    """Route de test pour vérifier que l'application répond"""
    return "Face swap test route is working!"

@face_swap_web_bp.route('/minimal')
def minimal():
    """Route HTML ultra minimale garantie de fonctionner"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Face Swap - Page Minimale</title>
        <style>
            body { 
                font-family: Arial, sans-serif; 
                background: #0f172a; 
                color: white; 
                text-align: center; 
                padding: 30px; 
            }
            h1 { color: #0ea5e9; }
            form { margin: 20px auto; max-width: 500px; }
            .button { 
                background: #0ea5e9; 
                color: white; 
                border: none; 
                padding: 10px 20px; 
                border-radius: 5px; 
                cursor: pointer; 
            }
        </style>
    </head>
    <body>
        <h1>Face Swap - Version Minimale</h1>
        <p>Cette page est une version minimaliste qui devrait fonctionner même si le reste du site a des problèmes.</p>
        
        <form action="/web/face-swap/process" method="post" enctype="multipart/form-data">
            <div style="margin: 20px 0;">
                <label for="source">Image source (visage à utiliser):</label><br>
                <input type="file" name="source_image" id="source" accept="image/*">
            </div>
            
            <div style="margin: 20px 0;">
                <label for="target">Image cible (où placer le visage):</label><br>
                <input type="file" name="target_image" id="target" accept="image/*">
            </div>
            
            <div>
                <button type="submit" class="button">Échanger les visages</button>
            </div>
        </form>
        
        <p>
            <a href="/web/face-swap/test" style="color: #0ea5e9;">Vérifier la route de test</a>
        </p>
    </body>
    </html>
    """

@face_swap_web_bp.errorhandler(413)
def request_entity_too_large(error):
    """Gestion des erreurs de taille de fichier"""
    return jsonify({
        'success': False,
        'error': 'Fichier trop volumineux. Taille maximale : 5MB'
    }), 413

@face_swap_web_bp.errorhandler(429)
def ratelimit_handler(error):
    """Gestion des erreurs de rate limiting"""
    return jsonify({
        'success': False,
        'error': 'Trop de requêtes. Veuillez réessayer plus tard.'
    }), 429 