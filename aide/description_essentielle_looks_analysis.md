# Description Essentielle - Looks Analysis (/web/looks-analysis)

## Structure Visuelle

### Interface Principale
```html
<div class="container mx-auto px-4 py-8">
    <!-- En-tête -->
    <header class="mb-8">
        <h1 class="text-3xl md:text-4xl font-bold gradient-text">
            Analyse de Style
        </h1>
        <p class="mt-2 text-gray-600">
            Obtenez une analyse détaillée de votre style vestimentaire
        </p>
    </header>

    <!-- Contenu Principal -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
        <!-- Zone de Upload -->
        <div class="lg:col-span-4">
            <div class="bg-white rounded-xl shadow-lg p-6">
                <h2 class="text-xl font-semibold mb-6">
                    Téléchargez votre photo
                </h2>

                <!-- Upload Zone -->
                <div class="upload-zone">
                    <input type="file" 
                           id="look-image" 
                           class="hidden" 
                           accept="image/*"
                           @change="handleImageUpload">
                    
                    <label for="look-image" 
                           class="relative block w-full aspect-square border-2 
                                  border-dashed border-gray-300 rounded-lg 
                                  hover:border-indigo-500 transition-colors 
                                  cursor-pointer">
                        
                        <!-- État Initial -->
                        <div v-if="!imagePreview" 
                             class="absolute inset-0 flex flex-col items-center 
                                    justify-center text-gray-500">
                            <svg class="w-12 h-12 mb-4" fill="none" stroke="currentColor">
                                <!-- Icône upload -->
                            </svg>
                            <span class="text-sm">
                                Cliquez ou glissez une photo
                            </span>
                        </div>

                        <!-- Prévisualisation -->
                        <img v-else 
                             :src="imagePreview" 
                             class="absolute inset-0 w-full h-full object-cover rounded-lg">
                    </label>
                </div>

                <!-- Options d'Analyse -->
                <div class="mt-6 space-y-4">
                    <div class="form-group">
                        <label class="block text-sm font-medium text-gray-700">
                            Type d'Analyse
                        </label>
                        <select v-model="analysisType" 
                                class="mt-1 block w-full rounded-md border-gray-300">
                            <option value="full">Analyse Complète</option>
                            <option value="style">Style Uniquement</option>
                            <option value="colors">Couleurs Uniquement</option>
                        </select>
                    </div>

                    <button @click="analyzeImage"
                            :disabled="!imagePreview || processing"
                            class="w-full py-3 px-4 bg-indigo-600 text-white rounded-lg
                                   hover:bg-indigo-700 focus:outline-none focus:ring-2
                                   focus:ring-indigo-500 focus:ring-offset-2
                                   disabled:opacity-50 disabled:cursor-not-allowed">
                        {{ processing ? 'Analyse en cours...' : 'Analyser' }}
                    </button>
                </div>
            </div>
        </div>

        <!-- Zone de Résultats -->
        <div class="lg:col-span-8">
            <div class="bg-white rounded-xl shadow-lg p-6">
                <h2 class="text-xl font-semibold mb-6">Résultats de l'Analyse</h2>

                <!-- Loading State -->
                <div v-if="processing" 
                     class="flex flex-col items-center justify-center py-12">
                    <div class="loading-spinner"></div>
                    <div class="mt-4 text-gray-600">
                        Analyse en cours...
                    </div>
                </div>

                <!-- Résultats -->
                <div v-else-if="results" class="space-y-8">
                    <!-- Style Analysis -->
                    <section v-if="results.style" class="space-y-4">
                        <h3 class="text-lg font-semibold">Style Vestimentaire</h3>
                        <div class="grid grid-cols-2 gap-4">
                            <div v-for="(score, style) in results.style" 
                                 :key="style"
                                 class="bg-gray-50 p-4 rounded-lg">
                                <div class="text-sm font-medium text-gray-700">
                                    {{ style }}
                                </div>
                                <div class="mt-2 relative pt-1">
                                    <div class="overflow-hidden h-2 text-xs flex 
                                                rounded bg-gray-200">
                                        <div :style="{ width: `${score}%` }"
                                             class="shadow-none flex flex-col text-center 
                                                    whitespace-nowrap text-white justify-center 
                                                    bg-indigo-500">
                                        </div>
                                    </div>
                                    <span class="text-xs text-gray-600 mt-1">
                                        {{ score }}%
                                    </span>
                                </div>
                            </div>
                        </div>
                    </section>

                    <!-- Color Analysis -->
                    <section v-if="results.colors" class="space-y-4">
                        <h3 class="text-lg font-semibold">Palette de Couleurs</h3>
                        <div class="flex flex-wrap gap-4">
                            <div v-for="color in results.colors" 
                                 :key="color.hex"
                                 class="color-chip">
                                <div class="w-12 h-12 rounded-lg shadow-inner"
                                     :style="{ backgroundColor: color.hex }">
                                </div>
                                <span class="text-xs text-gray-600 mt-1">
                                    {{ color.name }}
                                </span>
                            </div>
                        </div>
                    </section>

                    <!-- Recommendations -->
                    <section v-if="results.recommendations" class="space-y-4">
                        <h3 class="text-lg font-semibold">Recommandations</h3>
                        <div class="bg-gray-50 rounded-lg p-6">
                            <ul class="space-y-3">
                                <li v-for="(rec, index) in results.recommendations" 
                                    :key="index"
                                    class="flex items-start">
                                    <svg class="w-5 h-5 text-indigo-500 mr-2 mt-0.5" 
                                         fill="none" 
                                         stroke="currentColor">
                                        <!-- Icône check -->
                                    </svg>
                                    <span class="text-gray-700">{{ rec }}</span>
                                </li>
                            </ul>
                        </div>
                    </section>
                </div>

                <!-- État Initial -->
                <div v-else class="flex flex-col items-center justify-center py-12 text-gray-500">
                    <svg class="w-16 h-16 mb-4" fill="none" stroke="currentColor">
                        <!-- Icône analyse -->
                    </svg>
                    <p>Téléchargez une photo pour commencer l'analyse</p>
                </div>
            </div>
        </div>
    </div>
</div>
```

