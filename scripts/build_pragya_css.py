import re
from pathlib import Path

src = Path(r"C:\Users\sudha_22wqh89\Downloads\pragyametrics-v02.html").read_text(encoding="utf-8")
css = re.search(r"<style>(.*?)</style>", src, re.DOTALL).group(1)
css = re.sub(
    r"/\* ==== TOP NAV ==== \*/.*?/\* ==== HERO ==== \*/",
    "/* ==== HERO ==== */",
    css,
    flags=re.DOTALL,
)
css = re.sub(
    r"/\* ==== FOOTER ==== \*/.*?/\* ==== RESPONSIVE ==== \*/",
    "/* ==== RESPONSIVE ==== */",
    css,
    flags=re.DOTALL,
)

SCOPE = "body.page-pragya .pragya-main"


def prefix_block(block: str) -> str:
    block = block.strip()
    if not block:
        return block
    # @media wrapper
    media = re.match(r"(@media[^{]+)\{(.+)\}$", block, re.DOTALL)
    if media:
        inner = prefix_rules(media.group(2))
        return f"{media.group(1)}{{\n{inner}\n}}"
    return prefix_rules(block)


def prefix_rules(css_text: str) -> str:
    out = []
    depth = 0
    buf = ""
    for ch in css_text:
        buf += ch
        if ch == "{":
            depth += 1
            if depth == 1:
                sel, rest = buf[:-1].rsplit("{", 1) if "{" in buf[:-1] else (buf[:-1], "")
                sel = sel.strip()
                if sel.startswith("@"):
                    out.append(sel + "{")
                elif sel:
                    for part in sel.split(","):
                        part = part.strip()
                        if part in ("from", "to") or part.endswith("%"):
                            out.append(part + "{")
                        else:
                            out.append(f"{SCOPE} {part}" + "{")
                else:
                    out.append("{")
                buf = ""
        elif ch == "}":
            depth -= 1
            out.append(buf)
            buf = ""
    return "".join(out)


# Simpler line-based approach for flat CSS
lines_out = []
in_media = None
buffer_sel = []

def flush_rule(selector, body_lines):
    global lines_out
    if not selector:
        return
    sel = selector.strip()
    if sel.startswith("@"):
        lines_out.append(sel + " {")
    else:
        parts = [p.strip() for p in sel.split(",") if p.strip()]
        prefixed = ", ".join(f"{SCOPE} {p}" for p in parts)
        lines_out.append(prefixed + " {")
    lines_out.extend(body_lines)
    lines_out.append("}")


# Parse with regex for rule blocks
pattern = re.compile(
    r"(@media[^{]+)\{((?:[^{}]|\{[^{}]*\})*)\}|([^{}@]+)\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}",
    re.DOTALL,
)

base = """/* Pragya™ product page */
body.page-pragya{
  font-family:'Inter',system-ui,-apple-system,sans-serif;
  background:#fff;color:#0f172a;
}
body.page-pragya #main-content.pragya-main{
  --bg:#fff;--bg-soft:#f8fafc;--bg-softer:#f1f5f9;--bg-dark:#0a1628;--bg-darker:#050d17;
  --text:#0f172a;--text-mid:#334155;--text-muted:#475569;--text-light:#94a3b8;
  --primary:#1e40af;--primary-dark:#1e3a8a;--primary-light:#3b82f6;
  --accent:#0891b2;--accent-light:#06b6d4;--accent-bright:#67e8f9;
  --success:#059669;--warning:#d97706;--danger:#dc2626;
  --border:#e2e8f0;--border-strong:#cbd5e1;
  --radius:12px;--radius-sm:8px;
  --shadow-sm:0 1px 3px rgba(15,23,42,0.06);
  --shadow:0 4px 16px rgba(15,23,42,0.08);
  --shadow-lg:0 12px 40px rgba(15,23,42,0.14);
  padding-top:0;margin-top:0;
}
body.page-pragya header#header{border-bottom:1px solid rgba(174,249,241,0.15);}
body.page-pragya nav a.nav-products{font-weight:600;color:var(--highlight-text,#fff)!important;}
body.page-pragya nav a.new-badge::after{content:'NEW';margin-left:6px;background:#0891b2;color:#fff;font-size:9px;padding:2px 6px;border-radius:4px;font-weight:700;vertical-align:middle;letter-spacing:.7px;}
body.page-pragya .pragya-main a{color:var(--primary);}
body.page-pragya .pragya-main a:hover{color:var(--accent);}
.product-spotlight{background:linear-gradient(135deg,#0a1628,#0d2a4a);padding:4rem 0;color:#e0e0e0;}
.product-spotlight h2{color:#fff;font-size:2rem;margin-bottom:1rem;}
.product-spotlight p{color:#cbd5e1;max-width:720px;margin-bottom:1.5rem;}
.product-spotlight-badges{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:1.5rem;}
.product-spotlight-badge{background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.14);padding:6px 12px;border-radius:6px;font-size:11px;color:#cbd5e1;}
.product-spotlight-ctas{display:flex;flex-wrap:wrap;gap:12px;}
.services-product-banner{background:rgba(30,64,175,0.12);border:1px solid rgba(8,145,178,0.35);border-radius:12px;padding:2rem;margin-bottom:2.5rem;}
.services-product-banner h3{color:var(--highlight-text);margin-bottom:0.75rem;}
.services-product-banner p{margin-bottom:1rem;color:var(--light-text);}
.blog-pragya-cta{background:rgba(8,145,178,0.12);border-left:4px solid #0891b2;padding:1.5rem 2rem;margin:2rem 0;border-radius:0 8px 8px 0;}
.blog-pragya-cta h3{margin-bottom:0.5rem;color:var(--highlight-text);}
"""

