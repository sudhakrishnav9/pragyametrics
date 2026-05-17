import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
pat = re.compile(
    r'<a href="[^"]*(?:pragya-cnc|setu-bridge)[^"]*" class="nav-products-trigger">Products<span class="nav-badge">NEW</span></a>'
)
btn = (
    '<button type="button" class="nav-products-trigger" '
    'aria-expanded="false" aria-haspopup="true">'
    'Products<span class="nav-badge">NEW</span></button>'
)
for p in list(ROOT.glob('*.html')) + list(ROOT.glob('blogs/*.html')) + list((ROOT / 'products').glob('*.html')):
    text = p.read_text(encoding='utf-8')
    new, n = pat.subn(btn, text)
    if n:
        p.write_text(new, encoding='utf-8')
        print(p.relative_to(ROOT), n)
