// static/js/modal.js
const modal = document.getElementById('contact-modal');
const backdrop = document.getElementById('modal-backdrop');
const closeBtn = document.getElementById('modal-close');
const form = document.getElementById('contact-form');
const submitBtn = document.getElementById('submit-btn');
const successMsg = document.getElementById('success-msg');

// Open modal — attach to all CTA buttons
const ctaButtons = document.querySelectorAll('[data-open-modal]');
ctaButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
        e.preventDefault();
        openModal();
    });
});

function openModal() {
    modal.classList.remove('hidden');
    modal.classList.add('flex');
    document.body.style.overflow = 'hidden';
}

function closeModal() {
    modal.classList.add('hidden');
    modal.classList.remove('flex');
    document.body.style.overflow = '';
}

// Close on backdrop click
backdrop.addEventListener('click', closeModal);

// Close on X button
closeBtn.addEventListener('click', closeModal);

// Close on ESC key
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeModal();
});

// Form submission via fetch
form.addEventListener('submit', async (e) => {
    e.preventDefault();

    // Clear previous errors
    document.querySelectorAll('.error-msg').forEach(el => {
        el.classList.add('hidden');
        el.textContent = '';
    });

    // Update button state
    submitBtn.textContent = 'Sending...';
    submitBtn.disabled = true;

    const formData = new FormData(form);

    try {
        const response = await fetch('/contact/', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': formData.get('csrfmiddlewaretoken'),
            }
        });

        const data = await response.json();

        if (data.status === 'success') {
            const formEl = document.getElementById('contact-form');
            const successEl = document.getElementById('success-msg');

            form.classList.add('hidden');
            successMsg.classList.remove('hidden');

            formEl.style.display = 'none';
            successEl.style.display = 'block';
            successEl.style.textAlign = 'center';
            successEl.style.padding = '2rem 0';

            // Auto close after 3 seconds
            setTimeout(() => {
                closeModal();
                formEl.style.display = 'block';
                successEl.style.display = 'none';
                formEl.reset();
                submitBtn.textContent = 'Send Message';
                submitBtn.disabled = false;
            }, 3000);


        } else if (data.status === 'invalid') {
            // Show field errors
            Object.entries(data.errors).forEach(([field, errors]) => {
                const errorEl = document.querySelector(`[data-field="${field}"]`);
                if (errorEl) {
                    errorEl.textContent = errors[0];
                    errorEl.classList.remove('hidden');
                }
            });
            submitBtn.textContent = 'Send Message';
            submitBtn.disabled = false;

        } else {
            alert('Something went wrong. Please try again.');
            submitBtn.textContent = 'Send Message';
            submitBtn.disabled = false;
        }

    } catch (err) {
        alert('Network error. Please try again.');
        submitBtn.textContent = 'Send Message';
        submitBtn.disabled = false;
    }
});