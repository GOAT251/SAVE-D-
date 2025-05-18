import os
from datetime import timedelta
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(os.path.join('instance', '.env'))

# Configuration de base
DEBUG = True
TESTING = False
SECRET_KEY = os.getenv('SECRET_KEY', 'change-this-in-production')

# Configuration de la base de données
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///instance/app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Configuration du cache
CACHE_TYPE = os.getenv('CACHE_TYPE', 'simple')
CACHE_DEFAULT_TIMEOUT = 300

# Configuration du serveur
HOST = '0.0.0.0'
PORT = int(os.getenv('PORT', 5000))

class Config:
    """Base configuration."""
    # Flask
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev')
    FLASK_ENV = os.environ.get('FLASK_ENV', 'development')
    
    # Base de données
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = SQLALCHEMY_TRACK_MODIFICATIONS
    
    # Cache
    CACHE_TYPE = CACHE_TYPE
    CACHE_DEFAULT_TIMEOUT = CACHE_DEFAULT_TIMEOUT
    
    # API
    HUGGING_FACE_API_KEY = os.environ.get('HUGGING_FACE_API_KEY')
    
    # Stripe
    STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY')
    STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
    
    # Sécurité
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    
    # Rate Limiting
    RATELIMIT_STORAGE_URL = "memory://"
    
    # Upload
    MAX_CONTENT_LENGTH = int(os.environ.get('MAX_CONTENT_LENGTH', 5 * 1024 * 1024))  # 5MB
    UPLOAD_FOLDER = os.path.join('static', 'uploads')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

    # Demo Mode
    DEMO_MODE = os.getenv('DEMO_MODE', True)

    # Redis
    REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')

    # Ensure upload folder exists
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False
    REMEMBER_COOKIE_SECURE = False

class ProductionConfig(Config):
    DEBUG = False
    # Configuration spécifique à la production
    CACHE_TYPE = 'redis'
    SESSION_COOKIE_SECURE = True 