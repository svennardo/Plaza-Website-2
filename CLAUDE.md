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

Photos live in `public/assets/images/`, organized in subfolders:

- `gallery/` — all gallery photos (referenced by the `photos` array in the inline JS of `index.html`)
- `main/` — hero / main media
- `who_we_are/` — about section
- `team/` — one subfolder per team member (`cole`, `fabi`, `faxe`, `jonas`, `kono`, `sven`)

The gallery `photos` array is shuffled on every load (`.sort(() => Math.random() - 0.5)`) and run through `encodeURI` so filenames with spaces/parentheses resolve correctly. Each photo shows a per-photographer Instagram credit overlay: files containing `giovanna` → `@joe.vna`, all others → `@moritz.photogrphy`. When adding new gallery images, add their path to that array.

**Keep images web-sized.** Gallery photos must be downscaled to max 1920 px on the long edge (quality ~82), which keeps each file well under ~1 MB. Full-resolution camera originals (10–18 MB / 18 MP) make the page appear to "not load" — the browser stalls decoding them and the dev server queues the huge transfers. Resize with Pillow before committing, e.g.:

```python
from PIL import Image, ImageOps
im = ImageOps.exif_transpose(Image.open(f)).convert("RGB")
w, h = im.size; s = 1920 / max(w, h)
if s < 1: im = im.resize((round(w*s), round(h*s)), Image.LANCZOS)
im.save(f, "JPEG", quality=82, optimize=True, progressive=True)
```

## Website sections

1. **Hero** — full-viewport with action photo background, animated entrance
2. **About** — mission, 4 pillars (Kultur / Kunst / Sport / Jugend)
3. **Stats bar** — accent-colored strip with key numbers
4. **Gallery** — masonry grid, randomized photos with per-photographer Instagram credit, lightbox with keyboard navigation
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
