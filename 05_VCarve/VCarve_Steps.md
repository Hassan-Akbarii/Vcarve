# VCarve Practice Steps

Reference interface: VCarve Pro V12.5. Names and panel positions can differ between versions. This is a suggested lab, not a claim that the files have been opened or cut in VCarve here.

## Session 1 Inspect a real native file

Open 08_Free_Samples/Native_Samples_and_Tutorials.html. Download R01 and open **Welcome Sign.crv** with **File > Open**. Save a working copy. Inspect job dimensions, units, Z datum, tool list, geometry layers and existing toolpaths. Play its preview. Change one noncritical design feature, recalculate and preview again. Undo or save a new revision. Watch R02 before the board exercise. Your ArtCAM experience transfers conceptually to stock, tools, profiles and simulation; first learn VCarve's job/sheet structure and selection behavior.

## Session 2 Warm up with a simple DXF

1. Create a single-sided job in millimetres, **140 x 100 x 12 mm**. XY datum is the lower-left stock corner. Z zero is the top surface.
2. Import **03_CAD/Warmup_Plate_Stock_mm.dxf** as vectors, keeping its original position. The outer part must measure **100 x 60 mm**, its bottom-left must be **20,20**, and both holes must be **10 mm diameter**, centered at **40,50** and **100,50**.
3. If import centers or moves the vectors, reposition the complete imported group by matching the REF_STOCK rectangle to the 140 x 100 job boundary. Never center only the CUT layers. Hide REF_STOCK afterward.
4. Set up a 6 mm flat cutter for simulation. Pocket the two holes first, then profile the outer rectangle on its outside. Avoid selecting the stock rectangle.
5. Preview all operations. Save **Warmup_Plate_A.crv**. Export or capture a preview. This is only a familiarization exercise; no real machining is required.

## Session 3 Build the joint coupon jobs

Import each coupon into its own job. Read exact stock XY from 03_CAD/geometry_manifest.json; both use **28 mm stock thickness**. Open each **...Stock_mm.dxf** from 04_Joint_Test, preserve coordinates and check REF_STOCK against the job boundary. The assembled coupon reference is **160 x 120 mm**. Do not use the assembled drawing for one common-line cut.

Select the closed **CUT_COUPON_A_MAPLE** outline only for A; select **CUT_COUPON_B_WALNUT** only for B. Baseline profiles follow each outline on the **outside**. VCarve handles cutter radius from the tool definition: do not add another half-tool offset to the CAD. Keep both CAD edges nominal.

For initial simulation, use the parameter table below. Add a light finishing pass and inspect the remaining material. Put starts, ramps and any tabs on non-mating or sacrificial areas. Exact tab count, retention method, final-pass loading and clamp clearances must be agreed with the actual operator before a physical cut.

| Field | Simulation exercise value |
|---|---|
| T01 diameter and flutes | 6.35 mm, 2 flutes, flat end |
| Stock thickness | 28.00 mm |
| Start depth | 0.00 mm |
| Through-cut depth | 28.20 mm, assuming a sacrificial spoilboard |
| Maximum stepdown for the lab | 2.00 mm; inspect the actual pass list |
| Spindle | 18000 rpm |
| Feed | 1800 mm/min |
| Plunge | 400 mm/min |
| Entry | Ramped entry in waste, outside fixture keep-outs |
| Baseline fit allowance | 0.000 mm |
| Separate last-pass allowance | 0.15 mm radial, for simulation review |
| Simulation safe clearance | 15 mm above stock; use the real fixture clearance before cutting |
| Example tabs | 12 mm length x 2.2 mm toolpath tab thickness; 2.0 mm stock remains with the stated 28.2 mm cut depth |

These numbers fill the virtual scenario; they are **not verified cutting recommendations**. The calculated feed corresponds to 0.05 mm/tooth at 18000 rpm and two flutes. Confirm the actual cutter maker's data, flute length, stock, machine stiffness, chip evacuation and retention before adopting any value. A full-depth last pass engages the whole edge height; do not assume its load is safe merely because the roughing stepdown is small. Tab height is referenced to cut depth in VCarve, so check the remaining stock in the preview.

Save A as **Coupon_A_Maple_A.crv**. Save three B variants: **B00** with final allowance 0, **B025** with -0.025 mm, **B050** with -0.050 mm. For an outside closed profile, a negative allowance makes the part smaller. With A nominal, the intended seam clearance changes by approximately the selected radial amount, not the cutter radius. The whole B outline is affected in this simple test. These three offsets are a comparison experiment, not three guaranteed good glue joints. Keep an unchanged nominal CAD copy.

## Session 4 Build five board jobs

1. Open **03_CAD/Stock_and_Parts.csv**. Create one single-sided job per part using its stock dimensions and **28 mm Z thickness**. All stock length directions are +Y.
2. Import the matching **P01...P05...Stock_Layout_mm.dxf**. Keep the existing placement. Match REF_STOCK to the job boundary if import changes it. Record that all parts have at least 20 mm design margin before physical fixtures are added.
3. Use **CUT_Pxx_MATERIAL** only. Hide REF_STOCK and REF_GRAIN. Check one closed contour, no accidental mirror, correct ID/material, no open or duplicated vector inside that job.
4. Set up and preview the nominal outside profile. The stock layout represents the **pretrim component**, not the finished board perimeter. Use the accepted coupon process only after a real test; otherwise retain zero allowance and label the result simulation-only.
5. Keep tab locations on the two 3 mm end-trim strips and out of all four glue interfaces. Check every entry, exit, clamp zone and tool reach with the operator. Change the fixture rather than sanding a tab from an accurate joint edge.
6. Save separate files such as **RP_P01_Maple_A.crv** through **RP_P05_Maple_A.crv**. One job per part is the beginner route. Multi-sheet projects can be introduced once the setup is understood.
7. Create a VCarve job sheet for each saved job. Add the part ID, grain arrow, retention method, fixture photo/sketch, tool ID, setup owner, revision and test status using 06_Templates/Setup_Sheet.md.
8. Capture your own previews. A CAD rendering supplied in this pack is not a VCarve toolpath preview.

## Session 5 Practise a client change

Request: increase finished width from 508 to **520 mm**, retaining 381 mm height and five-part material order. First make a copy of the parameter JSON. Set finished_width_mm to 520 and revision to B, then generate a new output directory. Check the new master assembly measures 520 x 381 and regenerate all stock schedules.

Import the updated part vectors into copies of the native jobs; remove or archive the superseded geometry. Reapply the appropriate toolpath template or reselect geometry and recalculate. Check stock, vector links, tabs and all previews again. Do not assume cached toolpaths follow the imported revision automatically. Save revision B, a new setup sheet and a short change log.

Alternatively, practise a manual node edit in a copy of the VCarve master. Update both sides of the shared boundary from the same edited curve. Do not edit mating outlines independently. Choose one authoritative master route for each revision.

## Session 6 Define the real posting milestone

The custom exercise stops before machine posting. Before release, confirm exact machine/controller, installed VCarve version, post processor, units, tool-change behavior, spindle commands, datum, safe heights, tool library and fixtures. The shop operator reviews the posted file and conducts the appropriate dry run and test. Include posted files only after that setup is validated. Never run machine code bundled with a tutorial as if it matched the shop.
