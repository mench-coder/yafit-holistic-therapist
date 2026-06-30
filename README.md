# Yafit — Holistic Body-Mind Therapist

Static one-page website for **יפית מוכתרי**, a holistic body-mind therapist in Tel Aviv.

> **This is NOT Yaff Living.**  
> Yaff Living (property management) is a separate Next.js project.  
> See: `../YAFF LIVING - Property Management & Care/yaff-living`

## Official business card (approved 30.6.2026)

**Share link (WhatsApp):** https://mench-coder.github.io/yafit-holistic-therapist/card-f.html?v=2

Only `card-f.html` is active for distribution. Versions A–E are archived.

**Analytics:** GA4 `G-ZDRSXKQDRL` — https://analytics.google.com/

## Quick start

```bash
npm install
npm run dev
```

Open **http://localhost:5500**

| Project | Port | Stack |
|---------|------|-------|
| **Yafit Holistic Therapist** (this repo) | `5500` | Static HTML/CSS/JS |
| **Yaff Living** (separate repo) | `3000` | Next.js 16 |

## Project structure

```
YAFF - Holistic Therapist/
├── index.html              # Main one-pager site
├── assets/
│   ├── images/             # Site photos (hero, about, bach flowers)
│   └── logos/              # SVG logos used on the site
├── LOGO/                   # Logo exploration & variants (EN/HE)
├── תמונות יפית/            # Source photos (not served directly)
└── package.json            # Dev server only (http-server on :5500)
```

## Customization

- **WhatsApp:** Real number `972547744141` (+972 54-774-4141) is set in `index.html` and all `card-*.html` files.
- **Photos:** Site images live in `assets/images/`. Source files are in `תמונות יפית/`.
- **Logos:** Production SVGs in `assets/logos/`; design variants in `LOGO/`.

## Tech

- Pure HTML / CSS / JavaScript
- RTL Hebrew (`dir="rtl"`)
- Google Fonts: Frank Ruhl Libre, Cormorant Garamond, Assistant
- No build step — `npm run dev` serves files as-is
