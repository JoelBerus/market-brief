#!/usr/bin/env python3
"""Build the static web page (web: html) from the JSON documents of every company.

Usage:
  build_page.py --datos <carpeta-web> --out index.html [--titulo "Mis inversiones"]

<carpeta-web> holds the same two collections the claude.ai page keeps in its database:
  empresas/<TICKER>.json            latest note of each company (replaced on every run)
  reportes/<TICKER>-<AAAA-MM-DD>.json   one small row per run (history)
The result is one self-contained HTML file: open it locally or host it anywhere (GitHub Pages, Netlify, a NAS).
Standard library only.
"""
import argparse
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAGE = HERE.parent / "assets" / "hub.html"
SLOT = '<script type="application/json" id="mb-data">null</script>'
SKELETON = ('<!doctype html><html lang="es"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1"></head><body>\n{}\n</body></html>\n')


def load(folder):
    if not folder.is_dir():
        return []
    return [json.loads(f.read_text(encoding="utf-8")) for f in sorted(folder.glob("*.json"))]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--datos", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--titulo", default="Mis inversiones")
    a = ap.parse_args()
    data = {"titulo": a.titulo,
            "empresas": [e for e in load(a.datos / "empresas") if e.get("estado", "activo") != "cerrado"],
            "reportes": load(a.datos / "reportes")}
    blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    page = PAGE.read_text(encoding="utf-8")
    if SLOT not in page:
        raise SystemExit("assets/hub.html no tiene el bloque mb-data; no se puede inyectar los datos.")
    page = page.replace(SLOT, f'<script type="application/json" id="mb-data">{blob}</script>')
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(SKELETON.format(page), encoding="utf-8")
    print(f"{a.out} · {len(data['empresas'])} empresa(s), {len(data['reportes'])} nota(s)")


if __name__ == "__main__":
    main()
