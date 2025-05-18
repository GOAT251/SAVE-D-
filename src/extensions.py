"""
Extensions Flask pour l'application MOG AI
Centralise les extensions pour faciliter l'initialisation
"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_caching import Cache
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS

# Import extensions with try/except to make them optional
try:
    db = SQLAlchemy()
    migrate = Migrate()
except ImportError:
    db = None
    migrate = None
    print("SQLAlchemy/Migrate not available - database functionality disabled")

try:
    cache = Cache()
except ImportError:
    cache = None
    print("Flask-Caching not available - caching disabled")

# Limiter pour protéger contre les abus
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://",
    strategy="fixed-window"
)

def init_extensions(app: Flask):
    """Initialise toutes les extensions avec l'application Flask"""
    if db:
        db.init_app(app)
        migrate.init_app(app, db)
    
    if cache:
        cache.init_app(app)
    
    # CORS
    CORS(app)
    
    # Rate Limiter
    limiter.init_app(app) 