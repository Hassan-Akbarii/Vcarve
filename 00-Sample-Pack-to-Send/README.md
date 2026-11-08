# River No. 1 — simulation sample

Prepared for Cossatot Works as a method sample, not as production files.

This folder shows how the five-piece maple and walnut board would be programmed before a shop test: one shared mating curve, outside cutter compensation, a separate last-pass stock, and three coupon allowances so the real fit can be chosen after a test cut.

Software used: Vectric Aspire 12.503. Native files are `.crv3d`. They have not been checked in VCarve Pro. No G-code has been posted. Nothing in this folder has been cut or measured.

## What is included

| Folder | Contents |
| --- | --- |
| `01_Previews` | Aspire reset-stock previews |
| `02_Setup_Notes` | Stock, zero, tool, depth, allowance, and tabs |
| `03_Job_Sheets` | Aspire HTML job sheets. Times in those sheets are software estimates |
| `04_Native_Aspire` | Editable Aspire 12.5 jobs |

## Files

| File | What it shows |
| --- | --- |
| `Coupon_A_Maple_A` | Maple side of the joint coupon. Final fit allowance 0.000 mm. Stock 140 × 160 × 28 mm |
| `Coupon_B_Walnut_B00_A` | Walnut side, same nominal curve, allowance 0.000 mm. Stock 145 × 160 × 28 mm |
| `Coupon_B_Walnut_B025_A` | Same walnut vectors, allowance −0.025 mm |
| `Coupon_B_Walnut_B050_A` | Same walnut vectors, allowance −0.050 mm |
| `RP_P01_Maple_A` | First maple board piece. Stock 200 × 430 × 28 mm. Allowance 0.000 mm |
| `RP_P02_Walnut_A` | First walnut board piece. Stock 135 × 430 × 28 mm. Allowance 0.000 mm |

The nominal curves were not redrawn between the three Coupon B files. Only the profile final-fit allowance changed. No allowance has been selected as the production fit.

## Settings used in every 28 mm job

- XY zero: lower-left corner of the stock. Z zero: top of the stock. Grain along +Y.
- Tool: 6.35 mm flat end mill, 2 flutes, 18000 rpm, 1800 mm/min feed, 400 mm/min plunge. These are practice values, not shop-approved speeds.
- Outside climb profile. Start depth 0. Cut depth 28.20 mm, which is 0.2 mm through 28 mm stock and assumes a sacrificial spoilboard.
- Passes: 2, 4, … 28, then 28.2 mm.
- Separate last pass leaves 0.15 mm radial stock. That is temporary finishing stock, not the fit allowance.
- Tabs: 12 mm long, 2.2 mm thick, on straight edges or short ends, clear of the mating curve.
- Clearance 15 mm. Home Z 20.32 mm above the stock. Clamps were not modeled.

## What this sample does not include

- Pieces P03, P04, and P05
- The 520 mm width revision
- A chosen fit allowance
- Posted machine code
- A physical test cut or a measured joint

The next production step is to confirm VCarve Pro version, machine, controller, cutter, workholding, and stock, then cut the coupon and measure the fit before programming the remaining pieces.
