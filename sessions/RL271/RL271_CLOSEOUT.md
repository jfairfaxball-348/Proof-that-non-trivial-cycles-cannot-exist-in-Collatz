# RL271 closeout

Date: 2026-09-07

Classification: **RADIUS5_KAPPA3_FLAT_SECTOR_CLOSED_HEIGHT2_MASS4PLUS1_OPEN**.

RL271 closes every flat Radius-5 topology carrying `|kappa|=3`:

- `[4,1]` — closed;
- `[3,1,1]` — closed;
- `[2,2,1]` — closed;
- `[2,1,1,1]` — closed;
- `[1,1,1,1,1]` — closed.

The generation does **not** close the full `|kappa|=3` sector. The height-two mass-four-plus-one family inherited from RL265 remains open and is the sole successor target.

Important audit correction made before promotion: determinant-three finite covers must allow the endpoint `q=L`. Restoring those endpoints adds 77 structurally capable tuples to the three-component cover, 90 to the four-component cover, and 112 to the singleton cover. Every restored endpoint has zero structural states in the corresponding finite certificate. No promoted theorem relies on the invalid blanket restriction `q<L`.

The frozen verification package contains:
- an exact `[4,1]` reconstruction replay;
- one combined full-`D` verifier for `[3,1,1]` and `[2,2,1]` over the corrected 3,514-tuple cover;
- primary and independent secondary `[2,1,1,1]` structural/full-`D` solvers over the 1,332-tuple cover;
- primary and alternate `[1,1,1,1,1]` sparse meet-in-the-middle certificates over all 3,009 tuples;
- an exhaustive direct-word `A<=18` regression across all five flat leaves;
- exact pair CSVs and SHA-256 metadata.

Successor: **RL272**, targeting only the remaining height-two mass-four-plus-one `|kappa|=3` family. RL272 must not activate `|kappa|=5` until the height-two family is closed or an authoritative checkpoint explicitly changes that policy.

Frozen/unchanged: Gate A, fifth retained selector, selector enumeration, general Radius-n. Radius 4 remains locally promoted. Gate B, Radius 5 as a whole, and global non-trivial-cycle exclusion remain open.

Knowledge catalogues: **stale/deferred** in this connector closeout; they are generated metadata and are not hand-edited as part of the mathematical promotion gate.
