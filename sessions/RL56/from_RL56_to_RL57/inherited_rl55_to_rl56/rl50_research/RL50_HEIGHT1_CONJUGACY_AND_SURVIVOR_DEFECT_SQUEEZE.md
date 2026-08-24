# RL50 — height-one Collatz conjugacy and explicit-survivor defect squeeze

Date: 2026-08-22

## Status

**ANALYTIC STRUCTURAL IDENTITIES + EXACT RATIONAL CERTIFICATES + ONE LIVE EXTERNAL-COMPUTATION COROLLARY.**

This note does not close Gate A.  It does two things that materially change the next attack:

1. identifies the zero-area height-one odd-continuation exactly with the shortcut Collatz map itself, explaining why a proof that isolates that subsystem risks circularity;
2. uses the safe explicit continued-fraction survivor together with the phase scalar to force a constant-size rank-defect/zero-mass window.

The published/stable external floor remains `2^71`.  A separate corollary records the current Barina project status `2075*2^60`, observed on the primary project page on 2026-08-22; this live status is kept distinct from the peer-reviewed 2025 `2^71` theorem.

## 1. Exact height-one conjugacy

At height one, let

`J = T+1`.

When `J` is odd, the compatible zero-area edges are

`00: J -> (J+1)/2`,

`11: J -> (3J+1)/2`.

Exactly one result is odd.  Put

`n := (J-1)/2`.

Then:

- if `n` is even, the odd-preserving edge is `00`, and
  `n' = n/2`;
- if `n` is odd, the odd-preserving edge is `11`, and
  `n' = (3n+1)/2`.

Therefore the deterministic odd-preserving synchronized continuation is exactly conjugate to the shortcut Collatz map

`C(n) = n/2` for even `n`,

`C(n) = (3n+1)/2` for odd `n`.

This is not an analogy: it is an exact change of variables.

### Normalized lift under the conjugacy

At height one, write `g=2^i/3^p` and

`L := g n = g(J-1)/2 = gT/2`.

On the odd-preserving synchronized edge,

- `n` even / `00`: `g' = 2g`, so `L'=L`;
- `n` odd / `11`: `g' = 2g/3`, so `L'=L+g/3`.

Thus `L` is exactly the standard monotone normalization of the shortcut Collatz orbit: even steps are neutral, odd steps add `g/3`.

This recovers the RL49 height-one telescope in a more conceptual form.

## 2. The canonical negative pump is the negative Collatz 3-cycle

The canonical RL entrance is

`J=-13`, hence `n=-7`.

The deterministic odd-preserving synchronized orbit is

`J: -13 -> -19 -> -9 -> -13`

with edge word

`11,00,11`.

Under `n=(J-1)/2` this is exactly

`-7 -> -10 -> -5 -> -7`,

the classical negative shortcut-Collatz 3-cycle.

Across one macro, starting with weight `g`,

- `g` is multiplied by `8/9`;
- the synchronized `S`-mass is
  `g/3 + (4g/3)/3 = 7g/9`.

Hence `r` repeated negative macros from the canonical start `g=1` contribute exactly

`S_neg(r) = 7(1-(8/9)^r) < 7`.

This explains the old neutral-pumping obstruction exactly: the RL quotient contains a scaled copy of a genuine negative Collatz cycle.

Similarly the positive height-one cycle

`J=3 <-> 5`

is the ordinary shortcut cycle

`n=1 <-> 2`,

and its synchronized macro multiplies `g` by `4/3`.  The genuine prefix cap is therefore essential for controlling positive synchronized pumping.

## 3. Strategic consequence

A uniform proof based only on the height-one odd-continuation cannot simply "solve" its deterministic dynamics without risking a re-embedding of the original Collatz problem.

The live Gate-A proof must use information not present in that conjugate subsystem, specifically at least one of:

- the full-phase scalar/strip;
- the exact prefix cap on `g`;
- the weighted excursion defect `E`;
- higher-height area data.

This is a proof-strategy obstruction, not a counterexample to Gate A.

## 4. Safe explicit survivor

Using only the accepted published floor `N>=2^71`, RL50 has exactly one above-`log_2(3)` continued-fraction survivor below the rigorous Legendre gate:

