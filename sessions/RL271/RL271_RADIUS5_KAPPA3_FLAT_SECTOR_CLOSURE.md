# RL271 — Radius-5 `|kappa|=3` flat-sector closure

Date: 2026-09-07

Classification: **RADIUS5_KAPPA3_FLAT_SECTOR_CLOSED_HEIGHT2_MASS4PLUS1_OPEN**.

## Shared determinant-three framework
Orient to `kappa=+3` by exact source/target reversal. Then `qA-mL=3`, so `gcd(A,L)|3` and `gcd(m,A)|3`. The determinant-window calculation gives `W_i(m)=q-g_(i-1)`. Every theorem hit test retains the complete positive `D=2^A-3^L`.

## Flat leaf closures

### `[4,1]`
The four-edge positive block plus one negative singleton reduces to coefficients `C in {15,17,21,27,29,35,47,65}`. The audited exponent tail is `L-v <= (A-u)+2`; the stronger version without `+2` is false. The infinite reduction leaves `A<=56`. Exact reconstruction gives 10,762 structural states, 7,748 in positive `D`, and zero full-`D` hits.

### `[3,1,1]` and `[2,2,1]`
A longest-zero-gap cut gives `U=floor((2A+2)/3)` and `0<|E|<=5*3^(7+h)*2^(U-h)` with `h=min(m,A-m)`. Non-bracketing `A>=609` is excluded; the bracketing LMN bound is `A<=261279`, followed by an exact top-denominator compression. The corrected finite cover has 3,514 structural-capable tuples, maximum `A=335`, including 77 `q=L` endpoints.

For `[3,1,1]`, two anchored sign orders give 69,057,294 configurations and 6,857,644 binary states, split exactly 3,428,822 / 3,428,822; full-`D` hits are zero.

For `[2,2,1]`, one anchored sign order gives 34,528,647 configurations and 3,302,985 binary states; full-`D` hits are zero.

### `[2,1,1,1]`
A four-component cut gives `U4=floor((3A+1)/4)` and determinant-window count `r=hL/A +/- 3/A`, hence `0<|E|<=5*3^(7+r)*2^(U4-r)`. Non-bracketing `A>=375` is excluded and the bracketing LMN cutoff is `A<=163052`. The exact finite cover has 1,332 structural-capable tuples, maximum `A=195`, including 90 `q=L` endpoints. Three anchored orders give 182,221,338 configurations and 9,673,883 states, split 3,198,979 / 3,275,925 / 3,198,979, with zero full-`D` hits. A second reconstruction independently agrees.

### `[1,1,1,1,1]`
A five-component cut gives `U5=floor(4A/5)` and again `r=hL/A +/- 3/A`. Non-bracketing `A>=1604` is excluded; the bracketing LMN ceiling is `A<=690205`. Exact arithmetic leaves 3,009 determinant tuples, maximum `A=650`, split by `gcd(m,A)` as 2,255 / 754, with 112 `q=L` endpoints.

In the gcd-one sector, binary reconstruction is equivalent to alternation of ten singleton boundary events. Three feasible order-preserving families contain 3,747,495,821; 1,533,154,639; and 1,303,105,056 structural states. With `z=2^m 3^(-q) mod D`, the sparse test is `-1+z^u1+3z^u2+9z^u3+27z^u4=0 mod D` up to an invertible power of 3.

In the gcd-three sector write `A=3a,m=3b`, so `qa-bL=1`. Each physical residue class has signed flow sum one. With row-zero positives `u<v`, residue-one positive `s`, residue-two positive `w`, and `h=w-L mod a`, realizability reduces to two four-event alternations and `a<L+h-s<2a`; fixed `(s,h)` multiplicity is `(min(s,h)-1)(a-max(s,h)-1)`. This gives 1,256,107,283 states. The sparse test is `-3+3z^u+9z^v+6z^s+c z^w=0 mod D`, with `c=12` for `s<w` and `c=4` for `w<s`.

The singleton total is 7,839,862,799 states. The primary meet-in-the-middle certificate examines 13,640,991 side entries and finds zero admissible low-64 collisions; an independent variable split examines 11,626,528 side entries and again finds zero. Exact equality modulo `D` would imply a low-64 collision, hence full-`D` hits are zero.

## Red teams
The independent exhaustive direct-word replay through `A<=18` reproduces exact orientation symmetry for every flat family and zero full-`D` hits. It also reproduces proper-factor-only counterexamples, checks zero-cut numerator indexing, includes the negative sentinel `A=11,L=7,D=-139,Q=18904`, and uses no primitivity filter. The earlier scratch restriction `q<L` was corrected before promotion; all restored `q=L` endpoints are included and have zero structural states.

## Outgoing state
Every flat `|kappa|=3` Radius-5 family is closed. The height-two mass-four-plus-one family remains open. Therefore the complete `|kappa|=3` sector, Radius 5, Gate B and global exclusion remain open; `|kappa|=5` remains frozen.
