from pathlib import Path

src = Path(r"C:\Users\sudha_22wqh89\Downloads\pragyametrics-v02.html").read_text(encoding="utf-8")
start = src.index("<!-- ============== HERO ============== -->")
end = src.index("<!-- ============== FOOTER ============== -->")
main = src[start:end].strip()

main = main.replace(
    '<a href="#engagement" class="cta-btn cta-btn-lg">Schedule a Plant-Readiness Conversation &rarr;</a>',
    '<a href="../contact.html" class="cta-btn cta-btn-lg">Schedule a Plant-Readiness Conversation &rarr;</a>',
)
main = main.replace(
    '<a href="#architecture" class="cta-btn cta-btn-outline cta-btn-lg">Request Executive Overview</a>',
    '<a href="mailto:info@pragyametrics.com?subject=Pragya%20Executive%20Overview%20Request" class="cta-btn cta-btn-outline cta-btn-lg">Request Executive Overview</a>',
)

header = """    <header id="header">
        <motion></motion>
"""

header = """    <header id="header">
        <div class="logo-container">
            <a href="../index.html" style="display:flex;align-items:center;text-decoration:none;">
                <img src="../images/brain.png" alt="Pragyametrics Logo" class="logo">
                <div class="logo-text-container">
                    <span class="logo-text">Pragya<span class="highlight">metrics</span></span>
                    <span class="tagline" id="tagline">Where Knowledge Meets Intelligence</span>
                    <div class="connection-line" id="connection-line"></motion>
                </div>
            </a>
        </div>
        <nav>
            <a href="../index.html#about">About</a>
            <a href="../services.html">Services</a>
            <a href="../methodology.html">Methodology</a>
            <a href="pragya-cnc.html" class="nav-products new-badge">Products</a>
            <a href="../engagement-models.html">Engagement Models</a>
            <a href="../blog.html">Blog</a>
            <a href="../contact.html">Contact Us</a>
        </nav>
        <div class="mobile-menu-toggle" id="mobile-menu-toggle">
            <span></span><span></span><span></span>
        </motion>
    </header>
    <div class="mobile-menu" id="mobile-menu">
        <nav>
            <a href="../index.html#about">About</a>
            <a href="../services.html">Services</a>
            <a href="../methodology.html">Methodology</a>
            <a href="pragya-cnc.html" class="nav-products new-badge">Products</a>
            <a href="../engagement-models.html">Engagement Models</a>
            <a href="../blog.html">Blog</a>
            <a href="../contact.html">Contact Us</a>
        </nav>
    </div>
"""

# fix typos motion -> span/div
header = header.replace("<motion>", "<span>").replace("</motion>", "</span>")
header = header.replace('<div class="connection-line" id="connection-line"></span>', '<motion></motion>')
header = header.replace("<motion></motion>", '<motion></motion>')

header = """    <header id="header">
        <div class="logo-container">
            <a href="../index.html" style="display:flex;align-items:center;text-decoration:none;">
                <img src="../images/brain.png" alt="Pragyametrics Logo" class="logo">
                <div class="logo-text-container">
                    <span class="logo-text">Pragya<span class="highlight">metrics</span></span>
                    <span class="tagline" id="tagline">Where Knowledge Meets Intelligence</span>
                    <div class="connection-line" id="connection-line"></div>
                    <motion></motion>
                </div>
            </a>
        </div>
        <nav>
            <a href="../index.html#about">About</a>
            <a href="../services.html">Services</a>
            <a href="../methodology.html">Methodology</a>
            <a href="pragya-cnc.html" class="nav-products new-badge">Products</a>
            <a href="../engagement-models.html">Engagement Models</a>
            <a href="../blog.html">Blog</a>
            <a href="../contact.html">Contact Us</a>
        </nav>
        <div class="mobile-menu-toggle" id="mobile-menu-toggle">
            <span></span><span></span><span></span>
        </div>
    </header>
    <motion></motion>
"""

header = header.replace("<motion></motion>", '<div class="particles-container" id="particles-container"></motion>')
header = header.replace("</motion>", "</div>")
header = header.replace('<motion></motion>', '<div class="mobile-menu" id="mobile-menu">PLACEHOLDER</div>')

# Too messy - write header as clean string
header = """    <header id="header">
        <div class="logo-container">
            <a href="../index.html" style="display:flex;align-items:center;text-decoration:none;">
                <img src="../images/brain.png" alt="Pragyametrics Logo" class="logo">
                <motion></motion>
            </a>
        </div>
"""

