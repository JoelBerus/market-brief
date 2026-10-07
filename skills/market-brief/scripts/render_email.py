#!/usr/bin/env python3
"""Fill assets/email.html from a company's JSON document (the same shape the page uses).

Usage:
  render_email.py empresa.json [--titulo "Mis inversiones"] [--web-url URL] [--out correo.html] [--texto correo.txt]

--web-url   link for "Leer la nota completa"; omit it for email-only mode (the block is removed).
--texto     also write the plain-text alternative.
Standard library only.
"""
import argparse
import html
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEMPLATE = HERE.parent / "assets" / "email.html"
MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
         "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
MARCAS = {"rojo": ("#ad3f37", "○", "Rojo"), "ambar": ("#94600d", "◐", "Ámbar"), "verde": ("#2f7a4f", "●", "Verde")}
MONO = "font-family:'JetBrains Mono',Menlo,Consolas,monospace"


def usd(n):
    return "n/d" if n is None else f"${n:,.2f}"


def pct(n, d=1):
    if n is None:
        return "n/d"
    sign = "+" if n > 0 else "−" if n < 0 else ""
    return f"{sign}{abs(n):.{d}f}%"


def fecha_larga(iso):
    from datetime import date
    y, m, d = (int(x) for x in iso.split("-"))
    return f"{DIAS[date(y, m, d).weekday()]} {d} de {MESES[m - 1]}"


def fecha_corta(iso):
    _, m, d = (int(x) for x in iso.split("-"))
    return f"{d} {MESES[m - 1][:3]}"


def norm(c):
    c = (c or "").lower().replace("á", "a").split(" ")[0]
    return c if c in MARCAS else "rojo"


def fill(tpl, values):
    return re.sub(r"\{\{(\w+)\}\}", lambda m: values.get(m.group(1), m.group(0)), tpl)


def repeat(tpl, name, items, row_values):
    pat = re.compile(rf"<!-- repeat:{name} -->\n?(.*?)<!-- /repeat:{name} -->\n?", re.S)
    return pat.sub(lambda m: "".join(fill(m.group(1), row_values(x)) for x in items), tpl)


def render(e, titulo, web_url):
    esc = html.escape
    p = e["posicion"]
    precio = e["precio"]
    valor = p["acciones"] * precio
    gan = valor - p["costo"]
    falta = p["meta"] / precio - 1
    b = lambda s: f'<b style="{MONO}">{s}</b>'
    dinero = (f"Tus acciones valen {b(usd(valor))}. Pagaste <span style=\"{MONO}\">{usd(p['costo'])}</span>, "
              f"así que vas {'ganando' if gan >= 0 else 'perdiendo'} {b(f'{usd(abs(gan))} ({pct(gan / p['costo'] * 100)})')}. ")
    if valor >= p["metaTotal"]:
        dinero += f"Superas tu meta de {usd(p['metaTotal'])} por {b(usd(valor - p['metaTotal']))}."
    else:
        dinero += (f"Para tu meta de {usd(p['metaTotal'])} faltan {b(usd(p['metaTotal'] - valor))}: "
                   f"el precio tendría que subir {pct(falta * 100)}, hasta {usd(p['meta'])}.")

    tpl = re.sub(r"<!--(?!\s*/?(repeat|if):).*?-->\n?", "", TEMPLATE.read_text(encoding="utf-8"), flags=re.S)
    if web_url:
        tpl = re.sub(r"<!-- /?if:web -->\n?", "", tpl)
    else:
        tpl = re.sub(r"<!-- if:web -->.*?<!-- /if:web -->\n?", "", tpl, flags=re.S)

    tpl = repeat(tpl, "noticias", e.get("noticias", [])[:3], lambda n: {
        "SIGNO": {"+": "+", "-": "−"}.get(n.get("signo"), "·"),
        "FECHA": fecha_corta(n["fecha"]), "TITULO_NOTICIA": esc(n["titulo"]),
        "URL": esc(n.get("url") or "#"), "FUENTE": esc(n.get("fuente") or "Fuente")})
    tpl = repeat(tpl, "semaforos", e.get("semaforos", []), lambda s: {
        "COLOR": MARCAS[norm(s["color"])][0], "MARCA": MARCAS[norm(s["color"])][1],
        "CUANDO": esc(s["cuando"]), "ETIQUETA": esc(s.get("etiqueta") or MARCAS[norm(s["color"])][2]),
        "TEXTO": esc(s["texto"])})
    filas = e.get("comparables", {}).get("filas", [])
    me = next((r for r in filas if r["ticker"] == e["ticker"]), {})
    tpl = repeat(tpl, "comparables", [r for r in filas if r["ticker"] != e["ticker"]], lambda r: {
        "GUTTER": "+" if r.get("ytd") is not None and me.get("ytd") is not None and r["ytd"] > me["ytd"] else "",
        "TICKER_C": esc(r["ticker"]), "NOMBRE_C": esc(r.get("nombre", "")), "YTD": pct(r.get("ytd"), 0),
        "ANALISTAS": esc(r.get("analistas") or "n/d"), "PRECIO_C": usd(r.get("precio")), "URL_C": esc(r.get("url") or "#")})
    return fill(tpl, {
        "TITULO": esc(titulo), "TITULAR": esc(e["titular"]), "NUM": str(e["reporte"]["numero"]),
        "EMPRESA": esc(e["nombre"]), "FECHA_LARGA": fecha_larga(e["reporte"]["fecha"]), "RESUMEN": esc(e["resumen"]),
        "DINERO": dinero, "LECTURA": esc(e.get("comparables", {}).get("lectura", "")), "WEB_URL": esc(web_url or "")})


def texto(e, web_url):
    s = " · ".join(f"{x['cuando']}: {(x.get('etiqueta') or MARCAS[norm(x['color'])][2]).lower()}" for x in e.get("semaforos", []))
    lines = [f"{e['ticker']} · nota {e['reporte']['numero']} · {fecha_larga(e['reporte']['fecha'])}", "",
             e["titular"], "", e["resumen"], "", s]
    if e.get("noticias"):
        lines += ["", "Qué cambió: " + e["noticias"][0]["titulo"]]
    if web_url:
        lines += ["", "Nota completa:", web_url]
    lines += ["", "Semáforos según tus reglas. No es asesoría financiera; la decisión de vender es tuya."]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("empresa")
    ap.add_argument("--titulo", default="Mis inversiones")
    ap.add_argument("--web-url")
    ap.add_argument("--out")
    ap.add_argument("--texto")
    a = ap.parse_args()
    e = json.loads(Path(a.empresa).read_text(encoding="utf-8"))
    out = render(e, a.titulo, a.web_url)
    if "{{" in out:
        sys.exit("Quedaron campos sin rellenar: " + ", ".join(sorted(set(re.findall(r"\{\{(\w+)\}\}", out)))))
    if a.out:
        Path(a.out).write_text(out, encoding="utf-8")
    else:
        sys.stdout.write(out)
    if a.texto:
        Path(a.texto).write_text(texto(e, a.web_url), encoding="utf-8")


if __name__ == "__main__":
    main()
