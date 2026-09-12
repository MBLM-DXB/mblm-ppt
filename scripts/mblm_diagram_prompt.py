#!/usr/bin/env python3
"""Build mblm-diagram / allumni-diagram image-gen prompts (stdlib only).

Examples:
  python3 scripts/mblm_diagram_prompt.py --archetype inbound --topic "Inbound engine"
  python3 scripts/mblm_diagram_prompt.py --archetype generic --topic "Launch" \\
      --steps "Discover|Define|Build|Launch|Measure" --write prompts.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ARCHETYPES = {
    "brand-rollout": {
        "name": "Brand Implementation three-column Essence/Story/Experience",
        "layout": "three-column",
        "canvas": "16:9 1280x720",
        "default_steps": [
            "ESSENCE: Brand Discovery (circled-R + magnifier); Brand Promise; Identity/Brand Arch.; Design System; Brand Templates; Brand Guidelines",
            "STORY: Brand Messaging; Application Templates; Marketing Content & Materials; Go To Market Campaign",
            "EXPERIENCE: Employee Launch; External Launch; Website; Channel Planning; Social Media Strategy; Brand Roll Out",
        ],
        "slug": "brand_rollout",
    },
    "inbound": {
        "name": "Inbound Marketing 5-step horizontal flow",
        "layout": "horizontal-flow",
        "canvas": "~1100x280 content strip or 1280x720 centered",
        "default_steps": [
            "ATTRACT — megaphone + line-chart",
            "CONVERT — person + document + speech-bubble",
            "NURTURE — email-envelope + person-group-3",
            "CLOSE — bar-chart + circled-R",
            "DELIGHT — gear + magnifier + person-group-3",
        ],
        "slug": "inbound_marketing",
    },
    "video": {
        "name": "Brand Video Production 5-step horizontal flow",
        "layout": "horizontal-flow",
        "canvas": "~1100x280 content strip or 1280x720 centered",
        "default_steps": [
            "CONCEPT — speech-bubble + person",
            "SCRIPT & PLAN — document + person-group-3",
            "PRODUCTION — camera + person",
            "EDIT & REVIEW — monitor + magnifier",
            "PUBLISH — video-frame + megaphone",
        ],
        "slug": "brand_video",
    },
    "generic": {
        "name": "Generic horizontal N-step flow (3–5)",
        "layout": "horizontal-flow",
        "canvas": "~1100x280 content strip or 1280x720 centered",
        "default_steps": [
            "STEP_1 — document + magnifier",
            "STEP_2 — person + speech-bubble",
            "STEP_3 — monitor + gear",
            "STEP_4 — bar-chart + circled-R",
            "STEP_5 — package-box + megaphone",
        ],
        "slug": "generic_process",
    },
}


CONTRACT_BLOCK = """CANVAS: {canvas}
BACKGROUND: pure white #ffffff
STROKE: black #000000 only, ~1–1.5pt, round linecaps and round linejoins
FILL: none on icons EXCEPT solid black social circles with white letterforms
NO: color, gradients, shadows, opacity, blur, decorative boxes around icons, body paragraphs inside the art
ICON RULES: detailed illustrative line icons (not blobs/silhouettes). Use only mblm-diagram / allumni icon library vocabulary. Each icon ~48–64px; groups of 2–4 on one baseline, ~8px apart."""


def slugify(text: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "_", text.strip().lower()).strip("_")
    return s[:48] or "process"


def parse_steps(raw: str | None, defaults: list[str]) -> list[str]:
    if not raw:
        return list(defaults)
    parts = [p.strip() for p in raw.split("|") if p.strip()]
    if not parts:
        return list(defaults)
    return parts


def build_prompt(archetype_key: str, topic: str, steps: list[str]) -> str:
    meta = ARCHETYPES[archetype_key]
    layout_note = (
        "Three-column: large light serif column titles (~48–56pt); section labels uppercase "
        "small-caps ~9pt medium gray; thin #cccccc rules; icon clusters under rules; generous "
        "whitespace; ~40px column gaps."
        if meta["layout"] == "three-column"
        else "Horizontal flow: 3–5 steps left-to-right; icon cluster above; uppercase small-caps "
        "label below; thin connector arrows (line + arrowhead) between steps."
    )
    steps_block = "\n".join(f"- {s}" for s in steps)
    return f"""Create a single process diagram PNG matching the allumni / mblm-diagram monoline contract exactly.

{CONTRACT_BLOCK.format(canvas=meta["canvas"])}

ARCHETYPE: {meta["name"]}
TOPIC: {topic}
STEPS / SECTIONS:
{steps_block}

LAYOUT:
- {layout_note}

OUTPUT: one clean PNG, labels only (no paragraph copy), centered composition with padding from edges.
""".strip()


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Print mblm-diagram image-gen prompt")
    p.add_argument(
        "--archetype",
        required=True,
        choices=sorted(ARCHETYPES.keys()),
        help="inbound | brand-rollout | video | generic",
    )
    p.add_argument("--topic", default="", help='Process topic, e.g. "Inbound engine"')
    p.add_argument(
        "--steps",
        default="",
        help='Pipe-separated steps/labels, e.g. "Attract|Convert|Close"',
    )
    p.add_argument(
        "--write",
        metavar="PATH",
        help="Optional path to write an image_prompts.json fragment",
    )
    p.add_argument("--slug", default="", help="Override diagram_<slug>.png basename")
    args = p.parse_args(argv)

    meta = ARCHETYPES[args.archetype]
    topic = args.topic.strip() or meta["name"]
    steps = parse_steps(args.steps or None, meta["default_steps"])
    if args.archetype == "generic" and args.steps:
        # user provided bare labels — keep as labels only
        steps = [s if "—" in s or "-" in s else s for s in steps]
    prompt = build_prompt(args.archetype, topic, steps)
    slug = args.slug.strip() or f"{meta['slug']}_{slugify(topic)}"
    filename = f"diagram_{slug}.png"

    print(prompt)
    print()
    print(f"# suggested_filename: {filename}")
    print("# §VIII: Acquire Via=ai|user; Type=Illustration; Crop=no-crop; Purpose=process diagram")

    if args.write:
        fragment = {
            "images": [
                {
                    "filename": filename,
                    "acquire_via": "ai",
                    "type": "Illustration",
                    "crop": "no-crop",
                    "purpose": "process diagram",
                    "archetype": args.archetype,
                    "topic": topic,
                    "prompt": prompt,
                }
            ]
        }
        out = Path(args.write)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(fragment, indent=2) + "\n", encoding="utf-8")
        print(f"# wrote: {out}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
