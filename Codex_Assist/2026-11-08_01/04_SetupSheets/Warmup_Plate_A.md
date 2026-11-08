# Warm-up plate

Status: SIMULATION_VERIFIED. Saved by Aspire 12.503, reopened, recalculated and previewed from reset stock.

Stock: 140 x 100 x 12 mm; single-sided; lower-left XY; top Z. Plate: 100 x 60 mm at (20,20); 10 mm holes at (40,50) and (100,50). Dimensions checked in Aspire.

Source: supplied warm-up DXF, coordinate-preserving R12 compatibility export (original Aspire import rejected at line 96). All four vector layers retained. Pocket selects only CUT_HOLE_1 and CUT_HOLE_2; profile selects only CUT_OUTER. REF_STOCK excluded from both stored selections.

Tool: job-local SIM_ONLY_T02_EndMill_6mm, 6 mm end mill, 2 flutes, number 2, 18000 rpm, feed 1800 mm/min, plunge 400 mm/min, stepover 2.4 mm. No tool database definitions overwritten.

Operations: holes pocket first, outside climb profile second. Start depth 0; through depth 12.2 mm (assumed sacrificial spoilboard). Actual pass list 2,4,6,8,10,12,12.2 mm. Profile fit allowance 0; separate full-depth last-pass radial stock 0.15 mm. Smooth 10 mm ramp at the top-left exterior start. Four 2D tabs at edge midpoints, length 12 mm, toolpath thickness 2.2 mm, nominal 2 mm remaining stock.

Clearance: 5.08 mm; home Z 20.32 mm. Warm-up-only virtual choices; clamp geometry unmodeled. Fixture strength, clearance and cutter usable length unverified.

App-generated sheet: Warmup_Plate_A_Summary.html. Any times in that sheet are software estimates, not measured cycle times. Physical cutting, fit measurements, operator acceptance and machine-specific posting: NOT_PERFORMED.
