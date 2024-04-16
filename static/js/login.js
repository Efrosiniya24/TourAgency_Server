document.addEventListener('DOMContentLoaded', function() {
    const registerButton = document.getElementById('signUp');

    registerButton.addEventListener('click', function(event) {
        event.preventDefault();
        window.location.href = '/signUp';
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const registerButton = document.getElementById('signIn');

    registerButton.addEventListener('click', function(event) {
        event.preventDefault();
        window.location.href = '/mainAdmin';
    });
});