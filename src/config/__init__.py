import os
from pathlib import Path

class Config:
    """Configuration management for MOG AI application."""
    
    def __init__(self):
        self.env_file = '.env'
        self.example_env_file = '.env.example'
        self.required_vars = {
            'HUGGINGFACE_API_KEY': '',  # Must be set by user
            'FLASK_ENV': 'development',
            'FLASK_DEBUG': '1',
            'SECRET_KEY': 'dev-key-temporary',
            'PORT': '5000'
        }
        
        # Create .env file if it doesn't exist
        self._ensure_env_file()
        
        # Load environment variables
        self._load_env_vars()
    
    def _ensure_env_file(self):
        """Create .env file if it doesn't exist."""
        if not os.path.exists(self.env_file):
            try:
                with open(self.env_file, 'w', encoding='utf-8') as f:
                    for key, value in self.required_vars.items():
                        f.write(f'{key}={value}\n')
                print(f"Created {self.env_file} with default values")
                print("Please set your HUGGINGFACE_API_KEY in the .env file")
            except Exception as e:
                print(f"Warning: Could not create {self.env_file}: {str(e)}")
                print("Using default environment variables")
    
    def _load_env_vars(self):
        """Load environment variables from .env file."""
        try:
            if os.path.exists(self.env_file):
                with open(self.env_file, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith('#'):
                            key, value = line.split('=', 1)
                            os.environ[key.strip()] = value.strip()
            
            # Ensure all required variables are set
            for key, default_value in self.required_vars.items():
                if key not in os.environ:
                    os.environ[key] = default_value
                    
            # Check if HUGGINGFACE_API_KEY is empty
            if not os.environ.get('HUGGINGFACE_API_KEY'):
                print("Warning: HUGGINGFACE_API_KEY is not set. Please set it in your .env file")
        except Exception as e:
            print(f"Warning: Error loading environment variables: {str(e)}")
            print("Using default environment variables")
            for key, value in self.required_vars.items():
                os.environ[key] = value
    
    @staticmethod
    def get(key, default=None):
        """Get an environment variable."""
        return os.environ.get(key, default)
    
    @staticmethod
    def set(key, value):
        """Set an environment variable."""
        os.environ[key] = value

# Create a singleton instance
config = Config() 