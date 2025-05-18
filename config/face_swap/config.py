"""Configuration for face swap service"""

class FaceSwapConfig:
    # API Configuration
    API_URL = "https://api-inference.huggingface.co/models/InstituteForTheStudyOfLearning/face-swap"
    MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    REQUEST_TIMEOUT = 30  # seconds
    
    # Cache Configuration
    CACHE_ENABLED = True
    CACHE_TIMEOUT = 3600  # 1 hour
    
    # Image Processing
    MAX_IMAGE_DIMENSION = 2048  # Maximum width/height
    JPEG_QUALITY = 85  # Quality for JPEG compression
    
    @classmethod
    def allowed_file(cls, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in cls.ALLOWED_EXTENSIONS 