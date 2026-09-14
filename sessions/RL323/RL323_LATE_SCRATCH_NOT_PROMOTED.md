# RL323 late scratch preserved after concurrent closeout

Date: 2026-09-14
Status: UNPROMOTED CARRYOVER SCRATCH — MUST BE REDERIVED/VALIDATED IN RL324 BEFORE USE

## Why this file exists

RL323 was atomically promoted on `main` while the connector closeout was still completing. The promoted RL323 ledger correctly contains the phase-aligned physical `H`-carry theorem, full `D0/H` ownership identities, zero-carry matched-rank crossing, bottom-third residual, narrow prefix window, and the conditional bound

`r<=77265916075`.

A later in-session derivation had not yet reached the promoted tree. To avoid losing potentially promotion-grade progress while also respecting the closed RL323 proof state, that derivation is preserved here as **scratch only**.

It is not an RL323 theorem and must not be cited as authoritative until RL324 rederives and red-teams it.

## Candidate adjacent-rank bridge

At the promoted zero-carry matched rank `j`, RL323 proves

`z=2^r P_j+eta`,
`0<eta<2^r/3`,

where `r=u_j-v_j` and `z` is the physical state at the `j`-th early-row odd rank.

Define the standard interior matched-rank defect

`Delta_j=2^(d_j) P_j-Q_j`,
`d_j=u_j-v_j`,

with `Q_j` the physical state at `v_j`. Thus at the zero-carry rank the candidate identification is

`Delta_j=-eta`.

For an interior rank `j<ell`, with

`a_j=u_(j+1)-u_j`,
`b_j=v_(j+1)-v_j`,
`d_(j+1)=d_j+a_j-b_j`,

the ordinary odd-to-odd equations give the exact interior recurrence

`2^(b_j) Delta_(j+1)=3 Delta_j+2^(d_j)-1`.

Substituting `Delta_j=-eta` gives

`2^(b_j) Delta_(j+1)=2^r-1-3eta`.

Because `eta<2^r/3`, the right side is nonnegative. The late scratch argued equality cannot persist: if `Delta_(j+1)=0` and `d_(j+1)>0`, parity is impossible because `2^(d_(j+1)) P_(j+1)` is even while the matched odd state is odd; if `d_(j+1)=0`, equality of the matched physical odd states would contradict primitivity. Hence the candidate conclusion is

`Delta_(j+1)>0`.

Moreover

`Delta_(j+1)<2^(r-b_j)=2^(d_(j+1)-a_j)`.

Therefore the next early-row physical state would have the Euclidean form

`Q_(j+1)=2^(d_(j+1))(P_(j+1)-1)+eta_(j+1)`

with complementary residual

`nu_(j+1)=2^(d_(j+1))-eta_(j+1)=Delta_(j+1)`

and

`0<nu_(j+1)<2^(d_(j+1)-a_j)<=2^(d_(j+1)-1)`.

Equivalently, the candidate bridge is

`floor(Q_(j+1)/2^(d_(j+1)))=P_(j+1)-1`.

## Interior-rank prerequisite

The late scratch also observed that the promoted zero-carry theorem gives crossing height `h>=2`. At the final late-row odd rank `u_ell`, the early-row lead satisfies `c_t<=1`. Hence the crossing rank should satisfy

`j<ell`,

so the next matched rank exists and the interior recurrence can be used without reviving the withdrawn cyclic-wrap claim.

This point must be checked explicitly in RL324 before the adjacent-rank bridge is promoted.

## Conditional sign observation

At the exact first external survivor, the late scratch further observed that the next physical state satisfies `P_(j+1)>=m>=2^71`; the exact first-survivor logarithmic enclosure makes

`D0 P_(j+1)-X>0`.

Thus, if the adjacent-rank bridge is validated, it appears to land directly in the surviving positive canonical sign regime.

This final sign statement is externally conditional and is not promoted here.

## RL324 use

The first RL324 action should be to rederive this bridge from the frozen RL323 definitions and red-team:

1. state alignment (`Q_j=z` at the matched rank);
2. proof that `j<ell`;
3. exclusion of the `Delta_(j+1)=0` equality case;
4. Euclidean quotient/remainder orientation;
5. scope of the positive-sign observation.

If all five pass, promote the adjacent zero-carry -> unit-minus-one pair as the first RL324 structural lemma and immediately consume the two neighboring genuine `D0/H` ownership pairs toward the parent-level closure target.

Do not turn this scratch into a support-enumeration programme.
