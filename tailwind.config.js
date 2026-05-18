/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./artisans/**/*.html",
  ],
  theme: {
    extend: {
      colors: {
        earth: {
          50:  '#fdf8f0', 100: '#f9edd8', 200: '#f2d9ac',
          300: '#e8be76', 400: '#dc9f44', 500: '#cc8228',
          600: '#b3681e', 700: '#944f1a', 800: '#78401b', 900: '#633619',
        },
        forest: { 500: '#2d6a4f', 600: '#1b4332', 700: '#081c15' },
      }
    }
  },
  plugins: [],
}
