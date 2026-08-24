# RL45 Research Attack Prompt

Continue the Collatz RL/3n+1 research from the RL44 audit as a skeptical research mathematician. Do not extend the finite `e<=40` cutoff unless a computation is being used to test a uniform theorem.

The RL44 audit validated the RL43 theorem/certificate layer and promoted the one-excursion `e<=40` phase computation to an exact finite certificate. The surviving branch remains the inherited near-resonant order-2 / `g=2`, `G=4` balanced-return branch.

## Primary target: terminal valuation theorem

For a canonical positive excursion entering physical gap 9, prove or falsify

`v2(D_E - 9*3^p) <= rho_E`.

Here `p` is excursion weight, `rho_E` transport area, and `D_E=Q(alpha)-Q(beta)>0`.

In the live one-excursion branch,

`D_E=2^a+3^ell`, `p=ell-2`,

so the left side is exactly `a`. Thus the theorem immediately implies

`rho_E>=a`, equivalently `e>=q+2`, `q=a-ell`.

Use the RL44 reduction of the `J/K` candidate. With

`H=e-z+1=rho_E-h+1`,

`J_d=T+3^d-2^d`,

`K=H+d(d+1)/2-1`,

all transition laws are known, and any divisibility counterexample at height `d>1` descends through compatible `10` steps to a height-one counterexample with the same normalized quotient. Therefore focus first on the terminal statement

`v2(T+1) <= H`

for positive terminal states, especially when `T+1` is a power of two. Do not insist on proving the stronger all-state invariant if a terminal-only proof is available.

Red-team aggressively. The unconditional strengthening `J_d<=2^K` is false; RL44 found a reachable counterexample `(d,e,T,H,K,J)=(1,30,4858,12,12,4859)`. Finite tests of the actual candidate through `e<=40` found no violation, but that is evidence only.

## Parallel target: quantitative radius-3 transplant

Let

`f(T)=3T^q-2`,

`P(T)=4+3 sum(T^b-T^c)`,

with `c-b=kq` for each run pair.

The exact comparator

`L(T)=2T^ell-1`

satisfies

`|Res(f,L)|=2^a-3^ell=X-Y`.

Since `X-Y|Res(f,P)` and `gcd(X-Y,3)=1`, it is enough to prove a 3-free resultant bound

`0 < |Res(f,P)|_(3') < X-Y`.

Exploit `c-b=kq` before applying any crude root bound. Modulo `f`, every pair collapses to one exponent class modulo `q` with a positive rational coefficient. Derive an exact reduced polynomial of degree `<q`, track coefficient heights and 3-adic content, and identify the sharp obstruction to beating the comparator resultant. The goal is a genuine RL19-style uniqueness theorem, not another finite residue scan.

Remember the key audit distinction: RL19 `k=1` worked modulo the large cubic cofactor `C=X^2+XY+Y^2`; RL43 works modulo the smaller factor `X-Y`. The same binomial anchor is real, but the quantitative lemma must be substantially sharper.

## Third target: multiple excursions

If time permits, derive the full-denominator `X-Y` phase relation for `N>1`. Seek support and coefficient complexity controlled by `E+N`, and determine whether each excursion still contributes phase pairs separated by multiples of `q`. This is required for eventual full branch closure unless another theorem forces `N=1`.

## Evidence discipline

Keep separate:

- analytic theorem;
- exact finite certificate;
- inherited dependency;
- external input;
- computational evidence;
- conjecture.

Do not import the external `R>=2^71` floor or LMN-dependent older radius-3 leaves unless explicitly needed and labelled. The specific RL19 cubic-skew `k=1` comparison is analytic and does not use LMN.

At the end, report whether the terminal valuation theorem was proved, weakened, or falsified; what the reduced resultant calculation reveals; and whether either route materially advances a uniform closure of the surviving RL branch.
