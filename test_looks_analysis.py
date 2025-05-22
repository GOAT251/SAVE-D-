from PIL import Image, ImageStat
import io
import os
from src.services.looks_analysis.service import OptimizedLooksAnalysisService

def test_analysis():
    # Créer une image test avec plusieurs couleurs
    img = Image.new('RGB', (300, 300))
    
    # Créer quelques zones de couleur
    for x in range(300):
        for y in range(300):
            if x < 100:
                img.putpixel((x, y), (200, 50, 50))  # Rouge
            elif x < 200:
                img.putpixel((x, y), (50, 200, 50))  # Vert
            else:
                img.putpixel((x, y), (50, 50, 200))  # Bleu

    # Sauvegarder l'image temporairement
    test_image_path = "test_outfit.jpg"
    img.save(test_image_path)

    try:
        # Créer un objet similaire à FileStorage
        class MockFileStorage:
            def __init__(self, filename):
                self.filename = filename
                self._file = open(filename, 'rb')
            
            def read(self):
                return self._file.read()
            
            def close(self):
                self._file.close()

            def __enter__(self):
                return self

            def __exit__(self, exc_type, exc_val, exc_tb):
                self.close()

        # Tester le service
        print("Initialisation du service d'analyse...")
        analyzer = OptimizedLooksAnalysisService()
        
        print(f"\nAnalyse de l'image test: {test_image_path}")
        with MockFileStorage(test_image_path) as mock_file:
            results = analyzer.analyze_image(mock_file)
        
        # Afficher les résultats
        print("\n=== Résultats de l'analyse ===")
        
        print("\nStyles:")
        for style, score in results["style"].items():
            print(f"- {style}: {score}%")
        
        print("\nCouleurs dominantes:")
        for color in results["colors"]:
            print(f"- {color['name']} ({color['hex']}) : {color['percentage']}%")
        
        print("\nRecommandations:")
        for rec in results["recommendations"]:
            print(f"- {rec}")

    finally:
        # Nettoyage
        if os.path.exists(test_image_path):
            os.remove(test_image_path)

if __name__ == "__main__":
    test_analysis() 