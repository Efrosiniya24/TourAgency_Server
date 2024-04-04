document.addEventListener('DOMContentLoaded', function() {
    const registerButton = document.getElementById('signIn');

    registerButton.addEventListener('click', function(event) {
        event.preventDefault();
        window.location.href = '/login';
    });
});