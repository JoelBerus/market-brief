---
name: market-brief
description: "Nota diaria, en lenguaje simple, de las acciones que tienes: precio, qué pasó y por qué, tres semáforos según tu meta de venta, comparables, y la entrega que elijas (página web, correo, ambas o solo notas). Una sola skill para todas tus empresas. Usar al pedir el brief, reporte o nota de un ticker («market-brief para SOFI»), al correr una tarea programada «<TICKER> Watch», al dar de alta una empresa para seguirla, al preguntar cómo va una empresa o por notas anteriores, o al pedir «el brief de todas»."
license: MIT
---

# Market brief

Una skill para todas tus empresas. Cada corrida trabaja **una** empresa (el ticker viene en el pedido); «todas» = una corrida por cada empresa activa, una a la vez. Suele correr desatendida: no pidas confirmaciones durante un reporte. Español, frases cortas, lenguaje de persona. Nunca inventes precios: si una fuente falla, usa otra. No es asesoría financiera y nunca ejecutes compras ni ventas.

## 1. Cargar la configuración
Buscar `config.yaml` en este orden y usar el primero que exista:
1. la ruta en la variable de entorno `MARKET_BRIEF_CONFIG`;
2. `~/.config/market-brief/config.yaml`;
3. `config.yaml` junto a este archivo.

Si no hay ninguna: en una sesión con el usuario, copiar `config.example.yaml` a `~/.config/market-brief/config.yaml` y preguntarle solo lo necesario (carpeta de datos, canales, correo); desatendida, terminar y decir que falta la configuración. Todas las opciones están en `references/configuracion.md`.

## 2. Datos de la empresa
- Carpeta: `<datos>/<TICKER>/` con el archivo de la empresa (`archivo_empresa`, por defecto `empresa.md`), `Historial.md` y `Reportes/`.
- Frontmatter del archivo de la empresa: `ticker`, `empresa`, `mercado`, `comparables`, `ambar` (opcional: 86% del precio meta), `correo` (opcional: `siempre` | `cambios` | `nunca`), `estado` (`activo` | `cerrado`) y la posición: `acciones`, `costo_total`, `meta_total` o `meta_accion`.
- Si `portafolio` está configurado, la posición (acciones, costo total, meta) sale de la fila del ticker en esa tabla y **no** del frontmatter (una sola fuente por dato).
- Si la carpeta no existe o falta un dato obligatorio: con el usuario, seguir `references/alta.md` (alta guiada, pregunta solo lo que falta y guarda el avance); desatendida, no publicar y avisar qué falta.

## 3. Reglas del semáforo
- **verde**: precio ≥ meta por acción → meta alcanzada.
- **ambar**: ámbar ≤ precio < meta, o tendencia alcista con catalizador en ≤ 7 días (resultados, tasas, cambio de recomendación).
- **rojo**: precio < ámbar, o tendencia bajista / noticia negativa relevante.
- Siempre tres: **Hoy**, **Próxima semana** (impulso + analistas + calendario) y **Próximo evento clave** (con fecha).
- **ALERTA** si el precio cae bajo el costo promedio o bajo el mínimo de 52 semanas: dilo en el titular.
El usuario puede cambiar estas reglas editando esta sección (ver `references/personalizar.md`).

