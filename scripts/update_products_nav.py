#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
OLD = re.compile(
    r'<a href="([^"]*?)(?:pragya-cnc|setu-bridge)\.html" class="nav-products(?: active)?">Products<span class="nav-badge">NEW</span></a>'
)


def blocks(prefix: str, active: str | None) -> tuple[str, str]:
    ap = ' class="active"' if active == 'pragya' else ''
    as_ = ' class="active"' if active == 'setu' else ''
    pragya = f'{prefix}pragya-cnc.html'
    setu = f'{prefix}setu-bridge.html'
    desktop = f'''<div class="nav-item-products">
            <a href="{pragya}" class="nav-products-trigger">Products<span class="nav-badge">NEW</span></a>
            <ul class="nav-products-dropdown" aria-label="Products">
                <li><a href="{pragya}"{ap}>Pragya&trade; <span>Maintenance intelligence</span></a></li>
                <li><a href="{setu}"{as_}>Setu&trade; <span>Bridge design intelligence</span></a></li>
            </ul>
        </div>'''
    mobile = f'''<motion class="nav-products-group">
            <span class="nav-products-label">Products<span class="nav-badge">NEW</span></span>
            <div class="nav-products-sublinks">
                <a href="{pragya}"{ap}>Pragya&trade;</a>
                <a href="{setu}"{as_}>Setu&trade;</a>
            </div>
        </div>'''.replace('<motion class="nav-products-group">', '<motion class="nav-products-group">').replace(
        '<motion class="nav-products-group">', '<div class="nav-products-group">'
    )
    return desktop, mobile


def main():
    for path in list(ROOT.glob('*.html')) + list(ROOT.glob('blogs/*.html')) + list((ROOT / 'products').glob('*.html')):
        text = path.read_text(encoding='utf-8')
        if 'Products<span class="nav-badge">' not in text:
            continue
        rel = path.relative_to(ROOT).as_posix()
        if rel == 'products/pragya-cnc.html':
            prefix, active = '', 'pragya'
        elif rel == 'products/setu-bridge.html':
            prefix, active = '', 'setu'
        elif rel.startswith('blogs/'):
            prefix, active = '../products/', None
        else:
            prefix, active = 'products/', None

        desktop, mobile = blocks(prefix, active)
        if 'nav-item-products' in text:
            print('skip (already)', rel)
            continue

        new = text
        # desktop: first match only (header)
        new = OLD.sub(desktop, new, count=1)
        # mobile: second match
        new = OLD.sub(mobile, new, count=1)

        if new != text:
            path.write_text(new, encoding='utf-8')
            print('OK', rel)


if __name__ == '__main__':
    main()
