# RL29 session results to audit

Date: 2026-08-21

## 1. Exceptional setting

Retain the inherited weak sector

`R == 91 mod288`, `G=12`, `H=4`,
`B=2^b`, `Y=3^e`, `z=B/Y`, `Y<B<2Y`.

Let

`u_j=T^j(R)`,
`v_j=T^j(R+12)`,
`w_j=T^j(R+4)`.

The three balanced blocks have common length `b`, common odd count `e`, and cyclic endpoints

`u_b=R+12`, `v_b=R+4`, `w_b=R`.

## 2. Stronger finite least-state lift

Starting from the inherited root class and enforcing leastness simultaneously on the three starts through the relevant ten-step lift gives only two unbounded residues modulo `1024`, namely `155` and `667`; these are the same class modulo `512`. The only other surviving finite branch is bounded to `R=91`, whose actual orbit later drops below 91.

Thus a genuine large survivor must satisfy

> `R == 155 mod512` and `R==1 mod9`, hence `R==667 mod4608`.

The candidate `R=667` also drops below itself, at step 24 (`572<667`). Therefore

> `R>=5275`.

The nine-bit prefixes are forced:

- `u: 110111101`,
- `v: 111011011`,
- `w: 111110111`.

At `s=6` all three prefix odd counts equal 5 and

`u_6=(243R+287)/64`,
`v_6=(243R+3167)/64`,
`w_6=(243R+1183)/64`,

so the synchronized gaps relative to `u_6` are

> `(45,14)`.

At `s=9`, `u,v` resynchronize pairwise with odd count 7 and

> `v_9-u_9=51`.

## 3. Exact recovery of `B-Y`

At an equal-count synchronized rotation `s`, rotate all three balanced blocks by `s`. Define

`U_s=Bv_s-Yu_s`,
`V_s=Bw_s-Yv_s`,
`W_s=Bu_s-Yw_s`.

Then

`A_s:=U_s+V_s+W_s=(B-Y)S_s`,
where `S_s=u_s+v_s+w_s`.

At `s=0,2,6`, direct calculation gives

`4S_2-9S_0=15`,
`64S_6-243S_0=749`,

and `gcd(15,749)=1`. In fact

`200S_2-207S_0-64S_6=1`.

Therefore

> `gcd(A_0,A_2,A_6)=B-Y`,

and explicitly

> `B-Y=200A_2-207A_0-64A_6`.

This supplies the absolute mode missing from the purely relative RL21 Fourier argument.

## 4. Exact recovery of the relative Eisenstein factor

Let `w^2+w+1=0` and

`F_s=U_s+wV_s+w^2W_s`.

At synchronization,

`F_s=(B w^2-Y) alpha_s`,
where
`alpha_s=u_s+w v_s+w^2w_s`.

Writing the physical synchronized gaps as `(G_s,H_s)=(v_s-u_s,w_s-u_s)`,

`alpha_s=-H_s+(G_s-H_s)w`.

Thus

`alpha_0=-4+8w`, with norm `112`,
`alpha_6=-14+31w`, with norm `1591=37*43`.

Since `gcd(112,1591)=1`, the two `alpha` values are coprime in the Eisenstein integers. An explicit Bezout identity is

> `(-19-11w)alpha_0+(5+3w)alpha_6=1`.

Hence

> `(-19-11w)F_0+(5+3w)F_6=B w^2-Y`.

Equivalently the physical numerators give

`B = 11U_0+8V_0-19W_0-3U_6-2V_6+5W_6`,

`Y = 8U_0-19V_0+11W_0-2U_6+5V_6-3W_6`.

The norm is

`N(Bw^2-Y)=B^2+BY+Y^2`.

Since `gcd(B-Y,B^2+BY+Y^2)=1` here, the forced rotations exactly own the two coprime factors of

`B^3-Y^3=(B-Y)(B^2+BY+Y^2)`.

**Important:** this factor ownership does not itself import the radius-3 sparse theorem, because the rotated block numerators can be dense.

## 5. Proposed `e>=67` strengthening

At `s=9`, the remaining `u,v` tails have equal length `b-9` and equal odd count `e-7`.

For a trajectory segment, the standard odd-correction product satisfies

`P = (2^L/3^m)*(endpoint/start)`.

Taking the ratio of the two tails gives

`K_9(R)`
`=((R+12)(2187R+29143))/((R+4)(2187R+3031))`.

Every odd factor on the `u` tail is at most `1+1/(3R)`, while the denominator tail product is >1. Hence

`K_9(R)<(1+1/(3R))^(e-7)`.

If `e-7<=59`, then

`(1+1/(3R))^(e-7)`
` <= (1+1/(3R))^59`
` <= 3R/(3R-59)`.

The last bound follows, for `59/(3R)<1`, from

`(1+x)^59 <= sum_{k>=0}(59x)^k = 1/(1-59x)`.

But

`K_9(R)-3R/(3R-59)`

has positive denominator and numerator

`1791R^2-2255057R-20633244`,

which is positive and increasing for `R>=5275`.

