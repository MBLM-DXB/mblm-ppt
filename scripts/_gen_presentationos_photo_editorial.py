#!/usr/bin/env python3
"""Generate PresentationOS tractor deck — photo-editorial + narrative-keynote + MBLM freeze."""
from __future__ import annotations
from pathlib import Path

OUT = Path("/workspace/mblm-ppt-master/projects/presentationos-photo-editorial_ppt169_20260912/svg_output")
NOTES = Path("/workspace/mblm-ppt-master/projects/presentationos-photo-editorial_ppt169_20260912/notes")
FONT = "BentonSansCond, Arial Narrow, Arial, sans-serif"
LOGO_L = "../images/MBLM_LOGO_White background.svg"
LOGO_D = "../images/MBLM_LOGO_dark background.svg"

def E(s: str) -> str:
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;"))

def open_svg() -> str:
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
        'width="1280" height="720" viewBox="0 0 1280 720">\n'
    )

def close() -> str:
    return "</svg>\n"

def logo_content(dark: bool = False) -> str:
    href = LOGO_D if dark else LOGO_L
    return (
        f'  <image id="layout-logo" x="1148.2" y="39.7" width="88.4" height="44.2" '
        f'href="{href}" preserveAspectRatio="xMidYMid meet"/>\n'
    )

def logo_cover(dark: bool = True) -> str:
    href = LOGO_D if dark else LOGO_L
    return (
        f'  <image id="layout-logo" x="40" y="40" width="138" height="69" '
        f'href="{href}" preserveAspectRatio="xMidYMid meet"/>\n'
    )

def page_num(n: int, fill: str = "#000000") -> str:
    return (
        f'  <text id="pg" x="1240" y="698" fill="{fill}" font-family="{FONT}" '
        f'font-size="12" font-weight="400" text-anchor="end">{n:02d}</text>\n'
    )

def tspan_lines(lines: list[str], x: float, start_dy: float, line_dy: float) -> str:
    parts = []
    for i, line in enumerate(lines):
        dy = start_dy if i == 0 else line_dy
        parts.append(f'<tspan x="{x:g}" dy="{dy:g}">{E(line)}</tspan>')
    return "".join(parts)

