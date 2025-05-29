// static/js/login.js
document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const usernameInput = document.getElementById('username');
    const passwordInput = document.getElementById('password');

    // Focus sur le champ username au chargement
    usernameInput.focus();

    // Efface les champs si une erreur est détectée (par exemple, après un POST invalide)
    form.addEventListener('submit', function () {
        if (form.querySelector('.alert-danger')) {
            passwordInput.value = ''; // Efface le mot de passe pour sécurité
        }
    });
});