# M.O.G AI

<p align="center">
  <img src="static/images/logo.svg" alt="MOG AI Logo" width="200"/>
</p>

## Description
M.O.G AI est une application Flask moderne et scalable conçue pour l'intelligence artificielle conversationnelle avancée.

## Repositories
- Main Repository: [MOGGIGN](https://github.com/GOAT251/moggign)
- Backup Repository: [SAVE](https://github.com/GOAT251/SAVE)

## Interface Interactive
Pour interagir avec le développement :
- ✅ Continuer le développement
- ⛔ Arrêter le développement
- ❓ Poser une question
- 🔄 Voir le statut actuel

## Prérequis
- Python 3.8+
- Redis (optionnel, pour le cache en production)
- Base de données SQLite (dev) ou PostgreSQL (prod)

## Installation

1. Cloner le repository
```bash
git clone https://github.com/GOAT251/moggign.git
cd moggign
```

2. Créer un environnement virtuel
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Installer les dépendances
```bash
pip install -r requirements.txt
```

4. Configuration
Créer un fichier `.env` à la racine du projet :
```env
FLASK_APP=src
FLASK_ENV=development
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///app.db
```

## Structure du Projet
```
mog-ai/
├── src/                # Code source principal
│   ├── models/        # Modèles de données
│   ├── routes/        # Routes API et Web
│   ├── services/      # Logique métier
│   └── utils/         # Utilitaires
├── config/            # Configuration
├── static/           # Fichiers statiques
│   ├── images/      # Images (logo, etc.)
│   ├── css/         # Styles
│   └── js/          # JavaScript
├── templates/        # Templates HTML
├── tests/           # Tests unitaires
└── aide/            # Documentation
```

## Développement Backend en cours

### Fonctionnalités implémentées :
- ✅ Structure scalable
- ✅ Configuration multi-environnement
- ✅ Système de cache
- ✅ Tests unitaires
- ✅ Monitoring

### En cours d'implémentation :
- 🔄 Routes API
- 🔄 Modèles de données
- 🔄 Services métier
- 🔄 Validation des données

## Développement

1. Lancer le serveur de développement
```bash
flask run
```

2. Exécuter les tests
```bash
pytest
pytest --cov=src tests/  # avec couverture
```

## Déploiement

### Local
```bash
# Démarrer en local
./start_local.bat  # Windows
```

### Production (Render)
L'application est déployée sur Render à l'adresse suivante :
[https://mog-ai.onrender.com](https://mog-ai.onrender.com)

Configuration Render :
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn "src:create_app()"`
- Python Version: 3.8
- Environment Variables:
  - `FLASK_APP=src`
  - `FLASK_ENV=production`
  - `SECRET_KEY=[votre-clé-secrète]`
  - `DATABASE_URL=[url-de-votre-base-de-données]`

## Progrès du Développement
Dernière mise à jour : 15/05/2024
- ✅ Implémentation de la structure scalable
- ✅ Configuration du déploiement Render
- ✅ Intégration du logo dans l'interface
- 🔄 Optimisation des performances
- 🔄 Tests d'intégration

## Contribution
1. Fork le projet
2. Créer une branche (`git checkout -b feature/AmazingFeature`)
3. Commit les changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## License
[MIT License]

## Contact
[GOAT251] 