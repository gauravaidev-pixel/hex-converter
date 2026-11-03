# Hex Converter — static site

Decimal ↔ hexadecimal converter. No server, no build step, no dependencies.
Everything runs in the browser, so the page works offline once it has loaded.

This is the static version of the old Flask app (`app.py`). Flask only served
three things — the HTML, `manifest.json` and `sw.js` — so the whole app is now
plain files. `requirements.txt` is not needed any more.

## Files

| File | What it is |
| --- | --- |
| `index.html` | The whole app: markup, CSS and JS in one file |
| `manifest.json` | PWA manifest (name, icons, theme colour) |
| `sw.js` | Service worker — caches the app so it opens offline |
| `icon-192.png`, `icon-512.png` | App icons (also used as `apple-touch-icon`) |

All paths are relative (`./`), so the site works at a domain root **and** at a
repo sub-path like `https://username.github.io/hex-converter/`.

## Deploy on GitHub Pages

1. Create a repo (or use the existing `hex-converter` repo) and add these files
   to the root of the `main` branch. Delete `app.py` and `requirements.txt`.
2. Repo → **Settings → Pages** → Source: **Deploy from a branch** →
   Branch: `main`, folder: `/ (root)` → **Save**.
3. Wait a minute; the site appears at `https://<username>.github.io/hex-converter/`.

Netlify or Cloudflare Pages work the same way: drag the folder in, no build
command, publish directory `/`.

Service workers need HTTPS, which all three give you for free. Opening
`index.html` straight from the file system (`file://`) will work, but the
offline cache and "Install app" button will not.

## What changed from the Flask version

- **Works without a server.** The conversion was already pure JavaScript;
  Flask only wrapped it.
- **Hex input actually works now.** The old input was `type="number"`, which
  browsers refuse to accept `FF` in — so hex → decimal was impossible to type.
  It is a text field now, with its own validation and placeholder per mode.
- **Big numbers are exact.** `parseInt` loses precision above 2^53; conversion
  now uses `BigInt`, so 30-digit values convert exactly.
- **Cleaner input.** Spaces, underscores, commas and the `0x` prefix are all
  accepted. Negative numbers work in both directions.
- **Inline errors instead of `alert()`**, plus live conversion as you type.
- **Copy** and **use as input** buttons on the result.
- **History** is unchanged in spirit (last 10, `localStorage`, tap to reuse) but
  no longer breaks when the stored JSON is corrupted.
- **Relative paths everywhere** so the PWA installs correctly from a repo
  sub-path; the old `start_url: "/"` and SW cache list `'/'` pointed at the
  wrong place on GitHub Pages.
- **Real PNG icons** instead of an emoji inside an SVG data-URI, which some
  devices render as a blank icon.

## Editing

Change the cache name in `sw.js` (`hex-converter-v1` → `v2`) whenever you ship
a change, otherwise returning visitors keep the old cached copy. The navigation
request is network-first, so the HTML normally updates on its own — bumping the
version is the safe habit.
