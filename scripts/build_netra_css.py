from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
css = (ROOT / "css" / "pragya.css").read_text(encoding="utf-8")
css = css.replace("page-pragya", "page-netra").replace("pragya-main", "netra-main").replace("--pm-", "--nu-")
i = css.find("/* —— Discovery blocks")
if i > 0:
    css = css[:i].rstrip()
extra = (ROOT / "scripts" / "netra_extra.css").read_text(encoding="utf-8")
(ROOT / "css" / "netra.css").write_text(css + "\n\n" + extra, encoding="utf-8")
print("Wrote css/netra.css")
