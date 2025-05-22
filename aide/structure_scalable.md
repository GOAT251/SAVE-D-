# M.O.G AI - Project Structure Documentation

## Core Project Structure

```
mog-ai/
├── .gitignore                     # Git ignore patterns (stays in root)
├── README.md                      # Project documentation (stays in root)
├── wsgi.py                        # WSGI entry point for production deployment
│
├── src/                          # Main application source code
│   ├── __init__.py              # App initialization and factory
│   ├── extensions.py            # Flask extensions setup
│   ├── routes/                  # All application routes
│   │   ├── web/                # Web interface routes
│   │   │   ├── __init__.py    # Main web routes
│   │   │   ├── face_swap.py   # Face swap interface routes
│   │   │   ├── looks_analysis.py # Look analysis routes
│   │   │   └── ai_video.py    # AI video generation routes
│   │   └── api/               # API routes
│   │       ├── __init__.py    # API initialization
│   │       └── face_swap.py   # Face swap API endpoints
│   ├── services/                # Business logic services
│   │   ├── face_swap/         # Face swap service
│   │   │   ├── __init__.py    # Service initialization
│   │   │   ├── service.py     # Main service logic
│   │   │   ├── processor.py   # Image processing
│   │   │   └── validator.py   # Input validation
│   │   ├── looks_analysis/    # Look analysis service
│   │   │   ├── __init__.py    # Service initialization
│   │   │   └── service.py     # Analysis logic
│   │   └── ai_video/         # AI video service
│   │       ├── __init__.py    # Service initialization
│   │       └── service.py     # Video generation logic
│   ├── models/                  # Data models
│   │   └── __init__.py        # Models initialization
│   └── utils/                  # Utility functions
│       ├── image_utils.py     # Image manipulation utilities
│       └── security.py       # Security utilities
│
├── deployment/                   # Deployment configuration
│   ├── gunicorn.conf.py        # Gunicorn config
│   ├── Procfile               # Heroku config
│   └── requirements.txt       # Python dependencies
│
├── instance/                     # Instance-specific files (gitignored)
│   ├── .env                    # Environment variables (contient HUGGING_FACE_API_KEY, VIDEO_AI_MODEL, MODEL_CACHE_PATH, RESULTS_PATH)
│   └── flask_monitoringdashboard.db  # Performance monitoring DB
│
├── config/                      # Configuration files
│   ├── __init__.py            # Config initialization
│   └── config.py              # Main configuration
│
├── static/                      # Static files
│   ├── css/                   # Stylesheets
│   │   ├── main.css         # Main styles
│   │   └── tailwind.css    # Tailwind output
│   ├── js/                    # JavaScript files
│   │   ├── face-swap.js     # Face swap functionality
│   │   ├── looks-analysis.js # Look analysis functionality
│   │   └── ai-video.js      # Video generation functionality
│   └── images/                # Image assets
│       ├── assets/           # UI assets (logos, icons)
│       └── examples/         # Example images
│
├── templates/                   # HTML templates
│   ├── base.html             # Base template with common layout
│   ├── index.html           # Landing page
│   ├── components/          # Reusable UI components
│   │   ├── navbar.html     # Navigation bar
│   │   ├── sidebar.html    # Sidebar menu
│   │   └── footer.html     # Footer component
│   ├── face_swap/          # Face swap templates
│   │   └── index.html      # Face swap interface
│   ├── looks_analysis/     # Look analysis templates
│   │   └── index.html      # Analysis interface
│   └── web/               # Web interface templates
│       └── ai_video/      # AI video templates
│           └── index.html # Video generation interface
│
├── scripts/                     # Utility scripts
│   ├── clean.py             # Cleanup script
│   └── start.bat           # Windows startup script
│
├── tests/                      # Test suite
│   ├── __init__.py
│   ├── conftest.py         # Test configuration
│   ├── test_services/     # Service tests
│   └── test_routes/      # Route tests
│
├── docs/                       # Documentation
│   ├── api/                  # API documentation
│   ├── deployment/          # Deployment guides
│   └── development/        # Development guides
│
└── aide/                       # Additional documentation
    └── structure_scalable.md  # Project structure guide

```

## File Organization Rules

### Root Directory Files
Only essential project files should remain in the root directory:
- `.gitignore` - Git ignore patterns
- `README.md` - Project documentation
- `wsgi.py` - Production WSGI entry point
- `app.py` - Development entry point

### WSGI Configuration (`wsgi.py`)
Le fichier `wsgi.py` est crucial pour le déploiement en production :
- Sert d'interface entre le serveur web (Gunicorn, uWSGI) et l'application Flask
- Permet le déploiement sur des serveurs de production
- Suit le standard WSGI (Web Server Gateway Interface)
- Sépare la configuration de développement de celle de production

