# Guide de Déploiement sur PythonAnywhere

## Prérequis

- Compte PythonAnywhere (compte gratuit ou payant)
- Le projet Django avec Tailwind CSS configuré

## Étapes de Déploiement

### 1. Cloner le projet sur PythonAnywhere

```bash
cd ~
git clone <votre-repo-url> kart
cd kart
```

### 2. Créer un virtualenv

```bash
mkvirtualenv --python=/usr/bin/python3.10 kart
pip install -r requirements.txt
```

### 3. Compiler le CSS Tailwind

**Pas nécessaire!** Le projet utilise Tailwind CSS via CDN.

Les fichiers suivants sont optionnels (pour une future optimisation):
- `tailwind.config.js`
- `postcss.config.js`
- `build.js`

### 4. Configurer Django

```bash
# Créer une copie de settings avec les variables d'environnement
python manage.py migrate
python manage.py collectstatic --noinput
```

### 5. Configurer le Web App sur PythonAnywhere

#### a. Créer une web app

- Allez à Dashboard > Web
- Cliquez sur "Add a new web app"
- Choisissez "Manual configuration"
- Sélectionnez Python 3.10

#### b. Configurer le WSGI

Éditez le fichier WSGI (`/var/www/<username>_pythonanywhere_com_wsgi.py`):

```python
# ============================================================================
# This file contains the WSGI configuration required to serve up your
# web application at http://<your-domain>.pythonanywhere.com/
# ============================================================================

import sys
import os

# Add your project directory to the sys.path
project_home = '/home/<username>/kart'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set environment variables
os.environ['DJANGO_SETTINGS_MODULE'] = 'BACK.settings'

# Import Django and setup
import django
from django.core.wsgi import get_wsgi_application
django.setup()

application = get_wsgi_application()
```

#### c. Configurer les fichiers statiques

Dans PythonAnywhere Web app settings:

| URL | Directory |
|-----|-----------|
| `/static/` | `/home/<username>/kart/staticfiles` |

### 6. Mettre à jour ALLOWED_HOSTS

Éditez `BACK/settings.py`:

```python
ALLOWED_HOSTS = ['<username>.pythonanywhere.com', 'localhost']
```

### 7. Redémarrer l'application

Allez à Dashboard > Web et cliquez sur "Reload"

## Configuration de Tailwind CSS

Le projet utilise **Tailwind CSS via CDN** - **aucune compilation nécessaire!**

La configuration est dans `artisans/templates/artisans/base.html`:

```html
<script src="https://cdn.tailwindcss.com"></script>
<script>
  tailwind.config = {
    theme: {
      extend: {
        colors: { earth, forest }
      }
    }
  }
</script>
```

### Avantages pour PythonAnywhere

- ✅ Aucun processus de build requis
- ✅ Aucune dépendance Node.js nécessaire
- ✅ Configuration en temps réel
- ✅ CDN global pour les meilleures performances

## Structure des fichiers statiques

```
artisans/
├── static/
│   └── (fichiers statiques Django: images, fonts, etc.)
├── templates/
│   └── artisans/
│       ├── base.html (Tailwind CDN chargé ici)
│       ├── dashboard.html
│       └── ...
```

## Important pour PythonAnywhere

1. **DEBUG = False** en production - modifiez `settings.py` avant le lancement
2. **ALLOWED_HOSTS** - Ajoutez votre domaine PythonAnywhere
3. **SECRET_KEY** - Remplacez par une clé sécurisée
4. **Pas besoin de npm ou Node.js** - Le CDN gère Tailwind

### Configuration DEBUG


```python
# BACK/settings.py
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
```

## Exemple de .env pour PythonAnywhere

Créez un fichier `.env` (que vous ne commitez pas):

```
DEBUG=False
SECRET_KEY=<votre-clé-secrète>
ALLOWED_HOSTS=votresite.pythonanywhere.com
```

## Troubleshooting

### Les styles CSS ne s'affichent pas

1. Vérifiez que `npm run build` a été exécuté
2. Exécutez `python manage.py collectstatic --noinput`
3. Rechargez l'application web dans PythonAnywhere

### Module not found errors

Vérifiez que le virtualenv est activé et que tous les packages sont installés:

```bash
pip list | grep -E 'Django|asgiref'
```

### Tailwind CSS ne compile pas

Vérifiez que node_modules existe:

```bash
npm install
npm run build
```
