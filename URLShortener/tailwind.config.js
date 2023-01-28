/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './URLShortener/templates/**/*.{html,js}'
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
  ],
}
