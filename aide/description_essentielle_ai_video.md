# Description Essentielle - AI Video (/web/ai-video)

## Structure Visuelle

### Interface Principale
```html
<div class="container mx-auto px-4 py-8">
    <!-- En-tête de la page -->
    <header class="mb-8">
        <h1 class="text-3xl md:text-4xl font-bold gradient-text">
            Génération de Vidéo IA
        </h1>
        <p class="mt-2 text-gray-600">
            Créez des vidéos uniques avec notre technologie d'IA avancée
        </p>
    </header>

    <!-- Interface principale -->
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <!-- Panneau de Configuration -->
        <div class="lg:col-span-1">
            <div class="bg-white rounded-xl shadow-lg p-6">
                <h2 class="text-xl font-semibold mb-6">Configuration</h2>
                
                <!-- Formulaire de génération -->
                <form @submit.prevent="generateVideo" class="space-y-6">
                    <!-- Description textuelle -->
                    <div class="form-group">
                        <label class="block text-sm font-medium text-gray-700 mb-2">
                            Description de la vidéo
                        </label>
                        <textarea 
                            v-model="description"
                            rows="4"
                            class="w-full px-3 py-2 border border-gray-300 rounded-md 
                                   focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500"
                            placeholder="Décrivez la vidéo que vous souhaitez générer..."
                        ></textarea>
                    </div>

                    <!-- Style de la vidéo -->
                    <div class="form-group">
                        <label class="block text-sm font-medium text-gray-700 mb-2">
                            Style
                        </label>
                        <select 
                            v-model="style"
                            class="w-full px-3 py-2 border border-gray-300 rounded-md">
                            <option value="realistic">Réaliste</option>
                            <option value="cartoon">Cartoon</option>
                            <option value="artistic">Artistique</option>
                        </select>
                    </div>

                    <!-- Durée -->
                    <div class="form-group">
                        <label class="block text-sm font-medium text-gray-700 mb-2">
                            Durée (secondes)
                        </label>
                        <input 
                            type="number"
                            v-model="duration"
                            min="1"
                            max="30"
                            class="w-full px-3 py-2 border border-gray-300 rounded-md">
                    </div>

                    <!-- Options avancées -->
                    <div class="form-group">
                        <button 
                            type="button"
                            @click="showAdvancedOptions = !showAdvancedOptions"
                            class="text-sm text-indigo-600 hover:text-indigo-800">
                            Options avancées
                        </button>
                        
                        <div v-if="showAdvancedOptions" class="mt-4 space-y-4">
                            <!-- FPS -->
                            <div class="form-group">
                                <label class="block text-sm font-medium text-gray-700">
                                    FPS
                                </label>
                                <select v-model="fps" class="mt-1 block w-full rounded-md border-gray-300">
                                    <option value="24">24 FPS</option>
                                    <option value="30">30 FPS</option>
                                    <option value="60">60 FPS</option>
                                </select>
                            </div>

                            <!-- Résolution -->
                            <div class="form-group">
                                <label class="block text-sm font-medium text-gray-700">
                                    Résolution
                                </label>
                                <select v-model="resolution" class="mt-1 block w-full rounded-md border-gray-300">
                                    <option value="720p">HD (720p)</option>
                                    <option value="1080p">Full HD (1080p)</option>
                                    <option value="4k">4K</option>
                                </select>
                            </div>
                        </div>
                    </div>

                    <!-- Bouton de génération -->
                    <button 
                        type="submit"
                        :disabled="processing"
                        class="w-full py-3 px-4 bg-indigo-600 text-white rounded-lg
                               hover:bg-indigo-700 focus:outline-none focus:ring-2
                               focus:ring-indigo-500 focus:ring-offset-2
                               disabled:opacity-50 disabled:cursor-not-allowed">
                        {{ processing ? 'Génération en cours...' : 'Générer la vidéo' }}
                    </button>
                </form>
            </div>
        </div>

        <!-- Zone de Prévisualisation -->
        <div class="lg:col-span-2">
            <div class="bg-white rounded-xl shadow-lg p-6">
                <h2 class="text-xl font-semibold mb-6">Prévisualisation</h2>
                
                <!-- État de chargement -->
                <div v-if="processing" class="flex flex-col items-center justify-center py-12">
                    <div class="loading-spinner"></div>
                    <div class="mt-4 text-gray-600">
                        Génération de votre vidéo...
                        <div class="text-sm text-gray-500">
                            Temps estimé: {{ estimatedTime }}
                        </div>
                    </div>
                </div>

                <!-- Résultat -->
                <div v-else-if="result" class="space-y-4">
                    <video 
                        controls
                        class="w-full rounded-lg shadow-md"
                        :src="result.url">
                    </video>
                    
                    <!-- Actions -->
                    <div class="flex justify-end space-x-4">
                        <button 
                            @click="downloadVideo"
                            class="btn-secondary">
                            Télécharger
                        </button>
                        <button 
                            @click="shareVideo"
                            class="btn-primary">
                            Partager
                        </button>
                    </div>
                </div>

                <!-- État initial -->
                <div v-else class="flex flex-col items-center justify-center py-12 text-gray-500">
                    <svg class="w-16 h-16 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <!-- Icône vidéo -->
                    </svg>
                    <p>Configurez et générez votre vidéo</p>
                </div>
            </div>
        </div>
    </div>
</div>
```

