# RL245 correction and demotion ledger

## C245.1 — binary owned-height strengthening

Affected prior file:
`sessions/RL245/RL245_SIX_UNIT_VALLEY_GEOMETRY_AND_SINGLETON_SWAP_CHECKPOINT_2026-09-04.md`

Affected statement: global-looking `h_(i+q) in {0,1}` on the doubled physical route.

Disposition: **DEMOTED**.

Exact replacement:
`h_i = wt(v[0:i]) - wt(u[0:i])`, with internal `h_(3+j)=d_j>=1`, and globally `h_i>=0` on the retained canonical half-word geometry.

Downstream repair: the common same-root negativity statement survives because it needs only
`P_i-h_(i+q) <= P_i`.
The exact q-window derivative, singleton-swap lemma, Branch A/B/C trichotomy, and flow-only countermodel remain valid.

## C245.2 — scratch determinant-sector conclusion

Disposition: **NOT PROMOTED**.

A scratch argument suggested there is no exact-distance-4 full-D self-rotation on the retained branch. Because the same research interval exposed notation/provenance collisions, RL246 must re-derive that statement from the exact RL240–RL243 sources before any use.
