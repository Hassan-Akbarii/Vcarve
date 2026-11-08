# Handoff checkpoint — 8 November 2026

## Current state

Coupon B is finished. All three allowance jobs are saved and simulation-verified. The user then stopped revision-A and revision-B work. P01 and P02 already exist from before that stop. P03–P05 and the five revision-B native jobs were not continued, and an unsaved P03 draft was discarded.

The completed native files were saved by **Aspire 12.503**:

| Job | Status |
| --- | --- |
| Tutorial_R01_Edited_A | `SIMULATION_VERIFIED` |
| Warmup_Plate_A | `SIMULATION_VERIFIED` |
| Coupon_A_Maple_A | `SIMULATION_VERIFIED` |
| Coupon_B_Walnut_B00_A | `SIMULATION_VERIFIED` |
| Coupon_B_Walnut_B025_A | `SIMULATION_VERIFIED` |
| Coupon_B_Walnut_B050_A | `SIMULATION_VERIFIED` |

See [Progress](07_Logs/Progress.md) for the current checklist and [Output_Index](07_Logs/Output_Index.md) for links to the actual artifacts. Eight native files exist and are simulation-verified: the tutorial, warm-up, Coupon A, three Coupon B jobs, P01, and P02.

## First steps for another assistant

1. Read this checkpoint, Progress, the Action Log, and Decisions. Read the package's [original task handoff](../../LOCAL_CODEX_ASPIRE_HANDOFF.md) for the full exercise. The latest user instructions in the conversation govern the current scope.
2. Preserve existing outputs. Do not recreate verified jobs simply because the session changed.
3. When the user resumes the Aspire workflow, inspect the real application state before interacting. After the Coupon B checkpoint, Aspire had no open document.
4. Preserve any unrelated or unsaved work found in the application. Use the correct current window and dialog.
5. Do not recreate the verified tutorial, warm-up, Coupon A, or the three Coupon B jobs. Do not recreate P01 or P02.
6. Do not start revision-A P03–P05 or any revision-B native job unless the user asks. Coupon B is the finished scope of the latest request. If board work is resumed later, set the final fit allowance back to 0.000 mm; the last Coupon B profile used -0.050 mm.

## Resolved locations

The Desktop path in the original handoff was stale. The actual project used for this run is:

```text
Windows pack: D:\Projects\Upwork\Aspire-project\River_Practice_Pack
WSL pack:     /mnt/d/Projects/Upwork/Aspire-project/River_Practice_Pack
Run:          Codex_Assist/2026-11-08_01
Application:  C:\Program Files\Aspire 12.5\x64\Aspire.exe
```

Relative links are intended to remain usable after transfer. Resolve the new local pack root before opening files. Do not assume another assistant has local Windows access just because the files are available.

In this session, shell writes through the mixed-case current directory returned `Read-only file system`, while explicit absolute paths under the authorized lowercase root `/mnt/d/projects/upwork/aspire-project/river_practice_pack` worked. Both spellings reached the same project files. Use the environment's actual writable root; this recovery did not require broadening permissions. Git also reported five original CSV paths as modified before the documentation update, although all 53 supplied checksum entries matched. Do not reset unrelated working-tree changes.

## Geometry authority and working inputs

- Revision A authority: [original parameters](../../07_Automation/parameters.json), finished 508 x 381 mm, pretrim 514 x 387 mm, stock thickness 28 mm.
- Revision B authority: [parameters_B.json](05_Revision_B/parameters_B.json). Only `finished_width_mm` and `revision` differ from A: 520 mm and B. Generated files are under [Generated](05_Revision_B/Generated/).
- The B manifest reports finished dimensions 520 x 381 mm and zero finished-area error; pretrim is 526 x 387 mm. It reports geometry checks, not application simulation.
- Aspire rejected the original warm-up R2000 DXF. Use the coordinate-preserving [A compatibility copies](01_WorkingSources/Aspire_R12/) and [B compatibility copies](05_Revision_B/Aspire_R12/) as appropriate. See [the discrepancy record](00_Inventory/Source_Discrepancies.md). Do not overwrite the originals or scale/offset the nominal mating geometry to work around an import error.
- All 53 entries in the original checksum list matched again during the documentation update. The initial inventory and compatibility-export comparison remain under [00_Inventory](00_Inventory/).

## Native jobs

Coupon B is finished. It uses 145 x 160 x 28 mm stock and unchanged nominal vectors:

| Expected filename in 02_Native_A | Final fit allowance |
| --- | --- |
| Coupon_B_Walnut_B00_A.crv3d | 0.000 mm |
| Coupon_B_Walnut_B025_A.crv3d | -0.025 mm |
| Coupon_B_Walnut_B050_A.crv3d | -0.050 mm |

Those three Coupon B files are saved in `02_Native_A`. Board jobs below were not the current task. P01 and P02 revision-A files already exist. P03–P05 and every revision-B native file were not continued. Board jobs use lower-left XY, stock-top Z, grain +Y, and nominal final fit allowance 0.000 mm.

| Part/material | Revision-A stock, mm | Revision-B stock, mm | Expected native filenames |
| --- | --- | --- | --- |
| P01 maple | 200 x 430 x 28 | 205 x 430 x 28 | RP_P01_Maple_A.crv3d / RP_P01_Maple_B.crv3d |
| P02 walnut | 135 x 430 x 28 | 140 x 430 x 28 | RP_P02_Walnut_A.crv3d / RP_P02_Walnut_B.crv3d |
| P03 maple | 240 x 430 x 28 | 245 x 430 x 28 | RP_P03_Maple_A.crv3d / RP_P03_Maple_B.crv3d |
| P04 walnut | 140 x 430 x 28 | 145 x 430 x 28 | RP_P04_Walnut_A.crv3d / RP_P04_Walnut_B.crv3d |
| P05 maple | 205 x 430 x 28 | 205 x 430 x 28 | RP_P05_Maple_A.crv3d / RP_P05_Maple_B.crv3d |

A native jobs belong in `02_Native_A`; B native jobs belong in the planned `05_Revision_B/Native` directory. Read stock sizes from the matching manifest when creating each job.

## Desktop access and recovery knowledge

The previous session ran in local WSL/bash and controlled the Windows Aspire UI through the project-local [PowerShell helper](07_Logs/aspire_desktop.ps1). It uses Windows window/control inspection, input events, screenshots, and saved JSON states. Running Windows PowerShell required the environment's approved execution escalation. A future session must establish its own available capabilities and comply with its approval controls.

The helper accepts a `-CommandFile` containing JSON. Existing inputs are in [commands](07_Logs/commands/); screenshot/state pairs are in [06_Evidence](06_Evidence/) and [07_Logs](07_Logs/). The highest existing action number is **151**. Use a new unique name for later evidence. State JSON written by Windows PowerShell has a UTF-8 BOM; Python readers should use `encoding='utf-8-sig'`.

Do not replay old command batches blindly. They contain absolute paths, historical coordinates, and sometimes transient window handles. Window size, DPI, dialogs, selection, and current job must be re-observed. The helper focuses the application even when collecting an empty-action snapshot. Inspect its implementation before reuse. Its current process selection also assumes one intended Aspire instance; resolve any ambiguity if several instances are open.

Known recovered issues:

- Per-monitor DPI awareness was needed to align screenshots and clicks.
- Aspire's file picker can run as its own `SandboxedFileDialog.exe`; the helper recognizes the exact Aspire executable path. Unrelated foreground processes remain grounds to stop input.
- Modal dialogs need focus through the active popup. A process title such as `XTPFrameShadow`, or an empty title, was not a reliable document identity; consult the screenshot and real main window.
- `Ctrl+Shift+S` did not provide the required Save As action in the observed UI. Explicit File > Save As worked. Explicit File > Save was also more reliable than assuming a keypress had saved the active job.
- Tool units and feed units needed separate checks; automatic tool-name updates could replace a custom name during editing. Set the final practice name after the numeric fields, then inspect the result.
- Pass optimization could exceed the intended 2 mm increment. Inspect the actual pass list and the Maintain exact tool pass depth option.

See [Action_Log](07_Logs/Action_Log.md) for evidence and remaining uncertainty. Earlier network/download trouble was recovered: R01, R02, and optional R03 files are now local. No fresh network or desktop test was performed while writing these notes.

## Delivery limits and transfer

No physical machining, measured fit, repeatability test, operator acceptance, machine-specific posting, or production release has been performed. The practice feeds, depths, tabs, and clearance are simulation choices. An accepted coupon variant has not been chosen.

Native output is Aspire `.crv3d`; compatibility with a receiving VCarve installation has not been verified. Official tutorial files retain Vectric attribution and their SOURCE.txt records. Include the full pack, this run, previews, setup sheets, and source/license records when transferring the package.