# Final clean version
header = """    <header id="header">
        <div class="logo-container">
            <a href="../index.html" style="display:flex;align-items:center;text-decoration:none;">
                <img src="../images/brain.png" alt="Pragyametrics Logo" class="logo">
                <div class="logo-text-container">
                    <span class="logo-text">Pragya<span class="highlight">metrics</span></span>
                    <span class="tagline" id="tagline">Where Knowledge Meets Intelligence</span>
                    <div class="connection-line" id="connection-line"></div>
                    <div class="particles-container" id="particles-container"></div>
                </div>
            </a>
        </div>
        <nav>
            <a href="../index.html#about">About</a>
            <a href="../services.html">Services</a>
            <a href="../methodology.html">Methodology</a>
            <a href="pragya-cnc.html" class="nav-products new-badge">Products</a>
            <a href="../engagement-models.html">Engagement Models</a>
            <a href="../blog.html">Blog</a>
            <a href="../contact.html">Contact Us</a>
        </nav>
        <motion></motion>
    </header>
    <div class="mobile-menu" id="mobile-menu">
        <nav>
            <a href="../index.html#about">About</a>
            <a href="../services.html">Services</a>
            <a href="../methodology.html">Methodology</a>
            <a href="pragya-cnc.html" class="nav-products new-badge">Products</a>
            <a href="../engagement-models.html">Engagement Models</a>
            <a href="../blog.html">Blog</a>
            <a href="../contact.html">Contact Us</a>
        </nav>
    </div>
"""
header = header.replace("<motion></motion>", '<motion></motion>')
header = header.replace(
    """        <nav>
            <a href="../index.html#about">About</a>
            <a href="../services.html">Services</a>
            <a href="../methodology.html">Methodology</a>
            <a href="pragya-cnc.html" class="nav-products new-badge">Products</a>
            <a href="../engagement-models.html">Engagement Models</a>
            <a href="../blog.html">Blog</a>
            <a href="../contact.html">Contact Us</a>
        </nav>
        <motion></motion>
    </header>""",
    """        <nav>
            <a href="../index.html#about">About</a>
            <a href="../services.html">Services</a>
            <a href="../methodology.html">Methodology</a>
            <a href="pragya-cnc.html" class="nav-products new-badge">Products</a>
            <a href="../engagement-models.html">Engagement Models</a>
            <a href="../blog.html">Blog</a>
            <a href="../contact.html">Contact Us</a>
        </nav>
        <motion></motion>
    </header>""",
)
header = header.replace(
    """        </nav>
        <motion></motion>
    </header>""",
    """        </nav>
        <div class="mobile-menu-toggle" id="mobile-menu-toggle">
            <span></span><span></span><span></span>
        </div>
    </header>""",
)

footer = """
    <footer id="footer">
        <div class="container">
            <div class="footer-content">
                <div class="company-info">
                    <h3>Pragyametrics</h3>
                    <p>8B, Phase-1, Manjri Greens,<br>Hadapsar, Pune, Maharashtra<br>India - 412307</p>
                </div>
                <div class="contact-info">
                    <h4>Contact Us</h4>
                    <p>📧 info@pragyametrics.com</p>
                    <p>📞 +91 77090 50817</p>
                </div>
            </div>
            <p class="copyright">© 2026 Pragyametrics (OPC) Private Limited. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
"""

head = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pragya&trade; by Pragyametrics &mdash; AI-Assisted Maintenance Intelligence | Read-only. Local-first. Citation-backed.</title>
    <meta name="description" content="Pragya&trade; by Pragyametrics is a read-only, local-first AI-assisted maintenance intelligence suite for industrial machine fleets. Citation-backed, multi-controller, deterministic by design. Built in India, India-first.">
    <meta name="keywords" content="AI maintenance India, predictive maintenance India, multi-controller AI, MTConnect OPC UA AI, plant floor AI, manufacturing AI India, Pragya AI maintenance, Pragyametrics Pragya">
    <meta property="og:title" content="Pragya&trade; by Pragyametrics &mdash; Your Plant's Maintenance Copilot | Pragyametrics">
    <meta property="og:description" content="AI that makes every engineer your best engineer. Read-only by design. Citation-backed. Multi-controller aware.">
    <meta property="og:type" content="website">
    <link rel="canonical" href="https://pragyametrics.com/products/pragya-cnc.html">
    <link rel="icon" href="../images/brain128.png" type="image/png">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Playfair+Display:wght@700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../css/style.css">
    <link rel="stylesheet" href="../css/animations.css">
    <link rel="stylesheet" href="../css/header.css">
    <link rel="stylesheet" href="../css/pragya.css">
    <script type="text/javascript">
            (function(c,l,a,r,i,t,y){
                c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
                t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
                y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
            })(window, document, "clarity", "script", "rgwjbwq5hz");
    </script>
    <script src="../js/clarity-user-tracking.js" defer></script>
    <script src="../js/script.js" defer></script>
</head>
<body class="page-pragya">
"""

html = head + header + '\n    <main id="main-content" class="pragya-main">\n' + main + '\n    </main>\n' + footer
out = Path(r"C:\Projects\pragya_site\products\pragya-cnc.html")
out.parent.mkdir(exist_ok=True)
out.write_text(html, encoding="utf-8")
print("wrote", out, "bytes", out.stat().st_size)
