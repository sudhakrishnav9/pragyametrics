from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
css = (ROOT / "css" / "pragya.css").read_text(encoding="utf-8")
css = css.replace("page-pragya", "page-setu").replace("pragya-main", "setu-main").replace("--pm-", "--su-")
i = css.find("/* —— Discovery blocks")
if i > 0:
    css = css[:i].rstrip()
extra = (ROOT / "scripts" / "setu_extra.css").read_text(encoding="utf-8")
(ROOT / "css" / "setu.css").write_text(css + "\n\n" + extra, encoding="utf-8")
print("Wrote css/setu.css")
