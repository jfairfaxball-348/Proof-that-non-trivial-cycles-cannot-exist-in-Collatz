# RL144 — RL143 run-fibre population repair and corrected height-one floor

Date: 2026-08-28

## 0. Outcome and classification

RL144 is a **stop-and-repair** session triggered while beginning the inherited
RL144 target.

The promoted RL143 height-one multiplicity-interval exclusion is demoted and
retracted. Its lower-width step treated the RL123 CRT boundary population at
depth `(j,k)=(2,1)` as if it were the RL122/RL123 two-odd-window population
`O_2`. These are different statistics once an odd run can have length greater
than two.

The invalid RL143 step was

`C_(2,1) = O_2 = gL-t`,

followed by

`W >= 18(g(2L-A)-1)`.

RL123 actually defines

`C_(2,1) = #{odd runs of length at least 2 whose following zero run has length at least 1}`,

whereas

`O_2 = sum_i max(o_i-1,0)`.

For an odd run of length four, for example, the run contributes one
`C_(2,1)` boundary but three `O_2` starts. Therefore the mod-18 CRT theorem
cannot multiply the whole `O_2` population by 18.

RL144 promotes two repaired analytic statements:

1. **RL144.1 — height-one ordinary odd runs have length at most four.**
2. **RL144.2 — corrected height-one CRT floor**

   `W >= (162/13) ( g(2L-A) - 3 )`.

The accompanying exact rational certificate shows that, even granting the
carried RL143 physical upper-width estimate and using the stronger exact RL137
least-state ceiling, this corrected floor does **not** contradict the upper
bound anywhere in the inherited one-defect range
`1 <= g <= 771,316,334,039`.

That last statement is a **method-barrier certificate**, not evidence that a
cycle exists. It says only that the repaired version of this particular
run-fibre/state-ceiling comparison excludes no multiplicity by itself.

No Gate A or Gate B status changes. No global nontrivial-cycle exclusion is
claimed. The Collatz conjecture is not proved.

## 1. Incoming constants and preserved state

The inherited first reduced survivor remains

`(A,L) = (217,976,794,617, 137,528,045,312)`.

Put

`K = 2L-A = 57,079,296,007`.

The inherited one-defect multiplicity ceiling remains

`G = 771,316,334,039`.

RL137's all-nonnegative least-state theorem remains available:

`m < 2^75`,

and, more sharply in its proof,

`m < R/(3 Delta)` with `R < 99,205,514,478`.

RL122.1--RL123.5 remain unchanged. RL139--RL142 remain unchanged: they exclude
specified compressed, one-deviant, consecutive-interface, and cyclic-interface
height-one contact families, but not arbitrary scattered contact support.

Only the RL143 interval exclusion is demoted here.

## 2. Exact population mismatch

Write the ordinary cyclic parity word in alternating positive runs

`1^(o_1)0^(z_1) ... 1^(o_t)0^(z_t)`.

Because every `z_i >= 1`, RL123's depth-2, one-zero boundary count is simply

`C_2 := C_(2,1) = #{i : o_i >= 2}`.                       (2.1)

But the two-odd-window count is

`O_2 = sum_i max(o_i-1,0)`.                               (2.2)

Thus `C_2 <= O_2`, with equality only when every odd run has length at most
two. RL143 established only `a_j in {1,2,3}` from the height-one defect
hypothesis; that does not force ordinary odd runs to have length at most two.

The mismatch is load-bearing because RL123.2 puts the **boundary states** in a
single class modulo 18, while RL122.2 puts all `O_2` endpoints only in a class
modulo 9. Interior two-odd endpoints and terminal two-odd endpoints have
different parity and cannot all be promoted to the same mod-18 class.

## 3. RL144.1 — height-one ordinary odd runs have length at most four

Let

`c_j = floor(A(j+1)/L) - floor(Aj/L)`

and in the height-one branch let `h_j in {0,1}` with

`a_j = c_j + h_j - h_(j+1)`.

