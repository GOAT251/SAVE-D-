# Description Essentielle - Face Swap (/web/face-swap)

## Structure Visuelle

### Interface Principale
```html
<div class="container mx-auto px-4 py-8">
    <!-- En-tête -->
    <header class="mb-8">
        <h1 class="text-3xl md:text-4xl font-bold gradient-text">
            Face Swap IA
        </h1>
        <p class="mt-2 text-gray-600">
            Échangez des visages avec notre technologie d'IA avancée
        </p>
    </header>

    <!-- Interface principale -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
        <!-- Zone de Upload -->
        <div class="lg:col-span-4">
            <div class="bg-white rounded-xl shadow-lg p-6">
                <h2 class="text-xl font-semibold mb-6">Images Source</h2>

                <!-- Source Image -->
                <div class="space-y-6">
                    <div class="upload-container">
                        <label class="block text-sm font-medium text-gray-700 mb-2">
                            Image Source (Visage à utiliser)
                        </label>
                        <div class="relative border-2 border-dashed border-gray-300 
                                  rounded-lg aspect-square hover:border-indigo-500 
                                  transition-colors">
                            <input type="file" 
                                   id="source-image" 
                                   class="hidden" 
                                   accept="image/*"
                                   @change="handleSourceUpload">
                            
                            <!-- État Initial -->
                            <div v-if="!sourcePreview" 
                                 class="absolute inset-0 flex flex-col items-center 
                                        justify-center text-gray-500 cursor-pointer">
                                <svg class="w-12 h-12 mb-4" fill="none" stroke="currentColor">
                                    <!-- Icône upload -->
                                </svg>
                                <span class="text-sm">Cliquez pour uploader</span>
                            </div>

                            <!-- Prévisualisation -->
                            <img v-else 
                                 :src="sourcePreview" 
                                 class="absolute inset-0 w-full h-full object-cover rounded-lg">
                        </div>
                    </div>

                    <!-- Target Image -->
                    <div class="upload-container">
                        <label class="block text-sm font-medium text-gray-700 mb-2">
                            Image Cible (Où placer le visage)
                        </label>
                        <div class="relative border-2 border-dashed border-gray-300 
                                  rounded-lg aspect-square hover:border-indigo-500 
                                  transition-colors">
                            <input type="file" 
                                   id="target-image" 
                                   class="hidden" 
                                   accept="image/*"
                                   @change="handleTargetUpload">
                            
                            <!-- État Initial -->
                            <div v-if="!targetPreview" 
                                 class="absolute inset-0 flex flex-col items-center 
                                        justify-center text-gray-500 cursor-pointer">
                                <svg class="w-12 h-12 mb-4" fill="none" stroke="currentColor">
                                    <!-- Icône upload -->
                                </svg>
                                <span class="text-sm">Cliquez pour uploader</span>
                            </div>

                            <!-- Prévisualisation -->
                            <img v-else 
                                 :src="targetPreview" 
                                 class="absolute inset-0 w-full h-full object-cover rounded-lg">
                        </div>
                    </div>
                </div>

                <!-- Options -->
                <div class="mt-6 space-y-4">
                    <div class="form-group">
                        <label class="block text-sm font-medium text-gray-700">
                            Mode de Fusion
                        </label>
                        <select v-model="blendMode" 
                                class="mt-1 block w-full rounded-md border-gray-300">
                            <option value="natural">Naturel</option>
                            <option value="smooth">Lissé</option>
                            <option value="sharp">Net</option>
                        </select>
                    </div>

                    <!-- Options avancées -->
                    <div class="form-group">
                        <button type="button"
                                @click="showAdvancedOptions = !showAdvancedOptions"
                                class="text-sm text-indigo-600 hover:text-indigo-800">
                            Options avancées
                        </button>
                        
                        <div v-if="showAdvancedOptions" class="mt-4 space-y-4">
                            <!-- Intensité -->
                            <div class="form-group">
                                <label class="block text-sm font-medium text-gray-700">
                                    Intensité de la Fusion
                                </label>
                                <input type="range" 
                                       v-model="intensity" 
                                       min="0" 
                                       max="100" 
                                       class="w-full">
                                <div class="flex justify-between text-xs text-gray-500">
                                    <span>Subtil</span>
                                    <span>Fort</span>
                                </div>
                            </div>

                            <!-- Préservation -->
                            <div class="form-group">
                                <label class="block text-sm font-medium text-gray-700">
                                    Préservation des Traits
                                </label>
                                <div class="mt-2 space-y-2">
                                    <label class="flex items-center">
                                        <input type="checkbox" 
                                               v-model="preserveFeatures.skin"
                                               class="rounded text-indigo-600">
                                        <span class="ml-2 text-sm text-gray-700">
                                            Teint de peau
                                        </span>
                                    </label>
                                    <label class="flex items-center">
                                        <input type="checkbox" 
                                               v-model="preserveFeatures.expression"
                                               class="rounded text-indigo-600">
                                        <span class="ml-2 text-sm text-gray-700">
                                            Expression
                                        </span>
                                    </label>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Bouton de génération -->
                    <button @click="generateSwap"
                            :disabled="!canGenerate || processing"
                            class="w-full py-3 px-4 bg-indigo-600 text-white rounded-lg
                                   hover:bg-indigo-700 focus:outline-none focus:ring-2
                                   focus:ring-indigo-500 focus:ring-offset-2
                                   disabled:opacity-50 disabled:cursor-not-allowed">
                        {{ processing ? 'Génération en cours...' : 'Générer' }}
                    </button>
                </div>
            </div>
        </div>

        <!-- Zone de Résultat -->
        <div class="lg:col-span-8">
            <div class="bg-white rounded-xl shadow-lg p-6">
                <h2 class="text-xl font-semibold mb-6">Résultat</h2>

                <!-- Loading State -->
                <div v-if="processing" 
                     class="flex flex-col items-center justify-center py-12">
                    <div class="loading-spinner"></div>
                    <div class="mt-4 text-gray-600">
                        Génération en cours...
                        <div class="text-sm text-gray-500">
                            Cela peut prendre quelques secondes
                        </div>
                    </div>
                </div>

                <!-- Résultat -->
                <div v-else-if="result" class="space-y-4">
                    <div class="relative aspect-video rounded-lg overflow-hidden">
                        <img :src="result.url" 
                             class="w-full h-full object-contain">
                    </div>

                    <!-- Actions -->
                    <div class="flex justify-end space-x-4">
                        <button @click="downloadResult"
                                class="btn-secondary">
                            Télécharger
                        </button>
                        <button @click="shareResult"
                                class="btn-primary">
                            Partager
                        </button>
                    </div>

                    <!-- Historique -->
                    <div v-if="history.length" class="mt-8">
                        <h3 class="text-lg font-semibold mb-4">
                            Générations Précédentes
                        </h3>
                        <div class="grid grid-cols-4 gap-4">
                            <div v-for="item in history" 
                                 :key="item.id"
                                 class="relative aspect-square rounded-lg overflow-hidden
                                        cursor-pointer hover:opacity-75 transition-opacity"
                                 @click="loadFromHistory(item)">
                                <img :src="item.thumbnail" 
                                     class="w-full h-full object-cover">
                            </div>
                        </div>
                    </div>
                </div>

                <!-- État Initial -->
                <div v-else class="flex flex-col items-center justify-center py-12 text-gray-500">
                    <svg class="w-16 h-16 mb-4" fill="none" stroke="currentColor">
                        <!-- Icône swap -->
                    </svg>
                    <p>Sélectionnez deux images pour commencer</p>
                </div>
            </div>
        </div>
    </div>
</div>
```

