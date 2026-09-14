# RL320 — late-row height and root-aligned carry target

Date prepared: 2026-09-14
Status: PREPARED, NOT STARTED

## Absolute objective

Continue toward excluding positive non-trivial Collatz cycles.

## Primary target: late-row-root height

At the first external survivor, the remaining ordered-row subbranch has the
global least odd state inside the rankwise late row. At the root offset the
prefix-count lead is an integer `s>=1`. Re-cutting at the least state gives
half-word weights `ell+s` and `ell-s`.

With `m` the least state, `y` the antipodal state, and

`K=y-3^s m`, one has

`U=3^sD0m+XK`,

`3^sV=3^sD0m-YK`,

`0<|K|<3^s2^35`,

`3` does not divide `K`.

Use genuine `D0` ownership, physical state packing, or a newly proved contact
interface theorem to do one of:

1. bound `s` independently of support;
2. force `K=0` or `3|K`, contradicting the frozen normal form;
3. obtain a gap-free finite certificate in `(s,K)`;
4. prove a clean barrier identifying the first missing ordinary-owned input.

Do not invoke RL140--RL142 until their height/contact hypotheses are proved.

## Secondary target: root-aligned finite caps

For a least-rooted balanced return,

`0<G<2^35`, `v2(G)<=34`.

If the recomputed envelope residue is nonzero and
`epsilon=kappa H+r`, then

`0<=kappa<2^34`.

Combine these caps with

`2^j delta_j == 3^(t_j)E (mod h)`,

`h(2p+1)=3delta+2q`,

`3^Bq<=2^nE`.

The target is an exact consumer that removes a branch or a parameter. Do not
restart a generic fixed-depth prefix scan; RL132 and RL263--RL264 remain
negative controls.

## Scope

- Internal-only frontier: `ell>=190537`.
- External-certificate-conditional frontier: `ell>=49,547,666,544`.
- Gate A: OPEN.
- Gate B: OPEN.
- Global positive non-trivial-cycle exclusion: OPEN.
- `g=1` remains separate.
