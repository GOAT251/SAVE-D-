# Instructions pour MOG AI - Face Swap

## Méthode simplifiée (recommandée)

1. Exécutez simplement:
```bash
python run.py
```

Ce script fait tout automatiquement:
- Configure l'environnement
- Nettoie les processus bloqués
- Crée l'environnement virtuel si nécessaire
- Installe les dépendances
- Démarre l'application

L'application sera disponible sur http://localhost:5000

## Méthode manuelle (alternative)

Si la méthode simplifiée ne fonctionne pas, suivez ces étapes:

1. Nettoyer les processus Python bloqués:
```bash
python clean.py
```

2. Configurer l'environnement:
```bash
python setup_env.py
```

3. Réinitialiser l'environnement virtuel:
```bash
python reset_venv.py
```

4. Activer l'environnement virtuel:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

5. Démarrer l'application:
```bash
python app.py
```

## Utilisation du Face Swap

1. Ouvrez l'application dans votre navigateur: http://localhost:5000
2. Uploadez une image source (le visage à utiliser)
3. Uploadez une image cible (où placer le visage)
4. Cliquez sur "Générer"

## Notes importantes

- L'application utilise l'API Hugging Face (nécessite une clé API)
- La première requête peut prendre du temps car le modèle doit se charger
- Taille maximum des images: 5MB

## Configuration

1. Créez un fichier `.env` à la racine du projet
2. Ajoutez votre clé API Hugging Face:
```
HUGGINGFACE_API_KEY=your-api-key-here
```

## Résolution des problèmes courants

- Si vous rencontrez une erreur de "module not found", exécutez:
  ```bash
  python reset_venv.py
  ```

- Si le terminal se bloque ou charge à l'infini, exécutez:
  ```bash
  python clean.py
  ```

- Si le face swap échoue avec une erreur d'API, c'est peut-être que le modèle est en train de se charger. Attendez un moment et réessayez. 