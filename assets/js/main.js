// Main JavaScript file per il sito statico

// Inizializzazione quando il DOM è caricato
document.addEventListener('DOMContentLoaded', function() {
    console.log('Sito caricato correttamente');
    
    // Evidenzia il link attivo nella navigazione
    highlightActiveLink();
    
    // Aggiungi smooth scrolling per i link interni
    addSmoothScrolling();
});

/**
 * Evidenzia il link di navigazione corrispondente alla pagina corrente
 */
function highlightActiveLink() {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('header nav a');
    
    navLinks.forEach(link => {
        const linkPath = new URL(link.href).pathname;
        if (linkPath === currentPath || 
            (currentPath === '/' && linkPath === '/index.html')) {
            link.style.fontWeight = 'bold';
            link.style.textDecoration = 'underline';
        }
    });
}

/**
 * Aggiunge smooth scrolling per i link interni
 */
function addSmoothScrolling() {
    const internalLinks = document.querySelectorAll('a[href^="#"]');
    
    internalLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

/**
 * Utility: Mostra un messaggio temporaneo
 * @param {string} message - Il messaggio da mostrare
 * @param {number} duration - Durata in millisecondi
 */
function showMessage(message, duration = 3000) {
    const messageDiv = document.createElement('div');
    messageDiv.textContent = message;
    messageDiv.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background-color: #3498db;
        color: white;
        padding: 1rem 2rem;
        border-radius: 5px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.2);
        z-index: 1000;
        animation: slideIn 0.3s ease-out;
    `;
    
    document.body.appendChild(messageDiv);
    
    setTimeout(() => {
        messageDiv.style.animation = 'slideOut 0.3s ease-in';
        setTimeout(() => messageDiv.remove(), 300);
    }, duration);
}
