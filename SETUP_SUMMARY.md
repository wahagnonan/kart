# 📋 Résumé de Configuration - Tailwind CSS & PythonAnywhere

## ✅ Ce qui a été fait

### 1. **Installation Tailwind CSS v4**
- ✅ Installé `tailwindcss`, `@tailwindcss/postcss`, `postcss`, `autoprefixer`
- ✅ Créé `tailwind.config.js` avec couleurs personnalisées (earth & forest)
- ✅ Créé `postcss.config.js` pour la compilation
- ✅ Créé `artisans/static/css/main.css` (fichier source Tailwind)
- ✅ Créé script de build `build.js` pour compiler le CSS
- ✅ Généré `artisans/static/css/output.css` (CSS compilé)
- ✅ Mis à jour `base.html` pour utiliser le CSS compilé au lieu du CDN

### 2. **Configuration Django pour production**
- ✅ Ajouté `STATIC_ROOT` et `STATICFILES_DIRS` dans `settings.py`
- ✅ Créé `BACK/wsgi_pythonanywhere.py` avec documentation complète

### 3. **Fichiers Python pour déploiement**
- ✅ Créé `requirements.txt` avec toutes les dépendances Python
  - Django==6.0.5
  - asgiref==3.11.1
  - sqlparse==0.5.5
  - tzdata==2026.2

### 4. **Documentation complète**
- ✅ Créé `DEPLOYMENT.md` - Guide complet PythonAnywhere
- ✅ Créé `TAILWIND_GUIDE.md` - Guide d'utilisation Tailwind CSS
- ✅ Créé `README.md` - Documentation du projet
- ✅ Créé `.env.example` - Template variables d'environnement
- ✅ Mis à jour `.gitignore` pour les fichiers générés

## 📦 Structure des fichiers

```
kart/
├── 📄 requirements.txt           ← Dépendances Python (pip)
├── 📄 package.json               ← Dépendances Node.js (npm)
├── 📄 tailwind.config.js         ← Configuration Tailwind
├── 📄 postcss.config.js          ← Configuration PostCSS
├── 📄 build.js                   ← Script de compilation CSS
├── 📄 .env.example               ← Variables d'environnement exemple
├── 📄 .gitignore                 ← Fichiers ignorés par Git
├── 📄 README.md                  ← Documentation générale
├── 📄 DEPLOYMENT.md              ← Guide PythonAnywhere
├── 📄 TAILWIND_GUIDE.md          ← Réference Tailwind CSS
├── BACK/
│   ├── settings.py               ← Modifié: STATIC_ROOT/STATICFILES_DIRS
│   ├── wsgi.py                   ← WSGI Django standard
│   └── wsgi_pythonanywhere.py    ← WSGI pour PythonAnywhere
├── artisans/
│   ├── static/css/
│   │   ├── main.css              ← Source Tailwind (🚫 ne pas éditer)
│   │   └── output.css            ← CSS compilé (généré par npm run build)
│   └── templates/artisans/
│       └── base.html             ← Modifié: utilise output.css
```

## 🚀 Commandes essentielles

### Développement local

```bash
# 1. Infrastructure
npm install              # Installer Node.js dependencies
pip install -r requirements.txt  # Installer Python dependencies

# 2. Démarrer en développement
npm run build           # Compiler Tailwind CSS UNE FOIS
python manage.py runserver  # Démarrer Django

# 3. Pendant le développement (optionnel)
npm run watch           # Recompiler CSS automatiquement quand les templates changent
```

### Avant chaque déploiement

```bash
# 1. Compiler le CSS
npm run build

# 2. Préparer les fichiers statiques
python manage.py collectstatic --noinput

# 3. Vérifier que tout compile
python manage.py check
```

### Sur PythonAnywhere

```bash
# 1. Première fois
git clone <repo> ~/kart
cd ~/kart
mkvirtualenv --python=/usr/bin/python3.10 kart
pip install -r requirements.txt
npm install

# 2. Compiler et déployer
npm run build
python manage.py collectstatic --noinput

# 3. Redémarrer depuis Dashboard > Web
```

