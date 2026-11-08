# Progress

Updated: **8 November 2026** (Asia/Tehran), after Coupon B was finished and further board work was stopped.

## Current state

**Coupon B is complete.** All three walnut allowance jobs are saved and simulation-verified. Aspire has no open document. An unsaved P03 draft was closed without saving.

Native deliverables: **8 saved of 16 required; 8 fully simulation-verified.** The requested stop is before the remaining revision-A and all revision-B board jobs. P01 and P02 were already saved before that stop.

| Stage | Result | Status / next check |
| --- | --- | --- |
| Access and inventory | Local WSL files and actual Windows Aspire control established; source inventory created | `SOURCE_CHECKED`; all 53 original checksum entries matched again during this update |
| A — R01 tutorial | Pocket depth edited; native copy and before/after previews saved; reopened, recalculated, fresh preview checked | `SIMULATION_VERIFIED` |
| A — R02 tutorial | Whole Garden Panel job inspected | Inspection complete; source unchanged |
| B — Warm-up | Holes pocketed before outside profile; native job, preview, notes, and HTML sheet saved; reopened/recalculated/fresh-preview checked | `SIMULATION_VERIFIED` |
| C — Coupon A | Reopened saved job, settings matched, recalculated, reset-stock preview inspected, native file saved again | `SIMULATION_VERIFIED` |
| C — Coupon B00 | Nominal walnut coupon, 0.000 mm final fit allowance, reopened and previewed | `SIMULATION_VERIFIED` |
| C — Coupon B025 | Same vectors, final fit allowance -0.025 mm, reopened | `SIMULATION_VERIFIED` |
| C — Coupon B050 | Same vectors, final fit allowance -0.050 mm, reopened | `SIMULATION_VERIFIED` |
| D — Board A P01 | 200 x 430 maple, reopened and previewed | `SIMULATION_VERIFIED` |
| D — Board A P02 | 135 x 430 walnut, reopened and previewed | `SIMULATION_VERIFIED` |
| D — Board A P03–P05 | Stopped at the user's request. The unsaved P03 draft was discarded | `NOT_STARTED` |
| E — Geometry B | 520 mm parameters, regenerated geometry, stock schedule, and R12 working copies available | `SOURCE_CHECKED`; no B native jobs |
| E — Native B | Five updated part jobs required | `NOT_STARTED` |

R03 Backyard BBQ Sign is downloaded locally; opening/editing it has not been performed and is optional.

## First action when the user resumes Aspire work

Do not continue revision-A or revision-B unless the user asks. Coupon B is the finished scope of this request. P01 and P02 already exist and should not be recreated.

## Blockers and unresolved checks

- No unresolved application blocker was recorded at the last successful action. The pause is for user monitoring and documentation.
- The original warm-up DXF import failed at line/offset 96; coordinate-preserving R12 working copies imported successfully. The failed import is recorded, not counted as success.
- Earlier download/network issues were recovered; R01, R02, and R03 project files are present. This does not establish current network health.
- Coupon A and Coupon B00 have completed their reopening checks. The reusable profile template has been saved but has not yet been loaded into another job and verified. Coupon B00 was set by reading the live profile form, not by loading that template.
- Fixture/clamp validation, actual tool measurements, physical fit and acceptance, and VCarve compatibility remain unverified. Machine-specific posting and physical cutting are `NOT_PERFORMED`.

## Records

- [Action log](Action_Log.md): attempts, failures, recovery, evidence.
- [Output index](Output_Index.md): existing deliverables and their verification status.
- [Learning guide](Workflow_Guide.md): steps and setting explanations.
- [Handoff checkpoint](../HANDOFF_STATUS.md): resolved paths and continuation context.

This file replaces an earlier checkpoint that stopped at the warm-up; Coupon A had subsequently been saved in actions 063–076. The tutorial setup note was also corrected to reflect its already completed reopening verification.
