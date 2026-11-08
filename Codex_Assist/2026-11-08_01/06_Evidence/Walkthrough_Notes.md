# Short walkthrough using the actual completed files

Checkpoint: 8 November 2026. This outline takes approximately 3–5 minutes to present. It does not claim the unfinished board jobs are complete.

## 1. Show the journal and current checkpoint

Open [Progress](../07_Logs/Progress.md) and [Output_Index](../07_Logs/Output_Index.md). Explain that four native jobs exist and each has completed saved-file simulation verification. Coupon B at -0.025 mm and -0.050 mm, and the board jobs, are still to create.

## 2. Demonstrate the native tutorial edit

Show the R01 [before](../03_Previews_A/Tutorial_R01_Before.png) and [after](../03_Previews_A/Tutorial_R01_Edited_A.png) previews. Explain the pocket-depth change from 0.325 to 0.300 inches. Show the [recalculation evidence](028_reopen_recalculate.png) and [fresh preview after reopening](029_tutorial_verified.png). Credit Vectric for the tutorial.

## 3. Demonstrate the warm-up setup

Open the [setup note](../04_SetupSheets/Warmup_Plate_A.md) and [actual preview](../03_Previews_A/Warmup_Plate_A.png). Point out the 140 x 100 x 12 mm stock, 100 x 60 mm plate, two 10 mm holes, holes-first operation order, and tabs. Explain why the actual 2 mm pass increments were checked rather than assumed.

Show [reopened-job preview evidence](062_warmup_verified.png). Distinguish saved editable CAM from an exported picture.

## 4. Show Coupon A without overstating its status

Use its [setup note](../04_SetupSheets/Coupon_A_Maple_A.md), [preview](../03_Previews_A/Coupon_A_Maple_A.png), and [HTML job sheet](../04_SetupSheets/Coupon_A_Maple_A_Summary.html). Explain outside cutter compensation, temporary 0.15 mm last-pass stock, and zero final fit allowance.

Then show the three Coupon B jobs. [B00](../04_SetupSheets/Coupon_B_Walnut_B00_A.md) uses 0.000 mm, [B025](../04_SetupSheets/Coupon_B_Walnut_B025_A.md) uses -0.025 mm, and [B050](../04_SetupSheets/Coupon_B_Walnut_B050_A.md) uses -0.050 mm. The nominal vectors are the same. The mating curve is fully cut, and the two tabs sit on the straight edges. No variant has been chosen as a winning fit.

## 5. Explain the revision and remaining work

Show [B parameters](../05_Revision_B/parameters_B.json) and [manifest](../05_Revision_B/Generated/geometry_manifest.json): width changes from 508 to 520 mm; height remains 381 mm. These are regenerated geometry, not native board toolpaths.

Finish with the next action from Progress. Physical fit measurements, machining, operator acceptance, and machine-specific posting have not been performed. The [handoff checkpoint](../HANDOFF_STATUS.md) tells the next assistant how to continue.
