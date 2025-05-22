from flask import Flask, render_template, request, jsonify, url_for, redirect
import os
from dotenv import load_dotenv
from src.services.ai_video.service import AIVideoService
from src.routes.web.looks_analysis import looks_analysis_bp
from src.routes.web.facial_analysis import facial_analysis_bp

# Charger les variables d'environnement
env_path = os.path.join(os.path.dirname(__file__), 'instance', '.env')
if os.path.exists(env_path):
    load_dotenv(env_path)
    print(f"Fichier .env chargé depuis {env_path}")
else:
    print(f"ATTENTION: Fichier .env non trouvé à {env_path}")

app = Flask(__name__, 
           static_folder='static',
           static_url_path='/static',
           template_folder='templates')

# Enregistrer les blueprints
app.register_blueprint(facial_analysis_bp)
app.register_blueprint(looks_analysis_bp)

# Créer l'instance du service dans le contexte de l'application
video_service = AIVideoService()

def init_video_service():
    global video_service
    if video_service is None:
        video_service = AIVideoService()
    return video_service

@app.route('/')
def index():
    return render_template('index.html', title="Accueil")

@app.route('/face-swap')
def face_swap():
    return render_template('face_swap/index.html', title="Face Swap")

@app.route('/web/ai-video/')
def ai_video():
    return render_template('web/ai_video/index.html', title="Génération de Vidéo AI")

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', title="Dashboard")

@app.route('/face-swap-process', methods=['POST'])
def face_swap_process():
    # Stub for processing face swap
    return jsonify({
        "success": True,
        "message": "Fonctionnalité en cours de développement",
        "image_url": "/static/images/example1.jpg"
    })

@app.route('/web/ai-video/generate', methods=['POST'])
def ai_video_generate():
    try:
        data = request.get_json()
        if not data or 'prompt' not in data:
            return jsonify({
                'success': False,
                'error': 'Le prompt est requis'
            }), 400
            
        # S'assurer que le service est initialisé
        service = init_video_service()
            
        # Paramètres optionnels avec valeurs par défaut
        num_frames = data.get('num_frames', 16)
        height = data.get('height', 256)
        width = data.get('width', 256)
        fps = data.get('fps', 8)
        
        # Générer la vidéo
        result = service.generate_video_from_text(
            prompt=data['prompt'],
            num_frames=num_frames,
            height=height,
            width=width,
            fps=fps
        )
        
        if result['success']:
            return jsonify(result)
        else:
            return jsonify(result), 500
            
    except Exception as e:
        app.logger.error(f"Erreur lors de la génération de la vidéo: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.context_processor
def utility_processor():
    def get_url_for(endpoint, **kwargs):
        try:
            return url_for(endpoint, **kwargs)
        except:
            # Fallback to direct URLs if endpoint not found
            if endpoint == 'web.index':
                return '/'
            elif endpoint == 'face_swap':
                return '/face-swap'
            elif endpoint == 'facial_analysis.index':
                return '/facial-analysis'
            elif endpoint == 'looks_analysis.index':
                return '/looks-analysis'
            elif endpoint == 'ai_video':
                return '/web/ai-video/'
            elif endpoint == 'dashboard':
                return '/dashboard'
            else:
                return '/'
    return dict(url_for=get_url_for)

if __name__ == '__main__':
    app.run(debug=True, port=5001) 