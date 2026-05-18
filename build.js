const fs = require('fs');
const path = require('path');
const postcss = require('postcss');
const tailwindcss = require('@tailwindcss/postcss');

const inputPath = path.join(__dirname, 'artisans/static/css/main.css');
const outputPath = path.join(__dirname, 'artisans/static/css/output.css');

const input = fs.readFileSync(inputPath, 'utf-8');

postcss([
  tailwindcss
]).process(input, { from: inputPath, to: outputPath })
  .then(result => {
    fs.writeFileSync(outputPath, result.css);
    console.log('✅ Tailwind CSS compiled successfully!');
  })
  .catch(err => {
    console.error('❌ Error compiling Tailwind CSS:', err);
    process.exit(1);
  });