Exemple d'utilisation avec Gunicorn :
```bash
gunicorn wsgi:app
```

### Deployment Files (`deployment/`)
All deployment-related files:
- `requirements.txt` - Python dependencies
- `gunicorn.conf.py` - Gunicorn configuration
- `Procfile` - Heroku configuration

### Instance Files (`instance/`)
Instance-specific files that should not be versioned:
- `.env` - Environment variables (contient HUGGING_FACE_API_KEY, VIDEO_AI_MODEL, MODEL_CACHE_PATH, RESULTS_PATH)
- `flask_monitoringdashboard.db` - Monitoring database
- Temporary files
- Local configurations

### Accès au fichier .env dans Cursor

IMPORTANT : Contrairement à ce qu'on pourrait penser, même si le fichier `.env` est listé dans `.cursorignore`, il reste accessible via les outils de lecture de Cursor. Voici comment y accéder :

1. **Méthode d'accès direct**
   - Utiliser le chemin relatif : `instance/.env`
   - Les outils de lecture de Cursor peuvent accéder au fichier malgré `.cursorignore`
   - Le fichier est protégé mais reste lisible pour les opérations autorisées

2. **Structure du fichier**
   Le fichier `.env` contient les configurations suivantes :
   ```env
   # Configurations Flask
   FLASK_APP=app
   FLASK_ENV=development
   FLASK_DEBUG=1
   FLASK_RUN_PORT=5001

   # Chemins du projet
   PROJECT_ROOT=D:\Projet
   
   # Configuration Hugging Face
   HUGGING_FACE_API_KEY=votre_clé_ici
   VIDEO_AI_MODEL=modelscope/damo-text-to-video-synthesis
   
   # Chemins des données
   MODEL_CACHE_PATH=D:\Projet\temp\models
   RESULTS_PATH=D:\Projet\temp\results
   ```

3. **Sécurité**
   - Le fichier reste protégé contre les modifications accidentelles
   - Les valeurs sensibles sont sécurisées
   - Git continue d'ignorer le fichier grâce à `.gitignore`
   - Cursor peut lire le fichier mais de manière contrôlée

4. **Bonnes pratiques**
   - Ne jamais commiter le fichier `.env`
   - Maintenir un `.env.example` pour la documentation
   - Sauvegarder les valeurs sensibles de manière sécurisée
   - Utiliser des chemins absolus pour les dossiers de données

## Essential Components

