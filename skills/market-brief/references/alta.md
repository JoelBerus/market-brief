# Alta guiada de una empresa

Sirve para empezar a seguir una empresa o completar datos que faltan. Pregunta solo lo que no sabes y guarda el avance, así el usuario puede retomarlo otro día («sigamos con el alta de NVDA»).

1. Si existe `<datos>/<TICKER>/alta.md`, leerlo y retomar. Si no, crear la carpeta y `alta.md` con esta tabla (Valor vacío, Estado `pendiente`):

   | Dato | Valor | Estado |
   |---|---|---|
   | Ticker | | |
   | Empresa y mercado | | se investiga |
   | Acciones | | |
   | Costo total (o precio por acción + comisión) | | |
   | Meta de venta (total o por acción) | | |
   | Umbral ámbar | | por defecto 86% del precio meta |
   | Comparables (4–6) | | se proponen |
   | Correo | | siempre · cambios · nunca |
   | Notas propias (opcional) | | |

2. Llenar sin preguntar lo que esté en el mensaje o en capturas del bróker, e investigar empresa, mercado, precio, mínimo y máximo de 52 semanas y 4–6 comparables del mismo sector.
3. Preguntar el resto en rondas de máximo 4 preguntas, con valores propuestos:
   - Meta: si no la tiene, dos opciones con números (p. ej. +25% y +50% sobre el costo, o el objetivo de los analistas).
   - Ámbar: 86% del precio meta.
   - Comparables: los investigados, para confirmar o cambiar.
   - Correo: `correo.por_defecto` de la config.
   Después de cada ronda, escribir las respuestas en `alta.md`.
4. Con todo listo: mostrar un resumen y pedir confirmación.
5. Crear `<archivo_empresa>` desde `assets/empresa.md` (sin dejar `{{`), `Historial.md` (encabezado y tabla vacía) y `Reportes/`. Si se usa `portafolio`, agregar la fila del ticker allí en lugar de poner la posición en el frontmatter. Borrar `alta.md`.
6. Ofrecer: correr ya la primera nota y programar la corrida diaria (ver `canales.md`).

## Cambios después del alta
- Compró o vendió: actualizar `acciones` y `costo_total` (o la fila de `portafolio`). El costo promedio de lo que queda no cambia al vender.
- Nueva meta o nuevo ámbar: editar el frontmatter. La próxima corrida lo refleja; con `web: artifact` también se puede actualizar `posicion` y `escala.marcas` de `empresas/<TICKER>` de inmediato.
- Dejar de seguirla: `estado: cerrado`. Con `web: artifact`, preguntar si borrar `empresas/<TICKER>` de la página (las notas anteriores quedan en `reportes` y en la carpeta).
