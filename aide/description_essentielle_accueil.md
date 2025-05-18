# Description Essentielle - Page d'Accueil (/)

## Structure Visuelle

### Interface Principale
```html
<div class="min-h-screen bg-gradient-to-b from-gray-50 to-white">
    <!-- Hero Section -->
    <section class="relative overflow-hidden">
        <!-- Background Pattern -->
        <div class="absolute inset-0 bg-grid-pattern opacity-5"></div>

        <!-- Hero Content -->
        <div class="container mx-auto px-4 py-16 md:py-24">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
                <!-- Text Content -->
                <div class="space-y-8">
                    <h1 class="text-4xl md:text-6xl font-bold">
                        <span class="gradient-text">MOG AI</span>
                        <br>
                        <span class="text-gray-900">
                            Intelligence Artificielle pour la Création Visuelle
                        </span>
                    </h1>
                    
                    <p class="text-xl text-gray-600">
                        Transformez vos idées en réalité avec nos outils d'IA avancés.
                        Face swap, génération de vidéos, et analyse de style en quelques clics.
                    </p>

                    <div class="flex flex-wrap gap-4">
                        <a href="{{ url_for('web.face_swap') }}" 
                           class="btn-primary">
                            Commencer
                        </a>
                        <a href="#features" 
                           class="btn-secondary">
                            Découvrir
                        </a>
                    </div>
                </div>

                <!-- Hero Image -->
                <div class="relative">
                    <div class="absolute inset-0 bg-gradient-to-tr from-indigo-500/20 
                                to-purple-500/20 rounded-3xl transform rotate-3"></div>
                    <img src="{{ url_for('static', filename='images/hero.webp') }}" 
                         alt="MOG AI Demo" 
                         class="relative rounded-2xl shadow-xl">
                </div>
            </div>
        </div>
    </section>

    <!-- Features Section -->
    <section id="features" class="py-16 md:py-24 bg-white">
        <div class="container mx-auto px-4">
            <h2 class="text-3xl md:text-4xl font-bold text-center mb-16">
                Nos Technologies
            </h2>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <!-- Face Swap -->
                <div class="feature-card">
                    <div class="icon-container">
                        <svg class="w-8 h-8" fill="none" stroke="currentColor">
                            <!-- Icône face swap -->
                        </svg>
                    </div>
                    <h3 class="text-xl font-semibold mb-4">Face Swap IA</h3>
                    <p class="text-gray-600">
                        Échangez des visages avec une précision incroyable grâce à 
                        notre technologie d'IA avancée.
                    </p>
                    <a href="{{ url_for('web.face_swap') }}" 
                       class="mt-4 inline-block text-indigo-600 hover:text-indigo-800">
                        En savoir plus →
                    </a>
                </div>

                <!-- AI Video -->
                <div class="feature-card">
                    <div class="icon-container">
                        <svg class="w-8 h-8" fill="none" stroke="currentColor">
                            <!-- Icône vidéo -->
                        </svg>
                    </div>
                    <h3 class="text-xl font-semibold mb-4">Génération de Vidéo</h3>
                    <p class="text-gray-600">
                        Créez des vidéos uniques à partir de simples descriptions 
                        textuelles.
                    </p>
                    <a href="{{ url_for('web.ai_video') }}" 
                       class="mt-4 inline-block text-indigo-600 hover:text-indigo-800">
                        En savoir plus →
                    </a>
                </div>

                <!-- Looks Analysis -->
                <div class="feature-card">
                    <div class="icon-container">
                        <svg class="w-8 h-8" fill="none" stroke="currentColor">
                            <!-- Icône analyse -->
                        </svg>
                    </div>
                    <h3 class="text-xl font-semibold mb-4">Analyse de Style</h3>
                    <p class="text-gray-600">
                        Obtenez des recommandations personnalisées basées sur 
                        l'analyse de votre style.
                    </p>
                    <a href="{{ url_for('web.looks_analysis') }}" 
                       class="mt-4 inline-block text-indigo-600 hover:text-indigo-800">
                        En savoir plus →
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- Demo Section -->
    <section class="py-16 md:py-24 bg-gray-50">
        <div class="container mx-auto px-4">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
                <!-- Demo Video -->
                <div class="relative aspect-video rounded-xl overflow-hidden shadow-xl">
                    <video autoplay loop muted playsinline 
                           class="w-full h-full object-cover">
                        <source src="{{ url_for('static', filename='videos/demo.mp4') }}" 
                                type="video/mp4">
                    </video>
                </div>

                <!-- Demo Content -->
                <div class="space-y-6">
                    <h2 class="text-3xl md:text-4xl font-bold">
                        Voyez la Magie en Action
                    </h2>
                    <p class="text-xl text-gray-600">
                        Notre technologie d'IA offre des résultats exceptionnels en 
                        quelques secondes. Essayez par vous-même !
                    </p>
                    <ul class="space-y-4">
                        <li class="flex items-center">
                            <svg class="w-6 h-6 text-green-500 mr-2" 
                                 fill="none" 
                                 stroke="currentColor">
                                <!-- Icône check -->
                            </svg>
                            <span>Résultats en temps réel</span>
                        </li>
                        <li class="flex items-center">
                            <svg class="w-6 h-6 text-green-500 mr-2" 
                                 fill="none" 
                                 stroke="currentColor">
                                <!-- Icône check -->
                            </svg>
                            <span>Haute qualité garantie</span>
                        </li>
                        <li class="flex items-center">
                            <svg class="w-6 h-6 text-green-500 mr-2" 
                                 fill="none" 
                                 stroke="currentColor">
                                <!-- Icône check -->
                            </svg>
                            <span>Interface intuitive</span>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section class="py-16 md:py-24">
        <div class="container mx-auto px-4">
            <div class="bg-gradient-to-r from-indigo-600 to-purple-600 
                        rounded-3xl p-12 text-center text-white">
                <h2 class="text-3xl md:text-4xl font-bold mb-6">
                    Prêt à Commencer ?
                </h2>
                <p class="text-xl mb-8 opacity-90">
                    Rejoignez des milliers d'utilisateurs qui créent déjà avec MOG AI.
                </p>
                <a href="{{ url_for('auth.register') }}" 
                   class="inline-block bg-white text-indigo-600 px-8 py-3 
                          rounded-lg font-semibold hover:bg-gray-100 
                          transition-colors">
                    Créer un Compte
                </a>
            </div>
        </div>
    </section>
</div>
```

