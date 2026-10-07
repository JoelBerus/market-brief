# Configuración

market-brief lee un solo archivo YAML. Orden de búsqueda: `$MARKET_BRIEF_CONFIG` → `~/.config/market-brief/config.yaml` → `config.yaml` junto a `SKILL.md`. Parte de `config.example.yaml`.

| Opción | Valores | Para qué |
|---|---|---|
| `titulo` | texto | Nombre de la página y encabezado del correo. Por defecto «Mis inversiones». |
| `zona_horaria` | IANA, p. ej. `America/Guayaquil` | Fechas y «próxima nota». |
| `moneda` | `USD`, … | Solo informativo; las plantillas muestran `$`. Cambia el símbolo en `assets/` si usas otra. |
| `datos` | ruta | Carpeta raíz. Una subcarpeta por empresa: `<datos>/<TICKER>/`. |
| `archivo_empresa` | nombre de archivo | Archivo de cada empresa dentro de su carpeta. `empresa.md` por defecto; `Contexto.md` si vienes de una bóveda de Obsidian. |
| `portafolio` | ruta o `null` | Tabla Markdown de posiciones. Si existe, acciones, costo y meta salen de ahí (ver abajo). |
| `diario` | patrón o `null` | Nota diaria donde avisar cambios de semáforo. `{fecha}` = AAAA-MM-DD. |
| `canales.web` | `artifact` · `html` · `no` | Página web. Ver `canales.md`. |
| `canales.correo` | `si` · `no` | Correo con la nota. |
| `web.artifact_url` | URL de claude.ai | Página publicada como Artifact (solo agentes Claude). |
| `web.salida_html` | ruta | Dónde se escribe la página estática. |
| `web.url_publica` | URL o `null` | Dónde publicas el HTML; se usa en el botón del correo. Sin ella, el correo no lleva botón en modo `html`. |
| `correo.para` | correo | Destinatario. |
| `correo.por_defecto` | `siempre` · `cambios` · `nunca` | Regla general; cada empresa puede cambiarla con `correo:` en su frontmatter. |
| `correo.herramienta` | `auto` · `archivo` | `auto`: usa el conector de correo del agente (Gmail, Outlook…). `archivo`: solo guarda el HTML. |
| `fuentes` | lista de URLs con `{ticker}` | Páginas a consultar primero. |

## Archivo de cada empresa
Frontmatter de `<datos>/<TICKER>/<archivo_empresa>` (plantilla: `assets/empresa.md`):

```yaml
ticker: SOFI
empresa: SoFi Technologies
mercado: NASDAQ
acciones: 50              # omitir si usas `portafolio`
costo_total: 750.00       # omitir si usas `portafolio`
meta_total: 1000          # o meta_accion: 20.00 (omitir si usas `portafolio`)
ambar: 17.20              # opcional; por defecto 86% del precio meta
comparables: [NU, HOOD, AFRM]
correo: siempre           # opcional; si no, usa correo.por_defecto
estado: activo            # cerrado = deja de aparecer y de correr
```
Debajo del frontmatter: **Estado actual** (lo reescribe cada corrida) y, si quieres, **Notas** (reglas de tu cuenta, retiro, impuestos) que solo se usan para responder preguntas.

## Tabla `portafolio` (opcional)
Para quien ya lleva sus posiciones en un archivo. market-brief busca la fila del ticker y lee estas columnas por nombre (el orden no importa): `Ticker`, `Acciones`, `Costo total` (o `Costo prom.`), `Meta` (`1000`, `20.00` o `1000 total = 20.00`). Al terminar actualiza solo `Último cierre`, `Valor`, `vs costo` y `Semáforo` si existen, y recalcula la sección `Totales` si la hay. Nunca toca otras columnas ni otros archivos.

## Varias configuraciones
¿Una cartera personal y otra familiar? Crea dos archivos y apunta `MARKET_BRIEF_CONFIG` al que quieras en cada tarea programada.
