"""
Optional extensions that can be enabled as needed
"""
import os

# Import extensions with try/except to make them optional
try:
    from flask_sqlalchemy import SQLAlchemy
    db = SQLAlchemy()
except ImportError:
    db = None
    print("SQLAlchemy not available - database functionality disabled")

try:
    from flask_caching import Cache
    # Système de cache
    cache_config = {
        'CACHE_TYPE': os.getenv('CACHE_TYPE', 'simple'),
        'CACHE_REDIS_URL': os.getenv('REDIS_URL'),
        'CACHE_DEFAULT_TIMEOUT': 300
    }
    cache = Cache(config=cache_config)
except ImportError:
    cache = None
    print("Flask-Caching not available - caching disabled")

try:
    from flask_limiter import Limiter
    from flask_limiter.util import get_remote_address
    # Rate limiting
    limiter = Limiter(
        key_func=get_remote_address,
        default_limits=["200 per day", "50 per hour"],
        storage_uri=os.getenv('REDIS_URL', 'memory://')
    )
except ImportError:
    limiter = None
    print("Flask-Limiter not available - rate limiting disabled") 