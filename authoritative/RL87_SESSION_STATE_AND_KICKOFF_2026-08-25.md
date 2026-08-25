# RL87 SESSION STATE AND RL88 KICKOFF

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

The exact first-Farey branch is now much narrower than the global Gate-A ledger.

## Incoming RL87 gate

Before RL87 mathematics:

- RL87 outer SHA-256: PASS;
- RL87 fresh internal manifest: PASS;
- RL86 fast verifier: PASS.

The frozen RL86/RL85 ledger was accepted under the verification-economy rule.

## RL87 main theorem state

### Physical synchronized difference

At height one,

`J=3A-B+1`.

Put

`delta=B-A`.

Across synchronized physical columns,

`00: delta -> delta/2`,

`11: delta -> 3delta/2`.

Hence a genuine synchronized block of length `n` satisfies

`2^n | delta_entry`.

For the primitive paired physical trajectories, `delta_entry!=0`, so

`2^n <= |delta_entry| <= M-R < M`.

With `alpha=(J-1)/2`, every such block has the exact entry form

`A=alpha+2^(n-1)m`,

`B=alpha+3*2^(n-1)m`.

For a maximal height-one block exiting by mismatch, `m` is odd and

`n=v_2(B-A)`.

### First-Farey physical block cap

RL85 gives

`M<400,000,000,000(3/2)^72,057,431,991`.

Using

`3^1,000,000<2^1,584,963`

and

`400,000,000,000<2^39`,

every genuine synchronized block in the exact first-Farey/full-phase intersection has

`boxed: n<=42,150,931,628.}`

### RL73 low-k intersection eliminated

RL73 forces one maximal post-first-mismatch height-one synchronized block with at least

`40,249,491,324,522,944`

aligned `00` columns in every hypothetical odd `27<=k<=165` Gate-A violation.

That block is impossible under the first-Farey block cap.

Therefore the exact first-Farey/full-phase intersection contains no such low-`k` violation.

This does **not** close the same `k` band globally; the first-Farey maximum cap is branch-specific.

### General first-Farey lower k bound

Using RL73's global skew/count identities, any Gate-A violation on the exact first-Farey branch must satisfy

`k>=156,601,916`.

Since even `k` is already closed,

`boxed: k>=156,601,917, k odd.}`

### First-Farey upper k bound

RL81 terminal ownership gives

`B_j=2^(k-2)N`.

With inherited `N>=2^71` and `B_j<=M`, the first-Farey physical cap gives

`boxed: k<=42,150,931,559.}`

### Surviving exact first-Farey Gate-A window

Any remaining Gate-A violation on this branch must have odd

`boxed: 156,601,917 <= k <= 42,150,931,559.}`

No direct enumeration is selected.

## Quotient finite-fiber audit

For fixed `J`, physical lifts satisfy

`max(R,ceil[(J+R-1)/3]) <= A <= min(M,floor[(J+M-1)/3])`.

Multiplicity is at most

`floor[(M-R)/3]+1`.

The inherited `930,959` distinct quotient states force only

`M-R>=232,740`

from raw range packing.  This is quantitatively useless at first-Farey scale.

The quotient-complexity theorem remains valid but is not the primary consumer on the eliminated low-`k` branch.

## Authoritative RL88 live obligation

Attack **multi-block dyadic valuation recycling** inside the surviving first-Farey window.

For the post-first-mismatch maximal height-one synchronized blocks, let

`n_r = block length`.

Each block obeys

`n_r<=42,150,931,628`,

and for a standard mismatch exit

`n_r=v_2(B_r-A_r)`.

RL73 still forces a large total number of height-one aligned `00` columns, but for high `k` that mass can be distributed over up to

`e<=H<k`

blocks.

RL88 must determine whether the active `01/10` excursions can repeatedly reset the common mode so as to regenerate high `v_2(B-A)`, or whether genuine full-`D` ownership imposes a non-recycling budget.

Preferred target forms:

- bound `sum_r n_r` by one physical/full-`D` resource;
- bound multiplicity of block entries with `v_2(B-A)>=t`;
- derive exact `N mod 2^t` constraints from block-entry normal forms and prove incompatibility across many blocks;
- use primitivity to forbid repeated reset data;
- or construct a rigorous common-mode family showing why no such global valuation budget follows from current information.

Mandatory red teams:

- RL81 common-mode freedom;
- RL79 generalized-increment homogeneity;
- RL20 address/physical separation;
- no `O(M)` state-count argument;
- no brute-force enumeration over the finite k window.

## Verification economy

After the RL88 bundle checksum, internal manifest, and fast RL87 verifier pass, accept this ledger.  Do not recursively rerun historical expensive certificates unless a dependency fails, a verifier fails, or an apparent contradiction triggers stop-and-repair.
