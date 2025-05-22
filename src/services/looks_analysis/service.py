"""Service logic for Looks Analysis"""
from PIL import Image, ImageStat
import io
from collections import Counter
import colorsys
import time
import hashlib
import logging

# Configuration du logger
logger = logging.getLogger(__name__)

class OptimizedLooksAnalysisService:
    def __init__(self):
        # Initialisation légère des modèles
        self.style_analyzer = LightweightStyleAnalyzer()
        self.color_analyzer = FastColorAnalyzer()
        self.cache = SimpleCache()

    def analyze_image(self, image_file) -> dict:
        """Analyse optimisée d'une image"""
        try:
            # 1. Prétraitement rapide
            image = self._preprocess_image(image_file)
            
            # 2. Génération d'une clé de cache unique
            cache_key = self.cache._generate_cache_key(image)
            cached_result = self.cache.get(cache_key)
            if cached_result:
                return cached_result

            # 3. Analyse parallèle du style et des couleurs
            style_result = self.style_analyzer.quick_analyze(image)
            color_result = self.color_analyzer.extract_dominant_colors(image, max_colors=4)

            # 4. Combinaison des résultats
            result = {
                'style': {
                    'Chic': style_result.get('chic', 0),
                    'Casual': style_result.get('casual', 0),
                    'Bohemian': style_result.get('bohemian', 0),
                    'Sporty': style_result.get('sporty', 0)
                },
                'colors': color_result,
                'recommendations': self._generate_smart_recommendations(style_result, color_result)
            }

            # 5. Mise en cache des résultats
            self.cache.set(cache_key, result, timeout=3600)
            return result

        except Exception as e:
            logger.error(f"Erreur d'analyse: {str(e)}")
            raise

    def _preprocess_image(self, image_file):
        """Prétraitement optimisé de l'image"""
        img = Image.open(image_file)
        
        # Redimensionnement intelligent
        max_size = (512, 512)  # Taille optimale pour l'analyse
        if img.size[0] > max_size[0] or img.size[1] > max_size[1]:
            img.thumbnail(max_size, Image.LANCZOS)
        
        # Conversion en RGB si nécessaire
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        return img

    def _generate_smart_recommendations(self, style_result, colors):
        """Génération rapide de recommandations pertinentes"""
        recommendations = []
        
        # 1. Recommandation basée sur le style dominant
        dominant_style = max(style_result.items(), key=lambda x: x[1])[0]
        if dominant_style == 'chic':
            recommendations.append("Ajoutez des accessoires raffinés pour renforcer votre style chic")
        elif dominant_style == 'casual':
            recommendations.append("Mixez avec une pièce élégante pour un look casual chic")
        elif dominant_style == 'bohemian':
            recommendations.append("Incorporez des textures naturelles pour accentuer le style bohème")
        elif dominant_style == 'sporty':
            recommendations.append("Associez avec une pièce structurée pour un look sport-chic")

        # 2. Recommandation basée sur les couleurs
        if len(colors) >= 2:
            main_color = colors[0]['name']
            second_color = colors[1]['name']
            recommendations.append(f"La combinaison {main_color}-{second_color} fonctionne bien, essayez d'ajouter {self._get_complementary_color(main_color)}")

        return recommendations[:3]  # Limiter à 3 recommandations pour la performance

    def _get_complementary_color(self, color_name):
        """Obtention rapide d'une couleur complémentaire"""
        color_pairs = {
            'Noir': 'Blanc',
            'Blanc': 'Noir',
            'Bleu': 'Orange',
            'Rouge': 'Vert',
            'Jaune': 'Violet'
        }
        return color_pairs.get(color_name, 'une couleur contrastante')

