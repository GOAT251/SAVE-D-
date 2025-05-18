# M.O.G AI - Face Swap Application

## Overview
M.O.G AI (Mastering Optical Grafting) is a Flask-based web application that provides face swapping capabilities using advanced AI technology. The application supports both local processing and API-based face swapping through HuggingFace.

## Features
- Face detection and swapping
- Modern, responsive UI
- Real-time processing
- Support for multiple image formats
- Rate limiting and caching
- Dashboard with usage statistics

## Quick Start

### Prerequisites
- Python 3.8+
- Redis (for caching)
- Virtual environment (recommended)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/mog-ai.git
cd mog-ai
```

2. Create and activate virtual environment:
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create .env file in instance/ directory:
```env
FLASK_APP=src
FLASK_ENV=development
SECRET_KEY=your-secret-key
HUGGING_FACE_API_KEY=your-api-key  # Optional for API mode
REDIS_URL=redis://localhost:6379
MAX_CONTENT_LENGTH=5242880
```

### Running the Application

#### Development Mode
```bash
# Windows
.\scripts\start.bat

# Linux/Mac
export FLASK_APP=src
export FLASK_ENV=development
flask run
```

#### Production Mode
```bash
gunicorn -c deployment/gunicorn.conf.py "src:create_app()"
```

## Project Structure
See [aide/structure_scalable.md](aide/structure_scalable.md) for detailed project structure documentation.

## Development

### Setting Up Development Environment
1. Install development dependencies:
```bash
pip install -r requirements.txt
```

2. Set up pre-commit hooks:
```bash
pre-commit install
```

### Running Tests
```bash
python -m pytest
```

### Code Style
- Follow PEP 8 guidelines
- Use type hints
- Write docstrings for functions and classes

## API Documentation

### Face Swap Endpoint
- **URL**: `/api/v1/face-swap`
- **Method**: `POST`
- **Body**: 
  - `source_image`: Face to use
  - `target_image`: Image to place the face on
- **Response**: Base64 encoded result image

## Configuration

### Environment Variables
- `FLASK_APP`: Application entry point
- `FLASK_ENV`: Environment (development/production)
- `SECRET_KEY`: Application secret key
- `HUGGING_FACE_API_KEY`: API key for HuggingFace (optional)
- `REDIS_URL`: Redis connection URL
- `MAX_CONTENT_LENGTH`: Maximum upload size

### Configuration Files
- `config/config.py`: Main configuration
- `deployment/gunicorn.conf.py`: Gunicorn settings
- `instance/.env`: Environment variables

## Maintenance

### Regular Tasks
1. Run cleanup script:
```bash
python scripts/clean.py
```

2. Update dependencies:
```bash
pip install --upgrade -r requirements.txt
```

3. Run tests:
```bash
python -m pytest
```

### Monitoring
- Check application logs in `logs/`
- Monitor Redis cache usage
- Review dashboard metrics

## Troubleshooting

### Common Issues

1. Application won't start
- Check if Redis is running
- Verify environment variables
- Ensure all dependencies are installed

2. Face swap fails
- Verify image formats
- Check image sizes
- Ensure face is detectable in images

3. Performance issues
- Clear Redis cache
- Run cleanup script
- Check server resources

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- HuggingFace for AI models
- Flask team for the web framework
- OpenCV team for image processing 