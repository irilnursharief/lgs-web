// static/js/hero-carousel.js
const slides = document.querySelectorAll('.hero-slide');
const dots = document.querySelectorAll('.hero-dot');
let current = 0;
let interval = null;
const DURATION = 10000; // 10 seconds

function goToSlide(index) {
    // Hide current slide
    slides[current].classList.add('hidden');
    slides[current].classList.remove('grid');
    dots[current].classList.remove('bg-primary-container', 'w-4');
    dots[current].classList.add('bg-surface-container');

    // Show new slide
    current = index;
    slides[current].classList.remove('hidden');
    slides[current].classList.add('grid');
    dots[current].classList.remove('bg-surface-container');
    dots[current].classList.add('bg-primary-container', 'w-4');
}

function nextSlide() {
    const next = (current + 1) % slides.length;
    goToSlide(next);
}

function startAutoRotate() {
    interval = setInterval(nextSlide, DURATION);
}

function stopAutoRotate() {
    clearInterval(interval);
}

// Dot click — manual navigation
dots.forEach(dot => {
    dot.addEventListener('click', () => {
        stopAutoRotate();
        goToSlide(parseInt(dot.dataset.index));
        startAutoRotate(); // restart timer after manual interaction
    });
});

// Pause on hover
const heroSection = document.getElementById('hero-slides');
if (heroSection) {
    heroSection.addEventListener('mouseenter', stopAutoRotate);
    heroSection.addEventListener('mouseleave', startAutoRotate);
}

// Init
startAutoRotate();