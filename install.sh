#!/usr/bin/env sh
# Enlaza skills/market-brief en las carpetas de skills de los agentes que tengas instalados.
# Uso: ./install.sh            (enlaces simbólicos: se actualizan con git pull)
#      ./install.sh --copy     (copias independientes)
set -e
SRC="$(cd "$(dirname "$0")" && pwd)/skills/market-brief"
MODE="${1:-link}"
installed=0
for dir in "$HOME/.claude" "$HOME/.codex" "$HOME/.agents" "$HOME/.cursor" "$HOME/.gemini" "$HOME/.copilot"; do
  [ -d "$dir" ] || continue
  # Codex también lee ~/.agents/skills: no la instales dos veces.
  if [ "$dir" = "$HOME/.agents" ] && [ -d "$HOME/.codex" ]; then continue; fi
  mkdir -p "$dir/skills"
  dest="$dir/skills/market-brief"
  if [ -e "$dest" ] || [ -L "$dest" ]; then
    echo "· $dest ya existe; no lo toco (bórralo si quieres reinstalar)"; continue
  fi
  if [ "$MODE" = "--copy" ]; then cp -R "$SRC" "$dest"; else ln -s "$SRC" "$dest"; fi
  echo "✓ $dest"; installed=$((installed + 1))
done
[ "$installed" -gt 0 ] || echo "No encontré carpetas de agentes (~/.claude, ~/.codex, ~/.agents, ~/.cursor, ~/.gemini, ~/.copilot)."
mkdir -p "$HOME/.config/market-brief"
if [ ! -f "$HOME/.config/market-brief/config.yaml" ]; then
  cp "$SRC/config.example.yaml" "$HOME/.config/market-brief/config.yaml"
  echo "✓ Configuración de ejemplo en ~/.config/market-brief/config.yaml: edítala antes de la primera corrida."
fi
