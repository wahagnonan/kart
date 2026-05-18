# Guide Tailwind CSS - Artisans CI

## Introduction

Ce projet utilise **Tailwind CSS v4** avec une architecture modiste pour le styling. Tailwind est un framework CSS utilitaire qui permet de construire des interfaces en composant des classes pré-définies.

**Documentation officielle:** https://tailwindcss.com

## Configuration du Project

### Fichiers de configuration

- **`tailwind.config.js`** - Configuration Tailwind (couleurs, thème, etc.)
- **`postcss.config.js`** - Configuration PostCSS pour Tailwind
- **`artisans/static/css/main.css`** - Fichier source Tailwind avec les directives @tailwind
- **`artisans/static/css/output.css`** - Fichier CSS compilé (généré automatiquement)

### Build et Compilation

#### Development

```bash
npm run build    # Compiler une seule fois
npm run watch    # Recompiler automatiquement lors des changements
```

#### Production

Avant de déployer sur PythonAnywhere:

```bash
npm run build
python manage.py collectstatic --noinput
```

## Architecture Tailwind

### Couleurs personnalisées

Les couleurs du projet sont définies dans `tailwind.config.js`:

#### Earth Colors (Terra/Terre)
```javascript
earth: {
  50:  '#fdf8f0',   // Extra clair
  100: '#f9edd8',
  200: '#f2d9ac',
  300: '#e8be76',
  400: '#dc9f44',
  500: '#cc8228',   // Principal
  600: '#b3681e',   // Sombre
  700: '#944f1a',
  800: '#78401b',
  900: '#633619'    // Très sombre
}
```

#### Forest Colors (Forêt)
```javascript
forest: {
  500: '#2d6a4f',   // Vert moyen
  600: '#1b4332',   // Vert foncé
  700: '#081c15'    // Très foncé
}
```

### Utilisation des couleurs

**Texte:**
```html
<p class="text-earth-500">Texte en terre</p>
<p class="text-forest-600">Texte en forêt foncé</p>
```

**Fond:**
```html
<div class="bg-earth-50">Fond clair</div>
<div class="bg-forest-600">Fond forêt foncé</div>
```

**Bordures:**
```html
<div class="border-earth-200">Bordure légère</div>
<div class="border-forest-500">Bordure forêt</div>
```

## Guide d'utilisation courante

### Layout

#### Flexbox
```html
<!-- Flex row (défaut) -->
<div class="flex">
  <div>Colonne 1</div>
  <div>Colonne 2</div>
</div>

<!-- Flex column -->
<div class="flex flex-col">
  <div>Ligne 1</div>
  <div>Ligne 2</div>
</div>

<!-- Espace entre -->
<div class="flex justify-between">...</div>

<!-- Centré -->
<div class="flex items-center justify-center">...</div>
```

#### Grid
```html
<div class="grid grid-cols-3 gap-4">
  <div>1</div>
  <div>2</div>
  <div>3</div>
</div>
```

### Espacements

```html
<!-- Padding (intérieur) -->
<div class="p-4">        <!-- tout -->
<div class="px-4">       <!-- horizontal -->
<div class="py-2">       <!-- vertical -->
<div class="pt-4">       <!-- top -->

<!-- Margin (extérieur) -->
<div class="m-4">        <!-- tout -->
<div class="mx-auto">    <!-- centré horizontalement -->
<div class="mb-2">       <!-- bottom -->
```

### Texte et typographie

```html
<!-- Taille -->
<p class="text-xs">Extra petit</p>
<p class="text-sm">Petit</p>
<p class="text-base">Normal (défaut)</p>
<p class="text-lg">Large</p>
<p class="text-xl">Très large</p>
<p class="text-2xl">2x large</p>

<!-- Poids -->
<p class="font-light">Léger</p>
<p class="font-normal">Normal</p>
<p class="font-semibold">Semi-gras</p>
<p class="font-bold">Gras</p>

<!-- Alignement -->
<p class="text-left">Aligner à gauche</p>
<p class="text-center">Centré</p>
<p class="text-right">Aligner à droite</p>
```

### Boutons et interactions

```html
<!-- Bouton de base -->
<button class="px-4 py-2 bg-earth-600 text-white rounded">
  Cliquer
</button>

<!-- Avec hover -->
<button class="px-4 py-2 bg-earth-600 text-white rounded hover:bg-earth-700 transition-colors">
  Cliquer
</button>

<!-- Bouton secondaire -->
<button class="px-4 py-2 border-2 border-earth-600 text-earth-600 rounded hover:bg-earth-50">
  Secondaire
</button>
```

### Cartes

```html
<div class="bg-white rounded-lg shadow-lg p-6">
  <h2 class="text-xl font-bold mb-3">Titre</h2>
  <p class="text-gray-600 mb-4">Description</p>
  <button>Action</button>
</div>
```

### Navigation

