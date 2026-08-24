# RL35 — anchor-run charging and a fixed global gain

Date: 2026-08-21

## Status

**ANALYTIC for `R>=10000`**, with an exact finite symbolic certificate. The numerical continued-fraction consequence additionally uses the inherited external computational input `R>=2^71`.

This is the first post-RL30 result in this continuation that converts the induced low-state dynamics of the support anchors into a fixed global saving rather than merely moving the local supporting line.

## 1. RL34 anchor items

Retain

`T(R)=256R/(256R-319)`

and

`S(R)=(531441R+1568693)/(531441R)`.

The two zero-slack RL34 anchor items are:

- `T`: the direct type-II `k=2,h=1` block, with `(n,V)=(5,8)`;
- `S`: the induced pair `E+T`, where `E` is direct type-II `k=3,h=1`, with `(n,V)=(12,19)`.

Their exact low-state maps are

`G_T(x)=(243x+319)/256`,

`G_S(x)=(531441x+1568693)/524288`.

The admissible start domains are

`T: a2 <= x < a1`,

`S: R <= x < a2`,

where

`a2=(256R-319)/243`,

`a1=(32R-23)/27`.

Their exact correction products are

`p_T(x)=(243x+319)/(243x)`,

`p_S(x)=(531441x+1568693)/(531441x)`.

Thus, once only anchor items remain, the next anchor type is determined by the current low-state height.

## 2. Itemization of the whole cycle

Use the RL34 extended-block partition.

- A `T` block not consumed by a preceding exceptional block is a `T` anchor item.
- If an exceptional `E=II(k=3,h=1)` is followed by `T`, group them into one `S` anchor item.
- If `E` is followed by any other forced `k=2` successor, group the pair into one **nonanchor composite item**.
- Every remaining block is a **nonanchor individual item**.

These items are disjoint and cover the cycle.

## 3. A reserve factor on every nonanchor item

Define

`Q(R)=(2000R+1)/(2000R)=1+1/(2000R)`.

The exact certificate proves that every nonanchor item with product `P`, odd length `n`, and valuation `V` satisfies

> `P * Q^(n+24) <= T^(12V-19n) S^(8n-5V)`.

The extra `24` phases are a reserve for at most two leftover anchor items, since each anchor item has odd length at most `12`.

The finite seed proof includes:

- all nonanchor residues `h=1,...,12`;
- special `h=13` bases for the two residues whose `h=1` cases are anchors/paired (`II2` and `II3`);
- all `E+k=2` nonanchor composites;
- the special composite `E+(II2,h=13)` base.

The period-12 extension is certified by

`P_HH^6 Q^12 <= S`.

## 4. Every 3, 4, or 5 consecutive anchor items pay their own `Q` factor

For a word `w` in the alphabet `{S,T}`, compose the exact affine low maps. The resulting correction product has the form

`P_w(x)=1+C_w/(M_w x)`,

so it decreases with the initial low state `x`.

For each word length `3,4,5`, the verifier reconstructs its exact admissible initial-state interval from the `S/T` domain inequalities. Empty words are certified empty for every `R>=10000`; for every admissible word the lower endpoint is exact and

> `P_w * Q^(n_w) <= T^(#T) S^(#S)`.

The admissible word lists are certified explicitly by the verifier.

## 5. Global charging argument

### If at least one nonanchor item exists

Rotate the cyclic item list to begin at a nonanchor item. After each nonanchor item, split the following maximal anchor run into consecutive 3-item chunks plus a remainder of at most two anchor items.

- Every 3-item chunk pays its own complete `Q^(n)` charge by Section 4.
- The preceding nonanchor item carries a reserve `Q^24`, enough to pay the remainder because two anchor items contain at most 24 odd states.

Thus every odd state in the cycle receives one factor `Q`.

### If every item is an anchor

Any item count `m>=3` is a sum of `3,4,5`, so the cyclic anchor word can be partitioned into certified 3/4/5-word chunks.

Pure-anchor cycles of one or two items are impossible for `R>=10000`: the six possible affine compositions `T,S,TT,TS,ST,SS` either have no positive fixed point or have their unique positive fixed point below `113`, hence below `R`.

Therefore in all cases

> **`lambda * Q^L <= T^(12A-19L) S^(8L-5A)`.**

This is the new global gain.

## 6. New coefficient

Set again

`beta=log 3/log 2`,

`x=log(lambda)/L`.

The global inequality gives

`x <= [N-log Q]/D`,

where

`N=(12beta-19)log T +(8-5beta)log S`,

`D=1-(12log T-5log S)/log 2`.

Hence

> **`limsup R log(lambda)/L <= 0.245797537816914843649363119811...`.**

This improves RL34 by an exact asymptotic `1/2000=0.0005`.

The two-anchor dynamical subsystem itself has invariant average tending to the RL23 local barrier

`1/(6 log 2)=0.24044917348...`,

so RL35 still leaves genuine dynamical slack; the `1/2000` charge is deliberately conservative and finitely certified.

## 7. Continued-fraction consequence

Using the inherited external floor `R>=2^71`, rigorous rational log intervals give

> **`L/gcd(A,L) >= 57,699,734,483`.**

This improves

- RL32: `57,494,140,717` by `205,593,766`;
- RL24H: `57,397,300,723` by `302,433,760`.

The next relevant denominator remains

`65,470,613,321`.

So no qualitative CF threshold is crossed and RL remains open.

## 8. Strategic meaning

RL35 supplies a concrete version of the kind of nonlocal charging mechanism the RL30 audit said was missing:

- local support anchors can individually saturate;
- their **successor dynamics cannot saturate indefinitely at their individual maxima**;
- long anchor runs pay a fixed dynamical saving;
- short anchor runs are charged to the positive slack of the neighboring nonanchor item.

This does not bridge to the closed radius-3 theorem, and it does not eliminate the open order-2, strict-excursion, higher-cyclotomic, or non-extremal order-3 branches. It is a stronger global packing theorem, not an RL closure theorem.

Verifier: `verify_rl35_anchor_run_charging.py`.
