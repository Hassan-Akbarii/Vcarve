# River Practice Board

An original training handoff based on the supplied freelance job description. This is a fictional client scenario, not Cossatot Works documentation or the actual River No. 1 design. All added dimensions and manufacturing choices are exercise assumptions.

## Start in this order

1. Open **00_Start_Here.pdf**. It explains the scenario, workflow and learning route.
2. Open **02_References/Board_Reference.png**, then **02_References/Drawing_Set.pdf**.
3. Read **01_Client_Brief/Practice_Client_Brief.md** as if you were the contractor receiving it.
4. Open **08_Free_Samples/Native_Samples_and_Tutorials.html**. Download R01 and R02. Each contains a genuine VCarve `.crv` project. R03 is optional. A Python downloader is included if easier.
5. Complete the warm-up in **03_CAD/Warmup_Plate_Stock_mm.dxf**.
6. Import the separate coupon stock files from **04_Joint_Test** into two VCarve jobs; create and preview their toolpaths.
7. Build all five board jobs using **03_CAD/P01...P05...Stock_Layout_mm.dxf** and **05_VCarve/VCarve_Steps.md**.
8. Save your own editable `.crv` files. Record evidence using **09_Client_Presentation**.

The custom board files supplied here are DXF and SVG geometry, not native CRV files. A native VCarve project and editable CAM settings must be created and saved in VCarve. No custom board toolpaths, machine code, actual test-cut results or VCarve screenshots have been fabricated.

## Units and layers

All custom CAD is millimetres at 1:1. Stock-layout files use lower-left stock XY origin and stock-top Z datum. Grain is parallel to +Y. Select the **CUT_** layer only for a part profile. **REF_STOCK** and **REF_GRAIN** are reference layers, never machining selections. SVG is a fallback; DXF is the recommended import route.

**Master_Finished_Assembly_mm.dxf** is the 508 x 381 mm finished reference. **Master_Pretrim_Assembly_mm.dxf** is the 514 x 387 mm glue-up reference. Do not generate one common-line cutting program from the assembled touching pieces. They use different wood stocks and need separate compensated profiles.

## What you can demonstrate

- Digital-only completion: geometry, CAM organization, previews, revision handling and documentation.
- Physical prototype completion: the above plus actual fit, machining behavior and repeatability evidence.

Only describe CNC woodworking experience or cut quality after doing the relevant physical work. The included client case-study template keeps those distinctions visible.
