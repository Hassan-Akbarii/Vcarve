# Coupon B — walnut, final fit allowance -0.025 mm

Status: **SIMULATION_VERIFIED**. Aspire 12.503 saved this job from the verified 0.000 mm coupon, with the final fit allowance and toolpath name as the only intended changes. The saved file was closed and reopened on 8 November 2026. Allowance, depth, last-pass stock, tabs, ramp, tool, and clearance matched this note. Recalculation reported the expected 0.2 mm through-cut warning and then the reset-stock preview was inspected.

## Geometry and job setup

- Stock: 145 x 160 x 28 mm; single-sided; lower-left XY and stock-top Z.
- Input: the same [R12 working DXF](../01_WorkingSources/Aspire_R12/04_Joint_Test/Coupon_B_Walnut_Stock_mm.dxf) and the same nominal vectors as [Coupon B00](Coupon_B_Walnut_B00_A.md).
- Machining outline: `CUT_COUPON_B_WALNUT` only. Nominal vectors were not edited. The negative allowance is the profile final fit offset, so the toolpath sits 0.025 mm inside the whole outline.
- Grain follows +Y. No fixture or clamp was modeled. This preview does not choose a winning fit.

## Recorded simulation settings

| Field | Value |
| --- | --- |
| Tool | Job-local SIM_ONLY_T01_EndMill_6.35mm; T01; flat end; 2 flutes |
| Spindle / feed / plunge | 18000 rpm / 1800 mm/min / 400 mm/min |
| Stepover / roughing increment | 2.54 mm (40%) / maximum 2.00 mm |
| Operation | Coupon_B025_Nominal_Outside_SIM_ONLY; outside climb profile |
| Start / cut depth | 0.00 / 28.20 mm |
| Roughing depth sequence | 15 passes; exact tool pass depth, inherited from the verified B00 list |
| Final fit allowance | -0.025 mm |
| Separate last-pass radial stock | 0.15 mm |
| Entry | Smooth 10 mm ramp |
| Tabs | Two; 12 mm length, 2.2 mm toolpath thickness; top straight edge and right straight edge, clear of the mating curve |
| Clearance Z1 | 15.00 mm above stock |
| Plunge gap / home Z | 5.08 / 20.32 mm |

The through-cut is 0.2 mm below the stock bottom in the virtual setup. The depth warning was acknowledged for the assumed sacrificial spoilboard. Fixture clearance is incomplete because clamps were not modeled.

## Saved artifacts

- [Native job](../02_Native_A/Coupon_B_Walnut_B025_A.crv3d)
- [Actual preview export](../03_Previews_A/Coupon_B_Walnut_B025_A.png)
- [Aspire HTML job sheet](Coupon_B_Walnut_B025_A_Summary.html)
- Preview: [159](../06_Evidence/159_b025_preview.png)
- Reopen field check: [167](../06_Evidence/167_b025_reopen_profile.png)

The HTML sheet is a software estimate, not a measured cycle time. Physical machining, measured fit, accepted allowance, and machine-specific posting: **NOT_PERFORMED**.
