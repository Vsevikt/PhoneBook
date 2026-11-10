const search = document.querySelector('#search');

const phoneInput = document.querySelector('[data-phone-validation]');

if (phoneInput) {
    const phoneError = document.querySelector('[data-phone-error]');
    const phonePattern = /^\+?[0-9 ]*[0-9]$/;

    const validatePhone = () => {
        const invalid = phoneInput.value !== '' && !phonePattern.test(phoneInput.value);
        phoneError.hidden = !invalid;
        phoneInput.setCustomValidity(invalid ? 'Use digits, spaces, and an optional + at the beginning.' : '');
    };

    phoneInput.addEventListener('input', validatePhone);
    phoneInput.form.addEventListener('submit', validatePhone);
}

if (search) {
    search.addEventListener('input', () => {
        document.querySelectorAll('.contact').forEach(contact => {
            contact.hidden = !contact.textContent.toLowerCase().includes(search.value.toLowerCase());
        });
    });
}
