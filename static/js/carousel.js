const track = document.getElementById('testimonial-track');
const cursor = document.getElementById('carousel-cursor');

if (track) {
    let isPaused = false;
    let isDragging = false;
    let startX = 0;
    let scrollLeft = 0;

    // Clone cards for infinite loop
    Array.from(track.children).forEach(card => {
        const clone = card.cloneNode(true);
        clone.setAttribute('aria-hidden', 'true');
        track.appendChild(clone);
    });

    // Auto scroll
    function autoScroll() {
        if (!isPaused) {
            track.scrollLeft += 0.5;
            if (track.scrollLeft >= track.scrollWidth / 2) {
                track.scrollLeft = 0;
            }
        }
        requestAnimationFrame(autoScroll);
    }

    const resumeScroll = () => {
        isDragging = false;
        setTimeout(() => { isPaused = false; }, 2000);
    };

    // Custom cursor — show on enter, hide on leave
    track.addEventListener('mouseenter', () => {
        cursor.classList.remove('hidden');
        cursor.classList.add('flex');
        track.style.cursor = 'none';
    });

    track.addEventListener('mouseleave', () => {
        cursor.classList.add('hidden');
        cursor.classList.remove('flex');
        track.style.cursor = 'default';
        resumeScroll();
    });

    // Mouse drag + cursor follow
    track.addEventListener('mousemove', (e) => {
        // Always follow mouse
        cursor.style.left = e.clientX + 'px';
        cursor.style.top = e.clientY + 'px';

        // Only drag if mousedown
        if (!isDragging) return;
        const x = e.pageX - track.offsetLeft;
        track.scrollLeft = scrollLeft - (x - startX) * 1.5;
    });

    track.addEventListener('mousedown', (e) => {
        isDragging = true;
        isPaused = true;
        startX = e.pageX - track.offsetLeft;
        scrollLeft = track.scrollLeft;
        // Scale up cursor on grab
        cursor.style.transform = 'translate(-50%, -50%) scale(0.85)';
    });

    track.addEventListener('mouseup', () => {
        cursor.style.transform = 'translate(-50%, -50%) scale(1)';
        resumeScroll();
    });

    // Touch support
    track.addEventListener('touchstart', (e) => {
        isPaused = true;
        startX = e.touches[0].pageX - track.offsetLeft;
        scrollLeft = track.scrollLeft;
    });

    track.addEventListener('touchmove', (e) => {
        const x = e.touches[0].pageX - track.offsetLeft;
        track.scrollLeft = scrollLeft - (x - startX) * 1.5;
    });

    track.addEventListener('touchend', () => {
        setTimeout(() => { isPaused = false; }, 2000);
    });

    autoScroll();
}