## Styles CSS

### Classes Spécifiques
```css
.upload-zone {
    @apply relative;
    
    &:hover .upload-overlay {
        @apply opacity-100;
    }
}

.upload-overlay {
    @apply absolute inset-0 bg-black bg-opacity-50 
           flex items-center justify-center text-white
           opacity-0 transition-opacity duration-200;
}

.color-chip {
    @apply flex flex-col items-center;
}

.loading-spinner {
    @apply w-12 h-12 border-4 border-indigo-500 border-t-transparent 
           rounded-full animate-spin;
}
```

### Animations
```css
@keyframes fade-up {
    0% {
        opacity: 0;
        transform: translateY(20px);
    }
    100% {
        opacity: 1;
        transform: translateY(0);
    }
}

.result-section {
    animation: fade-up 0.5s ease-out forwards;
}
```

## JavaScript (looks-analysis.js)

### Logique d'Analyse
```javascript
const LooksAnalysis = {
    data() {
        return {
            imageFile: null,
            imagePreview: null,
            analysisType: 'full',
            processing: false,
            results: null,
            error: null
        }
    },

    methods: {
        async handleImageUpload(event) {
            const file = event.target.files[0];
            if (!this.validateImage(file)) return;
            
            this.imageFile = file;
            this.imagePreview = await this.createPreview(file);
            this.results = null;  // Reset results
        },

        validateImage(file) {
            const validTypes = ['image/jpeg', 'image/png', 'image/webp'];
            if (!validTypes.includes(file.type)) {
                this.error = 'Format d\'image non supporté';
                return false;
            }
            
            const maxSize = 5 * 1024 * 1024;  // 5MB
            if (file.size > maxSize) {
                this.error = 'Image trop volumineuse';
                return false;
            }
            
            return true;
        },

        async createPreview(file) {
            return new Promise((resolve) => {
                const reader = new FileReader();
                reader.onload = (e) => resolve(e.target.result);
                reader.readAsDataURL(file);
            });
        },

        async analyzeImage() {
            if (!this.imageFile) return;

            this.processing = true;
            this.error = null;

            try {
                const formData = new FormData();
                formData.append('image', this.imageFile);
                formData.append('type', this.analysisType);

                const response = await fetch('/web/looks-analysis/analyze', {
                    method: 'POST',
                    body: formData
                });

                if (!response.ok) throw new Error('Erreur d\'analyse');

                const data = await response.json();
                this.results = data;

                // Analytics
                this.trackAnalysis();

            } catch (error) {
                this.error = error.message;
            } finally {
                this.processing = false;
            }
        },

        trackAnalysis() {
            analytics.track('look_analyzed', {
                type: this.analysisType
            });
        }
    }
};
```

## Backend (routes/web/looks_analysis.py)

### Route Web
```python
@bp.route('/looks-analysis')
def looks_analysis():
    """Page d'analyse de style"""
    return render_template(
        'web/looks_analysis/index.html',
        config=get_analysis_config()
    )

def get_analysis_config():
    """Configuration pour le frontend"""
    return {
        'maxFileSize': current_app.config['MAX_CONTENT_LENGTH'],
        'supportedFormats': ['image/jpeg', 'image/png', 'image/webp'],
        'analysisTypes': [
            {'value': 'full', 'label': 'Analyse Complète'},
            {'value': 'style', 'label': 'Style Uniquement'},
            {'value': 'colors', 'label': 'Couleurs Uniquement'}
        ]
    }
```

### Route API
```python
@bp.route('/looks-analysis/analyze', methods=['POST'])
@limiter.limit("5 per minute")  # Rate limiting
def analyze_look():
    """Analyse d'image"""
    try:
        if 'image' not in request.files:
            raise ValueError('Image manquante')

        image = request.files['image']
        analysis_type = request.form.get('type', 'full')

        # Validation
        if not allowed_file(image.filename):
            raise ValueError('Format de fichier non supporté')

        # Analyse
        result = looks_service.analyze(
            image=image,
            analysis_type=analysis_type
        )

        return jsonify({
            'success': True,
            'results': result
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400
```

