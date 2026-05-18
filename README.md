# Artisans CI - Guide de Démarrage

## 🎯 À propos du projet

Plateforme web pour la gestion des études terrain auprès des artisans en Côte d'Ivoire. Construite avec Django et stylisée avec Tailwind CSS v4.

## 🛠 Stack technologique

- **Backend:** Django 6.0.5
- **Frontend:** Tailwind CSS 4.3.0
- **Base de données:** SQLite (développement), PostgreSQL (production)
- **Python:** 3.10+
- **Node.js:** Pour la compilation Tailwind CSS

## 📋 Prérequis

- Python 3.10+
- Node.js 14+
- pip et npm

## 🚀 Installation locale

### 1. Cloner le projet

```bash
git clone <votre-repo> kart
cd kart
```

### 2. Créer et activer l'environnement virtuel

```bash
# Windows
python -m venv env
env\Scripts\activate

# macOS/Linux
python3 -m venv env
source env/bin/activate
```

### 3. Installer les dépendances Python

```bash
pip install -r requirements.txt
```

### 4. Installer les dépendances Node.js

```bash
npm install
```

### 5. Initialiser la base de données

```bash
python manage.py migrate
```

### 6. Créer un superutilisateur

```bash
python manage.py createsuperuser
```

### 7. Compiler le CSS Tailwind

```bash
npm run build
```

### 8. Démarrer le serveur de développement

```bash
python manage.py runserver
```

Ouvrez http://localhost:8000 dans votre navigateur.

## 📁 Structure du projet

```
kart/
├── artisans/                    # Application Django
│   ├── migrations/
│   ├── static/
│   │   └── css/
│   │       ├── main.css        # Source Tailwind
│   │       └── output.css      # CSS compilé (généré)
│   ├── templates/
│   │   └── artisans/
│   │       ├── base.html       # Template de base
│   │       ├── dashboard.html
│   │       ├── nouveau.html
│   │       ├── questions.html
│   │       └── reponses.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── BACK/                        # Configuration Django
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   └── wsgi_pythonanywhere.py  # Config pour PythonAnywhere
├── manage.py
├── package.json                # Dépendances Node.js
├── requirements.txt            # Dépendances Python
├── tailwind.config.js         # Config Tailwind CSS
├── postcss.config.js          # Config PostCSS
├── build.js                   # Script de compilation
├── TAILWIND_GUIDE.md          # Guide complet Tailwind
└── DEPLOYMENT.md              # Guide déploiement PythonAnywhere
```

## 💻 Commandes utiles

### Développement

```bash
# Compiler Tailwind CSS
npm run build

# Recompiler automatiquement
npm run watch

# Démarrer Django
python manage.py runserver

# Créer les migrations
python manage.py makemigrations

# Appliquer les migrations
python manage.py migrate

# Accéder à l'admin Django
# http://localhost:8000/admin/
```

### Production (PythonAnywhere)

```bash
# Compiler le CSS
npm run build

# Collecter les fichiers statiques
python manage.py collectstatic --noinput

# Redémarrer l'application
# Depuis le Dashboard PythonAnywhere
```

## 🎨 Tailwind CSS

### Fichier source
- **`artisans/static/css/main.css`** - Fichier source Tailwind (ne pas éditer)

### Fichier compilé
- **`artisans/static/css/output.css`** - CSS compilé (généré par npm run build)

### Couleurs personnalisées

**Earth Colors (Terra):**
- `earth-50` à `earth-900` (teintes de brun/orange)
- Utilisé pour les accents et les éléments importants

**Forest Colors (Forêt):**
- `forest-500`, `forest-600`, `forest-700` (teintes de vert)
- Utilisé pour la navigation et les fonds

### Utilisation

```html
<!-- Classe avec Earth -->
<div class="bg-earth-600 text-white">Contenu avec Earth</div>

<!-- Classe avec Forest (sidebar) -->
<aside class="bg-forest-600">Navigation</aside>

<!-- Responsive design -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
  Responsive grid
</div>
```

Pour un guide complet, voir [TAILWIND_GUIDE.md](TAILWIND_GUIDE.md).

## 📤 Déploiement sur PythonAnywhere

### Étapes rapides

1. Cloner le projet sur PythonAnywhere
2. Créer un virtualenv: `mkvirtualenv --python=/usr/bin/python3.10 kart`
3. Installer les dépendances: `pip install -r requirements.txt`
4. Compiler le CSS: `npm run build`
5. Collecter les statics: `python manage.py collectstatic --noinput`
6. Configurer le WSGI dans le Dashboard
7. Définir ALLOWED_HOSTS dans settings.py
8. Redémarrer l'application

Pour un guide détaillé, voir [DEPLOYMENT.md](DEPLOYMENT.md).

## 🔐 Configuration de sécurité

Avant le déploiement en production:

1. Modifier `DEBUG = False` dans `BACK/settings.py`
2. Changer la `SECRET_KEY` dans `settings.py`
3. Ajouter le domaine à `ALLOWED_HOSTS`
4. Configurer HTTPS
5. Utiliser une base de données robuste (PostgreSQL)

## 📚 Documentation

- [Django 6.0 Documentation](https://docs.djangoproject.com/en/6.0/)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [PythonAnywhere Help](https://help.pythonanywhere.com/)

## 🐛 Troubleshooting

### Styles CSS ne s'affichent pas
```bash
npm run build
python manage.py collectstatic --noinput
```

### Port 8000 déjà utilisé
```bash
python manage.py runserver 8001
```

### Erreurs de migration
```bash
python manage.py migrate --fake-initial
```

### Réinitialiser la base de données
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

## 📝 Licence

À définir

## 👨‍💻 Contributeurs

À définir
