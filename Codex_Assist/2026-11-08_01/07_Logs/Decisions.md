# Decisions

Updated: 8 November 2026. These decisions explain the actual working choices; they do not replace the user's latest instructions.

| Decision | Reason and scope |
| --- | --- |
| Use the actual D: workspace and `Codex_Assist/2026-11-08_01` inside the pack | The original handoff's Desktop path was stale. Outputs remain inside the authorized workspace and sources are preserved. |
| Parameter JSON is the geometry authority | A uses the supplied parameters; B uses its copied parameters with only width 520 mm and revision B changed. Direct native edits do not update that master automatically. |
| Save native Aspire `.crv3d` files | The extension was verified in the application's Save As dialog and the native jobs were saved by Aspire. VCarve `.crv` compatibility has not been established. |
| Retain Vectric tutorial provenance | R01/R02 are official learning examples, not original portfolio designs. Downloads include SOURCE.txt attribution. |
| Use R12 DXF working copies after the warm-up import failure | The supplied R2000 file was rejected. The compatibility comparison records preserved coordinates/layers/closure; originals were not repaired in place. |
| Keep nominal CAD joints and baseline final fit allowance at zero | Physical fit acceptance is absent. Coupon B allowance variants are separate CAM comparisons; no accepted variant has been selected. |
| Keep temporary finishing stock distinct from final fit allowance | The 0.15 mm separate last-pass radial allowance is temporary stock, not the final fit offset. |
| Use exact actual roughing increments | The first optimized warm-up list exceeded the intended 2 mm increment. Actual pass lists were checked and corrected. |
| Use job-local SIM_ONLY tools | Records practice values without overwriting existing real tool definitions. |
| Warm-up: 12.2 mm through depth, 5.08 mm clearance, 20.32 mm home Z | Additional virtual choices for 12 mm stock; not copied from the 28 mm stock settings. |
| Coupon A: 28.2 mm through depth, 15 mm clearance, 20.32 mm home Z | Matches the coupon practice depth/clearance; assumes a sacrificial spoilboard in the virtual exercise. |
| Keep tabs and entry away from mating curves | Warm-up has four edge-midpoint tabs; Coupon A has two on nonmating top/bottom edges. Coupon B00 has one tab on the top straight edge and one on the right straight edge. Automatic placement first put a tab on the curve; that tab was deleted. Board tabs belong in removable end waste when those jobs are created. |
| Coupon B00 used checked live profile fields rather than the saved template | The open profile form already carried the 28 mm session settings. Each field was read back. The binary template was not loaded, so template reuse is still unverified. |
| Save the representative profile template, then verify each reuse | The template exists, but loading/reusing it is pending. It does not establish the next part's selection or retention. |
| Pause CAD/CAM and add monitoring documents | The user requested a brief checkpoint, then durable teaching, failure/success, and continuation notes. The documentation update did not interact with Aspire. |
| Stop after Coupon B | The user finished the three Coupon B allowance jobs and stopped revision-A and revision-B. P01 and P02 remain as earlier saved jobs. The unsaved P03 draft was discarded. |

All cutting settings and retention concepts remain simulation only. Physical tests, machine-specific posting, and production release are `NOT_PERFORMED`. The original test-results working copy retains its unperformed measurements.
