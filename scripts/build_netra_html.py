#!/usr/bin/env python3
"""Build products/netra-incident.html from reference HTML."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
REF = Path(r"C:\Projects\CNC\imp-conv\whatsapp_unknown_20260517_192917_html\output\netratrade-incident-intelligence.html")
SETU = ROOT / "products" / "setu-bridge.html"
ARCH = ROOT / "scripts" / "netra_arch_block.html"
OUT = ROOT / "products" / "netra-incident.html"


def transform_body(html: str) -> str:
    html = html.replace("NetraTrade;", "Netra&trade;")
    html = html.replace("NetraTrade", "Netra&trade;")
    html = html.replace('class="shell"', 'class="container"')
    html = html.replace('class="eyebrow"', 'class="section-eyebrow"')
    html = html.replace('class="button primary"', 'class="cta-btn"')
    html = html.replace('class="button secondary"', 'class="cta-btn-outline cta-btn"')
    html = html.replace('class="stat-num"', 'class="stat-value"')
    html = html.replace('class="hero-lead"', 'class="hero-sub"')
    html = html.replace('class="hero-cta"', 'class="hero-ctas"')
    html = html.replace('<span class="pill accent">', '<span class="hero-badge">')
    html = html.replace("https://pragyametrics.com/contact.html", "../contact.html")

    html = re.sub(r'<section id="([^"]+)" class="section-alt"', r'<section id="\1" class="section section-alt"', html)
    html = re.sub(r'<section id="([^"]+)" class="section-dark"', r'<section id="\1" class="section section-dark"', html)
    for sid in (
        "problem", "flows", "impact", "agents", "differentiators", "architecture",
        "outputs", "evidence", "industries", "engagement", "why-us", "built-by", "faq",
    ):
        html = html.replace(
            f'<section id="{sid}" aria-labelledby',
            f'<section id="{sid}" class="section" aria-labelledby',
            1,
        )

    # Hero layout
    html = re.sub(
        r'(<section class="hero"[^>]*>\s*<div class="container">)\s*<div>',
        r'\1\n<div class="hero-inner">\n<div>',
        html,
        count=1,
    )
    html = re.sub(
        r'(<div class="hero-inner">\s*<div>\s*)<div class="section-eyebrow">',
        r'\1<div class="hero-eyebrow">',
        html,
        count=1,
    )
    html = html.replace('class="hero-visual"', 'class="product-visual netra-hero-visual"', 1)
    html = re.sub(
        r'(</div>\s*</div>\s*)</section>\s*<div class="trust-strip"',
        r'\1</div>\n</section>\n\n<div class="trust-strip"',
        html,
        count=1,
    )
    html = html.replace('class="shell trust-strip-inner"', 'class="container trust-strip-inner"')

    html = html.replace("section-head center", "section-head section-head-center")

    arch = ARCH.read_text(encoding="utf-8")
    html = re.sub(