# Remove :root and global resets from css - we handle via .pragya-main
css = re.sub(r":root\{[^}]+\}", "", css)
css = re.sub(r"\*,\*::before,\*::after\{[^}]+\}", "", css)
css = re.sub(r"html\{[^}]+\}", "", css)
css = re.sub(r"body\{[^}]+\}", "", css)
css = re.sub(r"\.container\{", f"{SCOPE} .container{{", css)
css = re.sub(r"^a\{", f"{SCOPE} a{{", css, flags=re.M)
css = re.sub(r"^a:hover\{", f"{SCOPE} a:hover{{", css, flags=re.M)
css = re.sub(r"^img,svg\{", f"{SCOPE} img,{SCOPE} svg{{", css, flags=re.M)
css = re.sub(r"^button\{", f"{SCOPE} button{{", css, flags=re.M)

# Prefix class/id selectors at start of rules (after comments/newlines)
def prefix_selector_line(m):
    sel = m.group(1)
    if sel.strip().startswith("@") or sel.strip().startswith(SCOPE):
        return m.group(0)
    parts = [p.strip() for p in sel.split(",")]
    return ", ".join(f"{SCOPE} {p}" for p in parts) + "{"

# Match selectors before { that aren't inside @media already handled
result = []
i = 0
while i < len(css):
    if css.startswith("@media", i):
        end = css.find("}", i)
        # find matching close for media - count braces
        depth = 0
        j = i
        while j < len(css):
            if css[j] == "{":
                depth += 1
            elif css[j] == "}":
                depth -= 1
                if depth == 0:
                    media_block = css[i : j + 1]
                    inner = re.match(r"(@media[^{]+)\{(.+)\}$", media_block, re.DOTALL)
                    if inner:
                        inner_css = inner.group(2)
                        fixed_inner = re.sub(
                            r"([^{}@/][^{]*?)\{",
                            lambda m: ", ".join(
                                f"{SCOPE} {p.strip()}"
                                for p in m.group(1).split(",")
                                if p.strip() and not p.strip().startswith(SCOPE)
                            )
                            + "{"
                            if m.group(1).strip()
                            and not m.group(1).strip().startswith("@")
                            else m.group(0),
                            inner_css,
                        )
                        result.append(inner.group(1) + "{" + fixed_inner + "}")
                    else:
                        result.append(media_block)
                    i = j + 1
                    break
            j += 1
        continue
    m = re.match(r"([.#a-zA-Z][^{]*?)\{", css[i:])
    if m and not css[i:].startswith("/*"):
        sel = m.group(1).strip()
        if sel and not sel.startswith(SCOPE):
            parts = [p.strip() for p in sel.split(",")]
            prefixed = ", ".join(f"{SCOPE} {p}" for p in parts)
            result.append(prefixed + "{")
            i += m.end()
            continue
    # comment or other
    nl = css.find("\n", i)
    if nl == -1:
        result.append(css[i:])
        break
    chunk = css[i : nl + 1]
    if chunk.strip().startswith("/*"):
        result.append(chunk)
    i = nl + 1

# Fallback: simple replace for lines starting with . or #
fixed_css = css
for sel_pat in [
    r"(?m)^(\.[a-zA-Z][^\{]*)\{",
    r"(?m)^(#[^\{]*)\{",
]:
    fixed_css = re.sub(
        sel_pat,
        lambda m: ", ".join(f"{SCOPE} {p.strip()}" for p in m.group(1).split(","))
        + "{",
        fixed_css,
    )

# Fix @media blocks manually
def fix_media(m):
    header, body = m.group(1), m.group(2)
    body2 = re.sub(
        r"([^{}]+)\{",
        lambda x: ", ".join(f"{SCOPE} {p.strip()}" for p in x.group(1).split(",")) + "{",
        body,
    )
    return header + "{" + body2 + "}"

fixed_css = re.sub(r"(@media[^{]+)\{(.+?)\}(?=\s*(?:@media|/\*|$))", fix_media, fixed_css, flags=re.DOTALL)

Path(r"C:\Projects\pragya_site\css\pragya.css").write_text(base + fixed_css, encoding="utf-8")
print("OK", len(base + fixed_css))
