# Coupon A — maple nominal baseline

Status: **SIMULATION_VERIFIED**. Aspire 12.503 reopened the saved job on 8 November 2026. Stock, datums, tool, depth, allowances, pass list, tabs, and clearance matched this note. All toolpaths recalculated. The expected 0.2 mm through-cut warning was acknowledged. A reset-stock preview showed the outside profile and two tabs on the non-mating edges. The native file was saved again.

## Geometry and job setup

- Stock: 140 x 160 x 28 mm; single-sided; lower-left XY and stock-top Z.
- Input: [R12 working DXF](../01_WorkingSources/Aspire_R12/04_Joint_Test/Coupon_A_Maple_Stock_mm.dxf), derived from the unchanged nominal source.
- Machining outline: `CUT_COUPON_A_MAPLE` only. Reference stock is excluded from the profile selection.
- Outline extents checked in Aspire: 98.088 x 120 mm. The coupon uses the middle 120 mm of J12 at full scale.
- Stock placement retained. Grain follows +Y.

## Recorded simulation settings

| Field | Value |
| --- | --- |
| Tool | Job-local SIM_ONLY_T01_EndMill_6.35mm; T01; flat end; 2 flutes |
| Spindle / feed / plunge | 18000 rpm / 1800 mm/min / 400 mm/min |
| Stepover / roughing increment | 2.54 mm (40%) / maximum 2.00 mm |
| Operation | Coupon_A_Nominal_Outside_SIM_ONLY; outside climb profile |
| Start / cut depth | 0.00 / 28.20 mm |
| Roughing depth sequence | 2, 4, …, 28, 28.2 mm; 15 passes |
| Final fit allowance | 0.000 mm |
| Separate last-pass radial stock | 0.15 mm; separate full-depth finishing pass |
| Entry | Smooth 10 mm ramp, exterior start near top-left; clear of mating curve |
| Tabs | Two on nonmating top/bottom straight edges; 12 mm length, 2.2 mm toolpath thickness; nominal 2 mm stock remaining |
| Clearance Z1 | 15.00 mm above stock |
| Plunge gap / home Z | 5.08 / 20.32 mm |

The through-cut is 0.2 mm below the stock bottom in the virtual setup. Its associated depth warning was acknowledged for the assumed sacrificial spoilboard. No fixture/clamp model or physical test validates these values.

## Saved artifacts and next check

- [Native job](../02_Native_A/Coupon_A_Maple_A.crv3d)
- [Actual preview export](../03_Previews_A/Coupon_A_Maple_A.png)
- [Aspire HTML job sheet](Coupon_A_Maple_A_Summary.html)
- [Saved profile template](SIM_ONLY_Outside_Profile_28mm.ToolpathTemplate) — reuse verification pending
- [Final recorded saved state](../06_Evidence/076_coupon_template_sheet.png)

Reopen evidence: [077](../06_Evidence/077_coupon_a_reopen.png), [081 profile](../06_Evidence/081_coupon_a_profile_edit.png), [083 pass list](../06_Evidence/083_coupon_a_pass_end.png), [091 preview](../06_Evidence/091_coupon_a_preview_run.png), [094 saved](../06_Evidence/094_coupon_a_save_native.png).

Software time estimates are not measured cycle times. Physical machining, measured fit, accepted allowance, repeatability, operator acceptance, and machine-specific posting: **NOT_PERFORMED**.
