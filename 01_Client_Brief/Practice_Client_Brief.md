# Practice Client Brief

**Client:** River Practice Workshop, a fictional woodworking shop. **Contractor:** Hassan and a woodworking/CNC collaborator. **Revision:** A. **Date:** 8 November 2026.

We want five separately machined hardwood components to assemble into a premium cutting board. The four flowing interfaces must fit with minimal hand fitting. Please build an editable VCarve workflow that our operator can understand and revise.

This original practice design was generated for training. It does not reproduce the actual client's product. The supplied job description establishes the 20 x 15 inch size, five maple/walnut pieces, editable VCarve deliverables, test support and machine-dependent posting. Everything below fills gaps for a simulated exercise.

## Product definition

- Finished plan dimensions: **508 x 381 mm** (20 x 15 in).
- Finished thickness: **25.4 mm**. Initial flat, parallel, planed blanks: **28.0 mm**.
- Five pieces, left to right: **P01 hard maple, P02 walnut, P03 hard maple, P04 walnut, P05 hard maple**.
- All grain runs parallel to the board's **381 mm direction**, the +Y axis. This is a face-grain board, not an end-grain board.
- The preassembly pieces include **3 mm external perimeter trim allowance**. Their combined untrimmed outline is **514 x 387 mm**. Joint curves remain nominal and shared.
- No juice groove, handle, engraving, dowel, biscuit, tongue or concealed fastener in the initial scope.
- After glue-up, flatten to final thickness, trim the perimeter and soften outside edges by the shop's manual process. No VCarve edge-rounding toolpath is required in this exercise.

## Assumed shop for simulation

- VCarve Pro **V12.5** reference interface. Save in a version confirmed with the receiving shop; do not assume a newer CRV opens in an older version.
- Hypothetical 3-axis router with at least **600 x 600 mm** XY travel, adequate Z clearance, a variable-speed spindle and a manual tool change. No real machine make, controller or post has been selected.
- Sacrificial spoilboard, stock datum stops and perimeter retention are available. The actual clamp geometry and clearances remain the operator's responsibility before cutting.
- T01 for simulation: **6.35 mm, two-flute, flat-ended carbide cutter**, sufficient cutting length for the stock. T02 for the warm-up: a **6 mm flat-ended cutter**. These are conceptual tool definitions, not confirmed purchases.
- The shop can plane stock, check moisture, measure tools, run test cuts, dry assemble, glue, clamp and flatten. Hassan handles the CAD/CAM workflow and documentation; the operator confirms physical cutting choices.

## Material and assembly assumptions

Use conditioned, sound stock, free from major defects in the joint areas. For this practice, record moisture readings with an **8 +/- 2 percent target**; this is an exercise assumption, not a universal material standard. All pieces should be acclimated together. Record actual moisture and stock flatness before testing.

Machine each piece from its own material blank. Keep parts retained until all joint-edge passes finish. Put any tabs on removable end waste, never on a final mating edge. Mark part ID, grain and reference face in pencil on the sacrificial stock. Dry assemble P01 through P05 with a common end datum. Use cauls and an end stop to resist sliding during glue-up. Use the shop's chosen woodworking adhesive and follow its instructions. After cure, flatten and finish the board using the shop's usual process. Adhesive selection, finish approval and consumer product qualification are outside this CAM exercise.

## Prototype acceptance for this exercise

- Nominal curves remain identical across each interface; fit adjustments are recorded as machining allowances, not untracked redraws.
- Coupon dry assembly closes under light hand pressure without hammering, splitting, burn marks or crushed fibers.
- Provisional joint check: a **0.10 mm feeler** should not enter the visible joint over most of its length under the agreed light pressure. Record local exceptions; this is a training target to discuss with the real client.
- Finished outer size: **508 +/- 0.5 x 381 +/- 0.5 mm**; thickness **25.4 +/- 0.3 mm**; diagonal difference **at most 1.0 mm**; flatness **at most 0.5 mm** under an agreed straightedge check. These are proposed practice criteria only.
- Repeat the accepted coupon setup on **three pairs** and record the spread. A clean simulation is not evidence of this physical repeatability.

## Deliverables and milestone boundary

1. Approved master vectors and annotated part/stock schedule.
2. One approved maple/walnut coupon strategy, then five editable native VCarve jobs.
3. Job sheets, previews, tool list, datum scheme, machining order and fit record.
4. Two defined test-cut revision rounds: round one for the coupon, round two for the full board. Extra design or machine changes require a revised scope.
5. Machine-specific posted code only after the actual machine, controller, post, tool and fixture are verified together.
6. A 3 to 5 minute recorded walkthrough and all editable sources.

For digital-only practice, stop after native projects and previews. Leave physical-test and machine-posting status as **not performed**.
