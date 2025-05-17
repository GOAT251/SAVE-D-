"""
Optional extensions that can be enabled as needed
"""
import os
from flask import Flask

# Import extensions with try/except to make them optional
try:
    from flask_sqlalchemy import SQLAlchemy
    db = SQLAlchemy()
except ImportError:
    db = None
    print("SQLAlchemy not available - database functionality disabled")

try:
    from flask_caching import Cache
    cache = Cache()
except ImportError:
    cache = None
    print("Flask-Caching not available - caching disabled")

try:
    from flask_limiter import Limiter
    from flask_limiter.util import get_remote_address
    limiter = Limiter(
        key_func=get_remote_address,
        default_limits=["200 per day", "50 per hour"]
    )
except ImportError:
    limiter = None
    print("Flask-Limiter not available - rate limiting disabled")

def init_extensions(app: Flask):
    """Initialize all available extensions"""
    if db:
        db.init_app(app)
    
    if cache:
        cache.init_app(app, config={
            'CACHE_TYPE': 'simple',
            'CACHE_DEFAULT_TIMEOUT': 300
        })
    
    if limiter:
        limiter.init_app(app) 