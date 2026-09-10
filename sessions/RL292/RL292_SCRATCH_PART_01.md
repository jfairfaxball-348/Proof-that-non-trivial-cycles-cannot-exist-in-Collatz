# RL292 local checkpoint (NOT PROMOTED)

BASE_HEAD: 6133a02d8d141ce9714190e9c8772e904832f95b
Incoming: RL292 fixed-seed Bellman danger-set contraction
Status: local scratch / NOT PROMOTED

## Rank-1 homogeneous 010 predecessor tower

Let P(M)=(8M-10)/3. If M is even and M≡2 (mod 3), then J=P(M) is a positive even checkpoint with v2(3J+2)=3 and the exact cost-one macro word 010 sends J to M.

For odd terminal exponent k and j>=0 define
M_j(k)=2+(8/3)^j(2^k-2).
Whenever j <= v3(2^k-2)=1+v3((k-1)/2), M_j(k) is an integer and
M_j --010--> M_{j-1}
for j>=1, ending at M_0=2^k.
Each M_j (j>=1) satisfies M_j≡2 (mod 8), hence v2(M_j)=1.
Therefore V(M_j)>=k-j.

By LTE, arbitrary tower depth R occurs for k≡1 mod 2*3^(R-1); e.g. k=1+2*3^(R-1) gives an R-step tower. For R>=4 these lie in the current k>=25 odd regime.

## 2-adic singularity corollary

For fixed R and k in the above congruence class tending to infinity,
M_R(k) -> lambda_R = 2-2(8/3)^R in Z_2,
while V(M_R(k)) >= k-R -> infinity.
Thus V is not locally bounded at lambda_R. Since lambda_R -> 2 in Z_2 as R->infinity, V is not locally bounded in any 2-adic neighborhood of 2 on the full physical height-one checkpoint graph.

Consequences: no 2-adically continuous / locally bounded endpoint-only supersolution, finite-residue potential, or finite shifted-valuation table can dominate the Rank-1 Bellman threat on the full physical graph. Fixed-seed ancestry must do essential global work.

Scope warning: these towers are exact physical/local kernel states. Global reachability of M_j from fixed seed is NOT claimed. No Gate-A residual contraction is promoted by this checkpoint.

Next intended attack: impose fixed-seed ballot ancestry on this explicit tower family and seek a lower bound on minimum historical area mu(M_j(k)), ideally mu(M_j(k)) >= k-j. This is a sharply parameterized subproblem of the RL292 danger-set contraction.

## Second checkpoint — exact homogeneous Rank-1 danger balls and shell-admissible singular towers

Status: ANALYTIC CANDIDATE / NOT PROMOTED.

Define the exact cost-one homogeneous stripped-unit map

T(J)=(3J+10)/8

on the t=3 branch, and for R>=1 define

N_R(J)=3^R(J-2)+2*8^R,
lambda_R=2-2(8/3)^R,

so T^R(J)=N_R(J)/8^R and N_R(J)=3^R(J-lambda_R).

### Exact backward danger-ball theorem

Let J>=2 be even and put n=nu_2(N_R(J)). If n>=3R+1, then the R-fold suffix (010)^R is automatically a genuine sequence of positive-even cost-one checkpoint macro-edges. Every intermediate checkpoint before the last has valuation exactly one, and the endpoint has

nu_2(T^R(J))=n-3R.

Therefore the Rank-1 Bellman threat satisfies

V(J) >= n-4R = nu_2(J-lambda_R)-4R.

Equivalently, the homogeneous R-step threat-r danger set is the 2-adic ball

nu_2(J-lambda_R) >= r+4R

(intersected with positive even integers, in the nontrivial range where the endpoint is even).

The proof is elementary from

N_(i+1)=3N_i+10*8^i.

If N_(i+1) has valuation >=3i+4, then N_i has exact valuation 3i+1. Hence T^i(J) is an even integer of valuation one, and

3T^i(J)+2=8(T^(i+1)(J)-1)

has exact valuation three because the next checkpoint is even.

### Shell-admissible unbounded tower strengthening

For every R>=1 choose any odd k with

v_3(2^k-2)>=R+1;

a simple infinite family is k == 1 (mod 2*3^R), by LTE.

For j=0,...,R set

M_j(k)=2+(8/3)^j(2^k-2).

Then:

