const acceptLinks = document.querySelectorAll('.accept-link');
acceptLinks.forEach(link => {
    link.addEventListener('click', event => {
        const acceptForm = event.target.nextElementSibling;
        acceptForm.classList.toggle('show');
    });
});