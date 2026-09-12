#!/usr/bin/env python3
"""Build mblm-cinematic image-gen prompts (stdlib only).

Examples:
  python3 scripts/mblm_cinematic_prompt.py --subject "two silhouettes" \\
      --action "walking toward light" --location "empty urban plaza at dusk" \\
      --light "low sun" --motion still --face obscured
  python3 scripts/mblm_cinematic_prompt.py --subject "hands at a window" \\
      --action "holding still" --location "loft interior" --light window \\
      --motion still --face soft --write prompts.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

LIGHT_PRESETS = {
    "low sun": "low sun (warm rim / backlight)",
    "neon": "neon practical (one warm/cyan-adjacent practical, still one warm read)",
    "window": "window light (warm interior spill against cool exterior grade)",
}

MOTION_CHOICES = ("blur", "still")
FACE_CHOICES = ("profile", "obscured", "soft")


def slugify(text: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "_", text.strip().lower()).strip("_")
    return s[:48] or "cinematic"


def normalize_light(raw: str) -> str:
    key = raw.strip().lower()
    if key in LIGHT_PRESETS:
        return LIGHT_PRESETS[key]
    # allow free text like "low sun|neon|window" already expanded
    return raw.strip() or LIGHT_PRESETS["low sun"]


def build_prompt(
    subject: str,
    action: str,
    location: str,
    light: str,
    motion: str,
    face: str,
) -> str:
    motion_line = (
        "subtle motion blur"
        if motion == "blur"
        else "deliberate stillness"
    )
    face_line = {
        "profile": "profile",
        "obscured": "obscured / silhouette",
        "soft": "soft focus",
    }[face]
    return f"""Create a single 16:9 cinematic photographic still for an MBLM presentation.

SUBJECT: {subject}
ACTION: {action}
LOCATION: {location}
LIGHT: cool blue-teal base grade + ONE warm source ({light}); backlight / rim preferred
MOTION: {motion_line}
FACE: {face_line} — never flat frontal smiling headshot
OPTICS: shallow depth of field, natural haze or soft flare OK
COMPOSITION: negative space for title overlay if cover/section; atmospheric, film-still, not corporate stock

NO: flat frontal office lighting, smiling LinkedIn headshots, handshake clichés, busy logo overlays in-frame, cartoon / illustration look

OUTPUT: one photoreal cinematic PNG, 16:9, suitable for full-bleed cover/section or framed content well.
""".strip()


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Print mblm-cinematic image-gen prompt")
    p.add_argument("--subject", required=True, help='e.g. "two silhouettes"')
    p.add_argument("--action", required=True, help='e.g. "walking toward light"')
    p.add_argument("--location", required=True, help='e.g. "empty urban plaza at dusk"')
    p.add_argument(
        "--light",
        default="low sun",
        help='Warm source: "low sun" | "neon" | "window" | free text',
    )
    p.add_argument(
        "--motion",
        default="still",
        choices=MOTION_CHOICES,
        help="blur | still",
    )
    p.add_argument(
        "--face",
        default="obscured",
        choices=FACE_CHOICES,
        help="profile | obscured | soft",
    )
    p.add_argument("--write", metavar="PATH", help="Optional path to write an image_prompts.json fragment")
    p.add_argument("--slug", default="", help="Override photo_<slug>.png basename")
    args = p.parse_args(argv)

    light = normalize_light(args.light)
    prompt = build_prompt(
        args.subject.strip(),
        args.action.strip(),
        args.location.strip(),
        light,
        args.motion,
        args.face,
    )
    slug_src = args.slug.strip() or f"{args.subject}_{args.location}"
    slug = slugify(slug_src)
    filename = f"photo_{slug}.png"

    print(prompt)
    print()
    print(f"# suggested_filename: {filename}")
    print(
        "# §VIII: Acquire Via=ai|user; Type=Photography; Crop=adaptive "
        "(heroes); Purpose=cinematic photo"
    )
    print("# placement: full-bleed OK cover/section/closing + dark overlay; content = half-bleed/well")

    if args.write:
        fragment = {
            "images": [
                {
                    "filename": filename,
                    "acquire_via": "ai",
                    "type": "Photography",
                    "crop": "adaptive",
                    "purpose": "cinematic photo",
                    "subject": args.subject.strip(),
                    "action": args.action.strip(),
                    "location": args.location.strip(),
                    "light": light,
                    "motion": args.motion,
                    "face": args.face,
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
