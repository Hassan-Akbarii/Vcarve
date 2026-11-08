# Coupon B — walnut, final fit allowance 0.000 mm

Status: **SIMULATION_VERIFIED**. Aspire 12.503 saved the job, then the saved file was closed and reopened on 8 November 2026. Stock thickness, datums, tool, depth, allowances, pass count, tabs, ramp, and clearance matched this note. Recalculation reported the expected 0.2 mm through-cut warning and then succeeded. A reset-stock preview showed the outside profile, a fully cut mating curve, and two tabs on straight edges.

## Geometry and job setup

- Stock: 145 x 160 x 28 mm; single-sided; lower-left XY and stock-top Z.
- Input: [R12 working DXF](../01_WorkingSources/Aspire_R12/04_Joint_Test/Coupon_B_Walnut_Stock_mm.dxf), derived from the unchanged nominal source.
- Machining outline: `CUT_COUPON_B_WALNUT` only. `REF_STOCK` was hidden before the profile was created and was not selected.
- Nominal vectors were not offset. The 0.000 mm value is the profile final fit allowance.
- Grain follows +Y. No fixture or clamp was modeled.

## Recorded simulation settings

| Field | Value |
| --- | --- |
| Tool | Job-local SIM_ONLY_T01_EndMill_6.35mm; T01; flat end; 2 flutes |
| Spindle / feed / plunge | 18000 rpm / 1800 mm/min / 400 mm/min |
| Stepover / roughing increment | 2.54 mm (40%) / maximum 2.00 mm |
| Operation | Coupon_B00_Nominal_Outside_SIM_ONLY; outside climb profile |
| Start / cut depth | 0.00 / 28.20 mm |
| Roughing depth sequence | 2, 4, …, 28, 28.2 mm; 15 passes; exact tool pass depth |
| Final fit allowance | 0.000 mm |
| Separate last-pass radial stock | 0.15 mm |
| Entry | Smooth 10 mm ramp |
| Tabs | Two; 12 mm length, 2.2 mm toolpath thickness. One on the top straight edge and one on the right straight edge, both clear of the mating curve |
| Clearance Z1 | 15.00 mm above stock |
| Plunge gap / home Z | 5.08 / 20.32 mm |

Automatic tab placement first put one tab on the mating curve. That tab was deleted and a tab was added on the top straight edge. The right-edge tab was left in place. The reset-stock preview shows both remaining tabs off the curve.

The through-cut is 0.2 mm below the stock bottom in the virtual setup. The depth warning was acknowledged for the assumed sacrificial spoilboard. Fixture clearance is incomplete because clamps were not modeled.

The profile form was filled from the live session values and each field was read back. The saved profile template was not loaded into this job, so template reuse is still unverified.

## Saved artifacts

- [Native job](../02_Native_A/Coupon_B_Walnut_B00_A.crv3d)
- [Actual preview export](../03_Previews_A/Coupon_B_Walnut_B00_A.png)
- [Aspire HTML job sheet](Coupon_B_Walnut_B00_A_Summary.html)
- Preview: [128](../06_Evidence/128_preview.png)
- Reopen and field check: [142](../06_Evidence/142_reopen.png), [147](../06_Evidence/147_edit_saved.png)
- Saved after that check: [151](../06_Evidence/151_save_reopen.png)

The HTML sheet reports a software time estimate of 00:08:17. That is not a measured cycle time. Physical machining, measured fit, accepted allowance, and machine-specific posting: **NOT_PERFORMED**. This preview does not choose a winning fit.