```html
<!-- Navbar -->
<nav class="bg-forest-600 px-4 py-3">
  <div class="flex justify-between items-center">
    <div class="text-white font-bold">Logo</div>
    <ul class="flex gap-6">
      <li><a href="#" class="text-white hover:text-earth-300">Lien</a></li>
      <li><a href="#" class="text-white hover:text-earth-300">Lien</a></li>
    </ul>
  </div>
</nav>
```

## Responsive Design

Tailwind utilise des breakpoints pour le responsive:

- `sm:` - 640px et plus
- `md:` - 768px et plus
- `lg:` - 1024px et plus
- `xl:` - 1280px et plus
- `2xl:` - 1536px et plus

### Exemple

```html
<!-- Caché sur mobile, visible sur tablette -->
<div class="hidden md:block">
  Contenu desktop
</div>

<!-- Colonne sur mobile, 2 colonnes sur desktop -->
<div class="grid grid-cols-1 md:grid-cols-2">
  <div>Colonne 1</div>
  <div>Colonne 2</div>
</div>

<!-- Taille adaptée par écran -->
<h1 class="text-lg md:text-2xl lg:text-4xl">Titre</h1>
```

## États et pseudo-classes

```html
<!-- Hover -->
<button class="hover:bg-earth-700">Survoler</button>

<!-- Focus -->
<input class="focus:ring-2 focus:ring-earth-400" />

<!-- Active -->
<button class="active:scale-95">Cliquer</button>

<!-- Disabled -->
<button disabled class="disabled:opacity-50 cursor-not-allowed">Désactivé</button>

<!-- Group hover -->
<div class="group hover:bg-gray-50">
  <p class="group-hover:text-earth-600">Texto changera selon le hover du parent</p>
</div>
```

## Animations

```html
<!-- Transition -->
<div class="transition-colors hover:bg-earth-600">
  Changement fluide
</div>

<!-- Animations intégrées -->
<div class="animate-spin">Tourner</div>
<div class="animate-pulse">Pulsation</div>
<div class="animate-bounce">Rebond</div>
```

## Utilité avancée

### Combine des classe

```html
<div class="flex items-center justify-between gap-4 p-6 bg-white rounded-lg shadow">
  <!-- Plusieurs classes pour un effet complet -->
</div>
```

### Variables CSS personnalisées

Si vous nécessitez des styles au-delà de Tailwind, modifier `artisans/static/css/main.css`:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer components {
  .btn-primary {
    @apply px-4 py-2 bg-earth-600 text-white rounded hover:bg-earth-700 transition-colors;
  }
}
```

Utilisez ensuite:
```html
<button class="btn-primary">Cliquer</button>
```

## Structure de Tailwind

Tailwind génère 3 couches de styles:

### @tailwind base
- Reset CSS standard
- Styles de base des éléments HTML

### @tailwind components
- Classes de composants réutilisables
- Classes personnalisées via @layer components

### @tailwind utilities
- Toutes les classes utilitaires (px-, py-, bg-, text-, etc.)
- La majorité des classes Tailwind

## Performance

### Production

Le fichier `output.css` généré contient UNIQUEMENT les classes utilisées dans votre HTML grâce au content purging.

Dans `tailwind.config.js`, la directive content spécifie les fichiers à scanner:

```javascript
content: [
  "./artisans/**/*.html",  // Tous les fichiers HTML du app
],
```

**Important:** Assurez-vous que tous les fichiers templates et statiques sont inclus dans la directive `content`.

## Ressources

- **Documentation officielle:** https://tailwindcss.com/docs
- **Tailwind UI Components:** https://tailwindui.com (exemples payants mais inspirant)
- **Tailwind CSS IntelliSense:** Extension VS Code pour l'autocomplétion
- **Tailwind Play:** https://play.tailwindcss.com (éditeur en ligne)

## Dépannage courant

### Les styles ne s'appliquent pas

1. Vérifiez que `npm run build` a été exécuté
2. Vérifiez que le fichier utilise les bonnes classes (pas de typos)
3. Vérifiez que le CSS est bien lié dans le template: `{% load static %} <link rel="stylesheet" href="{% static 'css/output.css' %}">`

### Classes inconnues

Tailwind ne compile que les classes utilisées dans les fichiers spécifiés dans `content`. Si une classe n'existe pas en output.css:

1. Vérifiez l'orthographe
2. Vérifiez que le fichier HTML est dans le chemin `./artisans/**/*.html`
3. Recompiler: `npm run build`

### Le watch ne recompile pas automatiquement

Installez chokidar (si manquant):
```bash
npm install -D chokidar-cli
```

## Bonnes pratiques

1. **Utilisez les couleurs personnalisées** - `earth-*` et `forest-*` pour la cohérence
2. **Enchaînez les classes** plutôt que d'écrire du CSS personnalisé
3. **Utilisez les breakpoints** pour l'adaptation mobile
4. **Créez des @layer components** pour les patterns récurrents
5. **Compilez en production** - ne comptez pas sur le CDN en production
