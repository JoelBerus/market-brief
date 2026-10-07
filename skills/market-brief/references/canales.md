# Canales: web, correo o ambos

Combina `canales.web` y `canales.correo` como quieras. La memoria (`Historial.md`, `Reportes/`) se escribe siempre.

| Quiero… | `web` | `correo` |
|---|---|---|
| Solo una página que abro cuando quiero | `html` o `artifact` | `no` |
| Solo el correo | `no` | `si` |
| Correo corto y la página con todo | `html` o `artifact` | `si` |
| Solo notas en mi carpeta (Obsidian, Git…) | `no` | `no` |

## web: artifact (Claude)
Una página privada en claude.ai que lee su propia base de datos. Cada corrida solo escribe datos, así que la página nunca se duplica ni crece.
- Requiere un agente Claude con las herramientas Artifact y ArtifactData (Claude Code, app de escritorio).
- **Primera vez**: publicar `assets/hub.html` con la herramienta Artifact declarando `capabilities: {db: {rules: [{path: "", read: "view", write: "owner"}]}}` (lectura para quien tenga acceso, escritura solo el dueño). Guardar la URL en `web.artifact_url`.
- **Cada corrida**: ArtifactData `batch` con `set` de `empresas/<TICKER>` (con `if_version` si existe) y `set` de `reportes/<TICKER>-<fecha>`.
- **Cambiar el diseño**: editar `assets/hub.html` y republicarlo con la misma `url` (los datos se conservan).
- Enlace a una empresa: `<artifact_url>#<TICKER>`.

## web: html (cualquier agente)
Un archivo HTML autocontenido con los datos dentro. Funciona en Codex, Cursor, Gemini CLI, Copilot o a mano.
- Cada corrida guarda `<datos>/web/empresas/<TICKER>.json` y `<datos>/web/reportes/<TICKER>-<fecha>.json`, y luego:
  `python3 scripts/build_page.py --datos <datos>/web --out <web.salida_html> --titulo "<titulo>"`
- Ábrelo con doble clic o publícalo donde quieras: GitHub Pages (sube la carpeta `web/`), Netlify, Cloudflare Pages, un NAS. Si lo publicas, pon la URL en `web.url_publica` para que el correo enlace a ella.
- Ojo: si lo publicas en un sitio público, cualquiera con el enlace ve tus posiciones. Usa un repositorio privado o un sitio con contraseña si no quieres eso.

## correo
- `scripts/render_email.py <empresa.json> [--web-url <url>#<TICKER>] --out correo.html --texto correo.txt` y enviar con el conector de correo del agente: HTML como cuerpo, texto como alternativa. Asunto sugerido: `<TICKER> · <titular>`.
- Sin `--web-url` (modo solo correo) el correo no lleva el botón «Leer la nota completa».
- Regla por empresa (`correo:` en su frontmatter, o `correo.por_defecto`): `siempre`, `cambios` (cambió el color de Hoy, se cumplió la meta o hay ALERTA) o `nunca`.
- Sin conector de correo (`herramienta: archivo` o el agente no tiene uno): guardar el HTML en `<datos>/salida/correo/<fecha>-<TICKER>.html` y decirlo.

## Programar la corrida diaria
- **Claude (app de escritorio)**: tarea programada con el prompt «Usa la skill market-brief para <TICKER> y genera la nota diaria.», días hábiles a la hora que quieras.
- **Cualquier CLI + cron** (ejemplo, 08:00 de lunes a viernes):
  ```
  0 8 * * 1-5  claude -p "Usa la skill market-brief para SOFI"   # Claude Code
  0 8 * * 1-5  codex exec "Usa la skill market-brief para SOFI"  # Codex CLI
  0 8 * * 1-5  gemini -p "Usa la skill market-brief para SOFI"   # Gemini CLI
  ```
  Revisa en tu herramienta qué permisos necesita en modo no interactivo (búsqueda web, escritura de archivos, correo).