def write(name: str, body: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text(body, encoding="utf-8")
    print("wrote", name)

# ── P01 Opening image ──────────────────────────────────────────────
def p01() -> None:
    body = open_svg()
    body += """  <defs>
    <linearGradient id="scrim" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#000000" stop-opacity="0.72"/>
      <stop offset="55%" stop-color="#000000" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0.15"/>
    </linearGradient>
  </defs>
"""
    body += '  <image href="../images/photo_tractor_field.jpg" x="0" y="0" width="1280" height="720" preserveAspectRatio="xMidYMid slice"/>\n'
    body += '  <rect x="0" y="0" width="1280" height="720" fill="url(#scrim)"/>\n'
    body += logo_cover(True)
    body += f'  <text id="title" x="40" y="340" fill="#FFFFFF" font-family="{FONT}" font-size="60" font-weight="300">'
    body += tspan_lines(["Turn complex products into", "sales experiences that convert."], 40, 0, 72)
    body += "</text>\n"
    body += f'  <text id="sub" x="40" y="520" fill="#FFFFFF" font-family="{FONT}" font-size="24" font-weight="400">PresentationOS</text>\n'
    body += close()
    write("P01.svg", body)

# ── P02 Recognized world ───────────────────────────────────────────
def p02() -> None:
    body = open_svg()
    body += '  <rect width="1280" height="720" fill="#FFFFFF"/>\n'
    # Right photo panel — magazine crop
    body += '  <image href="../images/photo_red_tractor.jpg" x="640" y="0" width="640" height="720" preserveAspectRatio="xMidYMid slice"/>\n'
    body += logo_content(False)
    body += f'  <text id="title" x="40" y="82" fill="#000000" font-family="{FONT}" font-size="47" font-weight="300">A commercial result</text>\n'
    body += f'  <text id="sub" x="40" y="120" fill="#000000" font-family="{FONT}" font-size="20" font-weight="400">Not presentation software. Not AR. Not a toolkit.</text>\n'
    # Quiet editorial body — left column
    body += f'  <text id="b1" x="40" y="220" fill="#000000" font-family="{FONT}" font-size="20" font-weight="400">'
    body += tspan_lines([
        "Manufacturers of complex products need",
        "buyers to explore, configure, and understand",
        "before the sales conversation starts.",
    ], 40, 0, 32)
    body += "</text>\n"
    body += f'  <text id="b2" x="40" y="360" fill="#000000" font-family="{FONT}" font-size="20" font-weight="400">'
    body += tspan_lines([
        "When interactive 3D configuration converts",
        "more leads into sales than other digital",
        "experiences, that becomes the foundation",
        "of company positioning.",
    ], 40, 0, 32)
    body += "</text>\n"
    body += page_num(2)
    body += close()
    write("P02.svg", body)

# ── P03 Content / agenda (quiet r2_12) ──────────────────────────────
def p03() -> None:
    items = [
        ("01", "World", "Commercial framing"),
        ("02", "Tension", "Static specs fail"),
        ("03", "Turn", "3D selling platform"),
        ("04", "Proof", "Case & data gaps"),
        ("05", "Market", "ICP & offer"),
        ("06", "Next", "Case study first"),
    ]
    body = open_svg()
    body += '  <rect width="1280" height="720" fill="#FFFFFF"/>\n'
    body += logo_content(False)
    body += f'  <text id="title" x="40" y="82" fill="#000000" font-family="{FONT}" font-size="47" font-weight="300">Content</text>\n'
    # More whitespace than media-r2 — fewer chrome lines, larger gaps
    xs = [100, 300, 500, 700, 900, 1100]
    cy = 340
    for i, ((num, t, d), x) in enumerate(zip(items, xs)):
        body += f'  <circle cx="{x}" cy="{cy}" r="36" fill="#000000"/>\n'
        body += f'  <text id="n{i}" x="{x}" y="{cy + 10}" fill="#FFFFFF" font-family="{FONT}" font-size="22" font-weight="700" text-anchor="middle">{num}</text>\n'
        body += f'  <text id="t{i}" x="{x}" y="{cy + 90}" fill="#000000" font-family="{FONT}" font-size="18" font-weight="700" text-anchor="middle">{E(t)}</text>\n'
        body += f'  <text id="d{i}" x="{x}" y="{cy + 120}" fill="#000000" font-family="{FONT}" font-size="14" font-weight="400" text-anchor="middle">{E(d)}</text>\n'
    # Thin dashed connector — gray only, no yellow
    body += f'  <line x1="136" y1="{cy}" x2="1064" y2="{cy}" stroke="#BFBFBF" stroke-width="1" stroke-dasharray="4 8"/>\n'
    body += page_num(3)
    body += close()
    write("P03.svg", body)

# ── P04 Tension ─────────────────────────────────────────────────────
def p04() -> None:
    body = open_svg()
    body += """  <defs>
    <linearGradient id="tScrim" x1="0%" y1="50%" x2="100%" y2="50%">
      <stop offset="0%" stop-color="#000000" stop-opacity="0.78"/>
      <stop offset="50%" stop-color="#000000" stop-opacity="0.45"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0.2"/>
    </linearGradient>
  </defs>
"""
    body += '  <image href="../images/photo_ag_equipment.jpg" x="0" y="0" width="1280" height="720" preserveAspectRatio="xMidYMid slice"/>\n'
    body += '  <rect x="0" y="0" width="1280" height="720" fill="url(#tScrim)"/>\n'
    body += logo_cover(True)
    body += f'  <text id="title" x="40" y="300" fill="#FFFFFF" font-family="{FONT}" font-size="47" font-weight="300">'
    body += tspan_lines(["Complex products are hard", "to sell with static specs."], 40, 0, 58)
    body += "</text>\n"
    body += f'  <text id="body" x="40" y="450" fill="#FFFFFF" font-family="{FONT}" font-size="20" font-weight="400">'
    body += tspan_lines([
        "Tractors carry features, attachments, use cases,",
        "and configurations that brochures cannot hold.",
    ], 40, 0, 32)
    body += "</text>\n"
    body += page_num(4, "#FFFFFF")
    body += close()
    write("P04.svg", body)

# ── P05 The turn ────────────────────────────────────────────────────
def p05() -> None:
    body = open_svg()
    body += '  <rect width="1280" height="720" fill="#FFFFFF"/>\n'
    body += logo_content(False)
    # Vast breathing room — one statement
    body += f'  <text id="title" x="40" y="82" fill="#000000" font-family="{FONT}" font-size="47" font-weight="300">The turn</text>\n'
    body += f'  <text id="hero" x="40" y="320" fill="#000000" font-family="{FONT}" font-size="47" font-weight="300">'
    body += tspan_lines([
        "A 3D product-selling platform",
        "for manufacturers.",
    ], 40, 0, 58)
    body += "</text>\n"
    body += f'  <text id="sub" x="40" y="480" fill="#000000" font-family="{FONT}" font-size="20" font-weight="400">'
    body += tspan_lines([
        "Explore and configure interactively — then deploy across",
        "websites, dealerships, field sales, exhibitions, and showrooms.",
    ], 40, 0, 32)
    body += "</text>\n"
    body += page_num(5)
    body += close()
    write("P05.svg", body)

# ── P06 Four outcomes (light — photo + short list) ──────────────────
def p06() -> None:
    outcomes = [
        "Higher conversion",
        "Better product understanding",
        "Content reuse across channels",
        "Centralized control",
    ]
    body = open_svg()
    body += '  <rect width="1280" height="720" fill="#FFFFFF"/>\n'
    body += '  <image href="../images/photo_field_dusk.jpg" x="0" y="0" width="520" height="720" preserveAspectRatio="xMidYMid slice"/>\n'
    body += logo_content(False)
    body += f'  <text id="title" x="560" y="82" fill="#000000" font-family="{FONT}" font-size="47" font-weight="300">Four outcomes</text>\n'
    body += f'  <text id="sub" x="560" y="120" fill="#000000" font-family="{FONT}" font-size="18" font-weight="400">What PresentationOS helps manufacturers achieve</text>\n'
    y0 = 220
    for i, o in enumerate(outcomes):
        y = y0 + i * 70
        # Round black bullet Ø≈80% of 20pt ≈ 16
        body += f'  <circle cx="576" cy="{y - 6}" r="8" fill="#000000"/>\n'
        body += f'  <text id="o{i}" x="604" y="{y}" fill="#000000" font-family="{FONT}" font-size="20" font-weight="400">{E(o)}</text>\n'
    body += page_num(6)
    body += close()
    write("P06.svg", body)

# ── P07 Proof beat ──────────────────────────────────────────────────
def p07() -> None:
    body = open_svg()
    body += '  <rect width="1280" height="720" fill="#000000"/>\n'
    body += logo_cover(True)
    body += f'  <text id="title" x="40" y="82" fill="#FFFFFF" font-family="{FONT}" font-size="47" font-weight="300">Proof</text>\n'
    # One dominant proof line — white only on black
    body += f'  <text id="proof" x="40" y="340" fill="#FFFFFF" font-family="{FONT}" font-size="32" font-weight="300">'
    body += tspan_lines([
        "A US tractor manufacturer’s 3D configurator",
        "became its highest-converting digital experience",
        "from lead to completed sale.",
    ], 40, 0, 48)
    body += "</text>\n"
    body += f'  <text id="note" x="40" y="540" fill="#FFFFFF" font-family="{FONT}" font-size="16" font-weight="400">Validated wording only — digital experience, not every sales channel.</text>\n'
    body += page_num(7, "#FFFFFF")
    body += close()
    write("P07.svg", body)

# ── P08 Case challenge / solution (photo-led two panels) ────────────
def p08() -> None:
    body = open_svg()
    body += '  <rect width="1280" height="720" fill="#FFFFFF"/>\n'
    body += logo_content(False)
    body += f'  <text id="title" x="40" y="82" fill="#000000" font-family="{FONT}" font-size="47" font-weight="300">Tractor case</text>\n'
    body += f'  <text id="sub" x="40" y="120" fill="#000000" font-family="{FONT}" font-size="18" font-weight="400">Challenge and solution — two panels</text>\n'
    # Left photo panel
    body += '  <image href="../images/photo_red_tractor.jpg" x="40" y="160" width="580" height="420" preserveAspectRatio="xMidYMid slice"/>\n'
    body += '  <rect x="40" y="500" width="580" height="80" fill="#000000" fill-opacity="0.75"/>\n'
    body += f'  <text id="ch" x="60" y="535" fill="#FFFFFF" font-family="{FONT}" font-size="18" font-weight="700">Challenge</text>\n'
    body += f'  <text id="chb" x="60" y="562" fill="#FFFFFF" font-family="{FONT}" font-size="14" font-weight="400">Features, attachments, use cases — hard via static specs</text>\n'
    # Right white panel with solution
    body += '  <rect x="660" y="160" width="580" height="420" fill="#F2F2F2"/>\n'
    # Blue line above card only
    body += '  <rect x="660" y="160" width="580" height="6" fill="#006AF1"/>\n'
    body += f'  <text id="sol" x="700" y="230" fill="#000000" font-family="{FONT}" font-size="24" font-weight="700">Solution</text>\n'
    body += f'  <text id="solb" x="700" y="290" fill="#000000" font-family="{FONT}" font-size="20" font-weight="400">'
    body += tspan_lines([
        "Interactive 3D configurator —",
        "explore, understand options,",
        "configure before the sales process.",
    ], 700, 0, 32)
    body += "</text>\n"
    body += f'  <text id="dep" x="700" y="430" fill="#000000" font-family="{FONT}" font-size="16" font-weight="400">'
    body += tspan_lines([
        "Website · Dealers · Field sales",
        "Exhibitions · Showrooms · Tablets",
    ], 700, 0, 26)
    body += "</text>\n"
    body += page_num(8)
    body += close()
    write("P08.svg", body)

# ── P09 Data we must secure ─────────────────────────────────────────
def p09() -> None:
    gaps = [
        "Exact lead-to-sale conversion rate",
        "Comparison vs other digital experiences",
        "Sales attributed or influenced",
        "Deployment period and traffic / sample size",
        "Named customer quotation approving the claim",
        "Funnel: visitors → configure → lead → quote → purchase",
    ]
    body = open_svg()
    body += '  <rect width="1280" height="720" fill="#FFFFFF"/>\n'
    body += logo_content(False)
    body += f'  <text id="title" x="40" y="82" fill="#000000" font-family="{FONT}" font-size="47" font-weight="300">Data we must secure</text>\n'
    body += f'  <text id="sub" x="40" y="120" fill="#000000" font-family="{FONT}" font-size="18" font-weight="400">Case-study data gaps — not invented tractor KPIs</text>\n'
    y0 = 180
    for i, g in enumerate(gaps):
        y = y0 + i * 70
        # Empty checkbox squares (data gaps) — not filled fake checks
        body += f'  <rect x="48" y="{y - 18}" width="22" height="22" fill="none" stroke="#000000" stroke-width="2"/>\n'
        body += f'  <text id="g{i}" x="90" y="{y}" fill="#000000" font-family="{FONT}" font-size="20" font-weight="400">{E(g)}</text>\n'
    body += page_num(9)
    body += close()
    write("P09.svg", body)

# ── P10 ROI illustration (labeled illustration only) ────────────────
def p10() -> None:
    body = open_svg()
    body += '  <rect width="1280" height="720" fill="#FFFFFF"/>\n'
    body += logo_content(False)
    body += f'  <text id="title" x="40" y="82" fill="#000000" font-family="{FONT}" font-size="47" font-weight="300">ROI illustration</text>\n'
    body += f'  <text id="sub" x="40" y="120" fill="#000000" font-family="{FONT}" font-size="18" font-weight="700">Illustration only — not the customer’s reported result</text>\n'
    # Yellow label bar (fill OK — not a line)
    body += '  <rect x="40" y="160" width="1200" height="48" fill="#FFF200"/>\n'
    body += f'  <text id="lab" x="60" y="192" fill="#000000" font-family="{FONT}" font-size="18" font-weight="700">Break-even = annual license ÷ contribution margin per incremental sale</text>\n'
    # Three sale markers — illustration graphic
    for i, (x, label, amt) in enumerate([
        (160, "Sale 1", "+$10k"),
        (520, "Sale 2", "+$10k"),
        (880, "Sale 3", "+$10k"),
    ]):
        body += f'  <circle cx="{x + 80}" cy="360" r="70" fill="#000000"/>\n'
        body += f'  <text id="s{i}" x="{x + 80}" y="350" fill="#FFFFFF" font-family="{FONT}" font-size="20" font-weight="700" text-anchor="middle">{E(label)}</text>\n'
        body += f'  <text id="a{i}" x="{x + 80}" y="380" fill="#FFFFFF" font-family="{FONT}" font-size="16" font-weight="400" text-anchor="middle">{E(amt)}</text>\n'
        if i < 2:
            body += f'  <line x1="{x + 160}" y1="360" x2="{x + 280}" y2="360" stroke="#006AF1" stroke-width="3"/>\n'
    body += f'  <text id="sum" x="640" y="500" fill="#000000" font-family="{FONT}" font-size="24" font-weight="300" text-anchor="middle">$30,000 license · three incremental sales at $10,000 margin</text>\n'
    body += f'  <text id="foot" x="640" y="540" fill="#000000" font-family="{FONT}" font-size="16" font-weight="400" text-anchor="middle">Example arithmetic only — request actual contribution margin from the customer.</text>\n'
    body += page_num(10)
    body += close()
    write("P10.svg", body)

# ── P11 Who / ICP ───────────────────────────────────────────────────
def p11() -> None:
    pillars = [
        ("Tractors / ag", "Primary vertical"),
        ("Construction", "Heavy equipment"),
        ("Material-handling", "Dealer networks"),
        ("Commercial vehicles", "Multi-config"),
    ]
    body = open_svg()
    body += '  <rect width="1280" height="720" fill="#FFFFFF"/>\n'
    body += logo_content(False)
    body += f'  <text id="title" x="40" y="82" fill="#000000" font-family="{FONT}" font-size="47" font-weight="300">Who we sell to</text>\n'
    body += f'  <text id="sub" x="40" y="120" fill="#000000" font-family="{FONT}" font-size="18" font-weight="400">Agricultural and heavy equipment — products ~$25,000+, multi-config, dealers</text>\n'
    xs = [100, 400, 700, 1000]
    for i, ((t, d), x) in enumerate(zip(pillars, xs)):
        body += f'  <circle cx="{x}" cy="280" r="40" fill="#000000"/>\n'
        body += f'  <text id="pn{i}" x="{x}" y="288" fill="#FFFFFF" font-family="{FONT}" font-size="20" font-weight="700" text-anchor="middle">{i+1:02d}</text>\n'
        body += f'  <text id="pt{i}" x="{x}" y="380" fill="#000000" font-family="{FONT}" font-size="18" font-weight="700" text-anchor="middle">{E(t)}</text>\n'
        body += f'  <text id="pd{i}" x="{x}" y="412" fill="#000000" font-family="{FONT}" font-size="14" font-weight="400" text-anchor="middle">{E(d)}</text>\n'
    body += f'  <text id="trig" x="40" y="520" fill="#000000" font-family="{FONT}" font-size="16" font-weight="400">'
    body += tspan_lines([
        "Triggers: new range launch · major trade show · website redesign · dealer expansion ·",
        "replacing PDFs / static selectors · digital commerce investment",
    ], 40, 0, 28)
    body += "</text>\n"
    body += page_num(11)
    body += close()
    write("P11.svg", body)

# ── P12 Offer (compact) ─────────────────────────────────────────────
def p12() -> None:
    body = open_svg()
    body += '  <rect width="1280" height="720" fill="#FFFFFF"/>\n'
    body += logo_content(False)
    body += f'  <text id="title" x="40" y="82" fill="#000000" font-family="{FONT}" font-size="47" font-weight="300">Commercial offer</text>\n'
    # Two sparse panels — not heavy card walls
    body += '  <rect x="40" y="160" width="580" height="420" fill="#000000"/>\n'
    body += f'  <text id="p1t" x="80" y="230" fill="#FFFFFF" font-family="{FONT}" font-size="24" font-weight="700">Conversion Proof Pilot</text>\n'
    body += f'  <text id="p1b" x="80" y="300" fill="#FFFFFF" font-family="{FONT}" font-size="20" font-weight="400">'
    body += tspan_lines([
        "One product experience",
        "Website or sales deployment",
        "8–12 week validation",
        "$10,000–$15,000 paid pilot",
    ], 80, 0, 40)
    body += "</text>\n"
    body += '  <rect x="660" y="160" width="580" height="420" fill="#F2F2F2"/>\n'
    body += '  <rect x="660" y="160" width="580" height="6" fill="#006AF1"/>\n'
    body += f'  <text id="p2t" x="700" y="230" fill="#000000" font-family="{FONT}" font-size="24" font-weight="700">Core annual license</text>\n'
    body += f'  <text id="p2h" x="700" y="310" fill="#000000" font-family="{FONT}" font-size="47" font-weight="300">$30,000</text>\n'
    body += f'  <text id="p2b" x="700" y="380" fill="#000000" font-family="{FONT}" font-size="20" font-weight="400">'
    body += tspan_lines([
        "Starting annual anchor",
        "Sales-assisted motion",
        "Pilot credit toward first year",
    ], 700, 0, 36)
    body += "</text>\n"
    body += page_num(12)
    body += close()
    write("P12.svg", body)

# ── P13 Close / next step ───────────────────────────────────────────
def p13() -> None:
    body = open_svg()
    body += """  <defs>
    <linearGradient id="cScrim" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#000000" stop-opacity="0.85"/>
      <stop offset="55%" stop-color="#000000" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0.2"/>
    </linearGradient>
  </defs>
"""
    body += '  <image href="../images/photo_field_dusk.jpg" x="0" y="0" width="1280" height="720" preserveAspectRatio="xMidYMid slice"/>\n'
    body += '  <rect x="0" y="0" width="1280" height="720" fill="url(#cScrim)"/>\n'
    body += logo_cover(True)
    # Supertext atmospheric (section/closing only) — outline, does NOT repeat headline
    body += (
        f'  <text id="super" x="640" y="280" fill="none" stroke="#FFFFFF" stroke-width="1.25" '
        f'font-family="{FONT}" font-size="160" font-weight="900" text-anchor="middle" '
        f'letter-spacing="0">NEXT</text>\n'
    )
    body += f'  <text id="title" x="40" y="420" fill="#FFFFFF" font-family="{FONT}" font-size="47" font-weight="300">'
    body += tspan_lines(["Create the executive case study", "before increasing marketing spend."], 40, 0, 56)
    body += "</text>\n"
    body += f'  <text id="close" x="40" y="580" fill="#FFFFFF" font-family="{FONT}" font-size="20" font-weight="400">Shift: convert more equipment buyers by letting them configure in 3D.</text>\n'
    body += page_num(13, "#FFFFFF")
    body += close()
    write("P13.svg", body)

def notes() -> None:
    NOTES.mkdir(parents=True, exist_ok=True)
    text = """# 1_Opening

Open on the image. Let the field and machine speak first. Then deliver the headline slowly: turn complex products into sales experiences that convert. This talk is about commercial outcomes for manufacturers, not presentation software.

---
# 2_Commercial_result

Name the recognized world. Buyers of complex equipment need to explore and configure before the sales conversation. If interactive three-D configuration converts more leads into sales than other digital experiences, that result becomes the foundation of positioning. Stay away from AR, toolkit, or PowerPoint framing.

---
# 3_Content

Walk the six beats lightly: world, tension, turn, proof, market, and next step. Keep the agenda quiet — orientation only, then move.

---
# 4_Tension

Make the problem felt. Tractors carry features, attachments, use cases, and configurations that static specs and brochures cannot hold. Dealers and buyers both pay the cost of that opacity.

---
# 5_The_turn

Deliver the category cleanly: a three-D product-selling platform for manufacturers. Buyers and sales reps explore and configure interactively; the same experience deploys across websites, dealerships, field sales, exhibitions, and showrooms.

---
# 6_Four_outcomes

Name the four outcomes without turning them into a consulting wall: higher conversion, better product understanding, content reuse across channels, and centralized control. Pause after each so the room can absorb them.

---
# 7_Proof

Read the validated proof line exactly: a US tractor manufacturer's three-D configurator became its highest-converting digital experience from lead to completed sale. Emphasize digital experience — not an unmeasured claim about every sales channel. Do not invent numbers.

---
# 8_Tractor_case

Challenge: complex configurations hard to communicate with static materials. Solution: an interactive three-D configurator so buyers explore and configure before the sales process. Deploy on the public website, dealer locations, field meetings, exhibitions, showrooms, and tablets.

---
# 9_Data_gaps

Treat this as a checklist of what the executive case study still needs: exact lead-to-sale conversion, comparison versus other digital experiences, sales attributed or influenced, deployment period and sample size, a named customer quotation, and the full funnel from visitors through purchase. These are gaps, not proven tractor KPIs.

---
# 10_ROI_illustration

Label this clearly as an illustration, not the customer's reported result. If contribution margin is ten thousand dollars per incremental sale, a thirty-thousand-dollar license breaks even after three incremental sales. Ask for the real margin; do not present the arithmetic as measured ROI.

---
# 11_ICP

Primary vertical is agricultural and heavy equipment. Ideal manufacturers have products around twenty-five thousand dollars and up, multiple configurations, dealer networks, expensive transport, trade-show participation, and enough web traffic to measure conversion. Name the priority segments and the trigger moments that open a conversation.

---
# 12_Offer

Keep the commercial motion compact. Conversion Proof Pilot: one product, website or sales deployment, eight to twelve weeks, ten to fifteen thousand dollars paid, with credit toward the first annual license. Core annual license starts from thirty thousand dollars, sales-assisted.

---
# 13_Close

Close on the most important next step: create an executive-quality case study from the tractor deployment before increasing marketing spend. Then restate the positioning shift — help equipment manufacturers convert more buyers by letting them explore and configure complex products in three-D.
"""
    (NOTES / "total.md").write_text(text, encoding="utf-8")
    print("wrote notes/total.md")

def main() -> None:
    p01(); p02(); p03(); p04(); p05(); p06(); p07()
    p08(); p09(); p10(); p11(); p12(); p13()
    notes()
    print("done", len(list(OUT.glob("P*.svg"))), "SVGs")

if __name__ == "__main__":
    main()