- every M_j is a positive even integer;
- for j>=1, M_j ==2 (mod 16), so t=3 exactly;
- for j<=R, M_j ==2 (mod 3), satisfying the inherited d=1 reachability residue class;
- M_j --010--> M_(j-1) is an exact cost-one checkpoint macro;
- the odd one-zero return before the final boundary zero is J0_j=2M_(j-1)-1;
- because the extra v3 margin gives M_(j-1)==2 (mod 9), every J0_j==3 (mod 9), hence nu_3(J0_j)=1 exactly, satisfying RL282's promoted reachable one-zero output shell at every level;
- M_0=2^k and V(M_R)>=k-R.

Thus the Rank-1 singularity is not removed by positivity, exact local legality, the inherited mod-3 checkpoint class, or the promoted one-zero mod-9 shell. For fixed R, k can tend to infinity and M_R tends 2-adically to lambda_R while threat tends to infinity.

The R=1,k=13 member is not merely local: M_1(13)=21842 and the frozen RL290 genuine chain contains 21842 --010--> 8192.

### Strategic consequence

This kills a larger class of would-be RL292 shortcuts than the first checkpoint alone. The missing regularizer cannot be any endpoint-only 2-adic potential, finite residue table, local one-zero shell condition, or local reachability congruence. The next attack must intersect these explicit danger balls with genuinely fixed-seed/global ballot ancestry (or an equivalent minimum-area object).

No global reachability is claimed for the general M_R(k) tower. No Gate-A residual contraction is promoted.

Regression support: /mnt/data/rl292_scratch/verify_rank1_danger.py (PASS).

## Third checkpoint — shifted fixed-point reset barrier and hazard-label ancestry candidate

Status: ANALYTIC BARRIER + FINITE CANDIDATE / NOT PROMOTED.

### A. Exact arbitrary phase-reset family for the J=2 fixed-point shift

For every odd N>=3 with N == 3 or 5 (mod 6), define

J_N = (2^(N+4)-2)/3,
M_N = 3*2^N+2.

Then J_N is a positive even d=1 checkpoint candidate satisfying the inherited reachable residue class J_N mod 3 in {0,2}. Moreover

nu_2(J_N-2)=3.

The exact x-word 0101 is a legal cost-one checkpoint macro:

J_N
 --0--> (d=2, J=2^(N+3)+2)
 --1--> (d=1, J0=2^(N+2)+1)
 --0--> (d=1, J1=2^(N+1)+1)
 --1--> M_N.

The height charge is exactly one (only the d=2 step pays one).

The odd one-zero return J0 satisfies

J0 == 6 (mod 9) when N==3 (mod 6),
J0 == 3 (mod 9) when N==5 (mod 6),

so nu_3(J0)=1 exactly: the family passes RL282's promoted one-zero output shell. The endpoint M_N is again 2 (mod 3).

But

nu_2(M_N-2)=N.

Hence one physical height-one macro can raise the fixed-point shifted valuation from 3 to arbitrary N. Therefore no edge-Lipschitz theorem based on nu_2(J-2), or any bounded correction of it by local height alone, can be the RL292 supersolution.

This is an analytic barrier, not merely finite evidence.

### B. Genuine fixed-seed witness of the reset

The N=11 member is genuinely reached from the fixed seed by the exact canonical x-word

001000111101101011111101101111011101110111101001110110111111001111101010001110111001110011101110100111110101011010111101101101

which ends at

(d,J,H)=(1,10922,17).

Appending 0101 gives exactly

(1,10922,17)
 -> (2,16386,17)
 -> (1,8193,18)
 -> (1,4097,18)
 -> (1,6146,18).

Here

nu_2(10922-2)=3,
nu_2(6146-2)=11.

So a large shifted-phase reset genuinely occurs on the fixed-seed graph; it is not solely a fake-family pathology.

### C. New hazard-label candidate

The same reset source has the exact identity

3 J_N + 2 = 2^(N+4).

This identifies the natural pre-reset label

t(J)=nu_2(3J+2).

It is exactly one plus the accelerated odd-Collatz removal label of J/2, and for t>=3 it is the length parameter in RL290's stripped-unit suffix 01 0^(t-2).

An independent exact H<=22 minimum-height scan (same normalized recurrence and exact positive-boundary quotient as the repaired RL282 verifier) found

boxed candidate:  t(J) <= mu(J)

for every positive even checkpoint in the certificate. There were 75,232 distinct positive-even physical J values after minimizing over H. The maximum t-H was 0, uniquely at J=2,H=3; the next strongest observed case was J=10922,H=17,t=15.

