from flask import Flask, render_template, request, jsonify, url_for, redirect
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

app = Flask(__name__, 
           static_folder='static',
           static_url_path='/static',
           template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html', title="Accueil")

@app.route('/face-swap')
def face_swap():
    return render_template('face_swap/index.html', title="Face Swap")

@app.route('/web/looks-analysis/')
def looks_analysis():
    return render_template('looks_analysis/index.html', title="Analyse de Look")

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
    # Stub for generating AI video
    return jsonify({
        "success": True,
        "message": "Vidéo générée avec succès",
        "video_url": "/static/videos/example.mp4"
    })

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
            elif endpoint == 'looks_analysis':
                return '/web/looks-analysis/'
            elif endpoint == 'ai_video':
                return '/web/ai-video/'
            elif endpoint == 'dashboard':
                return '/dashboard'
            else:
                return '/'
    return dict(url_for=get_url_for)

if __name__ == '__main__':
    app.run(debug=True, port=5001) 