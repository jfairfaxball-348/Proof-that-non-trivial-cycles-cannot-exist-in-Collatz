# RL88 SESSION STATE AND RL89 KICKOFF

Date: 2026-08-25

## Frozen global status

- radius-3 primitive/full-`D`: closed local theorem;
- Gate A even terminal `k`: closed analytically;
- Gate A terminal `k<=25`: closed by inherited exact finite certificate;
- Gate A odd `k>=27`: open globally;
- Gate A globally: open;
- Gate B globally: open;
- RL/nontrivial-cycle exclusion: open;
- Collatz conjecture: not proved.

The exact first-Farey branch is narrower, but it is not promoted to global Gate A.

## Incoming RL88 gate

- outer SHA-256: PASS;
- fresh internal manifest: PASS;
- RL87 fast verifier: PASS.

Verification economy was applied; no historical expensive suite was recursively replayed.

## Frozen RL88 main results

### Exact complete-excursion reset

For a complete height-one excursion of length `L`, with equal x/y odd count `r`,

`delta_next = [3^r delta_prev + K]/2^L`,

where `|K|<2^L3^r` and `K` is determined only by the two ordinary `+1` parity words.

The physical common mode cancels over the complete excursion.

### Aggregate reset budget

For the post-first-mismatch height-one synchronized blocks, let

- `z` = total height-one `00` count;
- `s` = total height-one `11` count;
- `Q=z+s` = total block length;
- `b` = number of blocks;
- `R` = total x-odd count in the complete excursions preceding them.

Then

`z-(log_2 3-1)s < log_2 M + (log_2 3)R + b`.

RL73 area gives

`R<=e+u_11`, `b<=e`, `e+u_00+u_11<=H<k`.

Splicing with

`Delta-2k+7=P+2c00+-c11++e`,

`Delta>=13,201,833,154,443,526,323`,

and the RL87 block cap

`C=42,150,931,628`

yields a new necessary first-Farey terminal bound.

### New first-Farey Gate-A window

Any surviving violation on the exact first-Farey/full-phase branch must have odd

`boxed: 2,921,384,819 <= k <= 42,150,931,559.}`

The old RL87 odd lower endpoint `156,601,917` is superseded on this branch.

### Near-capacity rigidity at the new lower endpoint

At

`k0=2,921,384,819`,

any survivor must satisfy

`Q>=123,139,091,657,887,804,990`.

Consequently:

- at least `k0-2=2,921,384,817` nonempty height-one synchronized blocks;
- `H>=k0-2`, hence `H in {k0-2,k0-1}`;
- average over `k0-1` possible block slots at least `42,150,931,605=C-23` (floor);
- at least `225,242,372` actual blocks have `n>=C-23`;
- for those blocks `delta=2^n m` has `|m|<2^24`;
- among all deficit values `0..23`, some exact signed `(deficit,m)` type repeats at least 7 times.

Repeated difference data is not yet a primitivity contradiction.

### Full-D congruence result and barrier

At a height-one block entry after `i` internal columns,

`2^(i+2)(B_i-A_i)=3^p(9N+61)+4(Q_y-Q_x)`.

Thus `2^n|(B_i-A_i)` forces one explicit class

`N == c (mod 2^(i+n+2))`.

But the paired parity prefix through the end of that block already fixes `N` modulo `2^(i+n+3)`.

Therefore successive high-valuation `N` congruences are nested cylinder information, not independent CRT constraints.  Since `D` is odd, full-`D` multiplication does not change that conclusion.

### Local red-team family

A minimal `01,10` excursion can regenerate arbitrary next block valuation `t`, for every `t>=1`, with an unbounded common-mode shift.  Therefore no local per-reset prohibition is available.

## Authoritative RL89 live obligation

Exploit **near-capacity block rigidity**.

The productive new regime is not “can reset valuation be large?”—it can.  The question is whether a genuine primitive first-Farey/full-`D` cycle can sustain billions of almost-maximal blocks while the area budget is within one unit of saturation and the odd entry cofactors live in tiny ranges.

Priority interfaces:

1. characterize the cases `H=e=k-1`, `H=e=k-2`, and `H=k-1,e=k-2`; these force all or almost all complete excursions to be minimal;
2. derive exact cofactor recurrences for minimal `01,10` resets;
3. use multiplicative order of `3 mod 2^t` plus small `m` to bound high-reset multiplicity;
4. add a common-mode selector (`J`, `L`, full-`D` content, primitive phase position) so repeated difference types become repeated paired-state data;
5. red-team any such selector against RL81 common-mode freedom and the explicit RL88 local family.

Do not restart the now-dead independent midpoint-congruence accumulation route.

## Verification economy

After the RL89 bundle checksum, internal manifest, and fast RL88 verifier pass, accept this ledger.  Do not recursively rerun historical expensive certificates unless a new proof depends on an unresolved historical definition, a verifier fails, or an apparent contradiction triggers stop-and-repair.
