#!/usr/bin/env python3
"""Build mblm-illustration image-gen prompts (stdlib only).

Examples:
  python3 scripts/mblm_illustration_prompt.py --topic "Brand system as a city" --accent yellow
  python3 scripts/mblm_illustration_prompt.py --topic "Signal landscape" --accent magenta \\
      --background paper --action "tiny figures receive signals" --shapes "towers, funnels" \\
      --write prompts.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ACCENTS = {
    "yellow": ("Yellow", "#FFF200"),
    "orange": ("Orange", "#FFBA00"),
    "magenta": ("Magenta", "#EC008C"),
    "violet": ("Violet", "#9700DC"),
    "blue": ("Blue", "#006AF1"),
    "cyan": ("Cyan", "#00AEFF"),
    "green": ("Green", "#00D300"),
}

BACKGROUNDS = {
    "white": "stark white #FFFFFF",
    "paper": "paper gray",
    "charcoal": "deep charcoal / near-black",
}


def slugify(text: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "_", text.strip().lower()).strip("_")
    return s[:48] or "metaphor"


def build_prompt(
    topic: str,
    accent_key: str,
    background_key: str,
    action: str,
    shapes: str,
    ratio: str,
) -> str:
    accent_name, accent_hex = ACCENTS[accent_key]
    bg = BACKGROUNDS[background_key]
    action_line = action.strip() or "tiny faceless figures inhabit the landscape"
    shapes_line = shapes.strip() or "oversized geometric structures, grids, architectural volumes"
    return f"""Create a single {ratio} PNG illustration in the MBLM Illustration System: Textured Metaphors style.

SUBJECT / TOPIC: {topic}
METAPHOR ACTION: {action_line}
KEY SHAPES: {shapes_line}

SCALE: tiny faceless abstracted human figures against huge architectural / geometric structures
BACKGROUND: {bg} — solid foundation, not a photo
ACCENT: exactly ONE color — {accent_name} {accent_hex} — never mix accents
TEXTURE: risograph / halftone / screen-print grain on accent fields; thin architectural linework in black or dark gray
ACTORS: faceless, abstracted — no readable faces, no corporate headshots
OPTIONAL: sparse MBLM-style glyphs or circled marks — not a logo product shot

COMPOSITION: art centered with generous padding from edges — NOT full bleed (unless cover/section hero)
NO: second accent colors, rainbow gradients, cluttered icon soup, photoreal office stock, text paragraphs inside the art

OUTPUT: one clean PNG, metaphorical and minimal, suitable for an MBLM content-slide image well.
""".strip()


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Print mblm-illustration image-gen prompt")
    p.add_argument("--topic", required=True, help='Metaphor topic, e.g. "Brand system as a city"')
    p.add_argument(
        "--accent",
        required=True,
        choices=sorted(ACCENTS.keys()),
        help="Exactly one MBLM accent",
    )
    p.add_argument(
        "--background",
        default="white",
        choices=sorted(BACKGROUNDS.keys()),
        help="white | paper | charcoal (default white)",
    )
    p.add_argument("--action", default="", help="What tiny figures / elements are doing")
    p.add_argument("--shapes", default="", help="Oversized structures / geometry vocabulary")
    p.add_argument("--ratio", default="16:9", help="Canvas ratio (default 16:9)")
    p.add_argument("--write", metavar="PATH", help="Optional path to write an image_prompts.json fragment")
    p.add_argument("--slug", default="", help="Override illustration_<slug>.png basename")
    args = p.parse_args(argv)

    topic = args.topic.strip()
    prompt = build_prompt(
        topic, args.accent, args.background, args.action, args.shapes, args.ratio
    )
    slug = args.slug.strip() or slugify(topic)
    filename = f"illustration_{slug}.png"
    accent_name, accent_hex = ACCENTS[args.accent]

    print(prompt)
    print()
    print(f"# suggested_filename: {filename}")
    print(
        "# §VIII: Acquire Via=ai|user; Type=Illustration; Crop=no-crop "
        "(adaptive for heroes); Purpose=metaphor illustration"
    )
    print(f"# accent_lock: {accent_name} {accent_hex} (never mix)")

    if args.write:
        fragment = {
            "images": [
                {
                    "filename": filename,
                    "acquire_via": "ai",
                    "type": "Illustration",
                    "crop": "no-crop",
                    "purpose": "metaphor illustration",
                    "accent": args.accent,
                    "accent_hex": accent_hex,
                    "background": args.background,
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
