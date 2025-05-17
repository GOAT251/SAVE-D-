#!/usr/bin/env python
"""
MOG AI application package initialization
"""

from flask import Flask
from flask_cors import CORS
import os

def create_app():
    """
    Create and configure the Flask application
    """
    # Get the absolute path to the static folder
    static_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))
    template_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
    
    app = Flask(__name__, 
                static_folder=static_folder,
                static_url_path='/static',
                template_folder=template_folder)
    
    # Configuration
    app.config.from_object("config.Config")
    
    # Initialize extensions
    CORS(app)
    
    # Register blueprints
    from .routes import api, web
    app.register_blueprint(api.bp)
    app.register_blueprint(web.bp)
    
    return app 