# RL319 closeout — crossing contraction, root transport, and bounded carry

Date: 2026-09-14
Status: CLOSED AND FROZEN
Incoming BASE_HEAD: `e5de124d61dcc33aea98646c2ccac9cd08b8d63b`
Successor: RL320

## 0. Executive conclusion

RL319 does not prove Gate A, Gate B, global positive non-trivial-cycle
exclusion, or the Collatz conjecture.

It does materially contract both branches inherited from RL318.

For the nonzero-residue cross-content branch, every phase gap is coprime to
the content modulus and has an exact residue determined by the complementary
full-denominator remainder. Rankwise order of the physical and shadow rows
then controls the entire post-crossing suffix numerator and gives the
support-independent inequality

`3^B q <= 2^n E`.

Here `q` is the magnitude immediately after the first strict sign crossing,
and `(n,B)` are the remaining shadow suffix counts.

For the ordered `epsilon=0` branch, RL319 proves the missing transport from
the least-root nonnegative-defect theorem to an arbitrary balanced cut. The
branch splits exactly:

1. the global least odd state lies in the rankwise late row; or
2. there is a genuine reduced balanced return rooted at the global least odd
   state.

In the root-aligned alternative at the first external survivor,

`0 < G < 2^35`,

so the two physical rows first differ by phase 34. If the recomputed envelope
residue is nonzero and `epsilon=kappa H+r`, then

`0 <= kappa < 2^34`.

This is the first support-independent bounded cofactor carry obtained from
the RL318 crossing programme.

The complementary late-row-root alternative is reduced to an exact scaled
contact. If its interface height is `s>=1`, the antipodal state is

`y=3^s m+K`,

where

`0 < |K| < 3^s 2^35` and `3` does not divide `K`.

The present inputs do not bound `s`, so this remaining branch is the primary
RL320 target.

`PARENT_DIFFICULTY_DELTA = EASIER`

## 1. Inherited setting

Let

`X=2^a`, `Y=3^ell`, `D0=X-Y`, `H=X+Y`.

At the first conditional external survivor,

`(a,ell)=(217,976,794,617,137,528,045,312)`

and `Delta=a log(2)-ell log(3)>0`.

Keep the frontiers distinct:

- internal-only: `ell>=190537`;
- conditional on the external `R>=2^71` certificate:
  `ell>=49,547,666,544`.

For a genuine `g=2` balanced return, write the physical rows as `u,v`, with
boundary states `R<x=R+G`, and let `tau` be the rankwise late envelope. In the
nonzero-residue branch put

`d=gcd(H,epsilon)`, `h=H/d>1`, `E=epsilon/d`.

The content-`h` physical row starts at `hR`, the coprime-content shadow starts
at `hR-E`, and their signed gap changes from `+E` to `-E`.

## 2. Phase residue and first-crossing identities

At phase `j` write

`P_j=h p_j`, `S_j`, `delta_j=P_j-S_j`,

and let `c_j,t_j` be the physical and shadow prefix weights. The shadow
prefix equation gives

`2^j delta_j == 3^(t_j) E (mod h)`.                       (2.1)

Since `gcd(h,6E)=1`, every phase satisfies

`gcd(delta_j,h)=1`.                                       (2.2)

The exact integer prefix identity is

`2^j delta_j`
` =hR(3^(c_j)-3^(t_j))`
`  +h[Q(u[0:j])-Q(tau[0:j])]`
`  +3^(t_j)E`.                                            (2.3)

At the first physical-even / shadow-odd crossing put

`P=hp`, `delta=P-S>0`, `q=-delta'>0`.

Then `p` is even and

`h(2p+1)=3delta+2q`,                                      (2.4)

with `gcd(delta,h)=gcd(q,h)=1` and

`(3delta+2q)/h == 1 (mod 4)`.                             (2.5)

These local conditions do not restrict `h`: for every allowed `h` and every
positive even `p`, the pair `P=hp`, `S=hp-1` realizes such a strict reverse
crossing. Therefore any closing theorem must consume the global suffix or
ordinary ownership.

Classification: **proved analytic mathematics plus exact method barrier**.

## 3. Rankwise suffix dominance

Cut immediately after the first crossing. Let the remaining physical and
shadow suffixes be `alpha,beta`, with common length `n`, weights `A,B`, and
outstanding prefix lead `c=B-A>=0`.

If their one positions are `a_1<...<a_A` and
`b_1<...<b_(A+c)`, global rankwise lateness gives

`b_(c+k)>=a_k` for `1<=k<=A`.

Expanding the numerators by rank proves

`Q(beta)>=Q(alpha)`,                                      (3.1)

with equality exactly when `c=0` and the suffix words agree.

