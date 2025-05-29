// static/js/register.js
document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const inputs = form.querySelectorAll('input, select');

    inputs.forEach(input => {
        input.addEventListener('input', function () {
            const errorList = this.nextElementSibling;
            if (errorList && errorList.classList.contains('errorlist')) {
                errorList.style.display = this.value ? 'block' : 'none';
            }
        });
    });
});