## Styles CSS

### Classes Spécifiques
```css
.gradient-text {
    @apply bg-clip-text text-transparent bg-gradient-to-r 
           from-indigo-600 to-purple-600;
}

.btn-primary {
    @apply inline-block px-6 py-3 bg-indigo-600 text-white 
           rounded-lg font-semibold hover:bg-indigo-700 
           focus:outline-none focus:ring-2 focus:ring-indigo-500 
           focus:ring-offset-2 transition-colors;
}

.btn-secondary {
    @apply inline-block px-6 py-3 border-2 border-indigo-600 
           text-indigo-600 rounded-lg font-semibold 
           hover:bg-indigo-50 focus:outline-none focus:ring-2 
           focus:ring-indigo-500 focus:ring-offset-2 
           transition-colors;
}

.feature-card {
    @apply bg-white p-8 rounded-xl shadow-lg hover:shadow-xl 
           transition-shadow;
}

.icon-container {
    @apply w-12 h-12 bg-indigo-100 text-indigo-600 rounded-lg 
           flex items-center justify-center mb-6;
}

.bg-grid-pattern {
    background-image: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23a5b4fc' fill-opacity='0.4'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
}
```

### Animations
```css
@keyframes float {
    0% {
        transform: translateY(0px);
    }
    50% {
        transform: translateY(-20px);
    }
    100% {
        transform: translateY(0px);
    }
}

.hero-image {
    animation: float 6s ease-in-out infinite;
}

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

.feature-card {
    animation: fade-up 0.5s ease-out forwards;
}
```

## JavaScript (home.js)

