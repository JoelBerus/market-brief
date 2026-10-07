---
name: Mis inversiones
description: A private daily note per company, written as release notes for each trading day.
colors:
  page: "#f4f5f7"
  ink: "#1c2330"
  slate: "#566072"
  rule: "#d8dce3"
  link: "#1f6f8b"
  mark: "#ffe8a3"
  on-mark: "#1c2330"
  verde: "#2f7a4f"
  ambar: "#94600d"
  rojo: "#ad3f37"
  page-dark: "#14181d"
  ink-dark: "#e4e7eb"
  slate-dark: "#9ba4b1"
  rule-dark: "#2a3038"
  link-dark: "#73c2da"
  mark-dark: "#e9cf6f"
  on-mark-dark: "#14181d"
  verde-dark: "#7cc79a"
  ambar-dark: "#e0b25e"
  rojo-dark: "#ee8f86"
typography:
  display:
    fontFamily: "Public Sans, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "1.75rem"
    fontWeight: 750
    lineHeight: 1.22
    letterSpacing: "-0.02em"
  body:
    fontFamily: "Public Sans, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.65
  title:
    fontFamily: "Public Sans, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "1rem"
    fontWeight: 650
    lineHeight: 1.65
  label:
    fontFamily: "Public Sans, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "1rem"
    fontWeight: 650
    letterSpacing: "0.06em"
    fontFeature: "all-small-caps"
  data:
    fontFamily: "JetBrains Mono, ui-monospace, SF Mono, Menlo, monospace"
    fontSize: "1rem"
    fontWeight: 400
    letterSpacing: "-0.01em"
    fontFeature: "tnum"
rounded:
  focus: "2px"
  plate: "3px"
spacing:
  page-inline: "16px"
  column: "44rem"
  gutter: "2.25rem"
  gutter-mobile: "1.6rem"
  row: "10px"
  row-index: "14px"
  section: "48px"
  note-top: "40px"
  measure: "62ch"
components:
  plate:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.page}"
    typography: "{typography.title}"
    rounded: "{rounded.plate}"
    padding: "0 0.45em"
  tab:
    textColor: "{colors.slate}"
    typography: "{typography.body}"
    padding: "8px 0 9px"
  tab-current:
    textColor: "{colors.ink}"
    typography: "{typography.title}"
  option-toggle:
    textColor: "{colors.slate}"
    typography: "{typography.body}"
    padding: "2px 0"
  option-toggle-pressed:
    textColor: "{colors.ink}"
    typography: "{typography.title}"
  figure-changed:
    backgroundColor: "{colors.mark}"
    textColor: "{colors.on-mark}"
    typography: "{typography.data}"
    padding: "0 1px"
  diff-row:
    typography: "{typography.body}"
    padding: "10px 0"
  section-heading:
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    padding: "0 0 0 2.25rem"
  reset-link:
    textColor: "{colors.link}"
    typography: "{typography.body}"
---

# Design System: Mis inversiones

## Overview

**Creative North Star: "Release Notes for a Trading Day"**

Each company's day ships as a version of a documentation page: a headline, a metadata row, a two-sentence summary, then a changelog. One centered column (44rem) on a cool page, ruled by hairlines, with a left diff gutter carrying `+`, `−`, `·` and `›` signs instead of icons or colored chips. Hierarchy comes from weight, small caps, and a single inverted plate, never from a third type size, boxes, or elevation.

Color is almost absent. Ink and slate carry the reading; one teal-blue is the only link and focus color; marker yellow appears only when a figure has been changed by the reader. State (far / close / target reached) is drawn as a mark (hollow, half, full circle), lightly tinted, so it survives without hue. The whole page works in light and dark with matched token sets, and the reader sets theme (Auto / Claro / Oscuro) and text size (15 to 22px root steps).

The world rejects the fintech dashboard (big price, cards, green/red tiles) and the cream editorial page.

**Key Characteristics:**
- One documentation column, hairline rules, left diff gutter on every list.
- Two type sizes only: 1.75rem headline and 1rem everything else.
- Public Sans for prose, JetBrains Mono only for data.
- State as drawn mark (hollow / half / full), tint secondary.
- One inverted plate per note ("última"); no cards, no shadows.
- The price control rewrites the note's own figures in place: old value struck, new value swept in marker yellow.

## Colors

A cool documentation palette: near-neutral blue-grey ink on a cool page, one teal-blue for interaction, one marker yellow for reader-changed figures, three quiet state tints. Every token has a dark twin, applied by `prefers-color-scheme: dark` unless `data-theme="light"`, or forced by `data-theme="dark"`.

