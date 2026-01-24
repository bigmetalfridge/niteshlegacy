const themeSwitcher = document.querySelector('.theme-switcher');
const body = document.body;

// Check for a saved theme in localStorage
const savedTheme = localStorage.getItem('theme');
if (savedTheme) {
    body.classList.add(savedTheme);
}

themeSwitcher.addEventListener('click', () => {
    body.classList.toggle('dark-theme');
    // Save the theme to localStorage
    if (body.classList.contains('dark-theme')) {
        localStorage.setItem('theme', 'dark-theme');
    } else {
        localStorage.removeItem('theme');
    }
});
