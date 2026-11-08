# P02 walnut — revision A

Status: **SIMULATION_VERIFIED**. Aspire 12.503 saved the job, then the saved file was closed and reopened on 8 November 2026. Name, zero final fit allowance, 28.2 mm depth, 0.15 mm last-pass stock, 15 passes, outside profile, and tabs matched this note. The expected through-cut warning was acknowledged. A reset-stock preview showed both long curves fully cut and one tab on each short end.

## Geometry and job setup

- Stock: 135 x 430 x 28 mm; single-sided; lower-left XY and stock-top Z. Grain follows +Y.
- Input: [R12 working DXF](../01_WorkingSources/Aspire_R12/03_CAD/P02_Walnut_Stock_Layout_mm.dxf).
- Machining outline: `CUT_P02_WALNUT` only. `REF_STOCK` and `REF_GRAIN` were hidden.
- Final fit allowance 0.000 mm. Nominal vectors were not offset.
- No fixture or clamp was modeled. Fixture clearance is incomplete.

## Recorded simulation settings

| Field | Value |
| --- | --- |
| Tool | Job-local SIM_ONLY_T01_EndMill_6.35mm; T01; flat end; 2 flutes |
| Spindle / feed / plunge | 18000 rpm / 1800 mm/min / 400 mm/min |
| Operation | RP_P02_Walnut_Outside_SIM_ONLY; outside climb profile |
| Start / cut depth | 0.00 / 28.20 mm; 15 exact 2 mm passes ending at 28.2 mm |
| Final fit allowance | 0.000 mm |
| Separate last-pass radial stock | 0.15 mm |
| Entry | Smooth 10 mm ramp |
| Tabs | Two; 12 mm length, 2.2 mm thickness; one on each short end, clear of both long curves |
| Clearance Z1 / plunge / home Z | 15.00 / 5.08 / 20.32 mm |

The through-cut is 0.2 mm below the stock bottom in the virtual setup and was acknowledged for the assumed sacrificial spoilboard.

## Saved artifacts

- [Native job](../02_Native_A/RP_P02_Walnut_A.crv3d)
- [Preview](../03_Previews_A/RP_P02_Walnut_A.png)
- [HTML job sheet](RP_P02_Walnut_A_Summary.html)
- Preview evidence: [246](../06_Evidence/246_p02_preview.png)
- Reopen: [255](../06_Evidence/255_p02_reopen_profile.png)

Physical machining, measured fit, and machine-specific posting: **NOT_PERFORMED**.
