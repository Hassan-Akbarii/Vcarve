# Learning guide — the actual Aspire practice workflow

This guide explains the completed steps and the planned continuation. It records the settings used in this run; it is not evidence that an unfinished job exists. See [Progress](Progress.md) for completion status and [Action_Log](Action_Log.md) for successes and failures.

## 1. Understand the geometry before creating toolpaths

The revision-A finished board is 508 x 381 x 25.4 mm. Its pretrim assembly is 514 x 387 mm, and its starting material is 28 mm thick. The extra 3 mm on each outside edge is trim waste. Each of the five pieces uses its own stock blank; the shared curved joints stay nominal, with zero CAD gap.

Stock size, part size, and finished assembly size are different values. Enter the stock dimensions in Job Setup; import the correctly placed part outline without scaling it to the stock boundary. Each part's grain follows +Y.

Read the stock schedule, material identity, datum, and revision together. A correct-looking maple part imported into a walnut job or an outdated stock size is still an incorrect setup.

## 2. Start with a genuine native example — completed

R01 Welcome Sign was opened with File > Open as a whole job. That preserves its job setup, vectors, tools, and toolpaths. It uses inches: stock 11 x 6 x 0.755, lower-left XY and stock-top Z.

The exercise changed the pocket depth from 0.325 to 0.300 inches and named that path `Pocket_0.300in_Practice`. The native working copy was saved as `.crv3d`, recalculated, previewed, reopened, and checked again. The cutout operation was retained.

Compare the [before](../03_Previews_A/Tutorial_R01_Before.png) and [after](../03_Previews_A/Tutorial_R01_Edited_A.png) previews. A preview alone is weaker evidence than reopening the saved job and recalculating it.

R02 Garden Panel was inspected to study its sheets, layers, and profile organization. Both tutorials are Vectric learning materials and retain their attribution.

## 3. Set up and verify imported vectors — completed for warm-up and Coupon A

1. Create a single-sided job with the intended units, stock X/Y/thickness, lower-left XY datum, and stock-top Z datum.
2. Import the matching stock-layout DXF. In this run the original warm-up DXF failed; the R12 working copies preserved its coordinates and imported successfully.
3. Check measurable dimensions inside Aspire. For the warm-up, the part is 100 x 60 mm, lower-left (20,20), with two 10 mm holes at (40,50) and (100,50). Coupon A's outline bounding box is 98.088 x 120 mm within 140 x 160 mm stock.
4. Check placement using `REF_STOCK`. If alignment is needed, move the entire imported set consistently. Do not center the part by itself and lose its stock datum.
5. Inspect the intended closed `CUT_` outlines and select only those needed by the operation. A visible reference rectangle is useful for alignment, but it must not become a machining selection. Hiding a layer alone does not establish the contents of a stored toolpath selection.

The original geometry remains available. Compatibility exports changed DXF record format and line endings, not the joint coordinates.

## 4. Use a clearly named practice tool

| Setting | Warm-up T02 | Coupon A T01 / planned 28 mm jobs |
| --- | --- | --- |
| Diameter | 6.00 mm | 6.35 mm |
| Type / flutes | Flat end mill / 2 | Flat end mill / 2 |
| Spindle | 18000 rpm | 18000 rpm |
| Feed / plunge | 1800 / 400 mm/min | 1800 / 400 mm/min |
| Maximum roughing increment | 2.00 mm | 2.00 mm |
| Stepover | 2.40 mm, 40% | 2.54 mm, 40% |

These are the exercise's virtual settings. The job-local tools are named `SIM_ONLY_T02_EndMill_6mm` and `SIM_ONLY_T01_EndMill_6.35mm`; the existing real tool database was not overwritten.

Check tool units and feed units separately. Inspect the values after changing them; in the observed dialog, numeric edits could regenerate the tool name, so the final custom name was entered last.

## 5. Separate three different profile settings

| Concept | Purpose | This run |
| --- | --- | --- |
| Cutter compensation | Places the cutter center relative to the nominal vector and cutter radius | Outside profile; do not pre-offset the CAD by another tool radius |
| Separate last-pass radial allowance | Leaves temporary material for a later finishing pass | 0.15 mm; removed by the separate last pass |
| Final fit allowance | Changes the final retained part size relative to nominal | 0.000 mm for Coupon A and planned board jobs |

