"""
Face Swap Service Package
Provides secure face swapping functionality with proper API key handling
"""

from .service import FaceSwapService
from .processor import ImageProcessor
from .validator import ImageValidator

# Expose FaceSwapService as FaceSwap for backward compatibility
FaceSwap = FaceSwapService

__all__ = ['FaceSwap', 'FaceSwapService', 'ImageProcessor', 'ImageValidator'] 