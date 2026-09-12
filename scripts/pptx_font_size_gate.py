#!/usr/bin/env python3
"""Gate: verify PPTX DrawingML font sizes (not SVG attributes).

SVG font-size is canvas px; exporter uses 1px = 0.75pt.
Author SVG as desired_pt / 0.75, then run this on the exported PPTX.
"""
from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
}


def slide_sizes(z: zipfile.ZipFile, name: str) -> list[float]:
    root = ET.fromstring(z.read(name))
    out: list[float] = []
    for rPr in root.findall(".//a:rPr", NS) + root.findall(".//a:defRPr", NS):
        sz = rPr.get("sz")
        if sz:
            out.append(int(sz) / 100.0)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("pptx", type=Path)
    ap.add_argument("--title-pt", type=float, default=47.0)
    ap.add_argument("--title-tol", type=float, default=1.0)
    ap.add_argument("--body-min", type=float, default=18.0)
    ap.add_argument("--body-max", type=float, default=20.0)
    ap.add_argument(
        "--require-title",
        action="store_true",
        help="Fail if a content slide has no size near title-pt",
    )
    args = ap.parse_args()

    if not args.pptx.is_file():
        print(f"missing pptx: {args.pptx}", file=sys.stderr)
        return 2

    fails: list[str] = []
    with zipfile.ZipFile(args.pptx) as z:
        slides = sorted(
            (n for n in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n)),
            key=lambda s: int(re.search(r"(\d+)", s).group(1)),
        )
        print(f"pptx={args.pptx.name} slides={len(slides)}")
        for sn in slides:
            sizes = sorted(set(slide_sizes(z, sn)))
            idx = int(re.search(r"(\d+)", sn).group(1))
            print(f"  slide{idx}: {sizes}")
            # Heuristic: largest non-supertext size should be near title on most slides
            # Supertext can be >=100pt — ignore those for title check
            content = [s for s in sizes if s < 100]
            if not content:
                fails.append(f"slide{idx}: no text sizes")
                continue
            biggest = max(content)
            # Cover may be 60pt; photo overlay 40pt; content titles 47pt
            near_title = any(abs(s - args.title_pt) <= args.title_tol for s in content)
            near_cover = any(abs(s - 60.0) <= 1.5 for s in content)
            near_photo = any(abs(s - 40.0) <= 1.5 for s in content)
            if args.require_title and not (near_title or near_cover or near_photo):
                fails.append(
                    f"slide{idx}: no ~{args.title_pt}pt title (sizes={content})"
                )
            # Body band: any mid sizes should not sit in the broken 13.5 band
            mid = [s for s in content if 10 <= s <= 30]
            bad_mid = [s for s in mid if 12.5 <= s <= 14.5]  # classic 18*0.75 failure
            if bad_mid and not any(args.body_min - 0.6 <= s <= args.body_max + 0.6 for s in mid):
                fails.append(
                    f"slide{idx}: body looks underscaled {bad_mid} (want {args.body_min}-{args.body_max})"
                )

    if fails:
        print("FAIL")
        for f in fails:
            print(" ", f)
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
