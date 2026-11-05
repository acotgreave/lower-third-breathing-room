# Lower Third Breathing Room

A How To Speak Data design study, live at **https://2026midterms.howtospeakdata.com**.

CNN's 2026 midterms election-night lower third packs every number right up against its box. This page rebuilds that graphic in HTML on top of a broadcast screenshot so you can experiment with it:

- **Padding**: adds space around the numbers in the Senate, House and Montana panels. The graphic stays at its aired size (1776 × 329px on a 1080p frame), so the type shrinks to make room. Breaking News, the headline and Live never change.
- **Montana borders**: fades the heavy black rules from black to none.
- **Text case**: ALL CAPS (as aired) or mixed case.
- **Show original**: switches back to the aired graphic for comparison.

## Files

- `index.html`: the built, self-contained page that GitHub Pages serves.
- `src/page.html`: the editable page. `__IMG__` marks where the screenshot goes.
- `src/cnn-election-night.webp`: the broadcast screenshot.
- `build.py`: rebuilds `index.html` from `src/`. Run `python build.py` after editing.
- `CNAME`: the custom domain for GitHub Pages.

The screenshot is from CNN's broadcast and is used here for commentary on design.
