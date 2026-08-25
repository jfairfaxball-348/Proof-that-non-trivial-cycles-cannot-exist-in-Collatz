# RL89 target — near-capacity block rigidity and odd-cofactor packing

Date: 2026-08-25

## Authority

Continue from the frozen RL88 state.

RL88 proved that complete height-one excursions have an affine common-mode-free difference reset and used the global area budget to obtain the new exact first-Farey odd window

`2,921,384,819 <= k <= 42,150,931,559`.

Do not restart generic quotient packing, independent `N mod 2^t` accumulation, or a local claim that mismatch resets cannot create high valuation.  Those routes have now been explicitly red-teamed.

## 0. Frozen quantitative input

- `Delta0=13,201,833,154,443,526,323`;
- first-Farey block cap `C=42,150,931,628`;
- `log_2 M < 42,150,931,628.751333`;
- raw reset-budget threshold `k>=2,921,384,818`;
- odd reset-budget threshold `k>=2,921,384,819`;
- first-Farey terminal upper bound `k<=42,150,931,559`.

At the lower odd endpoint `k0=2,921,384,819`:

- total height-one block length
  `Q>=123,139,091,657,887,804,990`;
- at least `k0-2` nonempty blocks;
- `H>=k0-2` and therefore `H in {k0-2,k0-1}`;
- at least `225,242,372` blocks have length `n>=C-23`;
- some signed `(C-n,m)` type repeats at least 7 times.

## 1. First target: classify the saturated-area excursion grammar

Use

`e<=H<k`,

and the exact fact that every `10` has pre-height at least two.

At `k=k0`, `e>=k0-2` and `H>=k0-2`, leaving only:

- `e=H=k0-2`;
- `e=k0-2, H=k0-1`;
- `e=H=k0-1`.

If `e=H`, every unit of area is already consumed by the `e` mandatory `10` columns.  Prove carefully that every complete excursion is then the minimal two-column macro

`01,10`.

If `H=e+1`, classify the exact finite list of possible one-extra-area deviations from the minimal grammar.

Do this analytically, not by enumerating billions of excursions.

## 2. Minimal-excursion cofactor recurrence

For a maximal synchronized block write

`delta_entry=2^n m`, `m` odd.

If its synchronized word contains `s` `11` columns, then at block exit

`delta_exit=3^s m`.

For a minimal `01,10` excursion RL88 gives exactly

`delta_next=(3 delta_exit-1)/4`.

Thus the next block data obey

`boxed: 3^(s+1)m - 1 = 2^(n_next+2)m_next.}`

(with the appropriate sign convention if the physical difference is negative).

This is the primary RL89 arithmetic object.

Questions:

1. for `n_next>=C-d` and `|m|<2^(d+1)`, how many `s<C` can satisfy the congruence?
2. use the exact order
   `ord_(2^t)(3)=2^(t-2)` for `t>=3` where applicable;
3. determine whether fixed small `m` admits at most one `s` in the physical range for a given large threshold;
4. if so, what extra data are needed to turn that into a multiplicity bound on actual blocks?

## 3. Distributional strengthening beyond the single endpoint

RL88 gives a linear lower bound `Q_min(k)` and the universal capacity `C(k-1)`.

For thresholds `d>=0`, derive the exact forced number of blocks satisfying

`n>=C-d`

throughout an initial interval

`k0 <= k <= k1`,

not just at `k0`.

Select `k1` where the near-cap population remains large enough for a finite cofactor-type pigeonhole.

The aim is to eliminate an **interval** of k, not just sharpen one endpoint.

## 4. Common-mode selector is mandatory

RL88 already proved that repeated `(n,m)` / repeated difference does not force a repeated paired state.

Seek one exact additional coordinate that is:

- retained across the block compression;
- bounded or finite in the near-cap regime;
- strong enough that repeated `(n,m,selector)` forces repeated paired physical data.

Candidates:

- height-one `J` or `L=g(J-1)/2`;
- complete-excursion endpoint `Delta L`;
- full-`D` numerator/content class not already tautological with the parity cylinder;
- primitive phase offset / rotation ownership.

Do not use raw quotient distinctness with `O(M)` fibers.

## 5. Full-D role

The direct congruence

`N mod 2^(i+n+2)`

is already contained in the physical parity cylinder and must not be counted as independent information.

A useful full-`D` theorem must instead restrict the **allowed residues/types of the word numerator itself**, or couple two separated block endpoints in a way not implied by their ordinary prefix words.

## 6. Red teams

Every candidate closure must pass:

1. RL81 common-mode freedom;
2. RL79 generalized-increment homogeneity;
3. RL20 physical representative/packing separation;
4. primitivity: repeated differences are not repeated states;
5. first-Farey scope;
6. the explicit RL88 `01,10` arbitrary-reset family;
7. verification economy.

## 7. Desired outcomes

In priority order:

1. eliminate the lower endpoint `k0` analytically;
2. eliminate a nontrivial interval above `k0` using near-capacity/cofactor rigidity;
3. obtain a multiplicity theorem for near-maximal reset types after adding a valid common-mode selector;
4. further raise the first-Farey lower endpoint substantially;
5. or rigorously show that even the saturated-area/minimal-excursion regime retains enough common-mode freedom to realize the required cofactor recurrence, freezing this route.

No Gate A, Gate B, RL/nontrivial-cycle, or Collatz closure may be claimed unless actually proved.

## Close-out

Freeze the exact theorem/evidence/barrier ledger, create the next numbered authoritative bundle and sidecar, fresh-unpack it, verify the manifest, and run the fast verifier.