## Styles CSS

### Classes Spécifiques
```css
.upload-container {
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

.btn-primary {
    @apply px-6 py-2 bg-indigo-600 text-white rounded-lg
           hover:bg-indigo-700 focus:outline-none focus:ring-2
           focus:ring-indigo-500 focus:ring-offset-2
           transition-colors duration-200;
}

.btn-secondary {
    @apply px-6 py-2 border border-indigo-600 text-indigo-600
           rounded-lg hover:bg-indigo-50 focus:outline-none
           focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2
           transition-colors duration-200;
}

.loading-spinner {
    @apply w-12 h-12 border-4 border-indigo-500 border-t-transparent 
           rounded-full animate-spin;
}
```

### Animations
```css
@keyframes fade-in {
    0% {
        opacity: 0;
    }
    100% {
        opacity: 1;
    }
}

.result-fade {
    animation: fade-in 0.5s ease-out forwards;
}
```

## JavaScript (face-swap.js)

### Logique de Swap
```javascript
const FaceSwap = {
    data() {
        return {
            sourceFile: null,
            sourcePreview: null,
            targetFile: null,
            targetPreview: null,
            blendMode: 'natural',
            intensity: 75,
            preserveFeatures: {
                skin: true,
                expression: false
            },
            showAdvancedOptions: false,
            processing: false,
            result: null,
            error: null,
            history: []
        }
    },

    computed: {
        canGenerate() {
            return this.sourceFile && this.targetFile && !this.processing;
        }
    },

    methods: {
        async handleSourceUpload(event) {
            const file = event.target.files[0];
            if (!this.validateImage(file)) return;
            
            this.sourceFile = file;
            this.sourcePreview = await this.createPreview(file);
            this.result = null;  // Reset result
        },

        async handleTargetUpload(event) {
            const file = event.target.files[0];
            if (!this.validateImage(file)) return;
            
            this.targetFile = file;
            this.targetPreview = await this.createPreview(file);
            this.result = null;  // Reset result
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

        async generateSwap() {
            if (!this.canGenerate) return;

            this.processing = true;
            this.error = null;

            try {
                const formData = new FormData();
                formData.append('source', this.sourceFile);
                formData.append('target', this.targetFile);
                formData.append('blend_mode', this.blendMode);
                formData.append('intensity', this.intensity);
                formData.append('preserve_skin', this.preserveFeatures.skin);
                formData.append('preserve_expression', this.preserveFeatures.expression);

                const response = await fetch('/web/face-swap/generate', {
                    method: 'POST',
                    body: formData
                });

                if (!response.ok) throw new Error('Erreur de génération');

                const data = await response.json();
                this.result = data;
                
                // Add to history
                this.addToHistory(data);

                // Analytics
                this.trackGeneration();

            } catch (error) {
                this.error = error.message;
            } finally {
                this.processing = false;
            }
        },

        async downloadResult() {
            if (!this.result?.url) return;

            try {
                const response = await fetch(this.result.url);
                const blob = await response.blob();
                const url = window.URL.createObjectURL(blob);
                
                const a = document.createElement('a');
                a.href = url;
                a.download = `face-swap-${Date.now()}.png`;
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
                window.URL.revokeObjectURL(url);

            } catch (error) {
                this.error = 'Erreur lors du téléchargement';
            }
        },

        shareResult() {
            if (!this.result?.url) return;

            if (navigator.share) {
                navigator.share({
                    title: 'Mon Face Swap',
                    text: 'Regardez ce face swap généré avec MOG AI !',
                    url: this.result.url
                });
            } else {
                // Fallback
                this.copyToClipboard(this.result.url);
            }
        },

        addToHistory(result) {
            const historyItem = {
                id: Date.now(),
                thumbnail: result.url,
                params: {
                    blendMode: this.blendMode,
                    intensity: this.intensity,
                    preserveFeatures: { ...this.preserveFeatures }
                }
            };

            this.history.unshift(historyItem);
            if (this.history.length > 8) this.history.pop();
        },

        loadFromHistory(item) {
            this.blendMode = item.params.blendMode;
            this.intensity = item.params.intensity;
            this.preserveFeatures = { ...item.params.preserveFeatures };
            this.result = { url: item.thumbnail };
        },

        trackGeneration() {
            analytics.track('face_swap_generated', {
                blend_mode: this.blendMode,
                intensity: this.intensity,
                preserve_features: this.preserveFeatures
            });
        }
    }
};
```

