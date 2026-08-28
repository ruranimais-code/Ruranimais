document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('#signup-form');
    if (!form) return;
    form.addEventListener('submit', (event) => {
        const email = document.querySelector('#email');
        const password = document.querySelector('#senha');
        const confirmation = document.querySelector('#confirmar_senha');
        email.setCustomValidity('');
        confirmation.setCustomValidity('');
        if (!email.value.toLowerCase().endsWith('@ufrpe.br')) {
            event.preventDefault();
            email.setCustomValidity('Utilize um e-mail institucional @ufrpe.br.');
            email.reportValidity();
        } else if (password.value !== confirmation.value) {
            event.preventDefault();
            confirmation.setCustomValidity('As senhas não coincidem.');
            confirmation.reportValidity();
        }
    });
});
