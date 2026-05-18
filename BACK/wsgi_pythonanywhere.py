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
project_home = '/home/soro/kart'
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

