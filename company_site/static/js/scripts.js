document.addEventListener("DOMContentLoaded", function () {
    const track = document.querySelector(".scroll-carousel-track");
    const items = Array.from(track.children);

    if (!track || items.length === 0) {
        console.error("Carousel track or items not found.");
        return;
    }

    // Clone items for seamless looping
    items.forEach((item) => {
        const clone = item.cloneNode(true);
        track.appendChild(clone);
    });

    const itemWidth = items[0].offsetWidth + 20; // Include gap (adjust if needed)
    const totalItems = items.length; // Original item count
    const totalScrollWidth = itemWidth * totalItems; // Width of original items

    let scrollPosition = 0;

    function scrollCarousel() {
        scrollPosition -= 1; // Adjust speed (smaller = slower, larger = faster)

        // Reset position when the first set of items has scrolled out of view
        if (Math.abs(scrollPosition) >= totalScrollWidth) {
            scrollPosition = 0;
        }

        track.style.transform = `translateX(${scrollPosition}px)`;
        requestAnimationFrame(scrollCarousel);
    }

    scrollCarousel(); // Start scrolling
});