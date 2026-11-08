# Automation and Client Editability

The client needs an editable manufacturing master. That requires useful native geometry, tool definitions and recalculable toolpaths, plus the context needed to change them. A DXF and a pile of machine code are not a complete native handoff.

| Task | Best location now | Automation decision |
|---|---|---|
| Approve visual curves and product dimensions | CAD review with client | Human decision |
| Generate shared curves and dependent part outlines | Rhino/Grasshopper, Inventor or the included Python generator | Useful when dimensions or families change |
| Export DXF/SVG, part IDs and stock schedule | External generator | Worth automating; deterministic outputs |
| Import and organize native vectors | VCarve | Manual first; later a Lua Gadget may help |
| Define actual tools, datums and machining choices | VCarve plus operator review | Do not infer from generic geometry |
| Reuse accepted cutting strategy | VCarve toolpath templates | First automation to adopt |
| Review entry, tabs, retention and preview | VCarve plus shop operator | Review each revision |
| Create setup information | VCarve job sheets plus supplementary notes | Mostly repeatable once setup is approved |
| Export machine-specific code | VCarve with verified post | Final reviewed release step |
| Check physical fit, grain behavior and repeatability | Workshop | Measurements drive revisions |

## Recommended handoff structure

Use one native CRV per part initially. Name layers clearly; separate nominal masters, machining vectors and non-machining references. Keep generated CAD and editable vector exports beside the native jobs. Include a toolpath template after it has been created and tested inside VCarve; this pack does not fabricate a native template.

Teach the client three edit levels: cosmetic edits, dimension or joint edits, and machine/fixture changes. Cosmetic changes may need only a preview update. Geometry or thickness changes require toolpath recalculation and another review. Machine, tool or fixture changes invalidate the posted-code setup until checked again.

## Where your skills help

Your parametric design and ArtCAM background should shorten the learning path for geometry, dependencies and CAM concepts. Use the woodworker to review material behavior and assembly. If that person has no CNC experience, obtain a CNC operator's review before promising production-ready files. Automation does not establish cutting expertise.

## Keep one authoritative master per revision

The included Python parameters drive all generated outlines, schedules and transforms. A client can also edit the vectors directly in VCarve without Python. The optional **Master_Editable_Bezier_Assembly_mm.svg** retains exact cubic curves with a small number of control points for easier master editing; the primary DXF layouts use sampled closed polylines. Both are nominal assembly references rather than a ready common-line machining job. Direct edits do not flow back into the JSON. For each revision choose either the parameter master or the native-vector master, record that choice and archive the previous version. Never silently overwrite manual client edits with a regenerated DXF.

## Minimum sensible automation

For one five-piece board, the supplied generator is already enough. Create the CAM manually, save reusable VCarve templates, and keep a clear revision log. A custom Gadget becomes worthwhile when repeated products, many variants or measured setup time justify development. Python does not provide a substitute native CRV writer in this workflow; Lua Gadgets run inside the supported VCarve environment.
