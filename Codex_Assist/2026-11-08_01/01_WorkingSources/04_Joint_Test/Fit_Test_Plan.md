# Joint Fit Test Plan

## Purpose

Find a machining setup that produces repeatable maple/walnut joints. This test uses the middle **120 mm** of interface **J12** at full scale. The short sample is useful for fit adjustment, but it does not prove full-length retention, board distortion or glue-up quality.

## Digital baseline

The two nominal outlines share the same sampled boundary. The assembled reference is 160 x 120 mm. Each stock-layout file translates its part into a separate blank; the translation does not alter the interface. Geometry alone contains no cutter-radius offset or preset glue gap. Begin with both outside profiles at zero allowance.

## Physical sequence when a machine is available

1. Record machine, controller, post, tool ID, measured effective cutting size, runout observations, stock thickness, grain, moisture and fixture configuration. Use a simple dimensional calibration feature if tool or machine error is suspected.
2. Cut A in maple and three B versions in walnut. B00 uses 0 allowance; B025 uses -0.025 mm; B050 uses -0.050 mm. Retain A as the comparison datum if undamaged. Keep the same tool, orientation and cutting method.
3. Inspect at top, middle and bottom, then check edge squareness through the 28 mm thickness. A joint that fits only at the top may indicate taper, deflection or edge damage rather than the wrong nominal curve.
4. Photograph the dry fit under consistent lighting with a ruler and part IDs. Record feeler checks and pressure used. If a seam is uniformly tight, review effective tool size and allowance. Local gaps require investigation of geometry, machine behavior, grain and retention before adding blanket clearance.
5. After choosing a setup, cut three fresh pairs to check repeatability. Keep measured spread and photos; do not enter invented results in the template.
6. Approve the short coupon, then machine the complete five-part board as a second milestone. Check full-length joint fit, sliding in clamps, flattening allowance and finished dimensions.

## Distinguish three allowances

- Cutter compensation is the radius of the actual cutting tool accounted for by CAM.
- Roughing or finishing allowance is temporary material left for a later pass.
- Fit allowance changes the final size to tune assembly. Keep its value and affected edges explicit.

The nominal CAD stays unchanged while fit settings are tested. Shrinking all five complete outlines is not the default: it would affect every interface and outer edge. Apply only approved changes, and recheck final assembled dimensions after glue-up and trim.

## Practice acceptance and stops

Use the provisional acceptance criteria in the client brief. Stop to investigate if pieces move, burn, splinter, bow or require force. A simulated seam gap is not a physical test result. All machine operations remain unperformed in this supplied pack.