## Backend (routes/web/face_swap.py)

### Route Web
```python
@bp.route('/face-swap')
def face_swap():
    """Page de face swap"""
    return render_template(
        'web/face_swap/index.html',
        config=get_swap_config()
    )

def get_swap_config():
    """Configuration pour le frontend"""
    return {
        'maxFileSize': current_app.config['MAX_CONTENT_LENGTH'],
        'supportedFormats': ['image/jpeg', 'image/png', 'image/webp'],
        'blendModes': [
            {'value': 'natural', 'label': 'Naturel'},
            {'value': 'smooth', 'label': 'Lissé'},
            {'value': 'sharp', 'label': 'Net'}
        ]
    }
```

### Route API
```python
@bp.route('/face-swap/generate', methods=['POST'])
@limiter.limit("3 per minute")  # Rate limiting
def generate_swap():
    """Génération de face swap"""
    try:
        if 'source' not in request.files or 'target' not in request.files:
            raise ValueError('Images manquantes')

        source = request.files['source']
        target = request.files['target']
        
        # Paramètres
        params = {
            'blend_mode': request.form.get('blend_mode', 'natural'),
            'intensity': float(request.form.get('intensity', 75)) / 100,
            'preserve_skin': request.form.get('preserve_skin') == 'true',
            'preserve_expression': request.form.get('preserve_expression') == 'true'
        }

        # Validation
        for image in [source, target]:
            if not allowed_file(image.filename):
                raise ValueError('Format de fichier non supporté')

        # Génération
        result = swap_service.generate(
            source=source,
            target=target,
            **params
        )

        return jsonify({
            'success': True,
            'url': result['url']
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400
```