class LightweightStyleAnalyzer:
    """Analyseur de style léger et rapide"""
    def quick_analyze(self, image):
        # Analyse rapide basée sur les caractéristiques principales
        features = self._extract_basic_features(image)
        return self._calculate_style_scores(features)

    def _extract_basic_features(self, image):
        # Extraction des caractéristiques essentielles
        features = {
            'brightness': self._get_average_brightness(image),
            'contrast': self._get_contrast_level(image),
            'color_variety': self._get_color_variety(image),
            'color_stats': self._get_color_statistics(image),
            'texture': self._analyze_texture(image)
        }
        return features

    def _get_average_brightness(self, image):
        # Calcul de la luminosité moyenne
        stat = ImageStat.Stat(image)
        return sum(stat.mean) / len(stat.mean)

    def _get_contrast_level(self, image):
        # Calcul du contraste
        stat = ImageStat.Stat(image)
        return sum(stat.stddev) / len(stat.stddev)

    def _get_color_variety(self, image):
        # Analyse de la variété des couleurs
        colors = image.getcolors(image.size[0] * image.size[1])
        return len(colors) if colors else 0

    def _get_color_statistics(self, image):
        # Analyse des statistiques de couleur
        img_rgb = image.convert('RGB')
        pixels = list(img_rgb.getdata())
        
        # Calculer les moyennes R, G, B
        r_mean = sum(p[0] for p in pixels) / len(pixels)
        g_mean = sum(p[1] for p in pixels) / len(pixels)
        b_mean = sum(p[2] for p in pixels) / len(pixels)
        
        # Calculer la saturation moyenne
        saturations = []
        for r, g, b in pixels:
            max_rgb = max(r, g, b)
            min_rgb = min(r, g, b)
            if max_rgb == 0:
                saturations.append(0)
            else:
                saturations.append((max_rgb - min_rgb) / max_rgb)
        
        saturation_mean = sum(saturations) / len(saturations)
        
        return {
            'r_mean': r_mean,
            'g_mean': g_mean,
            'b_mean': b_mean,
            'saturation': saturation_mean
        }

    def _analyze_texture(self, image):
        # Analyse simplifiée de la texture
        img_gray = image.convert('L')
        pixels = list(img_gray.getdata())
        
        # Calculer les variations locales
        width, height = image.size
        variations = []
        
        for y in range(1, height-1):
            for x in range(1, width-1):
                center = pixels[y * width + x]
                neighbors = [
                    pixels[(y-1) * width + x],    # haut
                    pixels[(y+1) * width + x],    # bas
                    pixels[y * width + (x-1)],    # gauche
                    pixels[y * width + (x+1)]     # droite
                ]
                variation = sum(abs(n - center) for n in neighbors) / 4
                variations.append(variation)
        
        return sum(variations) / len(variations) if variations else 0

    def _calculate_style_scores(self, features):
        scores = {
            'chic': 0,
            'casual': 0,
            'bohemian': 0,
            'sporty': 0
        }

        # Caractéristiques de couleur
        color_stats = features['color_stats']
        brightness = features['brightness']
        contrast = features['contrast']
        texture = features['texture']
        color_variety = features['color_variety']

        # Score Chic
        # - Préfère les couleurs sombres ou neutres
        # - Contraste modéré à élevé
        # - Texture raffinée
        if brightness < 128:  # Couleurs sombres
            scores['chic'] += 30
        if 50 < contrast < 100:  # Contraste modéré
            scores['chic'] += 20
        if texture < 20:  # Texture raffinée
            scores['chic'] += 20
        if color_variety < 1000:  # Palette de couleurs limitée
            scores['chic'] += 30

        # Score Casual
        # - Couleurs moyennes
        # - Contraste modéré
        # - Texture moyenne
        if 100 < brightness < 180:  # Couleurs moyennes
            scores['casual'] += 25
        if 30 < contrast < 70:  # Contraste modéré
            scores['casual'] += 25
        if 10 < texture < 30:  # Texture moyenne
            scores['casual'] += 25
        if 500 < color_variety < 2000:  # Palette modérée
            scores['casual'] += 25

        # Score Bohemian
        # - Couleurs chaudes et saturées
        # - Contraste varié
        # - Texture riche
        if color_stats['saturation'] > 0.6:  # Couleurs saturées
            scores['bohemian'] += 30
        if color_variety > 2000:  # Grande variété de couleurs
            scores['bohemian'] += 30
        if texture > 25:  # Texture riche
            scores['bohemian'] += 40

        # Score Sporty
        # - Couleurs vives
        # - Contraste élevé
        # - Texture technique
        if brightness > 170:  # Couleurs vives
            scores['sporty'] += 25
        if contrast > 80:  # Contraste élevé
            scores['sporty'] += 25
        if 15 < texture < 25:  # Texture technique
            scores['sporty'] += 25
        if color_stats['saturation'] > 0.7:  # Couleurs saturées
            scores['sporty'] += 25

        # Normalisation des scores
        total = sum(scores.values())
        if total > 0:
            scores = {k: int((v / total) * 100) for k, v in scores.items()}

        return scores

