# RL51 — stable z=27 elimination by terminal-power suffix rigidity

Date: 2026-08-22

## Status

**ANALYTIC REDUCTION + EXACT DENOMINATOR-INDEPENDENT FINITE CERTIFICATE.**

This note eliminates the `z=27` case for the sole stable continued-fraction survivor carried from RL50. It does **not** close Gate A globally and does not eliminate denominators outside the safe Legendre range.

The proof uses only stable RL50 inputs: the published `2^71` floor, the resulting sole safe continued-fraction survivor, the certified `E<5/3` bound for that survivor, the exact zero identity, the safe prefix cap, and the terminal condition `J=2^k`.

## 1. Data for z=27

For the sole safe survivor,

`a   = 123139092617126647266`,

`ell =  77692117359936589403`,

`q   =  45446975257190057863`.

If `z=27`, then

`# internal x-zeros = # internal y-zeros = z-1 = 26`,

`t=q-27`,

`k=t+3=q-24`,

and the internal word length is

`m=(ell-3)+26=ell+23`.

RL50 gives, stably,

`E<5/3`,

and the exact full-phase zero identity

`2 Zx + E = 12 + (27/2) zeta (1+2^-k) > 51/2`.

Therefore every genuine `z=27` survivor would satisfy the strict lower bound

`Zx > 143/12`.

## 2. The 26-zero x-schedule is forced uniquely

Let `p_j` be the number of x-ones before the j-th internal x-zero. Then

`p_1 <= p_2 <= ... <= p_26`,

and the j-th x-zero weight is

`w_j = 2^(p_j+j-1)/3^(p_j) = 2^(j-1)(2/3)^(p_j)`.

The safe post-zero prefix cap gives

`w_j < 17/30`.

For fixed `j`, `w_j` decreases strictly with `p_j`. Increasing any `p_j` can only increase the lower bound on every later `p_i`. Hence the total

`Zx=sum w_j`

is maximized by the coordinatewise greedy choice: at each zero, take the smallest nondecreasing `p_j` allowed by `w_j<17/30`.

The exact greedy sequence is

`[2,4,5,7,9,10,12,14,16,17,19,21,22,24,26,28,29,31,33,34,36,38,40,41,43,45]`.

Its zero mass is

`Zx_max = 35230240893098563079884 / 2954312706550833698643`

`        = 11.9250209414... > 143/12`.

To certify uniqueness above the phase threshold, classify every non-greedy sequence by its first deviation from the greedy vector. At that first index increase `p_j` by at least one, then maximize the remaining suffix greedily. The best such non-greedy total is exactly

`34856694325605944659660 / 2954312706550833698643`

`= 11.7985798349... < 143/12`.

Therefore any genuine `z=27` survivor is forced to use the greedy x-zero schedule exactly.

In particular

`p_26=45`,

so the last internal x-zero lies at zero-based column

`u_26=p_26+25=70`.

Thus every internal column from 71 to `m-1` has `x=1`. The required all-x-one suffix length is

`m-71 = ell-48 = 77692117359936589355`.

## 3. Backward terminal grammar for an all-x-one suffix

At height `d`, use the RL50 quotient

`Q_d := J + (2^d-1)`.

On an x=1 edge there are only two possibilities.

For `11` at fixed height,

`Q -> 3Q/2`.

Therefore a backward `11` predecessor exists iff `3|Q`, and is

`Q -> 2Q/3`.

For `10`, forward height drops by one and

`Q_{d-1}=(Q_d-1)/2`.

Therefore backward `10` is

`Q -> 2Q+1`,

and raises the height by one.

Every backward `10` consumes one y-zero. Since the complete internal word contains only 26 y-zeros, any backward predecessor chain lying entirely inside the all-x-one suffix uses at most 26 such steps.

The terminal state is

`d=1`, `J=2^k`, hence `Q_1=2^k+1`.

## 4. Exact finite 3-adic certificate

The companion verifier performs the complete backward search from `Q_1=2^k+1` with the two exact maps above and at most 26 backward `10` steps.

It is denominator-independent: it never constructs `2^k`. It evaluates only the necessary residues `2^k mod 3^r`.

Two independent implementations are included in the same verifier:

1. a residue BFS, with enough 3-adic precision to decide every possible 57-edge chain exactly;
2. a symbolic affine search representing every state as

   `Q=(A*2^k+B)/3^b`.

Both return the same sharp result:

`maximum possible all-x-one terminal suffix length = 56`.

Hence a terminal-power-compatible path cannot possess an all-x-one suffix of length 57, let alone length

`77692117359936589355`.

This contradicts the unique x-schedule forced in Section 2.

## 5. Theorem

> **RL51 stable z=27 elimination.** The sole continued-fraction survivor permitted by the stable published `2^71` floor cannot realize a genuine full-phase one-excursion object with `z=27`.

For this survivor `q` is odd, while inherited parity gives `t` even. Therefore

`z=q-t`

is odd. Combined with RL50's `z>=27`, the elimination above upgrades the sole stable survivor to

`z>=29`.

## 6. What this changes

This removes the tiny `~0.0134` scalar gap identified at the RL50->RL51 handover without using the live Barina floor and without improving the obsolete separable rank envelope.

The mechanism is genuinely coupled:

1. phase defect + prefix cap force a unique extremal x-prefix geometry;
2. that geometry creates an astronomically long x=1 suffix;
3. terminal power `J=2^k` admits only a bounded 3-adic predecessor suffix.

This is the first successful use in this line of attack of the proposed terminal-power/backward-macro interface.

It does **not** yet close `z>=29`, because with more x-zeros the phase mass no longer forces all x-zeros into the unique 26-zero extremizer. The next task is to extend the backward suffix certificate to suffixes containing a small number of x-zero edges, so that several final x-zero weights are forced into the terminal-negligible regime.

## Verification

Run:

`python3 rl51_research/verify_rl51_z27_terminal_tail.py`