Therefore the proposed conclusion is

> `e>=67`.

## 6. Orbit-sum / unsynchronized-support identity

For any parity word of length `b` and weight `e`, let `p(j)` count odd bits before time `j`, and let `Q` be its affine numerator. Then

> `sum_{j=0}^{b-1} 2^j/3^{p(j)} = 4Q/Y + B/Y - 1`.

Apply this to the three balanced blocks. Put

`q_j=2^j/3^{p_u(j)}`,
`a_j=p_v(j)-p_u(j)`,
`c_j=p_w(j)-p_u(j)`.

Since

`Z_v=sum_j q_j 3^{-a_j}`,
`Z_w=sum_j q_j 3^{-c_j}`,

and `1+w+w^2=0`, one obtains

> `sum_j q_j(1+w3^{-a_j}+w^2 3^{-c_j})`
> `=4(z w^2-1)(-4+8w)`.

In the basis `1,w`, the right side is

`(48z+16)+(16z-32)w`.

If `(a_j,c_j)=(0,0)`, the summand is exactly zero. Thus synchronized aligned times do not contribute directly to the relative cubic mode.

The pairwise `u-v` projection is

> `sum_j q_j(1-3^{-a_j})=32z+48`.

More generally, at a pair synchronization `s` with common odd count `p`,

> `sum_{j<s}q_j(1-3^{-a_j})=48-4r_sG_s`,
where `r_s=2^s/3^p` and `G_s=v_s-u_s`.

A synchronized sign reversal `G_s<0` therefore requires the partial transport to exceed 48.

Since a positive term requires `a_j>0` and is bounded above by `q_j`, while

`q_j <= z(R+12)/R`,

the bounds `R>=5275`, `z<46/45` imply

`46*z(R+12)/R < 48`.

So the first synchronized `u-v` sign reversal requires at least

> 47 aligned times with `a_j>0`.

At each such time the larger-count trajectory is itself forced high; this is a useful constant-scale precursor to the global theorem below.

## 7. Proposed scaling theorem: `Omega(e/log e)` high columns

For every aligned phase of every one of the three blocks, define

`q_i(j)=2^j/3^{p_i(j)}`.

The correction-product monotonicity along a balanced block gives

> `R <= q_i(j)x_i(j) < z(R+12)`.

### Unsynchronized columns

If the three prefix counts are not equal, two of the corresponding `q_i` differ by a factor at least 3. Using the scaled interval and leastness, one gets

> `max(u_j,v_j,w_j) > 3R^2/[z(R+12)]`.

For `R>=5275`, `z<46/45`, this is

> `>2.928R`.

### Synchronized runs

At a triple synchronization, suppose the next `r` parity bits are common. Equal length-`r` parity vectors imply the three current states lie in the same residue class modulo `2^r`. Since they are three distinct integers, their physical span is at least `2^(r+1)`.

The common scaled states all lie in an interval of width

`W=z(R+12)-R`
`=R(z-1)+12z`
`<23e/90+552/45`.

Therefore

> `q*2^(r+1)<W`.

After `k` common steps, the synchronized scaling factor is at most `2^k q`, so

`q_{j+k}<W/2^(r+1-k)`.

If this is below `1/2.9`, then every one of the three states exceeds `2.9R`. Consequently a synchronized run has at most

`C(e)=ceil(log_2(2.9*(23e/90+552/45)))`

columns where all three states can stay at or below `2.9R`.

### Counting

Let `U` be the number of unsynchronized aligned columns among `0,...,b-1`. There are at most `U+1` synchronized runs. Let `H` count aligned columns containing a phase above `2.9R`.

Every unsynchronized column is high, so

`H>=U`.

Across the synchronized runs, at most `C(e)(U+1)` columns can be low, so

`H>=b-C(e)(U+1)`.

Optimizing the two lower bounds gives

> `H >= (b-C(e))/(C(e)+1)`.

Since `B>Y` implies

`b>log_2(3)e`, while `C(e)=O(log e)`, the proposed theorem is

> `H=Omega(e/log e)`.

The three aligned blocks partition the `3b` cycle positions, so these are distinct phases.

## 8. What this does and does not bridge

What changed relative to RL27:

- factor ownership: both absolute and relative order-3 factors are now recoverable from bounded forced rotations;
- scaling: the braid obstruction is no longer merely `O(1)`; the proposed theorem forces an unbounded number of high phases.

What is still missing:

1. `Omega(e/log e)` is not obviously enough to change an asymptotic packing coefficient by a positive constant;
2. a high phase can be even, while the strongest inherited product-packing estimates are formulated around odd states/odd correction factors;
3. the rotated `F_s` numerators are generally dense, so radius-3 sparse uniqueness does not automatically apply;
4. the global dependency DAG still needs an audit: eliminating this sector may or may not be the last logical step to RL.

The best next theorem target is therefore not “more residues.” It is a **weighted synchronization-budget lemma** strong enough to recover an `Omega(e)` product/packing gain, or an algebraic theorem converting the exact factor ownership into the already-closed sparse/radius-3 machinery.
