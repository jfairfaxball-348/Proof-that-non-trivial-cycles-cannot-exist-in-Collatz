# RL325 correction and demotion ledger

Date: 2026-09-15
Status: FROZEN FOR RL325 CLOSEOUT

## C1 — scratch-only misuse of the RL319 physical-gap cap

A transient RL325 scratch step attempted to use

`G<2^35`

inside the live ordered late-row-root branch and from it derive

`n<=G<2^35`.

This is **not valid at the live scope** and is not promoted.

The RL319 theorem `0<G<2^35` was proved only in the **root-aligned alternative**, under the assumption that a balanced boundary is the global least odd state `m`. RL319 separately treats the complementary late-row-root alternative and there proves only the scaled-contact bound

`0<|K|<3^s 2^35`.

The current RL325 branch is the late-row-root/canonical `K<0` branch, so the root-aligned absolute `G` cap cannot be transferred.

### Valid retained replacement

RL325 retains the genuinely proved live-branch inequality

`n-5/6 < (X/Y)G`,

together with the crossing-prefix theorem

`G<2^z`

and the global two-ended zero budget

`z<=floor(d rho/ell)`.

These yield the valid self-consistent carry contraction without any absolute `G<2^35` assumption.

Classification: **explicit scratch-only demotion / scope repair before promotion**.

No previously committed authoritative theorem is altered by this correction.

## C2 — no cyclic-wrap resurrection

The RL325 ownership telescope is promoted only for genuine **linear** matched-rank intervals. No cyclic recurrence or wrap claim is made or restored.

Classification: **scope preservation, no correction to prior authority**.
