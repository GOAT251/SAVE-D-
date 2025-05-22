from src.services.looks_analysis.service import LooksAnalysisService
import os
from werkzeug.datastructures import FileStorage
from PIL import Image, ImageDraw

def create_test_outfit_image():
    """Create a test image with multiple colors to simulate an outfit"""
    img = Image.new('RGB', (300, 400), color='white')
    draw = ImageDraw.Draw(img)
    
    # Draw a blue shirt
    draw.rectangle([50, 50, 250, 200], fill='#3B82F6')
    
    # Draw brown pants
    draw.rectangle([75, 200, 225, 350], fill='#92400E')
    
    # Draw some red accessories
    draw.ellipse([100, 25, 130, 55], fill='#EF4444')
    
    # Save the image
    image_path = "static/images/examples/test_outfit.jpg"
    os.makedirs(os.path.dirname(image_path), exist_ok=True)
    img.save(image_path)
    return image_path

def test_looks_analysis():
    # Create a test image with multiple colors
    image_path = create_test_outfit_image()
    
    # Open the image file
    with open(image_path, 'rb') as img_file:
        # Create a proper FileStorage object
        test_image = FileStorage(
            stream=img_file,
            filename="test_outfit.jpg",
            content_type="image/jpeg"
        )
        
        # Initialize the service
        print("Initializing service...")
        analyzer = LooksAnalysisService(model_name="test_model")
        
        # Test the analysis with the multi-color image
        print(f"\nAnalyzing outfit image: {image_path}")
        results = analyzer.analyze_image(test_image)
        
        # Print results
        print("\n=== Analysis Results ===")
        
        print("\nStyles:")
        for style, score in results["style"].items():
            print(f"- {style}: {score}%")
        
        print("\nCouleurs:")
        for color in results["colors"]:
            print(f"- {color['name']} ({color['hex']}) : {color['percentage']}%")
        
        print("\nRecommandations:")
        for rec in results["recommendations"]:
            print(f"- {rec}")

if __name__ == "__main__":
    test_looks_analysis() 