Since `L < A < 2L`, every `c_j` is 1 or 2.

Moreover `2(A-L) > L`, equivalently `2A > 3L`. Therefore the binary
mechanical increment `c_j-1` has density greater than one half, and two
consecutive values `c_j=c_(j+1)=1` are impossible. Directly, if both were 1,
then

`floor(A(j+2)/L)-floor(Aj/L)=2`,

whereas subtracting the baseline `2` would force two consecutive zero
increments of slope `(A-L)/L > 1/2`, impossible because their two-step floor
increment is at least one.

Now inspect an edge with `a_j=1`.

- If `c_j=1`, validity forces `h_(j+1)=h_j`; a rise would give `a_j=0` and a
  fall gives `a_j=2`.
- If `c_j=2`, `a_j=1` forces the unique transition `h_j=0 -> h_(j+1)=1`.

Hence a consecutive string of `a_j=1` edges contains at most one `c_j=2`
edge: that edge is a rise to height one, and a second `c=2` edge could not
again be a rise without an intervening fall, which itself is not an `a=1`
edge. But the `c=1` edges are never consecutive. Therefore there cannot be
four consecutive `a=1` edges.

An ordinary odd run of length `r` contains `r-1` consecutive accelerated gaps
with exponent `a=1`. Consequently

### Theorem RL144.1

Every ordinary odd run in a height-one full-count exponent profile has

`1 <= r <= 4`.                                            (3.1)

Classification: **analytic structural theorem**. This is a statement about
height-one exponent profiles; it does not assert affine cycle ownership.

The bound is genuinely stronger than what RL143 used, but it still permits
runs of length three or four, so it does not repair the old population
identity.

## 4. RL144.2 — corrected CRT population floor

For a hypothetical primitive ordinary cycle in the height-one branch, define

`C_r = #{odd runs with length at least r}`, `r=2,3,4`.

Every following zero run has length at least one. RL123.2 therefore gives the
three valid boundary-fibre floors

`W >= 18 (C_2-1)`,                                        (4.1)

`W >= 54 (C_3-1)`,                                        (4.2)

`W >= 162(C_4-1)`.                                        (4.3)

If some `C_r=0`, the corresponding displayed right side is negative and the
inequality remains trivially true because `W>=0`.

Because RL144.1 gives odd-run lengths at most four, the exact tail-sum identity
is

`gL - t = C_2 + C_3 + C_4`.                               (4.4)

There are `t` positive zero runs with total zero count `g(A-L)`, so

`t <= g(A-L)`

and hence

`C_2+C_3+C_4 >= g(2L-A) = gK`.                            (4.5)

Take the convex combination of (4.1)--(4.3) with weights

`9/13, 3/13, 1/13`.

The three coefficients equalize:

`(9/13)18 = (3/13)54 = (1/13)162 = 162/13`.

Therefore

`W >= (162/13)(C_2+C_3+C_4-3)`

and by (4.5):

### Theorem RL144.2 — repaired height-one run-fibre floor

`W >= (162/13)(g(2L-A)-3)`.                               (4.6)

Classification: **analytic global ordinary-owned physical lower bound**, under
the same hypothetical primitive-cycle and height-one premises needed for the
RL123 CRT boundary theorem.

This replaces, and is strictly weaker than, the invalid RL143 coefficient-18
floor.

## 5. Exact method-barrier comparison

To test whether (4.6) still closes any part of the inherited multiplicity
range, RL144 intentionally gives the route every favorable carried constant
available.

Use the exact RL137 proof constant

`R < 99,205,514,478`

and its implication

`m < R/(3 Delta)`.

Also grant the carried RL143 height-one physical estimate

`W < 6 exp(g Delta) m`.                                   (5.1)

Using the rigorous logarithm enclosure

`Delta_lo < Delta < Delta_hi`

and `exp(x) <= 1/(1-x)` for `0<=x<1`, obtain the certified comparison ceiling

