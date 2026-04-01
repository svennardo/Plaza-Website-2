# Plaza-Website-2

## Project overview

Website for **Plaza e.V.** — a nonprofit in Magdeburg focused on culture, skateboarding, art, and youth. The site is a static single-page site served by Python's built-in HTTP server.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 src/main.py
```

Opens at `http://localhost:8080` and auto-launches in browser.

## Project structure

```
public/
  index.html            ← Full website (HTML + CSS + JS, single file)
  assets/
    images/             ← Place photos here as plaza-01.jpg … plaza-32.jpg
src/
  main.py               ← HTTP server entry point (serves public/)
requirements.txt        ← Runtime dependencies (currently empty)
```

## Images

Place the 32 skate event photos in `public/assets/images/` named:
`plaza-01.jpg` through `plaza-32.jpg`

The hero background uses `plaza-01.jpg`. The about section uses `plaza-03.jpg`, `plaza-05.jpg`, `plaza-13.jpg`. All 32 appear in the gallery.

## Website sections

1. **Hero** — full-viewport with action photo background, animated entrance
2. **About** — mission, 4 pillars (Kultur / Kunst / Sport / Jugend)
3. **Stats bar** — accent-colored strip with key numbers
4. **Gallery** — masonry grid, 32 photos, lightbox with keyboard navigation
5. **Team** — 7 founding members (from Satzung)
6. **Join** — membership form (posts to plaza@posteo.de via mailto)
7. **Contact** — address + contact form (posts to plaza@posteo.de via mailto)

## Club info (from Satzung)

- Full name: Plaza e.V.
- Address: Annastraße 27, 39108 Magdeburg
- Email: plaza@posteo.de
- Founded: 26. Mai 2021, Amtsgericht Stendal
- Founders: Jan-Riklef Rausch, Sven Meienberg, Fabian Garnich, Vincent Willenius, Caroline Knapp, Christian Künzel, Jonas Nitsche

## Development notes

- Use `python3` (not `python`) for all commands
- Virtual environment lives in `.venv/` (gitignored)
- Do not commit `.env` files
- All website code is in `public/index.html` — CSS and JS are inline

## Project instructions

- You should always behave as if you're one of the best and most creative frontend developers. Express that in the website as good as possible.
- Always update CLAUDE.md after you're finished developing.
