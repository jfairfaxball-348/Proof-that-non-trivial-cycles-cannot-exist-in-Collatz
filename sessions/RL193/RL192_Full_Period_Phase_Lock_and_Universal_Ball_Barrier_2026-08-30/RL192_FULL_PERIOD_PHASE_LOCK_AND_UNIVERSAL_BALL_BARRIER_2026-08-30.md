# RL192 — Full-Period Phase Lock and Universal-Ball Barrier

Date: 2026-08-30
Authoritative branch: sole high branch `(v,H,J,d)=(37,0,23,-1)`
Incoming authority: RL191 at commit `7e46d8dc2468bdfc0cf630425d7d079155adf577`

## 0. Outcome and classification

RL192 identifies the natural endpoint of the RL191 resonance route.  It does not extend the arbitrary finite cutoff.  Instead it proves an exact mechanical balance identity and evaluates the universal relaxed transport at the full chronological period `s=L`.

At that endpoint the necessary terminal overlap is all of the inherited extremal interval.  It splits at one exact rank into two exponent-sum atoms.  The corresponding zero-error affine centres are

`2^38 exp(-Delta)` and `2^37 exp(-Delta)`,

where `Delta=A ln 2-L ln 3` satisfies the exact rational certificate

`0<Delta<2^-40`.

Thus the permitted targets `2^38` and `2^37` miss the respective centres by less than `1/4` and `1/8`.  Every nonempty RL191 universal relaxed ball has radius at least `1/2`.  More strongly, setting every earlier relaxed error to zero and choosing only the final error requires magnitude below `1`, so both targets are explicitly admitted by the relaxation `|epsilon|<2`.

This is a **method barrier**, not a physical-realization theorem.  Actual errors are correlated height differences (with one carry term); arbitrary relaxed errors are not asserted to arise from a Collatz orbit.  The theorem proves that the universal bound and exact mechanical word alone cannot exclude the isolated/full-period case.  A successor must use the physical correlation among the `epsilon_i`, or an independent chronological/H21 consumer.

No branch, Gate, non-trivial-cycle, or global Collatz closure is claimed.

## 1. Frozen inherited state

Use the RL191 constants

`A=217976794617`, `L=137528045312`,
`B=A-L=80448749305`, `R=L-B=57079296007`,

and the necessary extremal terminal-rank interval

`E=[72797034370,103818202602]`.

For source rank `r_j=(r+jB) mod L`, the actual mechanical source bit is

`c_j=1` if `r_j<R`, and `c_j=2` otherwise.

RL191 proved the carry-completed relaxed transport

`2^{c_j} Delta_{j+1}=3 Delta_j+epsilon_j`, `|epsilon_j|<2`,

from terminal start value `Delta_0=3^37/2^21`.  At terminal separation `s`, the transition length is `n=s-37`, the zero-error centre is

`3^s/2^{21+S}`, where `S=sum_{j=0}^{n-1} c_j`,

and the two permitted later start gaps are `2^37` and `2^38`.

All RL191 scope locks remain active: necessary ranks are certificate states, total variation is not chronological excursion, and the H21 core remains open.

## 2. Exact mechanical exponent-sum identity

Adding `B=L-R` wraps precisely when `r_j>=R`.  Since `c_j-1` is the wrap indicator,

`r_{j+1}=r_j+B-L(c_j-1)`.

Summing for `j=0,...,n-1` gives

`r_n=r+nB-L(S-n)=r+nA-LS`.

Because `0<=r_n<L`, this proves the exact identity

`S=floor((r+nA)/L)`.

This controls the affine centre without enumerating the internal mechanical word.  It does not control the physical errors, whose correlations are the new open obligation.

## 3. Natural full-period phase lock

Set the terminal separation to the natural endpoint

`s=L`, `n=L-37`.

Since `(LB) mod L=0`, the necessary overlap is exactly `E`; this is the isolated/full-period periodic-copy case, not an assertion of two distinct realized terminals.

Put

`M=59L-37A=49013272579`,
`Q=L-M=(37B mod L)=88514772733`.

The interval `E` crosses `Q`.  From

`r+nA=(A-59)L+(r+M)`,

the exponent sum is constant on the two exact integer atoms:

- `r in [72797034370,88514772732]`: `S=A-59`;
- `r in [88514772733,103818202602]`: `S=A-58`.

Consequently the zero-error centres are respectively

`3^L/2^{A-38}=2^38(3^L/2^A)=2^38 exp(-Delta)`,

and

`3^L/2^{A-37}=2^37(3^L/2^A)=2^37 exp(-Delta)`,

where `Delta=A ln2-L ln3`.

This is an exact full-period phase lock.  It is derived from the natural period and the Diophantine mechanical identity, not from scanning a larger separation interval.

## 4. Exact target inclusion in the relaxed ball

The portable verifier encloses `ln 2` and `ln 3` by exact rational atanh series with rigorous tails and proves

`0<Delta<2^-40`.

For `Delta>0`, `0<1-exp(-Delta)<Delta`.  Hence

`2^38(1-exp(-Delta))<2^38*2^-40=1/4`,

and

`2^37(1-exp(-Delta))<1/8`.

The RL191 universal relaxed recurrence gives a final-step error contribution of radius `2/2^c`, at least `1/2` because `c` is `1` or `2`.  Both targets therefore lie strictly inside their corresponding relaxed balls.

There is also an explicit relaxed witness.  Set every earlier `epsilon_j` to zero.  At the final transition choose the sign toward the target and magnitude

`2^{c_{n-1}} * |target-centre|`.

Even for `c_{n-1}=2`, this magnitude is `<1` on the `2^38` atom and `<1/2` on the `2^37` atom.  It therefore obeys `|epsilon|<2`.

The witness is deliberately nonphysical: it uses only the relaxation and does not claim that an arbitrary final error equals an allowed height difference.  Its role is to prove insufficiency of the relaxed hypotheses.

## 5. Structural consequence and next obligation

The RL191 universal transport remains correct and valuable: it removed the mechanical seam and certified spacing through 1000.  RL192 shows exactly where a bound-only unbounded continuation fails.  At the full period the near-convergent relation `2^A/3^L=exp(Delta)` phase-locks the centre to the permitted target more tightly than even one relaxed error unit.

Therefore any proof excluding an isolated extremal triple must add at least one physical ingredient not present in the universal ball:

- the exact ordinary formula `epsilon_i=2^{-h_j}-2^{-h_i}` and its telescoping/correlation;
- the unique carry formula `epsilon_t=2-2^{-h_t}` and its forced location;
- a sign, valuation, incidence, recurrence, or ordering theorem for the physical height word;
- or an independent chronological/H21 consequence that rules out the necessary full-period pattern.

The certified `>480` ordinary corrected flow, `>80` directional `K` variation, and binding H21 `{33,34,35}` core remain open inputs.  RL192 does not infer excursion from variation and does not change the H21 charging budget.

## 6. Scope and status

Promoted:

- exact mechanical exponent-sum identity: **proved analytic mathematics**;
- full-period two-atom phase lock: **proved analytic mathematics**;
- `0<Delta<2^-40` and target-miss inequalities: **exact rational certificate supporting analytic mathematics**;
- relaxed single-error witness: **proved method barrier for the universal-bound-only route**.

Not promoted:

- physical realization of either relaxed witness;
- nonexistence or existence of an isolated/extremal triple;
- any cutoff extension beyond RL191's certified 1000;
- a chronological excursion or H21 incidence theorem;
- branch, Gate, non-trivial-cycle, or Collatz closure.
