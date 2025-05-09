/**
 * Enhanced Clarity User Tracking
 * For Pragyametrics.com - Compliant with privacy regulations
 */

(function() {
    // Wait for Clarity to be initialized
    function initClarityTracking() {
        // Check if Clarity is blocked
        if (typeof window.clarity === "undefined") {
            // Try again after a delay, but limit retries
            if (!window.clarityRetries) window.clarityRetries = 0;
            if (window.clarityRetries < 5) {
                window.clarityRetries++;
                setTimeout(initClarityTracking, 1000);
            } else {
                console.log("Clarity may be blocked by browser. Consider adding a consent notice.");
            }
            return;
        }

        // ===== 1. BASIC DEVICE & BROWSER INFO =====
        trackDeviceInfo();
        
        // ===== 2. PAGE & NAVIGATION INFO =====
        trackPageInfo();
        
        // ===== 3. USER INTERACTION TRACKING =====
        setupInteractionTracking();
    }

    // Track device and browser information
    function trackDeviceInfo() {
        try {
            // Device type detection
            const isMobile = /Android|webOS|iPhone|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
            const isTablet = /iPad|Android.*?Chrome\/[.0-9]* (?!Mobile)/i.test(navigator.userAgent);
            const deviceType = isMobile ? "mobile" : (isTablet ? "tablet" : "desktop");
            
            window.clarity("set", "device_type", deviceType);
            
            // Browser detection
            let browserName = "Unknown";
            const userAgent = navigator.userAgent;
            if (userAgent.indexOf("Firefox") > -1) browserName = "Firefox";
            else if (userAgent.indexOf("SamsungBrowser") > -1) browserName = "Samsung";
            else if (userAgent.indexOf("Opera") > -1 || userAgent.indexOf("OPR") > -1) browserName = "Opera";
            else if (userAgent.indexOf("Trident") > -1) browserName = "Internet Explorer";
            else if (userAgent.indexOf("Edge") > -1) browserName = "Edge";
            else if (userAgent.indexOf("Chrome") > -1) browserName = "Chrome";
            else if (userAgent.indexOf("Safari") > -1) browserName = "Safari";
            
            window.clarity("set", "browser", browserName);
            
            // Screen dimensions
            window.clarity("set", "screen_size", `${window.screen.width}x${window.screen.height}`);
            window.clarity("set", "viewport_size", `${window.innerWidth}x${window.innerHeight}`);
            
            // Language
            window.clarity("set", "language", navigator.language || "unknown");
            
            // Prioritize this session for recording
            window.clarity("upgrade", "detailed_session");
        } catch (e) {
            console.error("Error tracking device info:", e);
        }
    }

    // Track page and navigation information
    function trackPageInfo() {
        try {
            // Current page
            const pagePath = window.location.pathname;
            const pageName = pagePath.split('/').pop() || 'home';
            window.clarity("set", "page_name", pageName);
            
            // Referrer information
            if (document.referrer) {
                try {
                    const referrerURL = new URL(document.referrer);
                    window.clarity("set", "referrer_domain", referrerURL.hostname);
                    window.clarity("set", "referrer_full", document.referrer);
                } catch (e) {
                    console.log("Error parsing referrer");
                }
            }
            
            // URL parameters (UTM tracking)
            const urlParams = new URLSearchParams(window.location.search);
            for (const [key, value] of urlParams.entries()) {
                if (key.startsWith('utm_')) {
                    window.clarity("set", key, value);
                }
            }
            
            // Page load timing
            window.addEventListener('load', function() {
                if (window.performance && window.performance.timing) {
                    const timing = window.performance.timing;
                    const pageLoadTime = timing.loadEventEnd - timing.navigationStart;
                    if (pageLoadTime > 0) {
                        window.clarity("set", "page_load_time_ms", pageLoadTime);
                    }
                }
            });
        } catch (e) {
            console.error("Error tracking page info:", e);
        }
    }

    // Set up tracking for user interactions
    function setupInteractionTracking() {
        try {
            // Track CTA button clicks
            document.querySelectorAll('.cta-button, a[href="contact.html"]').forEach(button => {
                button.addEventListener('click', function() {
                    const buttonText = this.textContent.trim();
                    const buttonLocation = getElementLocation(this);
                    window.clarity("set", "cta_click", buttonText);
                    window.clarity("set", "cta_location", buttonLocation);
                });
            });
            
            // Track mobile menu interactions
            const mobileMenuToggle = document.getElementById('mobile-menu-toggle');
            if (mobileMenuToggle) {
                mobileMenuToggle.addEventListener('click', function() {
                    window.clarity("set", "mobile_menu_click", "true");
                });
            }
            
            // Track Engagement Models menu interactions
            const engagementMenuLink = document.querySelector('a[href="engagement-models.html"]');
            if (engagementMenuLink) {
                engagementMenuLink.addEventListener('mouseenter', function() {
                    window.clarity("set", "engagement_models_hover", "true");
                });
                
                engagementMenuLink.addEventListener('click', function() {
                    window.clarity("set", "engagement_models_click", "true");
                });
            }
            
            // Track scroll depth
            let maxScrollPercentage = 0;
            window.addEventListener('scroll', function() {
                const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
                const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
                const scrollPercentage = Math.round((scrollTop / scrollHeight) * 100);
                
                if (scrollPercentage > maxScrollPercentage) {
                    maxScrollPercentage = scrollPercentage;
                    
                    // Report at 25%, 50%, 75%, and 100%
                    if (scrollPercentage >= 25 && maxScrollPercentage < 50) {
                        window.clarity("set", "scroll_depth", "25%");
                    } else if (scrollPercentage >= 50 && maxScrollPercentage < 75) {
                        window.clarity("set", "scroll_depth", "50%");
                    } else if (scrollPercentage >= 75 && maxScrollPercentage < 100) {
                        window.clarity("set", "scroll_depth", "75%");
                    } else if (scrollPercentage >= 100) {
                        window.clarity("set", "scroll_depth", "100%");
                    }
                }
            });
        } catch (e) {
            console.error("Error setting up interaction tracking:", e);
        }
    }
    
    // Helper function to get element location
    function getElementLocation(element) {
        const rect = element.getBoundingClientRect();
        const viewportHeight = window.innerHeight;
        
        if (rect.top < viewportHeight / 3) return "top";
        if (rect.top < (viewportHeight * 2/3)) return "middle";
        return "bottom";
    }
    
    // Initialize when DOM is ready
    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", initClarityTracking);
    } else {
        initClarityTracking();
    }
})();
