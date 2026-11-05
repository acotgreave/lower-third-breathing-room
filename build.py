"""Build index.html from src/page.html, embedding the screenshot as a data URI.

Run:  python build.py
"""
import base64
from pathlib import Path

root = Path(__file__).parent
page = (root / "src" / "page.html").read_text(encoding="utf-8")
img = base64.b64encode((root / "src" / "cnn-election-night.webp").read_bytes()).decode()

html = (
    "<!doctype html>\n"
    '<html lang="en">\n<head>\n'
    '<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    '<meta name="description" content="A How To Speak Data design study: CNN\'s election-night lower third, '
    'rebuilt so you can trade type size for padding, soften borders and switch text case.">\n'
    '<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 200 220%22%3E'
    '%3Cpath d=%22M40,10 L160,10 A30,30 0 0 1 190,40 L190,140 A30,30 0 0 1 160,170 L110,170 L60,212 L82,170 L40,170 '
    'A30,30 0 0 1 10,140 L10,40 A30,30 0 0 1 40,10 Z%22 fill=%22%23fff%22 stroke=%22%230B1220%22 stroke-width=%228%22/%3E'
    '%3Cpath d=%22M41,150V120H69V150Z%22 fill=%22%2314336B%22/%3E%3Cpath d=%22M71,150V95H99V150Z%22 fill=%22%231E5FD9%22/%3E'
    '%3Cpath d=%22M101,150V70H129V150Z%22 fill=%22%2346B8E6%22/%3E%3Cpath d=%22M131,150V48H159V150Z%22 fill=%22%237DD3FC%22/%3E%3C/svg%3E">\n'
    "<style>*,*::before,*::after{box-sizing:border-box}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n"
    + page.replace("__IMG__", "data:image/webp;base64," + img)
    + "\n</html>\n"
)
(root / "index.html").write_text(html, encoding="utf-8")
print(f"index.html written ({len(html):,} bytes)")