## Service (services/face_swap/service.py)

### Logique Métier
```python
class FaceSwapService:
    def __init__(self):
        self.model = load_swap_model()
        self.face_detector = load_face_detector()
        self.storage = ImageStorage()

    def generate(self, source, target, blend_mode='natural', 
                intensity=0.75, preserve_skin=True, 
                preserve_expression=False):
        """Génération de face swap"""
        try:
            # Validation
            self._validate_images(source, target)

            # Prétraitement
            source_img = self._preprocess_image(source)
            target_img = self._preprocess_image(target)

            # Détection des visages
            source_faces = self.face_detector.detect(source_img)
            target_faces = self.face_detector.detect(target_img)

            if not source_faces or not target_faces:
                raise ValueError("Aucun visage détecté")

            # Configuration
            config = self._prepare_config(
                blend_mode=blend_mode,
                intensity=intensity,
                preserve_skin=preserve_skin,
                preserve_expression=preserve_expression
            )

            # Génération
            result_img = self.model.swap_faces(
                source_img=source_img,
                target_img=target_img,
                source_faces=source_faces,
                target_faces=target_faces,
                config=config
            )

            # Post-traitement
            processed_img = self._post_process(result_img)

            # Stockage
            result_url = self.storage.save(processed_img)

            return {
                'url': result_url,
                'source_faces': len(source_faces),
                'target_faces': len(target_faces)
            }

        except Exception as e:
            logger.error(f"Face swap failed: {str(e)}")
            raise

    def _validate_images(self, source, target):
        """Validation des images"""
        for image in [source, target]:
            if not image:
                raise ValueError("Image manquante")

            if not self._allowed_file(image.filename):
                raise ValueError("Format de fichier non supporté")

    def _preprocess_image(self, image):
        """Prétraitement de l'image"""
        img = Image.open(image)
        
        # Redimensionnement si nécessaire
        if img.size[0] > 1024 or img.size[1] > 1024:
            img.thumbnail((1024, 1024))
        
        return img

    def _prepare_config(self, **kwargs):
        """Préparation de la configuration"""
        return {
            'blend_mode': kwargs['blend_mode'],
            'intensity': kwargs['intensity'],
            'preserve_skin': kwargs['preserve_skin'],
            'preserve_expression': kwargs['preserve_expression'],
            'face_recognition_threshold': 0.6,
            'blend_mask_blur': 5,
            'color_correction': True
        }

    def _post_process(self, image):
        """Post-traitement de l'image"""
        # Optimisation
        return optimize_image(image)

    @staticmethod
    def _allowed_file(filename):
        """Vérifie l'extension du fichier"""
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'webp'}
```