## Styles CSS

### Classes Spécifiques
```css
.loading-spinner {
    @apply w-12 h-12 border-4 border-indigo-500 border-t-transparent 
           rounded-full animate-spin;
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

.form-group {
    @apply space-y-2;
}
```

### Animations
```css
@keyframes progress {
    0% { width: 0%; }
    100% { width: 100%; }
}

.progress-bar {
    @apply h-2 bg-indigo-500 rounded-full;
    animation: progress 30s linear;
}
```

## JavaScript (ai-video.js)

### Logique de Génération
```javascript
const AIVideo = {
    data() {
        return {
            description: '',
            style: 'realistic',
            duration: 10,
            fps: 30,
            resolution: '1080p',
            showAdvancedOptions: false,
            processing: false,
            result: null,
            error: null,
            estimatedTime: '2-3 minutes'
        }
    },

    computed: {
        isValid() {
            return this.description.length >= 10 && 
                   this.duration >= 1 && 
                   this.duration <= 30;
        }
    },

    methods: {
        async generateVideo() {
            if (!this.isValid) {
                this.error = 'Veuillez remplir tous les champs correctement';
                return;
            }

            this.processing = true;
            this.error = null;

            try {
                const response = await fetch('/web/ai-video/generate', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        description: this.description,
                        style: this.style,
                        duration: this.duration,
                        fps: this.fps,
                        resolution: this.resolution
                    })
                });

                if (!response.ok) throw new Error('Erreur de génération');

                const data = await response.json();
                this.result = data;

                // Tracking
                this.trackGeneration();

            } catch (error) {
                this.error = error.message;
            } finally {
                this.processing = false;
            }
        },

        async downloadVideo() {
            if (!this.result?.url) return;

            try {
                const response = await fetch(this.result.url);
                const blob = await response.blob();
                const url = window.URL.createObjectURL(blob);
                
                const a = document.createElement('a');
                a.href = url;
                a.download = `video-${Date.now()}.mp4`;
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
                window.URL.revokeObjectURL(url);

            } catch (error) {
                this.error = 'Erreur lors du téléchargement';
            }
        },

        shareVideo() {
            if (!this.result?.url) return;

            if (navigator.share) {
                navigator.share({
                    title: 'Ma vidéo générée par IA',
                    text: this.description,
                    url: this.result.url
                });
            } else {
                // Fallback
                this.copyToClipboard(this.result.url);
            }
        },

        trackGeneration() {
            // Analytics
            analytics.track('video_generated', {
                style: this.style,
                duration: this.duration,
                resolution: this.resolution
            });
        }
    }
};
```

## Backend (routes/web/ai_video.py)

### Route Web
```python
@bp.route('/ai-video')
def ai_video():
    """Page de génération vidéo"""
    return render_template(
        'web/ai_video/index.html',
        config=get_video_config()
    )

def get_video_config():
    """Configuration pour le frontend"""
    return {
        'maxDuration': current_app.config['MAX_VIDEO_DURATION'],
        'styles': [
            {'value': 'realistic', 'label': 'Réaliste'},
            {'value': 'cartoon', 'label': 'Cartoon'},
            {'value': 'artistic', 'label': 'Artistique'}
        ],
        'resolutions': [
            {'value': '720p', 'label': 'HD (720p)'},
            {'value': '1080p', 'label': 'Full HD (1080p)'},
            {'value': '4k', 'label': '4K'}
        ],
        'apiEndpoint': url_for('api.generate_video')
    }
```

