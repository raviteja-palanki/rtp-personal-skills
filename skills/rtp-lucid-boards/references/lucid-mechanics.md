# Lucid mechanics and delivery checks

Inspect the tools and current documentation available for the session. The original workflow named `lucid_edit_item`, `lucid_add_block`, and `lucid_export_document_as_PNG`; these are historical connector names, not calls to assume exist. No Lucid connector was available in the tool inventory during this editorial review. That does not establish what another session can access.

## Import and editing

Lucid Standard Import supports formatted text and defaults to automatic font scaling when no font size is provided. The old statement that import cannot set type size was too broad. Check the supported formatting and the resulting live shape. A custom `style.fontSize` field understood by a local drawing script is not automatically a valid Standard Import property. Likewise, a connector’s `font_size` or `auto_font_size` must follow that connector’s actual schema. [Standard Import reference](https://lucid.readme.io/v1.0/docs/reference-si).

Lucid has more than one API schema. Its custom-shape text style, for example, documents explicit point or pixel units; that does not make those exact fields valid in every importer. Confirm units in the interface being used and inspect the output. [Text-area documentation](https://lucid.readme.io/docs/textareas).

For Standard Import, retain the `.lucid` ZIP package with its `document.json` and any required data or images when reproducibility matters. Lucid warns that an unchanged import may render differently as the product evolves. Keep exported reference images and record later live edits instead of promising exact reconstruction from an old JSON alone. [Import overview](https://lucid.readme.io/docs/overview-si).

The September 2026 notes describe a disposed-Pipe error when editing some imported IDs. Treat it as an observed failure in that connector, not a universal rule. Fetch current IDs and inspect a small, reversible correction first. Preserve the source and relationships before recreating an affected shape. Do not delete every imported shape by default: IDs can participate in connections, groups, links, and other data.

For precise posters, disable assisted layout or automatic fitting when it overrides the intended geometry or text size. Verify that the chosen setting actually took effect. After edits, check tables and text colors in the export; a field’s intended color in JSON does not guarantee its rendered appearance.

## Export the actual document

Lucid’s current UI documents PDF, PNG, JPEG, and SVG export and local downloading. Available connector operations may be narrower. Choose the route that produces the needed artifact, then verify its page selection, crop, scale, and saved location. A missing PDF operation in one connector is not a product-wide lack of PDF export. [Lucid export help](https://help.lucid.co/hc/en-us/articles/16324571257492-Export-or-print-a-Lucid-document).

A genuine live export establishes what Lucid rendered. A local renderer establishes what that renderer produced. If a local reconstruction is necessary, label it, compare it against the live document where possible, and record any differences. Do not silently substitute it and claim it proves the imported board is readable.

The existing TAPMI helper is at `1_Projects/8_TAPMI_ai-for-management-2-course/2_session-notes/_tools/rasterize-print-boards.py`, relative to the Claude workspace. Its current implementation was read for this revision. It draws a subset of shape geometry with Pillow, uses pixel-sized fonts and role-based defaults, and does not implement the full Lucid renderer. Its defaults include a 20-pixel course label, not a verified 24-point minimum. It hardcodes session names, including an S03 path that does not match the discovered S07 discovery-board location. Inspect and scope it before any use; do not run it blindly over the teaching folders. This editorial task did not modify or regenerate existing boards.

## Verify scale at the destination

For a uniformly scaled raster image:

```text
effective pixels per inch = image width in pixels / placed width in inches
approximate final font em in points = font em in image pixels / effective pixels per inch × 72
```

Example: a 1920-pixel-wide image placed ten inches wide has 192 pixels per inch. Its 32-pixel font em prints at approximately 12 points. Increasing the raster resolution while preserving the same physical composition improves sharpness, not the physical text size. Actual visible letter height also depends on the font.

For a document with known physical source dimensions, multiply source point size by the scale factor. A 24-point label scaled to half its original size becomes 12 points. Check any additional scaling introduced by Word, slide placement, printer fit-to-page, margins, or export crop.

1920 × 1080 is a useful 16:9 projection starting canvas, not a required print format or a guarantee of print quality. Prefer a suitable vector export when available; otherwise choose sufficient raster resolution for the actual output and inspect it. A 300-PPI target can be useful for a raster print workflow, but tagging an inadequate image with 300 DPI does not create detail. A printer’s addressable DPI and an image’s effective PPI are different measures.

## Inspect what can fail

Read the whole asset at its intended size. Check clipping, missing glyphs, wrapping, field colors, stroke visibility, and alignment. Create and inspect an actual grayscale version for grayscale use, then a physical sample when the required use calls for one. Digital contrast calculations cannot reproduce every projector, photocopier, paper, or lighting condition.

Record the method: live export inspected, local reconstruction inspected, simulated scale checked, physical print checked, or actual classroom check. Do not collapse these into a generic “verified” label. Preserve the final asset’s identity and date with the review sheet so a later edit cannot inherit an unrelated pass.
