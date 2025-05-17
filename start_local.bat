@echo off
echo === MOG AI - DEMARRAGE LOCAL ===
echo.

REM Nettoyage des processus Python bloques
echo Nettoyage des processus Python bloques...
python clean.py

REM Verification de l'environnement virtuel
if not exist venv\ (
    echo Creation de l'environnement virtuel...
    python -m venv venv
)

REM Activation de l'environnement virtuel
call venv\Scripts\activate.bat

REM Installation des dependances
echo Installation/Mise a jour des dependances...
python -m pip install -r requirements.txt

REM Configuration de l'environnement
if not exist .env (
    echo Creation du fichier .env...
    (
        echo FLASK_APP=src
        echo FLASK_ENV=development
        echo FLASK_DEBUG=1
        echo SECRET_KEY=your-secret-key-change-this-in-production
        echo DATABASE_URL=sqlite:///instance/app.db
        echo HUGGINGFACE_API_KEY=your-huggingface-api-key
    ) > .env
)

REM Demarrage de l'application
echo.
echo Demarrage de l'application...
echo.
echo MOG AI va demarrer sur http://127.0.0.1:5000
echo Appuyez sur Ctrl+C pour arreter le serveur
echo.
echo === SERVEUR EN COURS D'EXECUTION ===
echo.

set FLASK_APP=src
set FLASK_ENV=development
set FLASK_DEBUG=1
python -m flask run --host=127.0.0.1 --port=5000 