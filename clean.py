import os
import signal
import psutil

def clean_python_processes():
    """Nettoie les processus Python bloqués"""
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if 'python' in proc.info['name'].lower():
                print(f"Arrêt du processus Python: {proc.info['pid']}")
                os.kill(proc.info['pid'], signal.SIGTERM)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

if __name__ == "__main__":
    clean_python_processes()
    print("Nettoyage terminé") 