"""
Point d'entrée WSGI pour l'application MOG AI
"""
from src import create_app

app = create_app()

if __name__ == "__main__":
    app.run() 