# RL46 Repair and Prefix-Cap Progress

Date: 2026-08-22

## Status legend

- **Analytic**: derived symbolically from the retained automaton / inherited RL42 cap, subject to audit of those inherited hypotheses.
- **Exact finite certificate**: exhaustive computation over a finite state graph with no heuristic pruning beyond stated dominance/necessary conditions.
- **Partial computation**: informative but not a certificate of the desired global statement.
- **Open**: not proved.

## Starting point

RL45 reduced the desired one-excursion excess bound to the terminal valuation target

\[
H\ge t+3=v_2(T+1),\qquad H=e-z+1,
\]

but showed that the unrestricted height-one quotient contains the ordinary Collatz map. Thus a proof that ignores the genuine near-minimum/prefix constraints risks circularity. RL46 restored those constraints.

## 1. Repair of the virtual neutral `11` pump

At the structural state `d=1, T=-2`, an `11` column is a true structural self-loop in `(d,T)` while advancing the column/rank bookkeeping. Earlier RL46 exploratory code virtualized this pump but incorrectly allowed it to be activated at a later virtual multiplicity without checking the prefix cap on the **first actual pump column**.

For a fixed pair `(a,ell)`, with `X=2^a`, `Y=3^ell`, actual column index `n=z+p_alpha`, the exact alpha-prefix cap used here is

\[
2^{n+2}Y^2\le 3^{p_\alpha+2}X^2.
\]

**Repair:** a virtual pump flag may be activated only if this inequality is already true at the first actual `11` column. Once one such pump is legal, another `11` increments both `n` and `p_alpha` by one, multiplying the left/right cap ratio by `2/3`; therefore every subsequent pump remains legal. This makes the virtual quotient sound.

Consequence: the formerly reported `e=43..49` universal-cap survivors and the putative `(65,41), e=52` exact-cap skeleton were artifacts of the unsound pump activation and are withdrawn.

## 2. Analytic restrictions restored in RL46

### 2.1 Internal invariant `3 does not divide T`

The canonical internal start is `T=-14`, hence `T != 0 (mod 3)`. For every valid internal transition

\[
T'=\frac{3^yT+x3^{d+y-1}-y}{2},\qquad (x,y)\in\{0,1\}^2,
\]

the nonzero residue mod 3 is preserved. The only potentially exceptional `y=0,x=1,d=1` case would make the next height zero and is not a valid internal transition.

At a genuine terminal crossing,

\[
T+1=2^{t+3}.
\]

If `t+3` were even then `2^{t+3}-1` would be divisible by 3. Therefore `t+3` is odd and

\[
\boxed{t\text{ is even}.}
\]

### 2.2 `t=0` is excluded by the terminal moved-rank cap

The inherited RL42 cap at the last moved odd rank yields

\[
\frac{2^{a-t-1}}{3^{\ell-1}}\le \zeta^2,
\qquad \zeta=\frac{2^a}{3^\ell},
\]

equivalently

\[
\frac{3}{2^{t+1}}\le \zeta.
\]

In the retained near-resonant window `zeta^2 < 16/15`, `t=0` would force `zeta >= 3/2`, impossible. Hence `t>=1`; combined with even parity,

\[
\boxed{t\ge2\text{ and }t\text{ is even}.}
\]

This is one reason the old normalized `t=0` countermodels are not physical one-excursion returns.

### 2.3 Exact area identity

For each internal column, the excess and zero-count increments are

\[
\Delta e=d-x,\qquad \Delta z=1-x.
\]

Therefore

\[
\Delta(e-z)=d-1.
\]

With the canonical initialization, defining

\[
H=e-z+1,
\]

gives the exact identity

\[
\boxed{H=\sum_{\text{internal columns}}(d-1).}
\]

Thus `H` is literally the discrete area above height one. Since terminal geometry has `q=z+t`,

\[
e\ge q+2
\iff H\ge t+3
\iff H\ge v_2(T+1).
\]

This is the clean combinatorial form of the missing theorem.

## 3. Exact finite certificates

### 3.1 `(a,ell,q)=(46,29,17)` — cutoff-free structural elimination

`verify_fixed_pair_prefixcap_cutofffree.py 46 29` searches the finite fixed-pair structural graph with the repaired neutral-pump quotient and no excess cutoff.

