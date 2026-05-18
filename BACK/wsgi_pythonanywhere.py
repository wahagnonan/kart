"""
WSGI config for BACK project - Optimized for PythonAnywhere

Usage on PythonAnywhere:
1. Copy this file to /var/www/<username>_pythonanywhere_com_wsgi.py
2. Update <username> placeholder with your actual username
3. Update sys.path with correct project path
4. Reload web app from Dashboard

For more information on WSGI:
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import sys
import os

# ============================================================================
# CONFIGURATION POUR PYTHONANYWHERE
# ============================================================================

# Ajoute le répertoire du projet au chemin Python
# IMPORTANT: Remplacer 'username' par votre nom d'utilisateur PythonAnywhere
project_home = '/home/username/kart'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# ============================================================================
# CONFIGURATION DJANGO
# ============================================================================

# Définit le module de paramètres Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BACK.settings')

# Import et setup Django
import django
from django.core.wsgi import get_wsgi_application

# Configure Django
django.setup()

# Récupère l'application WSGI
application = get_wsgi_application()

# ============================================================================
# NOTES IMPORTANTES POUR PYTHONANYWHERE
# ============================================================================

"""
1. STRUCTURE DES RÉPERTOIRES
   /home/username/kart/
   ├── manage.py
   ├── BACK/
   │   ├── settings.py
   │   ├── wsgi.py
   │   └── ...
   ├── artisans/
   │   ├── static/
   │   │   └── css/
   │   │       ├── main.css
   │   │       └── output.css (généré par Tailwind)
   │   └── templates/
   └── staticfiles/ (collecté par collectstatic)

2. VIRTUALENV
   Créer avec: mkvirtualenv --python=/usr/bin/python3.10 kart
   Basculer avec: workon kart

3. FICHIERS STATIQUES
   Exécutez: python manage.py collectstatic --noinput
   
   Dans PythonAnywhere Web App configuration:
   URL: /static/
   Directory: /home/username/kart/staticfiles

4. TAILWIND CSS
   Avant chaque déploiement:
   npm run build
   python manage.py collectstatic --noinput

5. DEBUG EN PRODUCTION
   Dans settings.py, mettre: DEBUG = False
   Ajouter ALLOWED_HOSTS: ALLOWED_HOSTS = ['username.pythonanywhere.com', 'localhost']

6. PROBLÈMES COURANTS
   - Module not found: Vérifier le virtualenv est activé
   - CSS manquants: Exécutez collectstatic
   - CSRF errors: Vérifier ALLOWED_HOSTS dans settings.py
"""
