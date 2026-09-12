# Image Generation Prompt Template — mblm-cinematic

Copy-paste into Image_Generator / Alumni image gen.

```text
Create a single 16:9 cinematic photographic still for an MBLM presentation.

SUBJECT: [who / what]
ACTION: [verb phrase]
LOCATION: [place / environment]
LIGHT: cool blue-teal base grade + ONE warm source ([low sun | neon | window | practical lamp]); backlight / rim preferred
MOTION: [subtle motion blur | deliberate stillness]
FACE: [profile | soft focus | obscured / silhouette] — never flat frontal smiling headshot
OPTICS: shallow depth of field, natural haze or soft flare OK
COMPOSITION: negative space for title overlay if cover/section; atmospheric, film-still, not corporate stock

NO: flat frontal office lighting, smiling LinkedIn headshots, handshake clichés, busy logo overlays in-frame, cartoon / illustration look

OUTPUT: one photoreal cinematic PNG, 16:9, suitable for full-bleed cover/section or framed content well.
```

## Short form (Alumni Prompt D style)

```text
Generate [N] 16:9 photographic stills for an MBLM deck about [TOPIC]:
- Cool blue-teal base + one warm backlight source
- Shallow DOF, haze/flare OK, faces in profile or obscured
- Mix motion blur and stillness
- Avoid smiling corporate headshots and flat frontal light

Shots needed:
1. Cover hero — [SCENE]
2. Section mood — [SCENE]
3. Closing — [SCENE]
```

## After generation

1. Save as `images/photo_<slug>.png` (and `projects/_host_images/` when used).
2. §VIII row: Acquire Via=`ai` or `user`; Type=Photography; Crop=`adaptive` (heroes); Purpose=cinematic photo.
3. Full-bleed OK on cover/section/closing with dark overlay; content slides prefer half-bleed / wells — see `IMAGES_GEN.md`.
