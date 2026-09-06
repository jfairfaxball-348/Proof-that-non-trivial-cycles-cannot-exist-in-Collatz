# RL265 certified facts

Classification: **RADIUS5_EXACT_BARRIER_FOUND**

1. The audited Radius-5 cyclic metric was independently reconstructed from the promoted numerator/root-rotation convention and cyclic earth-mover flow.
2. Exact replay through `A<=18` reproduces RL239 exactly: 181,542 positive-domain distance-5 word/shift instances; 10 full-`D` hits; all ten are the nonprimitive alternating `A=10,L=5,D=781` repetition.
3. Every exact distance-5 optimal flow belongs to exactly one of nine families:
   - flat: `[5]`, `[4,1]`, `[3,2]`, `[3,1,1]`, `[2,2,1]`, `[2,1,1,1]`, `[1,1,1,1,1]`;
   - height-two connected mass five;
   - height-two mass four plus one separate unit component.
4. For every exact distance-5 self-rotation, with optimal flow `g`,
   `kappa=sum g` satisfies `|kappa| in {1,3,5}`.
5. If the rotation shift is `m`, word length is `A`, and one-count is `L`, then for some integer `q`,
   `qA-mL=kappa`.
6. Hence `gcd(A,L)` divides `kappa`, so necessarily `gcd(A,L) in {1,3,5}`.
7. Topology-specific possible absolute skews:
   - `[5]`: `{5}`;
   - `[4,1]`: `{3,5}`;
   - `[3,2]`: `{1,5}`;
   - `[3,1,1]`, `[2,2,1]`, `[2,1,1,1]`, `[1,1,1,1,1]`: `{1,3,5}`;
   - height-two connected: `{5}`;
   - height-two `4+1`: `{3,5}`.
8. Every one of the nine topology families has an explicit primitive `D>1` witness with an exact distance-5 rotation but with no rotation at distance 3 or 4. Therefore no Radius-5 family reduces uniformly to Radius 3 or Radius 4 by cyclic shell crossing alone.
9. Under full-`D`, the remaining obstruction is arithmetic: `D` must divide a nonzero signed five-unit `2,3`-transport sum constrained by the topology and determinant sector.
10. The finite replay contains 4,590 distance-5 words with a proper nontrivial factor `gcd(Q,D)>1` but not full `D`; these are explicitly excluded from theorem evidence.
11. RL247's negative regression `00011110111` is reproduced exactly and remains outside positive-domain scope.
12. Gate A and the fifth retained selector were not touched. Gate B remains open. Radius 4 remains promoted locally. Radius 5 is not yet proved.
13. A simple Radius-n shell induction is falsified at Radius 5. A general Radius-n programme is deferred unless uniform determinant/S-unit arithmetic is later proved.
