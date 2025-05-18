#!/usr/bin/env python
"""
MOG AI application package initialization
"""

from flask import Flask
from flask_cors import CORS
import os
from dotenv import load_dotenv
from .extensions import db, migrate

def create_app(test_config=None):
    """
    Create and configure the Flask application
    """
    # Load environment variables from .env file
    load_dotenv()

    # Get the absolute path to the static folder
    static_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))
    template_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
    
    app = Flask(__name__,
                static_folder=static_folder,
                static_url_path='/static',
                template_folder=template_folder)
    
    # Configuration
    if test_config is None:
        app.config.from_object('config.config.Config')
    else:
        app.config.update(test_config)
    
    # Initialize extensions
    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Register blueprints
    from .routes.web import create_web_blueprint
    web_bp = create_web_blueprint()
    app.register_blueprint(web_bp, url_prefix='/web')
    
    return app 