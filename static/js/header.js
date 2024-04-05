document.addEventListener('DOMContentLoaded', function() {
    const loginButton = document.getElementById('AboutUsButton');

    loginButton.addEventListener('click', function(event) {
        event.preventDefault();
        window.location.href = '/aboutUs';
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const loginButton = document.getElementById('MainPageButton');

    loginButton.addEventListener('click', function(event) {
        event.preventDefault();
        window.location.href = '/';
    });
});


