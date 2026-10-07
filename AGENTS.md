# AGENTS.md

This repository ships one Agent Skill: **market-brief** (`skills/market-brief/`). It writes a daily, plain-language note in Spanish about a stock the user holds and delivers it as a web page, an email, both, or only Markdown notes.

## If your agent supports skills
Install `skills/market-brief/` into your skills folder (see `skills/market-brief/references/agentes.md`) or run `npx skills add JoelBerus/market-brief`. Then ask: «market-brief para SOFI».

## If it does not
When the user asks for a stock brief, daily note, or "market-brief para <TICKER>":
1. Read `skills/market-brief/SKILL.md` and follow it step by step.
2. Load the user's config (`$MARKET_BRIEF_CONFIG`, then `~/.config/market-brief/config.yaml`). If missing, start from `skills/market-brief/config.example.yaml` and ask the user only what is needed.
3. Use `canales.web: html` (not `artifact`, which needs Claude's Artifact tools). Build the page with `python3 skills/market-brief/scripts/build_page.py`.
4. Render the email with `python3 skills/market-brief/scripts/render_email.py` and send it with your mail connector, or save it to `<datos>/salida/correo/` if you have none.

## Working on this repository
- Keep scripts on the Python standard library only.
- `skills/market-brief/assets/hub.html` must keep the `<script type="application/json" id="mb-data">null</script>` slot (static mode) and the `claude.use('db')` path (Artifact mode).
- `skills/market-brief/assets/email.html` must keep its `{{FIELD}}`, `repeat:` and `if:web` markers.
- Visual rules live in `skills/market-brief/assets/DESIGN.md`.
- Check changes with the example: `python3 skills/market-brief/scripts/validar.py examples/datos/web/empresas/EJEM.json`, then rebuild `examples/web/index.html` and `examples/correo-ejemplo.html`.
- Never commit real holdings, personal emails, or artifact URLs. Examples use the fictional ticker EJEM.
- Not financial advice: never add features that place trades or move money.
