"""Génère index.html (page autonome pour GitHub Pages) à partir de carnet.html.
Les balises <title>, <meta> et <link> du début de carnet.html vont dans <head>,
pour qu'iOS trouve l'icône d'écran d'accueil et le nom de l'app."""
import pathlib, re
here = pathlib.Path(__file__).parent
src = (here / "carnet.html").read_text()
split = src.index("<style>")
head_tags = [l for l in src[:split].splitlines() if l.strip() and 'name="claude:' not in l]
body = src[split:]
out = ["<!doctype html>", '<html lang="fr">', "<head>", '<meta charset="utf-8">',
       '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">',
       *head_tags,
       "<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}</style>",
       "</head>", "<body>", body, "</body>", "</html>", ""]
(here / "index.html").write_text("\n".join(out))
