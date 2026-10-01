#!/usr/bin/env python3
"""Turns CV.md into index.html. Edit CV.md only, then run:  python3 build.py

Needs one package once:  pip3 install markdown
For the PDF: open index.html in Chrome, File > Print > Save as PDF (A4, margins default).
"""
import pathlib, sys
try:
    import markdown
except ImportError:
    sys.exit("Run first:  pip3 install markdown")

here = pathlib.Path(__file__).parent
body = markdown.markdown((here / "CV.md").read_text(encoding="utf-8"), extensions=["sane_lists"])
page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Saba Azadegan, CV</title>
<style>
  :root {{ --ink:#1b1b1b; --muted:#555; --line:#d8d8d8; --link:#1a4fa0; }}
  * {{ box-sizing: border-box; }}
  body {{ font: 15px/1.5 Georgia, "Times New Roman", serif; color: var(--ink); background:#fff;
         max-width: 780px; margin: 0 auto; padding: 32px 20px 60px; }}
  h1 {{ font-size: 2rem; margin: 0 0 4px; text-align: center; letter-spacing: .02em; }}
  h1 + p, h1 + p + p {{ text-align: center; margin: 2px 0; color: var(--muted); font-size: .92em; }}
  h2 {{ font-size: 1.05rem; text-transform: uppercase; letter-spacing: .06em; border-bottom: 1px solid var(--ink);
       padding-bottom: 3px; margin: 26px 0 10px; }}
  h3 {{ font-size: 1rem; margin: 14px 0 0; }}
  h3 + p {{ margin: 0 0 4px; color: var(--muted); }}
  p {{ margin: 6px 0; }}
  ul {{ margin: 4px 0 6px; padding-left: 20px; }}
  li {{ margin: 3px 0; }}
  a {{ color: var(--link); text-decoration: none; }}
  a:hover {{ text-decoration: underline; }}
  @media print {{
    @page {{ size: A4; margin: 14mm 14mm; }}
    body {{ font-size: 10pt; line-height: 1.38; max-width: none; padding: 0; }}
    h2 {{ margin: 14px 0 6px; }}
    h3 {{ break-after: avoid; }}
    a {{ color: var(--ink); }}
  }}
</style>
</head>
<body>
{body}
</body>
</html>
"""
(here / "index.html").write_text(page, encoding="utf-8")
print("Wrote index.html")
