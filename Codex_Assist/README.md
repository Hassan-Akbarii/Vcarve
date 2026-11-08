# River Practice Board — work journal

This folder records the actual Aspire work, its results, failed attempts, and the next steps. Start here when reviewing the package or handing it to another assistant.

Updated: **8 November 2026** (Asia/Tehran).

## Current checkpoint

Run: [2026-11-08_01](2026-11-08_01/).

Coupon B is finished. The three walnut jobs, at final fit allowances of 0.000, -0.025, and -0.050 mm, are saved and simulation-verified, together with the tutorial, warm-up, and Coupon A. P01 and P02 were also saved before the user stopped the board work. Revision-A P03–P05 and all revision-B native jobs were not continued. The 520 mm geometry files exist, and no revision-B native job was created.

**Aspire has no open document.** The last saved Coupon B file is Coupon_B_Walnut_B050_A.

## Read these files

| File | Purpose |
| --- | --- |
| [Progress](2026-11-08_01/07_Logs/Progress.md) | Current stage, verified results, unfinished work, and the next action |
| [Action log](2026-11-08_01/07_Logs/Action_Log.md) | Successful and failed attempts, recovery, and evidence |
| [Workflow guide](2026-11-08_01/07_Logs/Workflow_Guide.md) | Learn the steps and the reasons for the main settings |
| [Output index](2026-11-08_01/07_Logs/Output_Index.md) | Open the saved native jobs, previews, and setup sheets |
| [Handoff checkpoint](2026-11-08_01/HANDOFF_STATUS.md) | Instructions and context for resuming on this or another computer |
| [Decisions](2026-11-08_01/07_Logs/Decisions.md) | Source authority, provisional settings, and the reasons for choices |
| [Walkthrough notes](2026-11-08_01/06_Evidence/Walkthrough_Notes.md) | A short demonstration using the completed files |

## What the statuses mean

| Status | Meaning |
| --- | --- |
| `SOURCE_CHECKED` | Source or generated geometry inspected; no claim of completed native CAM |
| `NATIVE_SAVED` | Saved by Aspire; the complete reopen/recalculate/preview check remains pending |
| `SIMULATION_VERIFIED` | Saved native job reopened, toolpaths recalculated, and a fresh preview inspected |
| `NOT_STARTED` / `PENDING` | Work or a particular check has not been done |
| `BLOCKED` | A named dependency prevents a step |
| `NOT_PERFORMED` | A physical test, measurement, posting, or approval has not occurred |

Simulation verification does not establish physical fit or a production setup. Machine-specific posting and physical cutting have not been performed.

## How to maintain these notes

After each meaningful action, add an entry to the action log: intent, action, observed result, outcome, evidence, and the next step. Record failures as well as successes; keep the failed attempt when adding its recovery. Update Progress at checkpoints and before an interruption. Update the output index and setup note whenever a saved job or its settings change.

Use actual observations. A command file records an attempted action; it does not prove that the application accepted it. A saved file does not prove that it reopens correctly. If an interruption prevents checking a result, record the uncertainty and verify it before repeating the action.

For transfer, keep this directory inside the full River_Practice_Pack so the relative links, source geometry, and tutorial attribution travel together. See the handoff checkpoint for path and desktop limitations.
