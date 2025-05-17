#!/usr/bin/env python
"""
MOG AI application package initialization
"""

from flask import Flask
from flask_cors import CORS

def create_app():
    """
    Create and configure the Flask application
    """
    app = Flask(__name__, static_folder="../static", template_folder="../templates")
    
    # Configuration
    app.config.from_object("config.Config")
    
    # Initialize extensions
    CORS(app)
    
    # Register blueprints
    from .routes import api, web
    app.register_blueprint(api.bp)
    app.register_blueprint(web.bp)
    
    return app 