### Primary
- **Docs Teal** (link / link-dark): every link, the reset action, the focus outline, the caret, and the "today" dot on the simulator track. Nothing else.

### Secondary
- **Marker Yellow** (mark / mark-dark, text on it: on-mark / on-mark-dark): the highlight sweep behind figures the simulator changed, and text selection. Never a static decoration.

### Tertiary
- **State Tints** (verde, ambar, rojo and their -dark twins): stroke and fill of the drawn marks only. Never text, backgrounds, or gutters.

### Neutral
- **Cool Page** (page / page-dark): the single background; also the text color inside the inverted plate and the slider-thumb border.
- **Ink** (ink / ink-dark): body text, headings, current tab underline, the plate fill, the slider track and thumb, gutter signs for `+`/`−` rows.
- **Slate** (slate / slate-dark): metadata, dates, secondary lines, idle controls, struck old figures, neutral gutter signs, track ticks.
- **Hairline** (rule / rule-dark): row borders, tab baseline, scrollbar.

### Named Rules
**The Mark-Means-Changed Rule.** Marker yellow appears only on a figure the reader has altered (and on selection). A static highlight is a bug.

**The One Teal Rule.** Teal means "you can follow or act on this". It is never decorative, never a heading color.

**The No Green/Red Gutter Rule.** Diff signs `+` and `−` are ink, not green and red. Gain and loss read from the sign and the words.

## Typography

**Display Font:** Public Sans (with system-ui, -apple-system, Segoe UI, sans-serif)
**Body Font:** Public Sans
**Label/Mono Font:** JetBrains Mono (with ui-monospace, SF Mono, Menlo, monospace), data only

**Character:** A plain, public-documentation sans paired with a tabular mono that marks every price, date, ticker and note number as data. Mono is size-matched to prose with `font-size-adjust: 0.53`, so it never reads as a different size.

### Hierarchy
- **Display** (750, 1.75rem / 1.5rem under 560px, 1.22, -0.02em, balanced, max 24em): the note headline and empty-state headlines.
- **Title** (650, 1rem): brand (750), current tab, pressed option, figures, row titles, plate text, simulator label.
- **Body** (400, 1rem, 1.65, max 62ch): summary, diff items, check reasons, money paragraph.
- **Label** (650, 1rem, all-small-caps, 0.06em): section headings ("Qué cambió", "Cómo lo vemos", "Tu dinero") and "Fuentes". These are real h2 headings, not kickers.
- **Data** (400 or 600 in gutters/tickers, 1rem with size-adjust 0.53, tabular-nums, -0.01em): prices, percentages, dates, tickers, note numbers.

### Named Rules
**The Two Sizes Rule.** Only `--big` (1.75rem) and 1rem exist. Rank by weight (400 / 650 / 750), small caps, slate vs ink, and the plate. A third size is out of system.

**The Mono Is Data Rule.** JetBrains Mono wraps numbers, dates, tickers, and gutter signs. Never prose, never headings.

## Layout

A single column (max 44rem, centered, 16px inline page padding, 72px bottom). Every list is a two-column grid: a fixed diff gutter (`--gut`, 2.25rem; 1.6rem under 560px) and a `minmax(0,1fr)` body; peers and the index add a right-aligned `auto` number column. Section headings, the money paragraph, the simulator, and the footer indent by the gutter so all text shares one left edge after the sign column.

Rhythm: note starts 40px below the tabs; headline, 14px metadata row, 22px summary; sections 48px apart with 14px under the heading; rows 10px block padding (index rows 14px); footer 56px. Prose capped at 62ch. Root size is reader-controlled (15, 16, 17 default, 18.5, 20, 22px) and everything scales in rem/em from it. One breakpoint (560px) narrows the gutter and the headline.

## Elevation & Depth

Flat. No elevation shadows, no layered surfaces, no cards. Depth is replaced by hairline rules (1px rule) above each row and below the last, the 2px ink underline of the current tab, and the inverted plate. The only `box-shadow` in the system is the slider-thumb focus ring (`0 0 0 3px page, 0 0 0 5px link`), a focus device, not elevation.

### Named Rules
**The Nothing Boxed Rule.** No bordered or filled container wraps a block of content. Fills exist only inline: the plate, the marker sweep, selection.

## Shapes

