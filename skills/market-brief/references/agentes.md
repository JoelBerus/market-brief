# Usarla en cada agente

market-brief sigue el formato abierto Agent Skills: una carpeta con `SKILL.md` (frontmatter `name` y `description`) y archivos de apoyo. Cualquier agente que lea skills la puede usar; los que no, pueden seguir `SKILL.md` como instrucciones.

## Instalar
Con la CLI de skills (instala en los agentes que detecte):
```
npx skills add JoelBerus/market-brief
```
A mano, copia o enlaza `skills/market-brief/` en la carpeta de skills de tu agente:

| Agente | Carpeta de usuario | Carpeta del proyecto |
|---|---|---|
| Claude Code / app de Claude | `~/.claude/skills/` | `.claude/skills/` |
| Codex CLI | `~/.codex/skills/` o `~/.agents/skills/` | `.agents/skills/` |
| Cursor | `~/.cursor/skills/` | `.cursor/skills/` |
| Gemini CLI | `~/.gemini/skills/` | `.gemini/skills/` |
| GitHub Copilot | `~/.copilot/skills/` | `.github/skills/` |
| OpenCode y otros | `~/.agents/skills/` | `.agents/skills/` |

Las carpetas cambian entre versiones de cada herramienta: si no la detecta, revisa su documentación. `install.sh` en la raíz del repositorio crea los enlaces por ti.

## Qué puede hacer cada uno
| Capacidad | Claude | Otros agentes |
|---|---|---|
| Buscar precios y noticias | búsqueda web | búsqueda web o fetch de la herramienta |
| `web: artifact` (página en claude.ai) | sí | no: usa `web: html` |
| `web: html` | sí | sí (necesita Python 3 para `build_page.py`, o el agente inyecta el JSON a mano) |
| Correo | conector de Gmail u otro | su conector de correo, o `herramienta: archivo` |
| Programarla | tareas programadas de la app o `claude -p` + cron | `codex exec`, `gemini -p` + cron |

## Agentes sin soporte de skills
El repositorio trae `AGENTS.md`, que muchas herramientas leen solo (Codex, Cursor, Copilot, Jules…). Si la tuya no, pídele: «Lee skills/market-brief/SKILL.md y síguelo para SOFI».