## 4. Pasos de una corrida
0. Leer el archivo de la empresa, la posición y las últimas filas de `Historial.md`. Número de nota = último # + 1. Si ya hay una nota con la fecha de este cierre, es una corrección: conserva su número y reemplaza esa fila, ese reporte y ese documento.
1. **Datos**: buscar en la web (las URLs de `fuentes` en la config; `stockanalysis.com/stocks/<ticker>/` es fiable): cierre, variación del día, del mes y del año, mínimo y máximo de 52 semanas, recomendación y precio objetivo de analistas, próximo reporte de resultados.
2. **Noticias** de 24–72 h (hasta 30 días si no hay): por qué se movió. 2–4, con fecha y fuente.
3. **Comparables**: precio, 1 mes, en el año, recomendación, objetivo y URL para «ver más».
4. **Cálculos**: valor = acciones × precio; ganancia = valor − costo total; falta % = meta / precio − 1.
5. **Semáforos** según las reglas.
6. **Redactar** el documento de la empresa (forma exacta en `references/datos.md`; reglas de redacción abajo). Guardarlo como JSON y, si hay Python, validarlo con `scripts/validar.py`.
7. **Entregar** según `canales` (detalle en `references/canales.md`):
   - `web: artifact` (Claude con herramientas de Artifact): escribir `empresas/<TICKER>` y `reportes/<TICKER>-<fecha>` en la base de la página con ArtifactData, en un solo `batch` y con `if_version` si el documento ya existe. Nunca republicar el HTML para un reporte.
   - `web: html` (cualquier agente): guardar los dos JSON en `<datos>/web/empresas/` y `<datos>/web/reportes/` y regenerar la página con `scripts/build_page.py --datos <datos>/web --out <web.salida_html> --titulo "<titulo>"`.
   - `web: no`: nada.
   - `correo: si` y la regla de la empresa lo permite (`siempre`; `cambios` = cambió el color de Hoy, se cumplió la meta o hay ALERTA): `scripts/render_email.py` (con `--web-url` solo si hay web) y enviar con la herramienta de correo disponible. Sin herramienta de correo, guardar el HTML en `<datos>/salida/correo/` y decirlo.
8. **Memoria** (siempre, aunque no haya web ni correo):
   - `Historial.md`: agregar una fila (Fecha | # | Cierre | Día | Valor | vs costo | Falta meta | Hoy | Semana | Evento | Consenso | Nota).
   - `Reportes/<AAAA-MM-DD>.md`: frontmatter con las cifras del día y secciones Semáforos, Posición, Noticias, Comparables.
   - Reescribir **Estado actual** del archivo de la empresa; si hay `portafolio`, actualizar solo las columnas de cierre, valor, % y semáforo de su fila y los totales.
   - Si `diario` está configurado: una entrada solo si cambió el color de Hoy, se cumplió la meta o hay ALERTA.
9. Sin precio disponible: no publicar nota nueva; si el correo está activo, avisar con un correo corto.
10. Si un canal falla, seguir con los demás y decirlo (en el correo o en la respuesta).

## 5. Redacción
- **titular**: una frase de ≤ 12 palabras; qué pasó en relación con la meta.
- **resumen**: máximo dos oraciones: precio, valor frente a lo pagado, distancia a la meta y lo próximo importante.
- **noticias**: `titulo` (frase con punto), `texto` (1–2 frases: por qué importa), `signo` (`+` sube, `-` baja, `·` neutral), `fuente`, `url`.
- **semáforos**: `texto` de 1–2 frases con la razón. **comparables.lectura**: una frase.
- Lenguaje de persona: «los analistas recomiendan mantener», «piso / techo del año», «en el año». Nunca Hold, Buy, YTD o EPS sin explicar. Sin guiones largos ni frases de relleno.

## 6. Preguntas del usuario
- «¿Cómo va <TICKER>?» → la última nota (documento de la empresa o `Historial.md`) y el enlace web si existe. No correr un reporte nuevo salvo que lo pida.
- «¿Cómo van todas?» → resumen de todas las empresas activas (avisar si el último cierre tiene más de un día hábil).
- Notas anteriores → `Historial.md` y `Reportes/<fecha>.md`, citando la fecha (o la más cercana).
- Dar de alta, cambiar meta, comparables o canales de una empresa → `references/alta.md` y `references/configuracion.md`.
- «¿Vendo?» → semáforo de Hoy con su razón; la decisión es del usuario.
- Cambiar el aspecto de la página o del correo → `references/personalizar.md`.

## Archivos de esta skill
- `config.example.yaml` — configuración de ejemplo.
- `assets/hub.html` — la página (sirve para claude.ai y como HTML estático). `assets/email.html` — el correo. `assets/empresa.md` — archivo de empresa. `assets/skill-empresa.md` — skill mínima por empresa (opcional). `assets/DESIGN.md` — sistema visual.
- `scripts/` — `validar.py`, `build_page.py`, `render_email.py` (solo biblioteca estándar de Python).
- `references/` — configuración, datos, canales, alta, personalizar, agentes.
