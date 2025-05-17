import os
from pathlib import Path

class Config:
    """Configuration management"""
    
    def __init__(self):
        self.env_file = '.env'
        self.required_vars = {
            'FLASK_APP': 'src',
            'FLASK_ENV': 'development',
            'FLASK_DEBUG': '1',
            'SECRET_KEY': 'change-this-in-production',
            'DATABASE_URL': 'sqlite:///instance/app.db'
        }

    def load_env(self):
        """Load environment variables from .env file"""
        if not os.path.exists(self.env_file):
            self.create_env_file()
            print(f"Created {self.env_file} with default values")
            return

        try:
            with open(self.env_file, 'r', encoding='utf-8') as f:
                for line in f:
                    if '=' in line:
                        key, value = line.split('=', 1)
                        os.environ[key.strip()] = value.strip()

            # Set defaults for missing variables
            for key, default_value in self.required_vars.items():
                if key not in os.environ:
                    os.environ[key] = default_value

        except Exception as e:
            print(f"Warning: Error loading environment variables: {str(e)}")
            print("Using default environment variables")
            self.reset_to_defaults()

    def create_env_file(self):
        """Create a new .env file with default values"""
        with open(self.env_file, 'w') as f:
            for key, value in self.required_vars.items():
                f.write(f'{key}={value}\n')

    def reset_to_defaults(self):
        """Reset all configuration to default values"""
        for key, value in self.required_vars.items():
            os.environ[key] = value

    @staticmethod
    def get(key, default=None):
        """Get a configuration value"""
        return os.environ.get(key, default)

    @staticmethod
    def set(key, value):
        """Set a configuration value"""
        os.environ[key] = value

# Create a singleton instance
config = Config() 