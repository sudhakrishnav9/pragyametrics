#!/usr/bin/env python3
"""Add Netra to Products dropdown on all site pages."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
NETRA_LINE = '<li><a href="{p}netra-incident.html{active}">Netra&trade; <span>Incident intelligence</span></a></li>'
MOBILE_LINE = '<a href="{p}netra-incident.html{active}">Netra&trade;</a>'


def prefix_for(rel: str) -> str:
    if rel.startswith("products/"):
        return ""
    if rel.startswith("blogs/"):
        return "../products/"
    return "products/"


def patch_file(path: Path) -> bool:
    rel = path.relative_to(ROOT).as_posix()
    text = path.read_text(encoding="utf-8")
    if "nav-products-dropdown" not in text or "netra-incident" in text:
        return False
    p = prefix_for(rel)
    active_desktop = ' class="active"' if rel == "products/netra-incident.html" else ""
    active_mobile = ' class="active"' if rel == "products/netra-incident.html" else ""

    new = text
    if "setu-bridge.html" in text and "netra-incident" not in text:
        new = re.sub(
            r'(<li><a href="[^"]*setu-bridge\.html"[^>]*>Setu&trade;.*?</a></li>)\s*(</ul>)',
            r"\1\n                " + NETRA_LINE.format(p=p, active=active_desktop) + r"\n            \2",
            new,
            count=1,
        )
        new = re.sub(
            r'(<a href="[^"]*setu-bridge\.html"[^>]*>Setu&trade;</a>)\s*(</div>)',
            lambda m: m.group(1) + "\n                " + MOBILE_LINE.format(p=p, active=active_mobile) + "\n            " + m.group(2),
            new,
            count=1,
        )
    if new != text:
        path.write_text(new, encoding="utf-8")
        return True
    return False


def main():
    paths = list(ROOT.glob("*.html")) + list(ROOT.glob("blogs/*.html")) + list((ROOT / "products").glob("*.html"))
    for path in paths:
        if patch_file(path):
            print("OK", path.relative_to(ROOT))


if __name__ == "__main__":
    main()