class FastColorAnalyzer:
    """Analyseur de couleurs rapide et efficace"""
    def extract_dominant_colors(self, image, max_colors=4):
        # Réduction de la taille pour une analyse plus rapide
        img = image.copy()
        img.thumbnail((150, 150))

        # Conversion en RGB si nécessaire
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Obtention des couleurs dominantes
        pixels = img.getcolors(img.size[0] * img.size[1])
        if not pixels:
            return []

        # Tri par fréquence
        sorted_colors = sorted(pixels, key=lambda x: x[0], reverse=True)
        
        # Conversion en format hex et nommage des couleurs
        results = []
        total_pixels = sum(count for count, _ in sorted_colors)
        
        for count, (r, g, b) in sorted_colors[:max_colors]:
            hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
            percentage = (count / total_pixels) * 100
            
            results.append({
                'hex': hex_color,
                'name': self._get_color_name(r, g, b),
                'percentage': round(percentage, 1)
            })

        return results

    def _get_color_name(self, r, g, b):
        """Obtention rapide du nom de la couleur"""
        # Logique simplifiée de nommage des couleurs
        if max(r, g, b) < 30:
            return 'Noir'
        if min(r, g, b) > 225:
            return 'Blanc'
        if r > max(g, b) + 30:
            return 'Rouge'
        if g > max(r, b) + 30:
            return 'Vert'
        if b > max(r, g) + 30:
            return 'Bleu'
        return 'Neutre'

class SimpleCache:
    """Cache simple et léger"""
    def __init__(self):
        self._cache = {}
        self._timestamps = {}

    def get(self, key):
        """Récupération depuis le cache avec vérification de l'expiration"""
        if key in self._cache:
            timestamp = self._timestamps.get(key, 0)
            if time.time() - timestamp < 3600:  # 1 heure de validité
                return self._cache[key]
            else:
                del self._cache[key]
                del self._timestamps[key]
        return None

    def set(self, key, value, timeout=3600):
        """Stockage dans le cache avec timestamp"""
        self._cache[key] = value
        self._timestamps[key] = time.time()

    def _generate_cache_key(self, image):
        """Génération d'une clé de cache unique basée sur l'image"""
        return hashlib.md5(image.tobytes()).hexdigest()

# Example usage (for testing purposes, not part of the actual service class)
if __name__ == '__main__':
    # This part is for local testing of the service, it won't run in Flask
    class MockFileStorage:
        def __init__(self, filename):
            self.filename = filename
            self._file = open(filename, 'rb')
        
        def read(self):
            return self._file.read()
        
        def close(self):
            self._file.close()

    # Create a test image
    test_image = Image.new('RGB', (100, 100), color='red')
    test_image_path = "test_image.jpg"
    test_image.save(test_image_path)
    
    # Test the service
    mock_image = MockFileStorage(test_image_path)
    analyzer = OptimizedLooksAnalysisService()
    results = analyzer.analyze_image(mock_image)
    
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
    
    # Cleanup
    mock_image.close()
    import os
    os.remove(test_image_path) 