`U(g) = 6 * [99,205,514,478/(3 Delta_lo)] / (1-g Delta_hi)`. (5.2)

For every integer

`1 <= g <= 771,316,334,039`,

`g Delta_hi < 1`.

The ratio of the repaired lower floor to this ceiling is a concave quadratic
factor after clearing the positive denominator. Its exact integer maximum is
attained at one of the two integers adjacent to its rational vertex. The
carried verifier checks both and certifies

`max_g  [(162/13)(gK-3)] / U(g)
 < 0.896241 < 1`,                                         (5.3)

with the maximizing integer

`g = 556,387,125,038`.

Thus the repaired CRT floor and the favorable carried state ceiling do not
contradict one another anywhere in the full inherited one-defect range.

Equivalently, at the best point this route needs approximately an 11.58%
stronger lower-width coefficient (or an equivalent tightening elsewhere) to
reach equality. This percentage is diagnostic only; it is not a new proof
obligation by itself.

Classification: **exact rational method-barrier certificate**.

## 6. Correction/demotion ledger

### Demoted / retracted

**RL143 height-one multiplicity-interval exclusion**

`303,279,262,681 <= g <= 771,316,334,039`

is no longer authoritative as an exclusion theorem.

Reason: its equation (1) used the false population identification
`C_(2,1)=O_2`. The numeric verifier checked the resulting inequality but did
not verify the combinatorial identification, so the verifier passing does not
rescue the theorem.

### Preserved

- RL122 and RL123 run-fibre theorems and their exact definitions;
- RL137 all-nonnegative least-state ceiling;
- RL138 local-defect method barrier;
- RL139 compressed-path obstruction;
- RL140 one-deviant contact obstruction;
- RL141 consecutive-interface obstruction;
- RL142 cyclic-interface obstruction;
- inherited first reduced survivor and multiplicity ceiling.

No other theorem is demoted by this repair.

## 7. Mandatory red teams

### Population-semantics red team — PASS after repair

RL144 never substitutes a window count `O_r` for a boundary count `C_(r,1)`.
Every mod-`2*3^r` spacing is applied only to actual odd-to-even run boundaries.

### RL20 / full ownership — PASS

The physical width lower bounds are invoked only for a hypothetical actual
primitive ordinary cycle. The structural run-length lemma itself does not
pretend that a defect profile is a cycle.

### RL79 generalized increment — PASS

No generalized-increment normalization is used to cancel the ordinary affine
increment. The repaired result consumes only the already ordinary-owned RL123
boundary theorem.

### RL81 physical versus quotient — PASS

Only actual cycle states are counted in the CRT fibres.

### Verification economy — PASS

The repair re-audits only the first invalid dependency and its immediate
numerical consequence. Historical expensive certificates are not rerun.

## 8. Open frontier and next target

After repair, the authoritative state is weaker than the incoming RL143 claim:

- no full multiplicity interval is excluded by the RL143 run-fibre route;
- height-one arbitrary scattered contact profiles remain open;
- lower multiplicities remain open;
- mixed-height profiles remain open;
- negative defects remain open;
- Gate A and Gate B remain globally open;
- global nontrivial-cycle exclusion remains open;
- Collatz remains open.

RL145 should first try to recover the lost height-one strength using a
**genuinely valid correlation** unavailable to the repaired tail-count bound.
The most promising inherited resources are:

1. the parity split of two-odd endpoints into boundary versus continuing-run
   classes;
2. RL140--RL142 full-ownership contact-polynomial obstructions, especially the
   still-open scattered-support case;
3. exact mechanical restrictions on where length-three and length-four odd
   runs can occur.

A useful quantitative target is to improve the effective corrected coefficient
`162/13 = 12.4615...` to at least about `13.9043` under the same upper-width
input, or obtain an equivalent gain from a smaller state/width ceiling.

If that route hits a proved barrier, resume the inherited mixed-height and
negative-defect branches rather than restoring the invalid RL143 population
shortcut.
