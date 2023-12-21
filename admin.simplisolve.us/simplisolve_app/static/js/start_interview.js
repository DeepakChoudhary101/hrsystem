const rejectLinks = document.querySelectorAll('.accept-link');
    
rejectLinks.forEach(link => {
    link.addEventListener('click', event => {
        const rejectForm = event.target.nextElementSibling;
        rejectForm.classList.toggle('show');
    });
});