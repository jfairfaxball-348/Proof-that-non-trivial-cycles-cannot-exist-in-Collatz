#!/usr/bin/env python3
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
A=217_976_794_617
L=137_528_045_312
p=65_470_613_321
u=103_768_467_013
z=L-p
K0=1<<37
DELETED_Q=43_013_953
EXTERNAL_VERIFIED_FLOOR=1<<71
ROOT_LOWER=24_913_843_845_551_577_787_381
ROOT_UPPER=31_285_589_992_934_194_300_574

def b(i): return A*i//L

# Pin the inherited Diophantine constants used by the H21 height argument.
assert A*p-u*L == 1
assert z == 72_057_431_991

# Reconstruct the complete inherited e=16 prefix family exactly as in the
# RL217 portable verifier, but stop before the phase-51 automaton.  The
# phase-51 family is a subset, so a lower bound on this larger admissible
# window family is automatically a lower bound for every RL219 survivor.
bs=[b(i) for i in range(17)]
assert bs == [0,1,3,4,6,7,9,11,12,14,15,17,19,20,22,23,25]
c=[bs[i+1]-bs[i] for i in range(16)]
states={(0,1)}
for i in range(1,16):
    nxt=set()
    for h,Q in states:
        S=bs[i]-h
        for hn in range(h+c[i]):
            a=c[i]+h-hn
            assert a>=1
            nxt.add((hn,3*Q+(1<<S)))
    states=nxt
terminal=sorted(Q for h,Q in states if h==1)
assert len(terminal)==108_950

S=24
gap=3**16 * 2**13
mod16=3**16
mod17=3**17
inv16=pow(1<<(S+34),-1,mod16)
rows=[]
for Q in terminal:
    eta0=((1<<S)+Q)*inv16 % mod16
    if eta0%9 not in (0,8):
        continue
    y16=(1<<34)*eta0-1-gap
    num=(1<<S)*y16-Q
    assert num%mod16==0
    y0base=num//mod16
    valid=[]
    for t in range(3):
        y0=y0base+(1<<(S+34))*t
        if y0%3 and (y0+K0)%3:
            valid.append((t,y0))
    assert len(valid)==1
    t,y0=valid[0]
    eta=eta0+t*mod16
    rows.append((Q,eta,y0))
assert len(rows)==45_046
assert rows[0][0]==DELETED_Q

# Reconstruct the inherited exact two-sided k windows and terminal Hensel
# exclusions.  This matches RL217's incoming reconstruction exactly.
U=sum(Fraction(2,(2*n+1)*3**(2*n+1)) for n in range(7))
U+=Fraction(1,20*3**14)
W=U+Fraction(z,1<<40)
LB=Fraction(K0)*(L-W)/W
step=3*(1<<58)
CAPNUM=48*L*K0
M=1<<22
forbidden=pow(pow(3,34,M),-1,M)
r_odd=forbidden
r_even=(forbidden-21)%M
invN22=pow(mod17,-1,M)
records=[]
pre_hensel=post_hensel=hensel_removed=0
for Q,eta,y0 in rows:
    kmax=(CAPNUM-1-29*y0)//(29*step)
    num=LB.numerator-LB.denominator*y0
    kmin=0 if num<0 else num//(LB.denominator*step)+1
    n=kmax-kmin+1
    bad=set()
    for rr in (r_odd,r_even):
        k=((rr-eta)*invN22)%M
        if kmin<=k<=kmax:
            bad.add(k)
    records.append((Q,eta,y0,kmin,kmax,tuple(sorted(bad))))
    pre_hensel += n
    post_hensel += n-len(bad)
    hensel_removed += len(bad)
assert pre_hensel==331_935_455
assert post_hensel==331_935_285
assert hensel_removed==170
assert post_hensel-(records[0][4]-records[0][3]+1)==331_927_916

# Exact lower bound on the phase-16 odd state over every non-deleted prefix
# and every admissible k in its inherited finite window (after Hensel).
minimum=None
witness=None
for Q,eta,y0,lo,hi,badks in records:
    if Q==DELETED_Q:
        continue
    bad=set(badks)
    k=lo
    while k in bad:
        k+=1
    assert k<=hi
    x=eta+mod17*k
    y16=(1<<34)*x-1-gap
    if minimum is None or y16<minimum:
        minimum=y16
        witness={"Q":Q,"eta":eta,"root_base_y0":y0,"root_y_at_k":y0+step*k,"k":k,"x":x,"y16":y16}

assert minimum == 63_923_554_738_764_449_832_959
assert witness == {
    "Q":87_738_641,
    "eta":54_222_282,
    "root_base_y0":363_059_077_609_370_159,
    "root_y_at_k":24_913_843_852_126_965_674_543,
    "k":28_812,
    "x":3_720_840_598_638,
    "y16":63_923_554_738_764_449_832_959,
}

# RL219 analytic theorem (proved in the accompanying proof note) uses the
# inherited exact bound 0 < ln(lambda) < 2^-40, lambda=2^A/3^L, plus
# nonnegative physical height to show every shortcut state in a complete
# L-odd-step traversal is strictly greater than minimum/8.
# The verifier pins the finite arithmetic edge and the comparison with the
# stable externally inherited Barina 2025 verification interval [1,2^71].
safe_floor=minimum//8
assert safe_floor == 7_990_444_342_345_556_229_119
assert safe_floor > EXTERNAL_VERIFIED_FLOOR

# RL219 finite-library dyadic-ray sparsity theorem uses only the inherited
# exact root band and RL218 raw-word normal form.  Since ROOT_UPPER is
# strictly less than twice ROOT_LOWER, a fixed raw backward word applied to
# one dyadic seed ray can contribute at most one endpoint value to the whole
# current e=16 root band: successive t values satisfy Y_(t+1) >= 2 Y_t.
assert ROOT_UPPER < 2*ROOT_LOWER
root_band_margin=2*ROOT_LOWER-ROOT_UPPER
assert root_band_margin == 18_542_097_698_168_961_274_188

result={
    "status":"PASS",
    "classification":"exact finite arithmetic support for RL219 analytic bounded-blue no-go theorem",
    "e16_prefix_rows_reconstructed":45_046,
    "e16_live_prefixes_before_phase51":45_045,
    "rl216_incoming_candidates_after_deleted_prefix":331_927_916,
    "phase51_survivors_are_subset":139_581_280,
    "minimum_phase16_odd_state_over_superset":minimum,
    "minimum_witness":witness,
    "certified_physical_shortcut_floor":safe_floor,
    "stable_external_verified_interval_upper":EXTERNAL_VERIFIED_FLOOR,
    "root_lower_bound_integer":ROOT_LOWER,
    "root_upper_bound_integer":ROOT_UPPER,
    "twice_root_lower_minus_upper":root_band_margin,
    "fixed_word_dyadic_ray_endpoint_values_per_pair_in_root_band_max":1,
    "floor_margin_over_2pow71":safe_floor-EXTERNAL_VERIFIED_FLOOR,
    "new_candidate_deletions":0,
    "new_rank_exclusions":0,
    "frontier":13_415_865_871,
}
out=json.loads((ROOT/"certificates/verify_rl219_bounded_blue_floor_output.json").read_text())
assert out==result

print("PASS RL219 bounded certified-blue floor support")
print(f"min_y16={minimum} physical_floor={safe_floor}")
print(f"2^71={EXTERNAL_VERIFIED_FLOOR} margin={safe_floor-EXTERNAL_VERIFIED_FLOOR}")
print("candidate_deletions=0 rank_deletions=0 frontier=13415865871")