## Tests

### Tests Frontend
```javascript
describe('FaceSwap Component', () => {
    test('valide les formats d\'image', () => {
        const component = mount(FaceSwap);
        
        // Test fichier valide
        const validFile = new File([''], 'test.jpg', { type: 'image/jpeg' });
        expect(component.vm.validateImage(validFile)).toBe(true);

        // Test fichier invalide
        const invalidFile = new File([''], 'test.txt', { type: 'text/plain' });
        expect(component.vm.validateImage(invalidFile)).toBe(false);
    });

    test('active le bouton de génération', () => {
        const component = mount(FaceSwap);
        
        // État initial
        expect(component.vm.canGenerate).toBe(false);

        // Après upload des images
        component.vm.sourceFile = new File([''], 'source.jpg');
        component.vm.targetFile = new File([''], 'target.jpg');
        expect(component.vm.canGenerate).toBe(true);
    });
});
```

### Tests Backend
```python
def test_face_swap():
    """Test de face swap"""
    with open('tests/fixtures/source.jpg', 'rb') as source, \
         open('tests/fixtures/target.jpg', 'rb') as target:
        
        response = client.post(
            '/web/face-swap/generate',
            data={
                'source': source,
                'target': target,
                'blend_mode': 'natural',
                'intensity': '75',
                'preserve_skin': 'true',
                'preserve_expression': 'false'
            },
            content_type='multipart/form-data'
        )

        assert response.status_code == 200
        assert response.json['success'] is True
        assert 'url' in response.json
```

## Sécurité

### Validation des Fichiers
```python
def validate_swap_images(source, target):
    """Validation complète des images"""
    for image in [source, target]:
        # Vérification du format
        if not allowed_file(image.filename):
            raise ValueError('Format non supporté')

        # Vérification de la taille
        content = image.read()
        image.seek(0)
        if len(content) > current_app.config['MAX_CONTENT_LENGTH']:
            raise ValueError('Image trop volumineuse')

        # Vérification du contenu
        try:
            with Image.open(image) as img:
                img.verify()
        except:
            raise ValueError('Image corrompue')

        # Vérification des dimensions
        img = Image.open(image)
        min_size = 256
        if img.size[0] < min_size or img.size[1] < min_size:
            raise ValueError('Image trop petite')
```

### Protection CSRF
```python
@bp.route('/face-swap/generate', methods=['POST'])
@csrf.protect()
def generate_swap():
    # Implementation
```

## Monitoring

### Logging
```python
def log_swap(params, result):
    """Log de face swap"""
    logger.info(
        'Face swap completed',
        extra={
            'source_faces': result['source_faces'],
            'target_faces': result['target_faces'],
            'blend_mode': params['blend_mode'],
            'processing_time': result['processing_time']
        }
    )
```

### Métriques
```python
def track_swap_metrics(result):
    """Suivi des métriques de face swap"""
    metrics.increment('face_swaps_total')
    metrics.timing('swap_processing_time', result['processing_time'])
    metrics.gauge('swap_queue_size', queue.size())
``` 