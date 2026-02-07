document.addEventListener('DOMContentLoaded', () => {
    // --- 1. Hero Immediate Reveal (Fast Logic) ---
    // Specifically target hero elements for immediate/staggered reveal without waiting for scroll
    const heroElements = document.querySelectorAll('header [style*="opacity:0"], header [style*="opacity: 0"], #intro [style*="opacity:0"], #intro [style*="opacity: 0"]');

    heroElements.forEach(el => {
        el.style.opacity = '1';
        el.style.transform = 'translate3d(0, 0, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0)';
    });

    // Staggered H1 spans (Hero)
    const h1Spans = document.querySelectorAll('h1 .span-txt');
    h1Spans.forEach((span, index) => {
        setTimeout(() => {
            span.style.transition = 'all 0.8s ease-out';
            span.style.opacity = '1';
            span.style.transform = 'translate3d(0, 0, 0)';
        }, index * 100);
    });

    // Reveal "Ujet" large letters (Hero)
    const letters = document.querySelectorAll('.lg-slide-txt');
    letters.forEach((letter, index) => {
        setTimeout(() => {
            letter.style.transition = 'all 0.8s ease-out';
            letter.style.opacity = '1';
            letter.style.transform = 'translate3d(0, 0, 0)';
        }, 500 + index * 100);
    });

    // --- 2. Global Scroll Observer (Lazy Reveal) ---
    // This handles the rest of the page content
    const observerOptions = {
        root: null, // viewport
        rootMargin: '0px',
        threshold: 0.1 // 10% visible to trigger
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const el = entry.target;

                // Add transition locally if not present (inline styles might override classes)
                // We use a safe transition that doesn't conflict too much
                el.style.transition = 'opacity 0.8s ease-out, transform 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94)';

                // Force visibility and reset position
                el.style.opacity = '1';
                // Resetting transform is critical as Webflow sets initial transforms (e.g. translateY(50px))
                // We reset to identity matrix
                el.style.transform = 'translate3d(0, 0, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0)';

                el.classList.add('revealed');

                // Stop observing once revealed
                observer.unobserve(el);
            }
        });
    }, observerOptions);

    // Target all elements that are hidden by inline styles
    // Exclude hero elements that we already force-revealed (optional optimization, but safe to re-observe)
    const hiddenElements = document.querySelectorAll('[style*="opacity:0"], [style*="opacity: 0"]');

    hiddenElements.forEach(el => {
        // Optional: Skip if already revealed by hero logic (checking opacity manually is tricky due to computed style, 
        // but since we set inline style, we can check that. However, re-observing is harmless and ensures it stays visible).
        observer.observe(el);
    });

    // Also target lazyloaded images to ensure they fade in nicely if they rely on this
    const lazyImages = document.querySelectorAll('.lazyload');
    lazyImages.forEach(el => observer.observe(el));
});
