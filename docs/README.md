# Getting Things Done with Airflow: the slide deck

The course slides, written in [Slidev](https://sli.dev) with the Dataminded theme.
Converted from `Workflows with Airflow v2.pptx`, and reordered to follow the current exercise
sequence in the [repo README](../README.md) (`0_hello_airflow` through `11_connections_and_hooks`).

## Layout

| Path                              | What it is                                                     |
| ---------------------------------- | --------------------------------------------------------------- |
| `slides.md`                        | The deck. Speaker notes live in the HTML comments.             |
| `theme-preview.md`                 | One slide per theme layout and component — a visual reference, not part of the real deck. |
| `style.css`                        | Global CSS: cron box, exercise-path badge, comparison table.    |
| `theme/`                           | The `slidev-theme-dataminded` sources, linked from `package.json`. |
| `public/img/`                      | Screenshots and diagrams carried over from the original deck.  |
| `public/assets-preview/`           | Copies of `theme/assets/`, used only by `theme-preview.md` (Slidev can't serve files outside `public/`). |

## Working on the deck

```bash
cd docs
npm install        # once
npm run dev        # live preview on localhost:3030, press "p" for presenter mode
npm run export     # writes Workflows-with-Airflow.pdf next to slides.md
npm run build      # static site in dist/
npm run preview    # browse every layout/component in theme-preview.md
```

## Conventions

- Headings are two-tone: wrap the accent word in `<span class="dm-accent">...</span>`.
- Content slides use `layout: default` with a `label:` for the top-right tag. The label is the
  section name (`3 · Creating a DAG`) and stays constant between section dividers.
- Dividers use `layout: section`, exercise pointers use `layout: statement` — each exercise slide
  names the exact folder in `../workspace/exercises/` so students can find it immediately.
- Components (`DmColumns`, `DmProcess`/`DmPhase`, `DmBanner`) come from the theme. The reference
  deck lives in [datamindedbe/playground-agentic-slides](https://github.com/datamindedbe/playground-agentic-slides).
- No emdashes, and bold marks a single term rather than a whole claim.
- Progressive builds use single slides with `v-click`/code-block step ranges (`{all|1-2|4-6}`).
  `slidev export` flattens clicks to their final state, so keep the last state complete.
- `style.css` is loaded once at startup. After editing it, restart the dev server; hot reload
  does not pick it up.
- Slides render at 980x552 CSS pixels. Anything taller silently overflows the page in the PDF
  export, so check the export after adding a long code block or table.
- Exercise numbering must always match `../README.md`'s "Exercises" table — that table is the
  source of truth, not this deck.
