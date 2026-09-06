# RL264 — physical-lift affine-ray theorem, ownership equivalence, and Radius-4 distance barrier

Date: 2026-09-06
Classification: **ANALYTIC METHOD BARRIER / FALLBACK JUSTIFIED**

## 1. Scope

Work in the inherited odd-terminal full-phase setting with

`N=19+24h`,
`A_0=(9N+5)/8=22+27h`,
`B_0=(27N+127)/8=80+81h=3A_0+14`.

The canonical internal variables satisfy

`d_p=1+Y_p-X_p`,
`T_p=3^(d_p)A_p-B_p`,
`J_p=T_p+3^(d_p)-2^(d_p)`.

No result below closes Gate A or Gate B.

## 2. Finite-prefix free-base lift theorem

Fix any finite legal canonical x-driven prefix of length `p`, starting from `(d,J)=(1,-13)`, and let its forced companion parity word be `y`.

For the half-Collatz map

`F(n)=n/2` if `n` is even and `F(n)=(3n+1)/2` if `n` is odd,

every binary parity word of length `p` determines exactly one starting residue modulo `2^p`.

Because `A_0=22+27h` and `27` is odd, `h -> A_0 (mod 2^p)` is a bijection. Hence there is exactly one residue

`h=h_0 (mod 2^p)`

realizing the chosen canonical x-prefix. The identity `B_0=3A_0+14` together with the canonical physical identity then forces the companion B-trajectory to realize the canonical y-prefix.

Therefore every finite legal canonical prefix has infinitely many genuine positive physical lifts `h=h_0+2^p q`, `q>=0`.

## 3. Affine-ray theorem

For the lift family `h=h_0+2^p q`, let `X_p,Y_p` be the prefix-one counts.

Iteration of the affine half-Collatz map gives exactly

`A_p(h_0+2^p q)=A_p(h_0)+27*3^(X_p) q`,

`B_p(h_0+2^p q)=B_p(h_0)+81*3^(Y_p) q`.

Since `d_p=1+Y_p-X_p`,

`3^(d_p) * 27*3^(X_p) = 81*3^(Y_p)`.

Thus

`T_p=3^(d_p)A_p-B_p`

is invariant along the entire physical affine ray, and so is `J_p`.

Consequences:

- positivity and absolute physical magnitude impose no finite-prefix obstruction;
- carrying absolute `(A_p,B_p)` in a local finite state adds no independent canonical information unless an unbounded/global ownership datum is retained;
- this remains true in the hypothetical low-area regime `H<k`.

## 4. Terminal ownership is exactly the inherited phase quotient

For a complete internal word x of length `m`, weight `r=ell-3`, define

`Qx=sum_j 2^(a_j)3^(r-j)`,
`Qy=sum_j 2^(b_j)3^(r-j)`,
`Dcal=Qx-Qy`.

The A-trajectory terminal ownership equation, after substituting `N=19+24h`, reduces to

`(N-2)M = 69*3^r + 24Qx - 6*2^a + 8*2^(a-k-1)`,

where `M=2^a-3^ell`.

The inherited exact rank identity is

`3Qx-Qy = 14*3^r + 2^(a-1) - 2^(a-k-1)`.

Substitution gives exactly

`(N-2)M = 237*3^r - 12Dcal - 2^(a-k+1)`,

which is the already-promoted RL65 full-phase quotient equality.

Hence the terminal physical lift does not supply a second independent scalar ownership constraint. Once terminal canonical `d=1,J=2^k` and the A-endpoint ownership hold, the B-endpoint ownership follows from `B=3A-T`.

## 5. Exact cyclic transport profile of the full half-word pair

For

`u=110 x 1 0^t`,
`v=111 y 0^(t+1)`,
`k=t+3`,
`a=m+k+1`,

let `F_i` be the cumulative excess of v-ones over u-ones after position i around the length-a word.

Prefix legality gives `F_i>=0`. Exactly `k` entries of the cyclic edge profile are zero. The remaining `a-k` entries are the canonical internal heights

`d_0,...,d_m`.

Therefore

`sum_i F_i = (a-k)+H`

and

`sum_{F_i>0}(F_i-1)=H`.

If additionally `H<k` and `k<a/2`, then fewer than half of the profile entries are zero and fewer than half exceed one. Thus `1` is the unique median. The cyclic adjacent-transposition distance is therefore

`dist_cyc(u,v)=min_c sum_i |F_i-c| = H+k`.

## 6. Natural self-rotation distance

Full phase makes `W=uv` the genuine positive cycle parity word. Its half-period cyclic self-rotation is `vu`.

The cumulative transport profile from `uv` to `vu` is

`F_0,...,F_(a-1), -F_0,...,-F_(a-1)`.

This multiset is symmetric, so zero is a median and

`dist_cyc(uv,vu)=2 sum_i F_i = 2(a-k+H)`.

This identity is unconditional once the terminal/full-word construction above is valid.

In the retained large-a resonance branch used by the Gate-A work, inherited bounds imply `k<a/2`; hence the natural physical self-rotation has distance greater than `a`, far from exact Radius 4.

## 7. Radius-4 eligibility barrier

The promoted Radius-4 theorem is a theorem about a **single primitive full-D word and one of its exact-distance-4 cyclic self-rotations**.

The physical `N,N+4` construction does not automatically manufacture such an object:

- `u,v` are two half-words, not a word and its self-rotation;
- in the dangerous low-area regime their cyclic transport distance is `H+k`, not 4;
- the actual self-rotation `uv -> vu` has distance `2(a-k+H)`, not 4.

Therefore the integer orbit gap `N+4-N=4` must not be identified with Radius-4 word distance.

The older determinant-selected Gate-B rotations remain separate objects. RL264 obtains no new theorem forcing their counterflow into the already-closed Radius-4 range.

## 8. Method classification

The RL264 preferred physical-lift route is decisively closed as a standalone new Gate-A mechanism:

1. every finite canonical prefix has an infinite positive physical affine ray;
2. canonical `(d,T,J,H)` are invariant along that ray;
3. terminal ownership collapses exactly to the already-promoted RL65 full-phase quotient;
4. the natural physical self-rotation does not satisfy Radius-4 exact-distance eligibility.

A return to arithmetic selector work was therefore mathematically justified after this barrier. By explicit user direction at closeout, that fallback is now frozen rather than pursued.

Gate A: open and frozen as a future fallback.
Gate B: open.
Radius 4: proved locally; not invoked to close RL264.
Radius 5: not attempted in RL264.
