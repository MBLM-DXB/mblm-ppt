#!/usr/bin/env python3
"""Smoke checks for BentonSansCond PostScript face mapping on PPT export."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))

from svg_to_pptx.drawingml.utils import (  # noqa: E402
    parse_font_family,
    resolve_benton_cond_typeface,
)


def _assert(cond: bool, msg: str) -> None:
    if not cond:
        raise AssertionError(msg)


def main() -> None:
    cases = [
        ('BentonSansCond', '300', 'BentonSansCond-Light'),
        ('BentonSansCond', 'light', 'BentonSansCond-Light'),
        ('BentonSansCond', '100', 'BentonSansCond-Light'),
        ('BentonSansCond', '400', 'BentonSansCond-Regular'),
        ('BentonSansCond', 'normal', 'BentonSansCond-Regular'),
        ('BentonSansCond', '', 'BentonSansCond-Regular'),
        ('BentonSansCond', '500', 'BentonSansCond-Regular'),  # Medium banned
        ('BentonSansCond', 'medium', 'BentonSansCond-Regular'),
        ('BentonSansCond', '600', 'BentonSansCond-Bold'),
        ('BentonSansCond', '700', 'BentonSansCond-Bold'),
        ('BentonSansCond', 'bold', 'BentonSansCond-Bold'),
        ('BentonSansCond', '900', 'BentonSansCond-Black'),
        ('BentonSansCond', 'black', 'BentonSansCond-Black'),
        # Already suffixed — leave unchanged
        ('BentonSansCond-Light', '400', 'BentonSansCond-Light'),
        ('BentonSansCond-Regular', '700', 'BentonSansCond-Regular'),
        ('BentonSansCond-Bold', '300', 'BentonSansCond-Bold'),
        ('BentonSansCond-Black', '400', 'BentonSansCond-Black'),
        # Non-Benton untouched
        ('Arial', '300', 'Arial'),
        ('Segoe UI', '700', 'Segoe UI'),
    ]
    for family, weight, expected in cases:
        got = resolve_benton_cond_typeface(family, weight)
        _assert(got == expected, f'{family!r}+{weight!r} → {got!r}, want {expected!r}')

    # parse_font_family still returns first CSS face; mapping is separate
    fonts = parse_font_family(
        'BentonSansCond, Arial Narrow, Arial, sans-serif'
    )
    _assert(fonts['latin'] == 'BentonSansCond', fonts)
    mapped = resolve_benton_cond_typeface(fonts['latin'], '300')
    _assert(mapped == 'BentonSansCond-Light', mapped)

    fonts_light = parse_font_family(
        'BentonSansCond-Light, BentonSansCond, Arial Narrow, Arial, sans-serif'
    )
    _assert(fonts_light['latin'] == 'BentonSansCond-Light', fonts_light)
    mapped_light = resolve_benton_cond_typeface(fonts_light['latin'], '300')
    _assert(mapped_light == 'BentonSansCond-Light', mapped_light)

    print('OK: resolve_benton_cond_typeface mapping (%d cases)' % len(cases))


if __name__ == '__main__':
    main()
