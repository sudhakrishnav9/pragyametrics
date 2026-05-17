from pathlib import Path

p = Path(r"C:\Projects\pragya_site\products\pragya-cnc.html")
html = p.read_text(encoding="utf-8")
frag = Path(r"C:\Projects\pragya_site\products\_arch-diagram-fragment.html").read_text(encoding="utf-8")
start = html.index("<div class=\"arch-wrap\">")
end = html.index("<div class=\"arch-cta-band\">")
p.write_text(html[:start] + frag + "\n" + html[end:], encoding="utf-8")
print("patched", start, end)
