# M.O.G AI - Face Swap & AI Video Generation Platform

## Overview
M.O.G AI (Mastering Optical Grafting) is a comprehensive web platform that provides advanced AI-powered features:
- Face swapping with state-of-the-art AI models
- AI-powered video generation
- Look analysis and style recommendations
- Modern, responsive interface with Tailwind CSS

## Core Features

### 1. Face Swap
- Upload source and target images
- Real-time preview
- Multiple AI models support
- Batch processing capability
- Result history

### 2. AI Video Generation
- Text-to-video generation
- Style transfer
- Video editing capabilities
- Export in multiple formats

### 3. Look Analysis
- Style recommendations
- Color analysis
- Outfit suggestions
- Personalized advice

## Technical Stack

### Frontend
- HTML5 with semantic markup
- Tailwind CSS for styling
- Modern JavaScript (ES6+)
- Responsive design
- Progressive enhancement

### Backend
- Flask web framework
- Blueprint architecture
- RESTful API design
- Redis for caching
- SQLAlchemy ORM

### AI Integration
- HuggingFace models
- Custom AI pipelines
- Optimized processing
- Batch operations support

## Project Structure
```
mog-ai/
├── src/                          # Application source
│   ├── routes/                  # Route definitions
│   │   ├── web/                # Web interface
│   │   └── api/                # API endpoints
│   ├── services/               # Business logic
│   ├── models/                 # Data models
│   └── utils/                  # Utilities
├── templates/                   # HTML templates
│   ├── base.html              # Base layout
│   ├── components/            # Reusable components
│   └── pages/                 # Page templates
└── static/                     # Static assets
    ├── css/                   # Stylesheets
    ├── js/                    # JavaScript
    └── images/                # Image assets
```

## Installation

### Prerequisites
- Python 3.8+
- Redis server
- Node.js (for frontend build)
- Virtual environment

### Setup Steps

1. Clone and setup:
```bash
git clone https://github.com/yourusername/mog-ai.git
cd mog-ai
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate  # Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
npm install  # For frontend assets
```

3. Configure environment:
```bash
# Create instance/.env file
FLASK_APP=src
FLASK_ENV=development
SECRET_KEY=your-secret-key
HUGGING_FACE_API_KEY=your-api-key
REDIS_URL=redis://localhost:6379
```

4. Initialize database:
```bash
flask db upgrade
```

5. Run the application:
```bash
flask run
```

## Development Guidelines

### Frontend Development

#### 1. Templates
- Extend base.html for consistency
- Use components for reusability
- Follow BEM naming convention
- Implement responsive design

Example:
```html
{% extends "base.html" %}

{% block content %}
<div class="container mx-auto">
    {% include "components/upload.html" %}
    <!-- Page content -->
</div>
{% endblock %}
```

#### 2. JavaScript
- Use modules for organization
- Implement error handling
- Add loading states
- Follow clean code principles

Example:
```javascript
const ImageProcessor = {
    async process(image) {
        try {
            // Processing logic
        } catch (error) {
            this.handleError(error);
        }
    }
};
```

### Backend Development

#### 1. Routes
- Group related endpoints
- Validate inputs
- Handle errors gracefully
- Document API endpoints

Example:
```python
@bp.route('/face-swap', methods=['POST'])
@validate_input
def face_swap():
    try:
        result = service.process(request.files)
        return jsonify(result)
    except Exception as e:
        return handle_error(e)
```

#### 2. Services
- Separate business logic
- Use dependency injection
- Write unit tests
- Add proper logging

Example:
```python
class FaceSwapService:
    def __init__(self, processor, storage):
        self.processor = processor
        self.storage = storage

    def process(self, images):
        # Processing logic
```

## Best Practices

### Security
✅ Validate all inputs
✅ Sanitize file uploads
✅ Implement rate limiting
✅ Use secure headers
✅ Handle errors safely

### Performance
✅ Optimize image processing
✅ Implement caching
✅ Lazy load assets
✅ Minimize API calls
✅ Use CDN for assets

### Code Quality
✅ Follow style guides
✅ Write unit tests
✅ Document code
✅ Review pull requests
✅ Use linting tools

## Common Issues

### 1. Application
- Check Redis connection
- Verify API keys
- Ensure proper permissions
- Monitor resource usage

### 2. Development
- Use correct virtual env
- Update dependencies
- Clear cache when needed
- Check logs for errors

## Contributing
1. Fork the repository
2. Create feature branch
3. Follow code standards
4. Write tests
5. Submit pull request

## License
MIT License - see LICENSE file

## Support
- GitHub Issues
- Documentation
- Community forum 