### Route API
```python
@bp.route('/ai-video/generate', methods=['POST'])
@limiter.limit("2 per minute")  # Rate limiting
def generate_video():
    """Génération de vidéo"""
    try:
        data = request.get_json()
        
        # Validation
        if not data or 'description' not in data:
            raise ValueError('Description manquante')

        # Paramètres
        params = {
            'description': data['description'],
            'style': data.get('style', 'realistic'),
            'duration': min(int(data.get('duration', 10)), 30),
            'fps': int(data.get('fps', 30)),
            'resolution': data.get('resolution', '1080p')
        }

        # Génération
        result = video_service.generate(**params)

        return jsonify({
            'success': True,
            'url': result['url'],
            'duration': result['duration']
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400
```

## Service (services/ai_video/service.py)

### Logique Métier
```python
class AIVideoService:
    def __init__(self):
        self.model = load_video_model()
        self.storage = VideoStorage()

    def generate(self, description, style='realistic', 
                duration=10, fps=30, resolution='1080p'):
        """Génération de vidéo"""
        try:
            # Validation
            self._validate_params(description, duration, fps)

            # Préparation des paramètres
            params = self._prepare_params(
                description=description,
                style=style,
                duration=duration,
                fps=fps,
                resolution=resolution
            )

            # Génération
            video_data = self.model.generate(**params)

            # Post-traitement
            processed_video = self._post_process(video_data)

            # Stockage
            video_url = self.storage.save(processed_video)

            return {
                'url': video_url,
                'duration': duration,
                'size': len(processed_video)
            }

        except Exception as e:
            logger.error(f"Video generation failed: {str(e)}")
            raise

    def _validate_params(self, description, duration, fps):
        """Validation des paramètres"""
        if not description or len(description) < 10:
            raise ValueError("Description trop courte")

        if duration < 1 or duration > 30:
            raise ValueError("Durée invalide")

        if fps not in [24, 30, 60]:
            raise ValueError("FPS invalide")

    def _prepare_params(self, **kwargs):
        """Préparation des paramètres pour le modèle"""
        return {
            'prompt': kwargs['description'],
            'style': kwargs['style'],
            'num_frames': kwargs['duration'] * kwargs['fps'],
            'fps': kwargs['fps'],
            'resolution': self._get_resolution(kwargs['resolution'])
        }

    def _post_process(self, video_data):
        """Post-traitement de la vidéo"""
        # Optimisation
        return optimize_video(video_data)

    @staticmethod
    def _get_resolution(quality):
        """Conversion de la qualité en résolution"""
        resolutions = {
            '720p': (1280, 720),
            '1080p': (1920, 1080),
            '4k': (3840, 2160)
        }
        return resolutions.get(quality, (1920, 1080))
```

## Tests

### Tests Frontend
```javascript
describe('AIVideo Component', () => {
    test('valide les paramètres de génération', () => {
        const component = mount(AIVideo);
        
        // Test description invalide
        component.vm.description = 'Court';
        expect(component.vm.isValid).toBe(false);

        // Test paramètres valides
        component.vm.description = 'Une description suffisamment longue';
        component.vm.duration = 15;
        expect(component.vm.isValid).toBe(true);
    });
});
```

### Tests Backend
```python
def test_video_generation():
    """Test de génération de vidéo"""
    response = client.post('/web/ai-video/generate', json={
        'description': 'Une vidéo de test avec une description longue',
        'style': 'realistic',
        'duration': 10,
        'fps': 30,
        'resolution': '1080p'
    })

    assert response.status_code == 200
    assert response.json['success'] is True
    assert 'url' in response.json
```

## Sécurité

### Validation des Entrées
```python
def validate_video_params(data):
    """Validation des paramètres vidéo"""
    if not isinstance(data.get('duration'), int):
        raise ValueError('Duration must be an integer')
    
    if data.get('duration') > current_app.config['MAX_VIDEO_DURATION']:
        raise ValueError('Duration too long')
    
    if data.get('resolution') not in ['720p', '1080p', '4k']:
        raise ValueError('Invalid resolution')
```

### Rate Limiting
```python
def configure_rate_limits():
    """Configuration des limites de requêtes"""
    limiter.limit("2 per minute")(bp)
    limiter.limit("30 per hour")(bp)
```

## Monitoring

### Logging
```python
def log_video_generation(params, result):
    """Log de génération vidéo"""
    logger.info(
        'Video generation completed',
        extra={
            'description_length': len(params['description']),
            'duration': params['duration'],
            'style': params['style'],
            'processing_time': result['processing_time']
        }
    )
```

### Métriques
```python
def track_video_metrics(result):
    """Suivi des métriques de génération"""
    metrics.increment('video_generations_total')
    metrics.timing('video_processing_time', result['processing_time'])
    metrics.gauge('video_queue_size', queue.size())
``` 