Lines, not boxes. Horizontal hairlines divide rows; underlines (1px idle-transparent, 2px current) mark controls; dotted underlines mark preset prices. Corners appear only on the tiny inline shapes: plate (3px), focus outline (2px), slider thumb (3px). Marks are 16-unit circles (r 6.25, stroke 1.6) sized at 0.8em; the external-link glyph is a 12-unit stroked arrow at 0.75em, inline SVG with `currentColor`.

## Components

### Buttons
Text-only controls; no button chrome anywhere.
- **Shape:** none; inherits font, no background, no border, no padding.
- **Option toggles (theme, text size):** slate, 2px block padding, transparent 1px bottom border; hover ink; `aria-pressed="true"` turns ink, 650, underline in currentColor. Size buttons disable at the ends of the scale.
- **Preset stops (simulator):** slate text with a 1px dotted slate underline, price in mono; hover ink with ink underline.
- **Reset:** a teal underlined text action ("Volver al precio de hoy"), hidden when the price equals today.
- **Hover / Focus:** links thicken underline 1px to 2px on hover; every focusable gets a 2px teal outline, 3px offset, 2px radius.

### Inputs / Fields
- **Price range:** transparent 28px control over a 2px ink track; thumb a 6x22px ink bar (3px radius) with a 2px page-colored border. An SVG layer draws slate ticks (1px, 2px for strong stops) and a 4.5px teal dot at today's price.
- **Focus:** outline removed from the input, replaced by the double ring on the thumb.
- **Live state line:** below the track, a mark plus a sentence naming the resulting state, `aria-live="polite"`.

### Navigation
- **Top line:** brand (750) left, reading controls right, baseline-aligned, wraps on mobile.
- **Company tabs:** horizontal scroll row on a 1px hairline baseline, 22px gaps; each tab a mark plus the mono ticker; slate idle, ink on hover, current is ink 650 with a 2px ink underline sitting on the hairline. "Todas" appears only with more than one company.

### Inverted Plate
The single filled shape: ink background, page-colored text, 650, 0 0.45em padding, 3px radius. Used once per note, for "última" in the metadata row.

### Marks
State as shape: hollow circle = rojo (far), left-half filled = ambar (close), full = verde (target reached), each in its tint at 0.8em. Unknown state renders hollow with "sin dato". Each mark carries a `role="img"` label.

### Diff Gutter Rows
Changelog, checks, peers, version log, and index share one row: gutter cell (mono 600, slate; ink for `+`/`−`) or mark, body text, hairline above. Signs: `+` up, `−` down, `·` neutral, `›` the current company among peers.

### Figure Rewrite (signature)
Each figure in the money paragraph holds a `del` and an `ins`. When the simulated price differs from today, the `del` shows today's value in slate, 400, struck with a 1px line, and the `ins` shows the new value with the marker sweeping in from the left (background-size 0 to 100%, 0.5s `cubic-bezier(.16,1,.3,1)`), text switching to on-mark. Reduced motion disables the transition.

## Do's and Don'ts

### Do:
- **Do** keep every list on the diff-gutter grid (`--gut` + `minmax(0,1fr)`) with hairlines between rows.
- **Do** rank with weight 650/750, all-small-caps labels, slate vs ink, and at most one inverted plate per note.
- **Do** set every number, date, and ticker in JetBrains Mono with `font-size-adjust: 0.53` and tabular figures.
- **Do** express state as a hollow / half / full mark with an accessible label; tint is secondary.
- **Do** show reader-changed figures as struck slate old value plus marker-swept new value.
- **Do** ship both token sets; every new color needs a dark twin.

### Don't:
- **Don't** introduce a third type size; 1.75rem and 1rem are the system.
- **Don't** wrap content in cards, bordered boxes, or filled panels, and don't add elevation shadows.
- **Don't** color gutter signs, text, or backgrounds green/red; tints live only in marks.
- **Don't** use marker yellow for anything that wasn't changed by the reader.
- **Don't** use teal for anything that isn't a link, action, or focus.
- **Don't** use mono for prose or headings.

## Secondary surface: email.html

The daily email (table-based, inline styles, light only) maps the light tokens within Gmail's constraints: Public Sans with system fallbacks, JetBrains Mono for figures, the same diff gutter (32px column, + − · in ink), small-caps section headings, the inverted "última" plate, and teal links. Gmail runs no SVG, so the marks are the glyphs ○ ◐ ● tinted with the state hue; the headline is 26px. No tinted backgrounds, no cards; the call to action is a teal link, not a filled button.
