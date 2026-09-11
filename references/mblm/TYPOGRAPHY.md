# MBLM Typography

Locked 2026-09-10 + **v4.1.1 persistent layout lock** (content titles **47pt**; Supertext **≥150pt**; agenda = content). See `LAYOUT_METRICS.md`, `RESOLVED_DECISIONS.md`, `TEXT_BOXES.md`, visual catalogs.

## Official family

**BentonSansCond** (Benton Sans Condensed) is the **primary** face. On the user’s Mac it **is installed** under `~/Library/Fonts/` — generation on this machine must use Benton, not fallbacks.

### Installed faces (user Mac)

| File (under `~/Library/Fonts/`) | PostScript name | Role (v4.1 locks) |
|---|---|---|
| `BentonSansCond-Light.otf` | `BentonSansCond-Light` | Cover / content titles (sizes below) |
| `BentonSansCond-LightIta.otf` | `BentonSansCond-LightItalic` | Light italic |
| `BentonSansCond-Regular.otf` | `BentonSansCond-Regular` | **Body copy** (default **20pt**) |
| `BentonSansCond-RegIt.otf` | `BentonSansCond-RegularItalic` | Body italic |
| `BentonSansCond-Medium.otf` | `BentonSansCond-Medium` | Topic headers; emphasize within a phrase only |
| `BentonSansCond-MedIt.otf` | `BentonSansCond-MediumItalic` | Medium italic |
| `BentonSansCond-MediumSC.otf` | `BentonSansCond-MediumSC` | Medium small caps |
| `BentonSansCond-MedItSC.otf` | `BentonSansCond-MediumItalicSC` | Medium italic small caps |
| `BentonSansCond-Bold.otf` | `BentonSansCond-Bold` | **Accents / emphasis when type size < 24px** |
| `BentonSansCond-BoldIta.otf` | `BentonSansCond-BoldItalic` | Bold italic body emphasis |
| `BentonSansCond-Black.otf` | `BentonSansCond-Black` | Highlighted copy within phrase; **Supertext** (outline) |

Also installed (non-condensed): Benton Sans Regular / Italic / Bold / Bold Italic. Treat **BentonSansCond** as kit authority.

---

## HARD weight + size rules (v4.1.1 — impossible to miss)

1. **Headers / primary headlines** → BentonSansCond **Light** (not Medium, not Bold, not Black fill).
2. **Cover title** → **60pt or 72pt** Light (prefer **72** when it fits). **Cover only**.
3. **Cover subtitle** → **24pt or 32pt** (prefer **28–32**). Not 23.5.
4. **Content-slide titles** (agenda, value prop, ICP, tables, **all** non-cover / non-divider / non-thank-you) → Light **47pt only**. Never 54, never 24, never 32, never 28–36.
5. **Agenda title** (e.g. “Content”) → **content slide** → **47pt** Light. **Overrides** prior ≥72pt agenda rule.
6. **Divider / thank-you titles** → follow their pattern (large display / Supertext); not the content-title band.
7. **Content-slide subtitle** (under title) → **18pt or 20pt**, consistent deck-wide (prefer **20** when paired with 20pt body); fill **`#000000` only** (never dark grey `#404040` / `#333333` / etc.). Place **directly under** the title with a normal gap; left-aligned at content left margin (**1.05 cm**).
8. **Body / general content text** → **16pt or 20pt** Regular — lock **one** size deck-wide. Prefer **20pt** for primary body readability.
9. **Title alignment** → title **top edge** at **1.05 cm / ≈39.7 px** from slide top (same Y as content logo top / top margin); left-aligned at **1.05 cm** — `LAYOUT_METRICS.md`.
10. **Accents / emphasis when type size is below 24px** → **Bold**.
11. **Medium** → Topic headers; in-phrase emphasis only when matching hierarchy sheet.
12. **Highlighted copy** inside a sentence → **Black**.
13. **Kerning / tracking** → **normal** on titles and body. Do **not** expand letter-spacing / tracking.
14. **No kickers** → never place a kicker / eyebrow / label **above** the title (zero tolerance). Subheads **below** the title are OK when they are true section labels, not eyebrows.
15. **Editable text** → one text object per paragraph (`TEXT_BOXES.md`).
16. **Supertext** (atmospheric outline graphic):
    - BentonSansCond **Black**
    - Outline only (no fill), stroke **1.25pt**
    - Size **minimum 150pt**; increase so word(s) run **edge-to-edge** vertically or horizontally (within margins)
    - Short mood words (or brand name as graphic)
    - **Must NOT repeat the page headline**

### Hierarchy sheet mapping (spec_06)

| Role | Weight |
|---|---|
| Primary Headline | Light |
| Secondary Copy | Medium |
| Highlighted Copy | Black |
| Topic Header | Medium |
| Body Copy | Regular / Reg. Italic / Bold / Bold Italic |

---

## Tagline

Official descriptor: **"The Brand Intimacy Agency"**.

**Hard rule**: when the MBLM **logo is already on the slide**, **do not** place the tagline on that slide. Do not add an MBLM wordmark/text at the bottom either (`LOGOS.md`). Tagline may appear only on rare identity moments where the logo lockup is absent and the user explicitly wants the descriptor — default = omit with logo.

## Size guidance (@ 1280×720) — v4.1 locks

| Role | Size | Weight |
|---|---|---|
| **Cover title** | **60 or 72** (prefer 72) — cover only | Light |
| **Cover subtitle** | **24 or 32** (prefer 28–32) | Regular or Light |
| **Content page title** (incl. Agenda “Content”) | **47 only** | Light |
| **Divider / thank-you title** | Pattern-specific large / Supertext | Light or Black outline |
| **Content subtitle** under title | **18 or 20** (prefer 20); **`#000000`** | Regular |
| **Body / cards / bullets** | **16 or 20** locked deck-wide (**prefer 20**) | Regular |
| Topic header / card label | ~18–22 | Medium (or Bold if <24 emphasis) |
| Accent line <24 | ~12–22 | **Bold** |
| Supertext | **≥150**; edge-to-edge | Black outline **1.25pt** |
| KPI number | large display (may exceed title band) | Black or Light + small Regular label |
| Table header | ~12–16 | Bold/Medium; **normal kerning** |
| Page number | ~12 | Regular |

## Fallbacks (other machines only)

1. `Arial Narrow` → 2. `Arial`  
Record substitution; never claim Benton if substituted. On the user’s Mac, always Benton.

## Voice

- Formality: professional, intimate, confident (agency — not stiff consulting-ese).
- Person: we / you.
- Emoji: forbidden in client decks unless explicitly asked.
- Abbreviations: spell out on first use for client-facing terms; MBLM product names may stay as given.
