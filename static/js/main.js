// Handle responsive scaling
function handleResize() {
    const width = window.innerWidth;
    const container = document.querySelector('.main-container');
    
    if (width >= 992 && width <= 1600) {
        container.style.transform = 'scale(0.9)';
    } else if (width >= 700 && width <= 767) {
        container.style.transform = 'scale(0.8)';
    } else if (width >= 600 && width <= 700) {
        container.style.transform = 'scale(0.75)';
    } else if (width <= 600) {
        container.style.transform = 'scale(0.5)';
    } else {
        container.style.transform = 'scale(1)';
    }
}

function toggleMenu() {
    const leftMenu = document.querySelector('.left-menu');
    const isCollapsed = leftMenu.classList.contains('collapsed');
    
    if (isCollapsed) {
        leftMenu.classList.remove('collapsed');
        localStorage.setItem('menuCollapsed', 'false');
    } else {
        leftMenu.classList.add('collapsed');
        localStorage.setItem('menuCollapsed', 'true');
    }
}

// Initialize menu state
document.addEventListener('DOMContentLoaded', function() {
    const leftMenu = document.querySelector('.left-menu');
    const isCollapsed = localStorage.getItem('menuCollapsed') === 'true';
    
    if (isCollapsed) {
        leftMenu.classList.add('collapsed');
    } else {
        leftMenu.classList.remove('collapsed');
    }
});

