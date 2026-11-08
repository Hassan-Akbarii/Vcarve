# Output index

Checkpoint: **8 November 2026**. This index lists actual saved outputs, not planned files. CSV paths are relative to the run folder.

**8 native jobs saved; 8 fully simulation-verified; 8 required native jobs still to create.** See [Progress](Progress.md) and the [handoff](../HANDOFF_STATUS.md) for unfinished work.

## Native jobs

| Native file | Bytes on disk | Actual Aspire preview | Setup note | Verification |
| --- | ---: | --- | --- | --- |
| [Tutorial_R01_Edited_A.crv3d](../02_Native_A/Tutorial_R01_Edited_A.crv3d) | 2,585,600 | [Preview](../03_Previews_A/Tutorial_R01_Edited_A.png) | [Settings](../04_SetupSheets/Tutorial_R01_Edited_A.md) | `SIMULATION_VERIFIED` |
| [Warmup_Plate_A.crv3d](../02_Native_A/Warmup_Plate_A.crv3d) | 108,544 | [Preview](../03_Previews_A/Warmup_Plate_A.png) | [Settings](../04_SetupSheets/Warmup_Plate_A.md) | `SIMULATION_VERIFIED` |
| [Coupon_A_Maple_A.crv3d](../02_Native_A/Coupon_A_Maple_A.crv3d) | 267,776 | [Preview](../03_Previews_A/Coupon_A_Maple_A.png) | [Settings](../04_SetupSheets/Coupon_A_Maple_A.md) | `SIMULATION_VERIFIED` |
| [Coupon_B_Walnut_B00_A.crv3d](../02_Native_A/Coupon_B_Walnut_B00_A.crv3d) | 280,576 | [Preview](../03_Previews_A/Coupon_B_Walnut_B00_A.png) | [Settings](../04_SetupSheets/Coupon_B_Walnut_B00_A.md) | `SIMULATION_VERIFIED` |
| [Coupon_B_Walnut_B025_A.crv3d](../02_Native_A/Coupon_B_Walnut_B025_A.crv3d) | 279,040 | [Preview](../03_Previews_A/Coupon_B_Walnut_B025_A.png) | [Settings](../04_SetupSheets/Coupon_B_Walnut_B025_A.md) | `SIMULATION_VERIFIED` |
| [Coupon_B_Walnut_B050_A.crv3d](../02_Native_A/Coupon_B_Walnut_B050_A.crv3d) | 279,552 | [Preview](../03_Previews_A/Coupon_B_Walnut_B050_A.png) | [Settings](../04_SetupSheets/Coupon_B_Walnut_B050_A.md) | `SIMULATION_VERIFIED` |
| [RP_P01_Maple_A.crv3d](../02_Native_A/RP_P01_Maple_A.crv3d) | 1,128,960 | [Preview](../03_Previews_A/RP_P01_Maple_A.png) | [Settings](../04_SetupSheets/RP_P01_Maple_A.md) | `SIMULATION_VERIFIED` |
| [RP_P02_Walnut_A.crv3d](../02_Native_A/RP_P02_Walnut_A.crv3d) | 1,135,616 | [Preview](../03_Previews_A/RP_P02_Walnut_A.png) | [Settings](../04_SetupSheets/RP_P02_Walnut_A.md) | `SIMULATION_VERIFIED` |

The [CSV index](Output_Index.csv) contains exact source paths, application version, stock sizes, allowances, and statuses. Tutorial stock is actually in inches; CSV stock columns are converted to millimetres for the common schema. Blank tutorial allowance fields mean unrecorded, not zero. Physical-test status is `NOT_PERFORMED` for every row.

## Supporting outputs

| Artifact | Location / scope |
| --- | --- |
| Tutorial before preview | [Tutorial_R01_Before.png](../03_Previews_A/Tutorial_R01_Before.png) |
| Warm-up Aspire job sheet | [Warmup_Plate_A_Summary.html](../04_SetupSheets/Warmup_Plate_A_Summary.html) |
| Coupon A Aspire job sheet | [Coupon_A_Maple_A_Summary.html](../04_SetupSheets/Coupon_A_Maple_A_Summary.html) |
| Coupon B00 Aspire job sheet | [Coupon_B_Walnut_B00_A_Summary.html](../04_SetupSheets/Coupon_B_Walnut_B00_A_Summary.html) |
| Native profile template | [SIM_ONLY_Outside_Profile_28mm.ToolpathTemplate](../04_SetupSheets/SIM_ONLY_Outside_Profile_28mm.ToolpathTemplate); saved, reuse check pending |
| Revision-B parameters | [parameters_B.json](../05_Revision_B/parameters_B.json); finished width 520 mm |
| Revision-B vectors and schedule | [Generated](../05_Revision_B/Generated/); DXF/SVG, manifest, stock CSV; no native CAM |
| A compatibility DXFs | [Aspire_R12](../01_WorkingSources/Aspire_R12/) |
| B compatibility DXFs | [Aspire_R12](../05_Revision_B/Aspire_R12/) |
| Compatibility comparison | [DXF_Compatibility_Exports.json](../00_Inventory/DXF_Compatibility_Exports.json); 22 exports |
| Initial source inventory | [Source_Inventory.json](../00_Inventory/Source_Inventory.json); 55 entries |
| Supplied checksum results | [Checksum_Check.json](../00_Inventory/Checksum_Check.json); 53 entries, all matched again during the documentation update |
| Drawing review | [Page 1](../00_Inventory/Drawing_Page_1.png), [page 2](../00_Inventory/Drawing_Page_2.png), [page 3](../00_Inventory/Drawing_Page_3.png) |
| Official tutorial inputs | [Downloads](../01_WorkingSources/08_Free_Samples/Official_Downloads/); R01, R02, R03 and SOURCE.txt attribution; R03 exercise not performed |
| Actual app evidence | [Screenshots](../06_Evidence/) and [numbered JSON states](./); highest recorded action 151 |
| Desktop helper / attempted commands | [aspire_desktop.ps1](aspire_desktop.ps1), [commands](commands/); historical inputs require fresh UI and path checks |
| Physical-test working record | [Test_Results.csv](Test_Results.csv); measurements unperformed |
| Revision working record | [Revision_Log.csv](Revision_Log.csv); distinguishes geometry from CAM |

## Not delivered yet

- Revision-A P03, P04, and P05, and all five revision-B native jobs. Coupon B is complete. P01 and P02 are already saved. Further board work was stopped at the user's request.
- Profile-template reuse check. Coupon A and Coupon B00 reopening checks are complete.
- Physical cutting, measured fit, repeatability, operator acceptance, machine-specific code, and verified VCarve compatibility.

## Maintaining the index

Add a CSV row and a Markdown row after each new native file is actually saved. Update both when settings or verification status change. Link the matching source revision, preview, and setup record. Do not list an expected native filename as an existing deliverable.
