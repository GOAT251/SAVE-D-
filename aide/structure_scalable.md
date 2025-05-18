# M.O.G AI - Project Structure Documentation

## Core Project Structure

```
mog-ai/
├── .gitignore                     # Git ignore patterns (stays in root)
├── README.md                      # Project documentation (stays in root)
│
├── src/                          # Main application source code
│   ├── __init__.py              # App initialization and factory
│   ├── extensions.py            # Flask extensions setup
│   ├── routes/                  # All application routes
│   │   ├── web/                # Web interface routes
│   │   │   ├── __init__.py    # Main web routes
│   │   │   ├── face_swap.py   # Face swap interface routes
│   │   │   └── dashboard.py   # Dashboard routes
│   │   └── api/               # API routes
│   │       ├── __init__.py    # API initialization
│   │       └── face_swap.py   # Face swap API endpoints
│   ├── services/                # Business logic services
│   │   └── face_swap/         # Face swap service
│   │       ├── __init__.py    # Service initialization
│   │       ├── service.py     # Main service logic
│   │       ├── processor.py   # Image processing
│   │       └── validator.py   # Input validation
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
│   ├── .env                    # Environment variables
│   └── flask_monitoringdashboard.db  # Performance monitoring DB
│
├── config/                      # Configuration files
│   ├── __init__.py            # Config initialization
│   └── config.py              # Main configuration
│
├── static/                      # Static files
│   ├── css/                   # Stylesheets
│   ├── js/                    # JavaScript files
│   ├── images/                # Image assets
│   │   ├── assets/           # UI assets (logos, icons)
│   │   └── examples/         # Example images
│   └── uploads/              # User uploads (temporary)
│
├── templates/                   # HTML templates
│   ├── base.html             # Base template
│   ├── index.html           # Landing page
│   ├── dashboard.html       # Dashboard template
│   └── face_swap/          # Face swap templates
│       └── index.html      # Face swap interface
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

### Deployment Files (`deployment/`)
All deployment-related files:
- `requirements.txt` - Python dependencies
- `gunicorn.conf.py` - Gunicorn configuration
- `Procfile` - Heroku configuration

### Instance Files (`instance/`)
Instance-specific files that should not be versioned:
- `.env` - Environment variables
- `flask_monitoringdashboard.db` - Monitoring database
- Temporary files
- Local configurations

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