Recorded output:

- states: `61,347`
- terminal hits: `0`

Therefore there is **no exact-prefix-cap terminal geometry for this pair at any excess** within the retained automaton.

### 3.2 `(a,ell,q)=(65,41,24)` — unique structural hit, minimum excess 125

The same cutoff-free structural search gives one normalized terminal hit:

`(z,t,gout,p_alpha,p0,loops,need,pump,n,T) = (22,2,16,38,39,0,0,False,60,31)`.

Thus the sole structural terminal record has

\[
z=22,\quad t=2,\quad T=31,
\]

and uses no neutral pump family.

`min_excess_fixed_target_65_41.py` then performs a layer DP retaining the minimum excess for each exact structural state and reconstructs an explicit 59-column path. It proves

\[
\boxed{e_{\min}=125}.
\]

Hence

\[
H=125-22+1=104>5=t+3,
\]

and in particular

\[
e\ge125\gg q+2=26.
\]

### 3.3 `(a,ell,q)=(149,94,55)` — exact violation and equality exclusion

At actual column layer `n`, `p_alpha=n-z` is redundant. For a fixed exact state `(d,T,z)`, only the smallest accumulated `H` need be retained: all future transition/parity/cap tests are identical and smaller `H` dominates.

For a counterexample to `H>=t+3`, terminal `q=z+t` implies the necessary live-region condition

\[
H+z<q+3.
\]

`verify_fixed_pair_violation_layerdp.py 149 94` keeps exactly that counterexample-capable region and exhausts:

- total retained states over all layers: `5,816,094`
- peak layer size: `134,713`
- violations: none.

`verify_fixed_pair_boundary_layerdp.py 149 94` weakens the pruning to `H+z<=q+3`, thereby including the equality boundary. It exhausts:

- total retained states: `7,157,312`
- peak layer size: `165,496`
- violations: none
- equalities: none.

Thus, for this pair, no terminal state satisfies `H<=t+3`; the desired inequality holds with strict margin.

## 4. Partial q=79 computation — NOT a certificate

For the next coprime near-resonant pair

\[
(a,\ell,q)=(214,135,79),
\]

the same violation DP reached layer 81 before state growth became impractical in the straightforward implementation. The partial log records roughly `8.84 million` cumulative states and `811,493` states at layer 81.

This is **partial evidence only**. Do not state that q=79 is eliminated or that the terminal theorem is proved there.

## 5. What was learned strategically

1. The unrestricted height-one valuation automaton is too broad: it contains ordinary Collatz dynamics exactly.
2. Restoring the RL42 rank-by-rank prefix cap removes many nonphysical quotient trajectories.
3. The correct finite dynamic for fixed `(a,ell)` uses actual columns, makes `p_alpha=n-z` redundant, and allows minimum-`H` domination at fixed `(d,T,z)`.
4. The remaining computational obstruction at `q=79` is state growth in the exact `T` coordinate. The next analytic quotient should target that dimension without discarding the prefix cap.
5. RL45 already ruled out the naive universal absolute-resultant-size inequality. Do not revive it without new arithmetic input; the more plausible radius-3 route is gcd/subresultant/Bezout structure.

## 6. Exact proof state after RL46

### Analytic (subject to inherited-hypothesis audit)

- repaired first-pump legality rule and monotonic legality of subsequent neutral pumps;
- internal invariant `3 does not divide T`;
- terminal parity `t` even;
- inherited terminal moved-rank cap excludes `t=0`, hence `t>=2`;
- area identity `H=sum(d-1)` and equivalence `e>=q+2 <=> H>=t+3`.

### Exact finite certificates

- `(46,29,17)`: no prefix-cap terminal geometry at any excess in the finite structural quotient;
- `(65,41,24)`: sole structural terminal record has exact minimum excess `125`;
- `(149,94,55)`: no terminal violation `H<t+3` and no equality `H=t+3`.

### Partial / audit-pending computation

- `(214,135,79)`: only a partial run through layer 81; no theorem.

### Open

- a uniform, cutoff-free proof of `H>=t+3` for all retained coprime near-resonant pairs;
- the q=79 case and all larger pairs absent such a uniform lemma;
- the genuine quantitative radius-3 bridge / same-root arithmetic closure identified in RL44–RL45;
- global RL closure.