### Logique d'Animation
```javascript
const Home = {
    data() {
        return {
            isVideoPlaying: false,
            activeFeature: null
        }
    },

    mounted() {
        // Initialisation des animations
        this.initAnimations();
        
        // Démarrage automatique de la vidéo
        this.playDemoVideo();

        // Analytics
        this.trackPageView();
    },

    methods: {
        initAnimations() {
            // Animation des features au scroll
            const features = document.querySelectorAll('.feature-card');
            
            const observer = new IntersectionObserver(
                (entries) => {
                    entries.forEach(entry => {
                        if (entry.isIntersecting) {
                            entry.target.style.opacity = 1;
                            entry.target.style.transform = 'translateY(0)';
                        }
                    });
                },
                {
                    threshold: 0.1
                }
            );

            features.forEach(feature => {
                feature.style.opacity = 0;
                feature.style.transform = 'translateY(20px)';
                observer.observe(feature);
            });
        },

        playDemoVideo() {
            const video = this.$refs.demoVideo;
            if (video) {
                video.play().catch(() => {
                    // Fallback pour les navigateurs qui bloquent l'autoplay
                    this.isVideoPlaying = false;
                });
            }
        },

        showFeatureDetails(feature) {
            this.activeFeature = feature;
        },

        trackPageView() {
            analytics.track('home_page_viewed');
        }
    }
};
```

## Backend (routes/web/home.py)

### Route Web
```python
@bp.route('/')
def index():
    """Page d'accueil"""
    return render_template(
        'index.html',
        config=get_home_config()
    )

def get_home_config():
    """Configuration pour le frontend"""
    return {
        'features': [
            {
                'id': 'face-swap',
                'title': 'Face Swap IA',
                'description': 'Échangez des visages avec une précision incroyable.',
                'icon': 'face-swap',
                'url': url_for('web.face_swap')
            },
            {
                'id': 'ai-video',
                'title': 'Génération de Vidéo',
                'description': 'Créez des vidéos uniques par IA.',
                'icon': 'video',
                'url': url_for('web.ai_video')
            },
            {
                'id': 'looks-analysis',
                'title': 'Analyse de Style',
                'description': 'Obtenez des recommandations personnalisées.',
                'icon': 'analysis',
                'url': url_for('web.looks_analysis')
            }
        ],
        'demo_video_url': url_for('static', filename='videos/demo.mp4'),
        'hero_image_url': url_for('static', filename='images/hero.webp')
    }
```

## Tests

### Tests Frontend
```javascript
describe('Home Component', () => {
    test('initialise les animations au montage', () => {
        const component = mount(Home);
        const spy = jest.spyOn(component.vm, 'initAnimations');
        
        component.vm.$nextTick(() => {
            expect(spy).toHaveBeenCalled();
        });
    });

    test('démarre la vidéo automatiquement', () => {
        const component = mount(Home);
        const video = component.$refs.demoVideo;
        
        expect(video.play).toHaveBeenCalled();
    });
});
```

### Tests Backend
```python
def test_home_page():
    """Test de la page d'accueil"""
    response = client.get('/')
    
    assert response.status_code == 200
    assert b'MOG AI' in response.data
    assert b'Face Swap IA' in response.data
```

## Sécurité

### Protection XSS
```python
@bp.after_request
def add_security_headers(response):
    """Ajout des en-têtes de sécurité"""
    response.headers['Content-Security-Policy'] = "default-src 'self'; \
        style-src 'self' 'unsafe-inline'; \
        script-src 'self' 'unsafe-inline' 'unsafe-eval'; \
        img-src 'self' data: blob:; \
        media-src 'self' blob:;"
    return response
```

## Monitoring

### Logging
```python
def log_home_visit():
    """Log des visites de la page d'accueil"""
    logger.info(
        'Home page visited',
        extra={
            'user_agent': request.user_agent.string,
            'referrer': request.referrer
        }
    )
```

### Métriques
```python
def track_home_metrics():
    """Suivi des métriques de la page d'accueil"""
    metrics.increment('home_page_views')
    metrics.gauge('active_visitors', get_active_visitors())
``` 