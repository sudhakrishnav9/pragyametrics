// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Mobile menu functionality
    const mobileMenuToggle = document.getElementById('mobile-menu-toggle');
    const mobileMenu = document.getElementById('mobile-menu');
    
    if (mobileMenuToggle && mobileMenu) {
        mobileMenuToggle.addEventListener('click', function() {
            this.classList.toggle('active');
            mobileMenu.classList.toggle('active');
            document.body.classList.toggle('menu-open');
        });
    }

    // Add data flow elements to the brain
    const brainWrapper = document.querySelector('.brain-wrapper');
    if (brainWrapper) {
        for (let i = 0; i < 10; i++) {
            const dataFlow = document.createElement('div');
            dataFlow.className = 'data-flow';
            // Randomize position
            dataFlow.style.left = Math.random() * 100 + '%';
            dataFlow.style.top = Math.random() * 100 + '%';
            brainWrapper.appendChild(dataFlow);
        }
    }

    // Add scroll indicator to hero section
    const heroSection = document.querySelector('.hero');
    if (heroSection && !document.querySelector('.scroll-indicator')) {
        const scrollIndicator = document.createElement('div');
        scrollIndicator.className = 'scroll-indicator';
        heroSection.appendChild(scrollIndicator);
    }

    // Intersection Observer for scroll animations
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, {
        threshold: 0.1
    });

    // Observe sections
    document.querySelectorAll('.about, .pillars, .cta-banner').forEach(section => {
        observer.observe(section);
    });

    // Observe pillar cards and add index for staggered animation
    const pillars = document.querySelectorAll('.pillar');
    pillars.forEach((pillar, index) => {
        pillar.style.setProperty('--item-index', index);
        observer.observe(pillar);
    });

    // Typing effect for hero heading (optional)
    const heroHeading = document.querySelector('.hero-text h1');
    if (heroHeading && !heroHeading.classList.contains('typing-effect')) {
        // Only apply if not already using fade-in animation
        if (!heroHeading.classList.contains('animate-fadein')) {
            heroHeading.classList.add('typing-effect');
        }
    }

    // Handle header scroll effect
    window.addEventListener('scroll', function() {
        const header = document.querySelector('header');
        if (window.scrollY > 100) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });

    // Smooth scroll for navigation links
    document.querySelectorAll('nav a, .cta-button, .secondary-button').forEach(link => {
        link.addEventListener('click', function(e) {
            // Only apply to internal links
            if (this.getAttribute('href').startsWith('#')) {
                e.preventDefault();
                const targetId = this.getAttribute('href');
                const targetElement = document.querySelector(targetId);
                
                if (targetElement) {
                    window.scrollTo({
                        top: targetElement.offsetTop - 100,
                        behavior: 'smooth'
                    });
                    
                    // Close mobile menu if open
                    if (mobileMenu && mobileMenu.classList.contains('active')) {
                        mobileMenuToggle.classList.remove('active');
                        mobileMenu.classList.remove('active');
                        document.body.classList.remove('menu-open');
                    }
                }
            }
        });
    });

    // Add hover animation to brain image
    const brainImage = document.querySelector('.brain-image');
    if (brainImage) {
        brainImage.addEventListener('mouseover', function() {
            this.classList.add('animate-glow');
        });
        
        brainImage.addEventListener('mouseout', function() {
            this.classList.remove('animate-glow');
        });
    }
    
    // Create tagline particles - Call directly within main DOMContentLoaded event
    createTaglineParticles();
    // Also set a delayed call to ensure animations have started
    setTimeout(createTaglineParticles, 3000);
    
    // Add ripple effect to all buttons
    const buttons = document.querySelectorAll('.cta-button, .secondary-button');
    buttons.forEach(button => {
        button.addEventListener('click', createRipple);
    });
});

// Add header class for scrolled state on page load if needed
window.addEventListener('load', function() {
    const header = document.querySelector('header');
    if (window.scrollY > 100) {
        header.classList.add('scrolled');
    }
});

// Helper function for custom button ripple effect
function createRipple(event) {
    const button = event.currentTarget;
    
    const circle = document.createElement('span');
    const diameter = Math.max(button.clientWidth, button.clientHeight);
    const radius = diameter / 2;
    
    circle.style.width = circle.style.height = `${diameter}px`;
    circle.style.left = `${event.clientX - button.offsetLeft - radius}px`;
    circle.style.top = `${event.clientY - button.offsetTop - radius}px`;
    circle.classList.add('ripple');
    
    const ripple = button.querySelector('.ripple');
    if (ripple) {
        ripple.remove();
    }
    
    button.appendChild(circle);
}

// Tagline particles function - Define before it's used
function createTaglineParticles() {
    console.log("Starting tagline particles creation...");
    const particlesContainer = document.getElementById('particles-container');
    const tagline = document.getElementById('tagline');
    
    if (!particlesContainer || !tagline) {
        console.log("Missing elements:", !particlesContainer ? "particles-container" : "", !tagline ? "tagline" : "");
        return;
    }
    
    // Clear any existing particles
    particlesContainer.innerHTML = '';
    
    // Create more particles (increase from 20 to 30)
    for (let i = 0; i < 30; i++) {
        const particle = document.createElement('div');
        particle.className = 'tagline-particle';
        
        // Random initial position - span wider horizontally
        const randomX = Math.random() * 120 - 10; // From -10% to 110%
        const randomY = Math.random() * 30 - 15; // From -15px to +15px
        
        // Larger size for better visibility
        const size = Math.random() * 5 + 3;
        
        // Apply styles directly to the element
        particle.style.position = 'absolute';
        particle.style.width = `${size}px`;
        particle.style.height = `${size}px`;
        particle.style.backgroundColor = Math.random() > 0.5 ? '#4096ee' : '#50c878';
        particle.style.borderRadius = '50%';
        particle.style.left = `${randomX}%`;
        particle.style.top = `${randomY}px`;
        particle.style.opacity = '0';
        particle.style.boxShadow = `0 0 ${size * 2}px ${size}px ${Math.random() > 0.5 ? 'rgba(64, 150, 238, 0.5)' : 'rgba(80, 200, 120, 0.5)'}`;
        particle.style.zIndex = '10';
        
        // Set animation directly (avoid cssText which might have syntax issues)
        const animDuration1 = Math.random() * 3 + 3;
        const animDuration2 = Math.random() * 2 + 2;
        const animDelay = Math.random() * 2 + 4;
        
        particle.style.animation = `float-particle ${animDuration1}s ease-in-out ${animDelay}s infinite alternate, fade-particle ${animDuration2}s ease-in-out ${animDelay}s forwards`;
        
        particlesContainer.appendChild(particle);
    }
    
    console.log(`Created ${particlesContainer.children.length} particles`);
}
