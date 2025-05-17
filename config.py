import os
from pathlib import Path
from dotenv import load_dotenv

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent

# Default configuration
DEBUG = True
TESTING = False
SECRET_KEY = os.getenv('SECRET_KEY', 'change-this-in-production')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Environment-specific configuration
class Config:
    """Base configuration."""
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    SECRET_KEY = os.getenv('SECRET_KEY', 'change-this-in-production')
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5MB max file size
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

class ProductionConfig(Config):
    """Production configuration."""
    FLASK_ENV = 'production'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    FLASK_ENV = 'development'

class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

def get_config():
    """Get the current configuration based on FLASK_ENV."""
    config_name = os.getenv('FLASK_ENV', 'development')
    return config.get(config_name, config['default'])

# Configuration Flask
SECURITY_KEY = os.getenv('SECRET_KEY', 'change-this-in-production')
DEBUG = os.getenv('FLASK_DEBUG', '1') == '1'
TESTING = False

# Configuration de la base de données
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Configuration du cache
CACHE_TYPE = os.getenv('CACHE_TYPE', 'simple')
CACHE_REDIS_URL = os.getenv('REDIS_URL')
CACHE_DEFAULT_TIMEOUT = 300

# Configuration du téléchargement de fichiers
UPLOAD_FOLDER = 'uploads'
MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5MB max upload

# Configuration du serveur
HOST = '0.0.0.0'
PORT = int(os.getenv('PORT', 5000))

@staticmethod
def init_app(app):
    """Initialisation de l'application avec cette configuration"""
    # Assurez-vous que le dossier d'upload existe
    os.makedirs(os.path.join(app.root_path, Config.UPLOAD_FOLDER), exist_ok=True)

# Configuration active
current_config = get_config() 