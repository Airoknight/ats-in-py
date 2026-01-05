document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('hero-canvas');
    const context = canvas.getContext('2d');
    const frameCount = 33;
    const currentFrame = index => (
        `/static/images/hero_sequence/ezgif-frame-${index.toString().padStart(3, '0')}.jpg`
    );

    const images = [];
    const heroSection = document.querySelector('.hero-section');

    // Set canvas dimensions
    const updateCanvasSize = () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        // Redraw current frame if images potentially loaded
        const scrollTop = window.scrollY;
        const heroHeight = heroSection.offsetHeight;
        const windowHeight = window.innerHeight;
        const scrollFraction = Math.max(0, Math.min(1, scrollTop / (heroHeight - windowHeight)));
        const frameIndex = Math.min(frameCount - 1, Math.ceil(scrollFraction * frameCount));
        if (images[frameIndex] && images[frameIndex].complete) {
            drawFrame(frameIndex + 1);
        }
    };

    window.addEventListener('resize', updateCanvasSize);
    updateCanvasSize(); // Initial call

    // Preload images
    const preloadImages = () => {
        for (let i = 1; i <= frameCount; i++) {
            const img = new Image();
            img.src = currentFrame(i);
            images.push(img);
        }
    };

    const drawFrame = (index) => {
        const img = images[index - 1];
        if (img && img.complete) {
            // Calculate cover logic
            const ptrn = context.createPattern(img, 'no-repeat');
            // Actually, just drawImage with scaling to cover
            // But simplest is letting CSS object-fit work if we draw full image to canvas.
            // If we set canvas.width to window width, we should draw image to fill it.

            // Strategy: Draw image to fill the canvas while maintaining aspect ratio (crop)
            const hRatio = canvas.width / img.width;
            const vRatio = canvas.height / img.height;
            const ratio = Math.max(hRatio, vRatio);
            const centerShift_x = (canvas.width - img.width * ratio) / 2;
            const centerShift_y = (canvas.height - img.height * ratio) / 2;

            context.clearRect(0, 0, canvas.width, canvas.height);
            context.drawImage(img,
                0, 0, img.width, img.height,
                centerShift_x, centerShift_y, img.width * ratio, img.height * ratio);
        }
    };

    const img = new Image();
    img.src = currentFrame(1);
    images[0] = img;
    img.onload = () => {
        drawFrame(1);
    };

    const updateImage = index => {
        drawFrame(index);
    };

    window.addEventListener('scroll', () => {
        const scrollTop = window.scrollY;
        const heroHeight = heroSection.offsetHeight;
        const windowHeight = window.innerHeight;

        // 1. Text Fade Effect
        // Fade out completely after scrolling 500px or so
        const fadeStart = 0;
        const fadeEnd = 500;
        let opacity = 1 - (scrollTop - fadeStart) / (fadeEnd - fadeStart);
        opacity = Math.max(0, Math.min(1, opacity));

        // Also add a subtle translation
        const translateY = scrollTop * 0.4;

        const content = document.querySelector('.hero-content');
        if (content) {
            content.style.opacity = opacity;
            content.style.transform = `translate(-50%, calc(-50% + ${translateY}px))`;
        }

        // 2. Image Sequence Logic
        // Calculate scroll fraction within the hero section
        const scrollFraction = Math.max(0, Math.min(1, scrollTop / (heroHeight - windowHeight)));

        const frameIndex = Math.min(
            frameCount - 1,
            Math.ceil(scrollFraction * frameCount)
        );

        requestAnimationFrame(() => updateImage(frameIndex + 1));
    });

    preloadImages();

    // GSAP for other animations (optional, but using vanilla js for lightweight for now)
    // Navbar reveal on scroll setup if needed

    // --- Scroll Animation Observer ---
    const observerOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');

                // Add staggered animation for children if it's a grid
                if (entry.target.classList.contains('pricing-grid')) {
                    const cards = entry.target.querySelectorAll('.pricing-card');
                    cards.forEach((card, index) => {
                        setTimeout(() => {
                            card.style.opacity = '1';
                            card.style.transform = 'translateY(0)';
                        }, index * 100);
                    });
                }
            }
        });
    }, observerOptions);

    const revealElements = document.querySelectorAll('.reveal-on-scroll');
    revealElements.forEach((el) => observer.observe(el));
});
