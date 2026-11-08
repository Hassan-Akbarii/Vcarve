# P01 maple — revision A

Status: **SIMULATION_VERIFIED**. Aspire 12.503 saved the job, then the saved file was closed and reopened on 8 November 2026. Stock settings, tool, depth, zero final fit allowance, last-pass stock, 15 passes, tabs, ramp, and clearance matched this note. Recalculation reported the expected 0.2 mm through-cut warning. A reset-stock preview showed the curved joint fully cut and one tab on each short end.

## Geometry and job setup

- Stock: 200 x 430 x 28 mm; single-sided; lower-left XY and stock-top Z. Grain follows +Y, so the 430 mm length is Y.
- Input: [R12 working DXF](../01_WorkingSources/Aspire_R12/03_CAD/P01_Maple_Stock_Layout_mm.dxf).
- Machining outline: `CUT_P01_MAPLE` only. `REF_STOCK` and `REF_GRAIN` were hidden before the profile was created.
- Final fit allowance 0.000 mm. Nominal vectors were not offset.
- No fixture or clamp was modeled. Fixture clearance is incomplete.

## Recorded simulation settings

| Field | Value |
| --- | --- |
| Tool | Job-local SIM_ONLY_T01_EndMill_6.35mm; T01; flat end; 2 flutes |
| Spindle / feed / plunge | 18000 rpm / 1800 mm/min / 400 mm/min |
| Stepover / roughing increment | 2.54 mm (40%) / maximum 2.00 mm |
| Operation | RP_P01_Maple_Outside_SIM_ONLY; outside climb profile |
| Start / cut depth | 0.00 / 28.20 mm |
| Roughing depth sequence | 2, 4, …, 28, 28.2 mm; 15 passes; exact tool pass depth |
| Final fit allowance | 0.000 mm |
| Separate last-pass radial stock | 0.15 mm |
| Entry | Smooth 10 mm ramp |
| Tabs | Two; 12 mm length, 2.2 mm toolpath thickness; one on each short end, clear of the curved joint |
| Clearance Z1 | 15.00 mm above stock |
| Plunge gap / home Z | 5.08 / 20.32 mm |

The through-cut is 0.2 mm below the stock bottom in the virtual setup. The depth warning was acknowledged for the assumed sacrificial spoilboard.

## Saved artifacts

- [Native job](../02_Native_A/RP_P01_Maple_A.crv3d)
- [Actual preview export](../03_Previews_A/RP_P01_Maple_A.png)
- [Aspire HTML job sheet](RP_P01_Maple_A_Summary.html)
- Preview: [215](../06_Evidence/215_p01_preview.png)
- Reopen field check: [224](../06_Evidence/224_p01_reopen_profile.png)

The HTML sheet is a software estimate, not a measured cycle time. Physical machining, measured fit, and machine-specific posting: **NOT_PERFORMED**.
