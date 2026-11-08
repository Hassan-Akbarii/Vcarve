# Validation Report

Date: 8 November 2026. Status: geometry checked; VCarve import and CAM not performed here.

## Checks passed

- Finished assembly extent: 508 x 381 mm.
- Sum of five finished component areas: 193548.000 square mm; numerical area error below 0.000001 square mm.
- Sum of five pretrim component areas: 198918.000 square mm; outer extent 514 x 387 mm.
- Shared nominal edges reuse identical sampled coordinates in adjoining parts.
- All parts remain separate and ordered along the length; no crossing interfaces.
- Maximum sampled chord deviation from the original cubic curves: 0.000328 mm, measured on a dense evaluation grid.
- Minimum sampled interior boundary radius: 114.055 mm, compared with 3.175 mm simulation cutter radius. External corners are not part of this curvature check.
- Independent DXF reader parsed 11 files; all use millimetres and all CUT layers contain closed contours. Zero audit errors or repairs.
- Stock-layout coordinate translations reconstruct each source part within 0.0000011 mm rounding tolerance. At least 20 mm nominal stock margin surrounds every board part.
- All SVGs parse as XML; optional exact Bezier master is included.
- The 520 x 381 mm revision exercise regenerates successfully into a new output folder and preserves the supplied 508 mm revision.
- Official sample downloader was run against the three live URLs: three real CRV files retrieved; posted machine files excluded. These downloaded third-party files are not redistributed inside the pack.
- PDF files contain readable text inside the page boundaries. Their rendered pages were also visually inspected.

## Limits of this validation

Numerical precision is not achievable wood machining tolerance. No VCarve desktop application was available for import, native-file creation or toolpath calculation. No custom board CRV, G-code, machine cut, physical test, cycle-time result or acceptance record has been created. Cutter loading, fixture design, actual tool geometry, wood behavior and machine/controller compatibility require shop validation.

## Files parsed

- Master_Finished_Assembly_mm.dxf: 5 entities
- Master_Pretrim_Assembly_mm.dxf: 5 entities
- P01_Maple_Stock_Layout_mm.dxf: 3 entities
- P02_Walnut_Stock_Layout_mm.dxf: 3 entities
- P03_Maple_Stock_Layout_mm.dxf: 3 entities
- P04_Walnut_Stock_Layout_mm.dxf: 3 entities
- P05_Maple_Stock_Layout_mm.dxf: 3 entities
- Warmup_Plate_Stock_mm.dxf: 4 entities
- Coupon_A_Maple_Stock_mm.dxf: 2 entities
- Coupon_Assembly_mm.dxf: 2 entities
- Coupon_B_Walnut_Stock_mm.dxf: 2 entities

PDFs: 00_Start_Here.pdf (8 pages), Drawing_Set.pdf (3 pages).
