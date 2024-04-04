document.addEventListener('DOMContentLoaded', function() {
    const registerButton = document.getElementById('registerButton');

    registerButton.addEventListener('click', function(event) {
        event.preventDefault();
        window.location.href = '/registration';
    });
});