from flask import Flask, render_template, request, jsonify
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
    return "Application MOG AI - Version alternative fonctionnelle"

@app.route('/face-swap')
def face_swap():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Face Swap - Version d'urgence</title>
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
        <h1>Face Swap - Version d'Urgence</h1>
        <p>Cette page est une version minimale d'urgence qui fonctionne.</p>
        
        <form action="/face-swap-process" method="post" enctype="multipart/form-data">
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
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True, port=5001) 