## 🎨 Utilisation de Tailwind CSS

### Classes principales

```html
<!-- Couleurs Earth (Terra) -->
<div class="bg-earth-600 text-white">Élément principal</div>
<p class="text-earth-500">Texte accentué</p>

<!-- Couleurs Forest (Forêt) -->
<aside class="bg-forest-600">Sidebar verte</aside>

<!-- Layout Flexbox -->
<div class="flex items-center justify-between gap-4">
  <span>Gauche</span>
  <span>Droite</span>
</div>

<!-- Responsive -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
  Grille responsive
</div>
```

### Lors de la compilation

**IMPORTANT**: Tailwind CSS **ne compile que les classes utilisées** dans les fichiers HTML.

- Les fichiers scanés: `artisans/**/*.html`
- Le résultat: `output.css` contient UNIQUEMENT les styles nécessaires
- Taille finale: ~20-30 KB (au lieu de plusieurs MB)

## 📋 Checklist avant déploiement

- [ ] `npm run build` exécuté (CSS compilé)
- [ ] `python manage.py collectstatic --noinput` exécuté
- [ ] `DEBUG = False` dans `BACK/settings.py`
- [ ] `SECRET_KEY` remplacée par une clé sécurisée
- [ ] `ALLOWED_HOSTS` contient le domaine PythonAnywhere
- [ ] `.env` créé avec les variables d'environnement (non committé)
- [ ] WSGI configuré dans PythonAnywhere avec `wsgi_pythonanywhere.py`
- [ ] Fichiers statiques pointing vers `/staticfiles/`
- [ ] Application redémarrée depuis Dashboard

## 🔍 Fichiers importants à connaître

| Fichier | Utilité |
|---------|---------|
| `requirements.txt` | Dépendances Python (pip install) |
| `package.json` | Dépendances Node.js (npm scripts) |
| `tailwind.config.js` | Configuration couleurs et thème |
| `postcss.config.js` | Configuration pipeline CSS |
| `build.js` | Script de compilation manuelle |
| `BACK/settings.py` | Configuration Django (STATIC_ROOT) |
| `BACK/wsgi_pythonanywhere.py` | Configuration WSGI pour PythonAnywhere |
| `DEPLOYMENT.md` | Guide complet du déploiement |
| `TAILWIND_GUIDE.md` | Référence Tailwind CSS |

## ⚠️ Points critiques

### CSS ne s'affiche pas?
1. Exécutez `npm run build`
2. Vérifiez que `artisans/static/css/output.css` existe
3. Exécutez `python manage.py collectstatic --noinput` sur PythonAnywhere
4. Rechargez l'application

### Erreurs de module Django?
1. Vérifiez que le virtualenv est activé
2. Vérifiez `pip list | grep Django`
3. Vérifiez `PYTHONPATH` dans WSGI

### Tailwind à jour?
```bash
npm update
npm run build
```

## 📚 Pour aller plus loin

1. **Tailwind CSS:** Lire `TAILWIND_GUIDE.md`
2. **PythonAnywhere:** Lire `DEPLOYMENT.md`
3. **Django:** https://docs.djangoproject.com/en/6.0/
4. **Tailwind:** https://tailwindcss.com/docs

## 🎯 Prochaines étapes

1. [ ] Tester localement: `python manage.py runserver`
2. [ ] Tester la compilation: `npm run build`
3. [ ] Créer un compte PythonAnywhere
4. [ ] Pousser le code sur Git
5. [ ] Cloner et déployer sur PythonAnywhere
6. [ ] Configurer le domaine personnalisé (optionnel)

---

**Dernière mise à jour:** 18 Mai 2026
**Version Tailwind CSS:** 4.3.0
**Version Django:** 6.0.5
**Version Python:** 3.10+