`a   = 123139092617126647266`,

`ell =  77692117359936589403`,

`q   =  45446975257190057863`.

Put

`lambda = a log 2 - ell log 3 = log zeta > 0`.

The companion exact rational log-interval verifier proves a rigorous positive interval for `lambda`.  Since

`zeta-1 = exp(lambda)-1 > lambda`,

any external state floor `N>=R` gives

`N(zeta-1) > R lambda_lower`.

Under full phase,

`S = [27N(zeta-1)-127]/8`,

and the exact rank identity is

`2S+3E = 14 + (27/2) zeta (1-2^-k)`.

Also the phase squeeze gives

`zeta-1 < (398/45)/R`.

These three facts give exact constant-size bounds.

## 5. Published `2^71` corollaries

With `R=2^71`, exact rational interval arithmetic gives

`S > 11.2549528388... > 45/4`,

and

`E < 1.6633647742... < 5/3`.

So the sole safe sub-Legendre survivor, if it were a genuine full-phase object, would have

`boxed: S>45/4}`

and

`boxed: 0<=E<5/3}`.

### Candidate-specific zero-budget strengthening

The inherited full-phase identity gives

`Zy = S-1+g_end > S-1 > 41/4`.

Since `E=Zx-Zy>=0`,

`Zx > 41/4`.

RL50 already proved that every internal x-zero has weight strictly below `17/30`.  Eighteen such zeros could contribute only

`< 18*(17/30) = 51/5 < 41/4`.

Therefore the explicit survivor requires at least **19 internal x-zero columns**:

`boxed: # internal x-zero >=19}`,

hence

`boxed: z>=20}`.

This strengthens the uniform RL50 theorem `z>=17`, but only on this explicit continued-fraction stress point.

## 6. Current live Barina status: a sharper external corollary

The primary Barina verification page observed on 2026-08-22 reports contiguous convergence verification below

`R_live = 2075*2^60`.

This is slightly above `2^71 = 2048*2^60`.  Treating that page as a **live external computational status**, not as a replacement for the peer-reviewed published theorem, the same exact arithmetic gives

`S > 11.6126231155...`,

`E < 1.4249179230... < 3/2`.

Thus conditionally on the current live project status,

`boxed: E<3/2}`.

The corresponding live Legendre denominator gate is

`ell <= 93743841845618559377`,

and the same index-41 convergent above remains the unique survivor below it.

## 7. Exact future computational kill threshold for this survivor

The phase identity gives, for every allowed `k`,

`N(zeta-1) < 2zeta + 61/9`.

Using only the rigorous lower bound `zeta-1>lambda_lower` and the phase upper bound on `zeta`, the verifier proves:

- a contiguous floor `2236*2^60` is not enough for this simple bound;
- a contiguous floor `2237*2^60` **is sufficient** to contradict the phase inequality for this explicit survivor.

Therefore:

> If an independently trusted contiguous Collatz verification reaches `2237*2^60`, the sole current sub-Legendre full-phase survivor is eliminated outright, without any Gate-A enumeration.

This is a conditional forward threshold, not a present proof step.

## 8. What this does and does not solve

What is gained:

- exact diagnosis of the height-one neutral subsystem as Collatz-conjugate;
- a constant defect window `E<5/3` for the published-floor explicit survivor;
- a stronger candidate-specific zero count `z>=20`;
- a live-status refinement `E<3/2`;
- an exact external-computation threshold that would kill the survivor.

What remains open:

- proving `H>=t+3` for genuine full-phase objects;
- converting the small weighted defect `E` into an integer area/valuation contradiction;
- treating denominators above the Legendre gate without enumeration.

The next internal attack should therefore quotient the Collatz-conjugate synchronized macros by endpoint lift data and charge only deviations/excursions against `E`, while retaining the terminal valuation.  Trying to analyze the synchronized height-one orbit as a free-standing dynamical system is strategically circular.

## Verification

Run:

`python rl50_research/verify_rl50_height1_collatz_conjugacy.py`

`python rl50_research/verify_rl50_survivor_defect_squeeze.py`
