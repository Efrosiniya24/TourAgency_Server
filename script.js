const sidebar = document.querySelector('.sidebar');
const toggleButton = document.querySelector('.sidebar-toggle');

toggleButton.addEventListener('click', () => {
    sidebar.classList.toggle('active');
});