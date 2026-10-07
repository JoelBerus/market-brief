# Personalizar

Todo es texto plano: edita lo que quieras. Si cambias algo y quieres conservarlo al actualizar el repositorio, hazlo en un fork o en tu copia local.

## La página (`assets/hub.html`)
- **Colores**: el bloque `:root` al inicio del `<style>` define la paleta clara; los dos bloques siguientes, la oscura. Cambia los valores, no los nombres (`--page`, `--ink`, `--slate`, `--rule`, `--link`, `--mark`, `--verde`, `--ambar`, `--rojo`).
- **Letras**: Public Sans para el texto y JetBrains Mono para cifras (enlace de Google Fonts arriba). Cambia el enlace y las variables `--prose` y `--data`.
- **Nombre**: `titulo` en la config (modo `html`) o el texto de `<title>` y `.brand` (modo `artifact`).
- **Secciones**: cada sección sale de una función en el script (`detail()`): «Qué cambió», «Cómo lo vemos», «Tu dinero» (con el simulador), «Otras empresas», «Notas anteriores». Borra o reordena bloques; los datos que falten simplemente no se muestran.
- **Lector**: el visitante elige tema (Auto, Claro, Oscuro) y tamaño de letra; se recuerda en su navegador.
- El sistema visual completo está en `assets/DESIGN.md` (para mantener la coherencia si lo cambias con otro agente).
- Con `web: artifact`, republica con la misma `url` después de editar. Con `web: html`, la próxima corrida (o `build_page.py`) usa tu versión.

## El correo (`assets/email.html`)
Tablas y estilos en línea (Gmail no admite más). Cambia textos y colores libremente. Respeta los marcadores: `{{CAMPO}}`, los comentarios `repeat:` y el bloque `if:web`. Cada sección puede borrarse completa.

## Las reglas
- Semáforo: sección 3 de `SKILL.md`. Por ejemplo, otro porcentaje para el ámbar por defecto, o un cuarto semáforo.
- Redacción: sección 5 de `SKILL.md` (largo del titular, tono, palabras prohibidas).
- Fuentes de datos: `fuentes` en la config.

## Otro idioma
Las plantillas y la redacción están en español. Para otro idioma, traduce `SKILL.md` (secciones 3–6), los textos de `assets/hub.html` y `assets/email.html`, y los meses y días de `scripts/render_email.py`.

## ¿Una skill por empresa?
No hace falta: una skill sirve para todas y cada empresa es una carpeta. Así no se repite texto y una mejora llega a todas a la vez. Si tu agente necesita un nombre de skill por empresa (por ejemplo, para que una tarea programada la invoque por nombre), copia `assets/skill-empresa.md` a `<carpeta de skills>/<ticker>-brief/SKILL.md` y cambia el ticker: es una skill de 10 líneas que delega en market-brief.