### 1. Core Application (`src/`)
- **__init__.py**: Application factory and initialization
- **extensions.py**: Flask extensions setup
- **routes/**: All application endpoints
- **services/**: Core business logic
- **utils/**: Shared utilities

### 2. Configuration (`config/`)
- **config.py**: Environment-specific configurations
- **.env**: Environment variables (in instance/)

### 3. Templates and Static Files
- **templates/**: All HTML templates
- **static/**: CSS, JavaScript, images
- **uploads/**: Temporary file storage

### 4. Deployment Files
- **requirements.txt**: Python dependencies
- **Procfile**: Heroku configuration
- **gunicorn.conf.py**: Gunicorn settings

## Non-Essential but Recommended Components

### 1. Development Tools
- **.gitignore**: Git ignore patterns
- **scripts/**: Utility scripts
- **tests/**: Test suite
- **docs/**: Documentation

### 2. Monitoring and Debugging
- **flask_monitoringdashboard.db**: Performance monitoring
- **logs/**: Application logs (if needed)

## Directory Purposes

### src/
- Core application logic
- Route definitions
- Service implementations
- Utility functions

### config/
- Configuration management
- Environment-specific settings
- Secret management

### static/
- User-facing assets
- Uploaded files (temporary)
- CSS and JavaScript

### templates/
- HTML templates
- Reusable components
- Page layouts

### scripts/
- Development utilities
- Deployment scripts
- Maintenance tools

### tests/
- Unit tests
- Integration tests
- Test fixtures

### docs/
- API documentation
- Development guides
- Deployment instructions

### instance/
- Environment-specific files
- Sensitive configurations
- Temporary data

## Best Practices

### 1. Code Organization
- Keep related files together
- Use clear, descriptive names
- Maintain consistent structure

### 2. Configuration
- Use environment variables
- Separate config by environment
- Keep secrets in .env

### 3. Security
- Store uploads securely
- Validate user input
- Implement rate limiting

### 4. Development
- Follow PEP 8
- Write tests
- Document code

### 5. Deployment
- Use version control
- Implement CI/CD
- Monitor performance

## Common Issues and Solutions

### 1. File Organization
- **Issue**: Files in root directory
- **Solution**: Move to appropriate subdirectories

### 2. Configuration
- **Issue**: Hardcoded settings
- **Solution**: Use environment variables

### 3. Security
- **Issue**: Exposed secrets
- **Solution**: Use .env files

### 4. Development
- **Issue**: Missing documentation
- **Solution**: Maintain README and docs

## Required Environment Variables

```env
FLASK_APP=src
FLASK_ENV=development
SECRET_KEY=your-secret-key
HUGGING_FACE_API_KEY=your-api-key
REDIS_URL=redis://localhost:6379
MAX_CONTENT_LENGTH=5242880
```

## Running the Application

### Development
```bash
# Set environment variables
export FLASK_APP=src
export FLASK_ENV=development

# Install dependencies
pip install -r requirements.txt

# Run the application
flask run
```

### Production
```bash
# Using gunicorn
gunicorn -c deployment/gunicorn.conf.py "src:create_app()"
```

## Maintenance

### Regular Tasks
1. Clean temporary files
2. Update dependencies
3. Run tests
4. Monitor performance
5. Backup data

### Security
1. Update dependencies
2. Review access logs
3. Check for vulnerabilities
4. Update SSL certificates

## Troubleshooting

### Common Issues
1. Missing dependencies
2. Configuration errors
3. Permission issues
4. Storage problems

### Solutions
1. Check requirements.txt
2. Verify .env file
3. Check file permissions
4. Clean temporary files 

## Template Structure Details

### Base Template (base.html)
- Contains the main layout structure
- Includes necessary CSS and JavaScript
- Defines blocks for content injection
- Implements responsive sidebar navigation
- Handles user authentication state

```html
{% block content %}
<!-- Content goes here -->
{% endblock %}

{% block scripts %}
<!-- Page-specific scripts -->
{% endblock %}
```

### Page Templates
Each page template should:
- Extend base.html
- Define page-specific title
- Implement required content blocks
- Include necessary scripts
- Follow consistent structure

Example:
```html
{% extends "base.html" %}

{% block title %}Page Title{% endblock %}

{% block content %}
<div class="container mx-auto px-4">
    <!-- Page content -->
</div>
{% endblock %}
```

### Component Structure
Components should be:
- Reusable across pages
- Self-contained
- Well-documented
- Easy to maintain

Example component (components/upload.html):
```html
<div class="upload-component">
    <input type="file" class="hidden" id="{{ input_id }}">
    <label for="{{ input_id }}" class="upload-label">
        <!-- Upload UI -->
    </label>
</div>
```

## Frontend Best Practices

### 1. CSS Organization
- Use Tailwind CSS utility classes
- Keep custom CSS minimal
- Follow BEM naming convention for custom classes
- Maintain consistent spacing and layout

### 2. JavaScript Structure
- Use ES6+ features
- Implement error handling
- Add loading states
- Follow modular pattern

Example:
```javascript
// face-swap.js
const FaceSwap = {
    init() {
        // Initialize
    },
    handleUpload() {
        // Handle file upload
    },
    processImages() {
        // Process images
    }
};
```

### 3. Error Handling
- Display user-friendly error messages
- Implement proper form validation
- Show loading states during operations
- Handle API errors gracefully

### 4. Performance
- Lazy load images
- Minimize JavaScript bundles
- Use proper caching strategies
- Optimize asset delivery

## Backend Structure Details

### Route Organization
- Group related routes in blueprints
- Use consistent URL patterns
- Implement proper error handling
- Add request validation

Example:
```python
@bp.route('/face-swap', methods=['POST'])
def face_swap():
    try:
        # Process request
        return jsonify(result)
    except Exception as e:
        return handle_error(e)
```

### Service Layer
- Separate business logic from routes
- Implement proper error handling
- Use dependency injection
- Follow SOLID principles

Example:
```python
class FaceSwapService:
    def __init__(self, processor):
        self.processor = processor

    def process_images(self, source, target):
        # Process images
        return result
```

## Common Mistakes to Avoid

### 1. Frontend
- ❌ Mixing presentation and logic
- ❌ Inconsistent styling
- ❌ Poor error handling
- ❌ Unresponsive design

### 2. Backend
- ❌ Mixing concerns in routes
- ❌ Poor error handling
- ❌ Lack of input validation
- ❌ Missing documentation

### 3. Security
- ❌ Exposing sensitive information
- ❌ Missing input sanitization
- ❌ Weak authentication
- ❌ Insecure file handling

## Best Practices Checklist

### Frontend
✅ Use semantic HTML
✅ Follow responsive design principles
✅ Implement proper error handling
✅ Add loading states
✅ Validate user input
✅ Use consistent styling
✅ Optimize performance
✅ Add proper documentation

### Backend
✅ Separate concerns
✅ Implement proper validation
✅ Handle errors gracefully
✅ Use proper status codes
✅ Add logging
✅ Secure endpoints
✅ Document API endpoints
✅ Follow RESTful principles 