# Regenerating the Geometry

Python 3 is optional. The supplied DXF files can be used directly without it. The generator uses only the Python standard library.

From this directory on Windows run:

```powershell
py regenerate_geometry.py --params parameters.json --out ..\Generated_Variant
```

On macOS or Linux use python3 in place of py. The new folder contains vectors and schedules only; open/import them into VCarve to create native CAM. Existing files in the chosen output folder will be replaced, so always use a new variant folder when preserving a revision.

## Change exercise

Copy parameters.json to parameters_B.json. Set finished_width_mm to 520 and revision to B. Run with --params parameters_B.json and a fresh --out directory. The boundary positions and curve offsets scale with width; the height and thickness remain independent. This is proportional resizing, not a claim of a general product configurator.

There are four interior boundaries. Each uses two cubic Bezier spans, with seven X-offset controls and evenly spaced Y controls. Shared interface samples are reused exactly in both adjacent polygons. DXF exports use closed lightweight polylines with six decimal places; SVG uses the same sampled geometry. The nominal gap is zero and the generator does not apply machining fit allowances. The nominal_joint_gap_mm field is descriptive only: tune fit in CAM and record it, not by changing that JSON field.

geometry_manifest.json records stock dimensions and assembly-to-stock translations. It reports numerical geometry checks, not physical tolerance or machining accuracy. The supplied report adds denser sampling and import-parser checks. After any change, inspect the geometry and toolpaths in VCarve again.
