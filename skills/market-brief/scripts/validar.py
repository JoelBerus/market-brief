#!/usr/bin/env python3
"""Check a company's JSON document before publishing it (page, static HTML or email).

Usage:  validar.py empresa.json [empresa2.json ...]
Exit code 1 and a list of problems if something required is missing or malformed.
Standard library only.
"""
import json
import sys
from pathlib import Path

COLORES = {"verde", "ambar", "rojo"}


def check(e):
    errs = []
    for k in ("ticker", "nombre", "mercado", "titular", "resumen", "precio", "posicion", "reporte", "semaforos"):
        if e.get(k) in (None, "", []):
            errs.append(f"falta «{k}»")
    p = e.get("posicion") or {}
    for k in ("acciones", "costo", "metaTotal", "meta", "ambar"):
        if not isinstance(p.get(k), (int, float)):
            errs.append(f"posicion.{k} debe ser un número")
    r = e.get("reporte") or {}
    if not isinstance(r.get("numero"), int) or not str(r.get("fecha", "")).count("-") == 2:
        errs.append("reporte necesita «numero» (entero) y «fecha» (AAAA-MM-DD)")
    for i, s in enumerate(e.get("semaforos") or []):
        if s.get("color") not in COLORES:
            errs.append(f"semaforos[{i}].color debe ser verde, ambar o rojo")
        if not s.get("cuando") or not s.get("texto"):
            errs.append(f"semaforos[{i}] necesita «cuando» y «texto»")
    if len(e.get("semaforos") or []) != 3:
        errs.append("deben ser 3 semáforos: hoy, próxima semana y próximo evento")
    if str(e.get("resumen", "")).count(". ") > 1:
        errs.append("resumen: máximo dos oraciones")
    for i, n in enumerate(e.get("noticias") or []):
        if n.get("signo") not in ("+", "-", "·"):
            errs.append(f"noticias[{i}].signo debe ser +, - o ·")
        if n.get("url") and not str(n["url"]).startswith("https://"):
            errs.append(f"noticias[{i}].url debe empezar con https://")
    esc = e.get("escala")
    if esc and not (isinstance(esc.get("lo"), (int, float)) and isinstance(esc.get("hi"), (int, float)) and esc["lo"] < esc["hi"]):
        errs.append("escala necesita lo < hi")
    return errs


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    bad = False
    for path in sys.argv[1:]:
        errs = check(json.loads(Path(path).read_text(encoding="utf-8")))
        print(f"{path}: {'ok' if not errs else ''}")
        for err in errs:
            print(f"  - {err}")
        bad = bad or bool(errs)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