The planned Coupon B comparisons use final allowances 0.000, -0.025, and -0.050 mm. On the intended closed outside profile, the negative values reduce B's whole outline. They do not represent a measured seam gap or physical acceptance. Keep the original nominal vectors unchanged and record the exact CAM allowance per variant.

## 6. Check cut depths and the actual pass list

Warm-up stock is 12 mm thick; the virtual through-cut is 12.2 mm. The actual roughing depth sequence was set to **2, 4, 6, 8, 10, 12, 12.2 mm**. The separate profile finishing pass is additional.

Coupon A stock is 28 mm thick; its virtual through-cut is 28.2 mm. The roughing depths are **2, 4, …, 28, 28.2 mm**, giving 15 roughing passes, with a separate full-depth finishing pass.

Why inspect the list? The initial warm-up optimization distributed 12.2 mm across six 2.033 mm passes, despite a 2 mm tool pass-depth setting. Maintain exact tool pass depth was used and the generated list checked. Do not assume a nominal tool setting limits every optimized increment.

The extra 0.2 mm cuts into an assumed sacrificial spoilboard in simulation. Aspire's depth warning was reviewed for that specific cause. A different warning needs its own investigation.

## 7. Keep retention and entry away from mating edges

The warm-up pockets the holes first, then runs an outside climb profile. It has four tabs at straight-edge midpoints. Coupon A has two tabs on its nonmating top/bottom edges; its curved mating edge stays clear. Both use a smooth 10 mm ramp and an exterior start near the top-left region.

Tabs are 12 mm long and 2.2 mm thick in the toolpath settings. With a cut bottom 0.2 mm below stock, the nominal remaining stock at a tab is 2.0 mm. Inspect the preview rather than equating toolpath thickness directly with stock remaining.

For the unfinished board jobs, put tabs/entries in removable end waste, clear of joints. Template loading does not establish correct tab positions for a new part.

Warm-up clearance is 5.08 mm; Coupon A clearance is 15 mm. Home Z is 20.32 mm in both saved sheets. These are recorded virtual values; no clamp layout or physical retention test has been verified.

## 8. Calculate, preview, save, and verify persistence

For each job:

1. Inspect the selected machining outlines and exact settings.
2. Calculate all intended toolpaths; record and resolve errors, and document any specifically understood warning.
3. Reset the preview to fresh stock, then simulate the intended operation sequence.
4. Inspect the resulting shape, holes, tabs, mating edges, and retained material.
5. Use the native Save/Save As dialog and confirm the path and format. Explicit menu saves worked reliably in this session.
6. Reopen the saved native file. Confirm the stock, vectors, datums, tool definitions, and editable toolpath settings persist.
7. Recalculate and inspect a fresh preview again. Save changes and export matching evidence for the saved revision.
8. Update the setup sheet, action log, progress, and output index.

The tutorial and warm-up completed this sequence. Coupon A stops before the reopening check. The HTML setup-sheet times are application estimates, not measured cycle times.

## 9. Demonstrate a revision without losing the original — geometry complete, native CAM pending

Revision B changes finished width from 508 to 520 mm. Height remains 381 mm; the same 3 mm trim gives a 526 x 387 mm pretrim assembly. Only `finished_width_mm` and `revision` changed in the copied parameters.

The generator writes vectors and schedules into the chosen fresh output folder. It does not create native Aspire jobs. B's generated stock widths are 205, 140, 245, 145, and 205 mm; all stock lengths are 430 mm and thicknesses 28 mm.

When native work resumes, make B copies, use B's stock schedule and matching geometry, reselect the machining vectors, reposition tabs/entries as needed, recalculate every affected path, and repeat saved-file verification. Cached A toolpaths cannot establish the correctness of resized B geometry.

## 10. Recover from an interruption

Start with [Progress](Progress.md), then inspect the actual saved file and live app state. Determine whether the last action completed before repeating it. Historical command JSON records intent, while screenshots/state records and reopened native jobs establish what actually happened.

Update the action log after the recovery. Use `PENDING` for an unperformed check and `BLOCKED` only for a named obstacle. Physical tests, fit acceptance, machine-specific posting, and production release remain `NOT_PERFORMED` in this package.