## Service (services/looks_analysis/service.py)

### Logique Métier
```python
class LooksAnalysisService:
    def __init__(self):
        self.style_model = load_style_model()
        self.color_model = load_color_model()
        self.cache = Cache()

    def analyze(self, image, analysis_type='full'):
        """Analyse d'une image"""
        try:
            # Validation
            self._validate_image(image)

            # Prétraitement
            img = self._preprocess_image(image)

            # Cache check
            cache_key = self._generate_cache_key(img, analysis_type)
            cached_result = self.cache.get(cache_key)
            if cached_result:
                return cached_result

            # Analyse
            result = {}

            if analysis_type in ['full', 'style']:
                result['style'] = self._analyze_style(img)

            if analysis_type in ['full', 'colors']:
                result['colors'] = self._analyze_colors(img)

            if analysis_type == 'full':
                result['recommendations'] = self._generate_recommendations(
                    style=result['style'],
                    colors=result['colors']
                )

            # Cache result
            self.cache.set(cache_key, result)

            return result

        except Exception as e:
            logger.error(f"Look analysis failed: {str(e)}")
            raise

    def _validate_image(self, image):
        """Validation de l'image"""
        if not image:
            raise ValueError("Image manquante")

        # Vérification du format
        if not self._allowed_file(image.filename):
            raise ValueError("Format de fichier non supporté")

    def _preprocess_image(self, image):
        """Prétraitement de l'image"""
        img = Image.open(image)
        
        # Redimensionnement si nécessaire
        if img.size[0] > 1024 or img.size[1] > 1024:
            img.thumbnail((1024, 1024))
        
        return img

    def _analyze_style(self, image):
        """Analyse du style vestimentaire"""
        features = self.style_model.extract_features(image)
        
        return {
            'casual': self._calculate_score(features, 'casual'),
            'formal': self._calculate_score(features, 'formal'),
            'sporty': self._calculate_score(features, 'sporty'),
            'elegant': self._calculate_score(features, 'elegant')
        }

    def _analyze_colors(self, image):
        """Analyse des couleurs"""
        colors = self.color_model.extract_colors(image)
        
        return [
            {
                'hex': color.hex,
                'name': self._get_color_name(color),
                'percentage': color.percentage
            }
            for color in colors
        ]

    def _generate_recommendations(self, style, colors):
        """Génération des recommandations"""
        recommendations = []

        # Style recommendations
        dominant_style = max(style.items(), key=lambda x: x[1])[0]
        recommendations.extend(
            self._get_style_recommendations(dominant_style)
        )

        # Color recommendations
        color_palette = [color['name'] for color in colors]
        recommendations.extend(
            self._get_color_recommendations(color_palette)
        )

        return recommendations

    @staticmethod
    def _allowed_file(filename):
        """Vérifie l'extension du fichier"""
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'webp'}
```

## Tests

### Tests Frontend
```javascript
describe('LooksAnalysis Component', () => {
    test('valide les formats d\'image', () => {
        const component = mount(LooksAnalysis);
        
        // Test fichier valide
        const validFile = new File([''], 'test.jpg', { type: 'image/jpeg' });
        expect(component.vm.validateImage(validFile)).toBe(true);

        // Test fichier invalide
        const invalidFile = new File([''], 'test.txt', { type: 'text/plain' });
        expect(component.vm.validateImage(invalidFile)).toBe(false);
    });
});
```

### Tests Backend
```python
def test_look_analysis():
    """Test d'analyse de style"""
    with open('tests/fixtures/outfit.jpg', 'rb') as image:
        response = client.post(
            '/web/looks-analysis/analyze',
            data={
                'image': image,
                'type': 'full'
            },
            content_type='multipart/form-data'
        )

        assert response.status_code == 200
        assert response.json['success'] is True
        assert 'style' in response.json['results']
        assert 'colors' in response.json['results']
```

## Sécurité

### Validation des Fichiers
```python
def validate_image(file):
    """Validation complète de l'image"""
    # Vérification du format
    if not allowed_file(file.filename):
        raise ValueError('Format non supporté')

    # Vérification de la taille
    content = file.read()
    file.seek(0)
    if len(content) > current_app.config['MAX_CONTENT_LENGTH']:
        raise ValueError('Image trop volumineuse')

    # Vérification du contenu
    try:
        with Image.open(file) as img:
            img.verify()
    except:
        raise ValueError('Image corrompue')
```

### Protection CSRF
```python
@bp.route('/looks-analysis/analyze', methods=['POST'])
@csrf.protect()
def analyze_look():
    # Implementation
```

## Monitoring

### Logging
```python
def log_analysis(image_info, result):
    """Log d'analyse"""
    logger.info(
        'Look analysis completed',
        extra={
            'image_size': image_info['size'],
            'analysis_type': image_info['type'],
            'processing_time': result['processing_time']
        }
    )
```

### Métriques
```python
def track_analysis_metrics(result):
    """Suivi des métriques d'analyse"""
    metrics.increment('looks_analysis_total')
    metrics.timing('analysis_processing_time', result['processing_time'])
    metrics.gauge('analysis_queue_size', queue.size())
``` 