At the row endpoint the shadow exceeds the physical trajectory by `E`, so

`2^n E`
` =hp'(3^B-3^A)+3^B q+h[Q(beta)-Q(alpha)]`.

All terms besides `3^Bq` are nonnegative. Hence

`3^B q<=2^n E`.                                          (3.2)

Consequences:

- a terminal crossing has `q=E`;
- a nonterminal suffix with `3^B>2^n` has `q<E`;
- `q>=E` forces the remaining physical and shadow suffixes to be
  dyadic-dominant;
- equality in (3.2) forces `c=0`, `alpha=beta`, `3^B|E`, and `2^n|q`.

Classification: **proved analytic support-independent necessary condition**.

## 4. Least-root transport for the ordered branch

Root the full binary word of length `2a`, weight `2ell`, at the global least
odd state. Let `C(n)` count ones before half-step phase `n` and define

`F(n)=aC(n)-ell n`.

RL135.2 says the accelerated one positions `p_j` satisfy

`p_j<=floor(aj/ell)`.

If `c=C(n)`, then `n<=p_c<=floor(ac/ell)`, proving

`F(n)>=0` for every phase.                                (4.1)

Because `gcd(a,ell)=1`, zeros in one full period can occur only at phases
`0,a,2a`; the phase-`a` zero is exactly a least-rooted balanced return.

Now take an `epsilon=0` balanced cut at phase `s`, with late row `u` and early
row `v`. Their prefix counts obey `C_u(j)<=C_v(j)`, and balanced endpoints
give

`F(s+j)<=F(s+a+j)`.                                       (4.2)

If the least root lies in `v`, the right side equals zero at its offset;
(4.1) forces the paired phase in `u` also to be zero. Thus a least-rooted
balanced return exists. Otherwise the least root lies in `u`.

Re-cutting at the least root need not preserve `epsilon=0` or rankwise order;
the RL317 dichotomy must be recomputed there.

Classification: **proved analytic branch contraction**.

## 5. Root-aligned quantitative caps

Assume a balanced boundary is the least odd state `m`. RL135 gives `m<2^75`,
and RL318 gives

`G/m<exp(Delta)-1`.

The exact rational-log verifier proves

`Delta<log(1+2^-40)`,

so

`0<G<2^35`,                                               (5.1)

and RL21's first-difference valuation gives

`first_difference=v2(G)<=34`.                             (5.2)

In the nonzero-residue case, positivity of the early envelope numerator is

`q_sigma=V-epsilon>0`, with `V=D0m-YG`.

Therefore

`epsilon<V<D0m<D0 2^75`.

Also

`D0/H=tanh(Delta/2)<Delta/2<2^-41`.

For `epsilon=kappa H+r`, `0<r<H`, this proves

`0<=kappa<2^34`.                                         (5.3)

Classification: **proved analytic consequences plus exact rational-interval
certificate**.

## 6. Late-row-root scaled contact

In the remaining ordered subbranch the least root lies strictly inside the
late row at positive interface lead `s>=1`. Re-cutting at the least state
gives half-word weights `ell+s` and `ell-s`.

Let `y` be the antipodal state and set `K=y-3^s m`. The two half-word
equations give

`U=3^sD0m+XK`,

`3^sV=3^sD0m-YK`.

Positivity and the first-survivor logarithmic bound imply

`|K|<3^s2^35`.                                           (6.1)

Every positive-weight binary numerator is nonzero modulo `3`. Reducing the
first equation modulo `3` therefore gives

`K!=0 (mod 3)`.                                          (6.2)

The available inputs do not bound `s`; the band (6.1) grows like `3^s`.

Classification: **proved analytic normal form plus exact method boundary**.

## 7. Verification and evidence

Portable verifiers:

```sh
python3 -I verification/verify_rl319_crossing_residue.py
python3 -I verification/verify_rl319_suffix_dominance.py
python3 -I verification/verify_rl319_ordered_root_transport.py
python3 -I verification/verify_rl319_root_aligned_caps.py
python3 -I verification/verify_rl319_late_row_scaled_contact.py
```

All pass. The two rational-log comparisons are exact finite arithmetic.
Bounded word and state loops are regression evidence only.

## 8. Open obligations

1. Bound or consume the late-row interface height `s` using genuine `D0`
   ownership, physical packing, or a contact theorem beyond height one.
2. Consume the root-aligned finite caps `G<2^35` and `kappa<2^34` without
   restarting a fixed-depth prefix scan.
3. Preserve separate internal and external-conditional frontiers.
4. Keep `g=1` separate.

Gate A: OPEN.
Gate B: OPEN.
Global positive non-trivial-cycle exclusion: OPEN.
No Collatz-conjecture claim is made.
