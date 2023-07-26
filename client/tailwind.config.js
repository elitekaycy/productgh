/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        './public/**/*.html', // Scan HTML files in the public folder
        './src/**/*.vue',
        // Scan Vue component files in the src folder
        // Add other file paths if necessary
    ],
    theme: {
        extend: {}
    },
    plugins: []
}
