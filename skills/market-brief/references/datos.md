# Forma de los datos

Las cifras de los ejemplos son ilustrativas. Los mismos dos documentos alimentan la página (base de datos del Artifact o JSON del HTML estático) y el correo. Valídalos con `scripts/validar.py`. Ejemplo completo: `examples/datos/web/` en el repositorio.

## `empresas/<TICKER>` (se reemplaza completo en cada corrida)
```json
{
 "ticker": "SOFI", "nombre": "SoFi Technologies", "mercado": "NASDAQ",
 "estado": "activo",
 "reporte": {"numero": 12, "fecha": "2026-10-21", "proxima": "miércoles 22 de octubre, 08:00"},
 "titular": "SoFi se acerca a tu meta antes de sus resultados",
 "resumen": "Cerró en $18.40 y tus acciones valen $920.00, $170 más de lo que pagaste. Le falta 8.7% para tu meta y presenta resultados el 27 de octubre.",
 "precio": 18.40, "dia": 2.3,
 "posicion": {"acciones": 50, "costo": 750.00, "metaTotal": 1000, "meta": 20.00, "ambar": 17.20, "cuenta": "Mi bróker"},
 "semaforos": [
  {"cuando": "Hoy", "color": "ambar", "texto": "…"},
  {"cuando": "Próxima semana, 22 al 28 de octubre", "color": "ambar", "texto": "…"},
  {"cuando": "27 de octubre, resultados del trimestre", "color": "ambar", "etiqueta": "Ámbar alto", "texto": "…"}
 ],
 "escala": {"lo": 12, "hi": 34, "marcas": [
  {"p": 15.00, "t": "tu costo"},
  {"p": 14.88, "t": "piso del año", "c": "rojo"},
  {"p": 20.00, "t": "meta", "c": "verde", "fuerte": true},
  {"p": 20.33, "t": "analistas", "punteada": true},
  {"p": 32.73, "t": "techo del año"}
 ]},
 "noticias": [{"fecha": "2026-10-21", "titulo": "…", "texto": "…", "signo": "+", "fuente": "…", "url": "https://…"}],
 "comparables": {"titulo": "fintech · cierre del 21 oct", "lectura": "…", "filas": [
  {"ticker": "SOFI", "nombre": "SoFi", "precio": 18.40, "mes": 12.0, "ytd": -26, "analistas": "mantener", "objetivo": 20.33, "url": "https://stockanalysis.com/stocks/sofi/"},
  {"ticker": "NU", "nombre": "Nubank", "precio": 16.10, "mes": 3.1, "ytd": 44, "analistas": "comprar", "objetivo": 18.64, "url": "https://stockanalysis.com/stocks/nu/"}
 ]},
 "fuentes": [{"t": "StockAnalysis: SOFI", "url": "https://stockanalysis.com/stocks/sofi/"}]
}
```
- `color`: `verde` · `ambar` · `rojo`. `etiqueta` es opcional (p. ej. «Ámbar alto»).
- `mes`, `ytd`, `dia`: porcentajes; `null` si no hay dato. La propia empresa va también en `comparables.filas`.
- `escala` (simulador de la página): `lo` = floor(min(costo prom., mín 52s) × 0.9); `hi` = ceil(max(máx 52s, meta) × 1.05). `tu costo` y `meta` son fijas; piso, techo y analistas cambian. Las marcas con `fuerte` o con «costo» en el nombre se muestran como atajos.
- Las URLs deben empezar con `https://`.

## `reportes/<TICKER>-<AAAA-MM-DD>` (una por corrida)
```json
{"ticker": "SOFI", "fecha": "2026-10-21", "numero": 12, "cierre": 18.40, "dia": 2.3, "valor": 920.00, "vsCosto": 22.7, "faltaMeta": 8.7, "hoy": "ambar", "semana": "ambar", "evento": "ambar", "nota": "una línea"}
```

## Carpeta de la empresa (memoria)
```
<datos>/<TICKER>/
  empresa.md            # configuración (frontmatter), Estado actual, Notas
  Historial.md          # una fila por corrida
  Reportes/AAAA-MM-DD.md
<datos>/web/            # solo con web: html
  empresas/<TICKER>.json
  reportes/<TICKER>-<fecha>.json
<datos>/salida/correo/  # solo si el correo se guarda como archivo
```
