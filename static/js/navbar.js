const btn = document.getElementById('mobile-menu-btn');
const menu = document.getElementById('mobile-menu');
const bar1 = document.getElementById('bar1');
const bar2 = document.getElementById('bar2');
const bar3 = document.getElementById('bar3');

if (btn) {
    btn.addEventListener('click', () => {
        menu.classList.toggle('hidden');
        menu.classList.toggle('flex');
        bar1.classList.toggle('rotate-45');
        bar1.classList.toggle('translate-y-2');
        bar2.classList.toggle('opacity-0');
        bar3.classList.toggle('-rotate-45');
        bar3.classList.toggle('-translate-y-2');
    });
}