#!/usr/bin/env python3
import json
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
A=217_976_794_617
L=137_528_045_312
p=65_470_613_321
K0=1<<37

def b(i): return A*i//L

bs=[b(i) for i in range(17)]
assert bs == [0,1,3,4,6,7,9,11,12,14,15,17,19,20,22,23,25]
c=[bs[i+1]-bs[i] for i in range(16)]
assert c == [1,2,1,2,1,2,2,1,2,1,2,2,1,2,1,2]

# Exact root recurrence.  h0=h1=0 fixes the first edge a0=1 and Q1=1.
# A state at phase i is (h_i,Q_i), where
#   2^(b_i-h_i) y_i = 3^i y0 + Q_i.
states={(0,1)}
for i in range(1,16):
    nxt=set()
    for h,Q in states:
        S=bs[i]-h
        for hn in range(h+c[i]):  # a_i=c_i+h-hn >= 1
            a=c[i]+h-hn
            assert S+a == bs[i+1]-hn
            nxt.add((hn,3*Q+(1<<S)))
    states=nxt

terminal=sorted(Q for h,Q in states if h==1)
assert len(terminal)==108_950
assert len(set(terminal))==108_950
S=bs[16]-1
assert S==24

# Flat-K absolute source/root relation at e=16.
gap=3**16 * 2**13
assert gap == 2*K0*3**16//2**bs[16]
mod16=3**16
inv16=pow(1<<(S+34),-1,mod16)

eta_to_Q={}
mods9=Counter()
for Q in terminal:
    eta=((1<<S)+Q)*inv16 % mod16
    assert eta not in eta_to_Q
    eta_to_Q[eta]=Q
    mods9[eta%9]+=1
assert mods9 == Counter({3:33410,0:29286,2:22359,8:15760,6:6167,5:1968})
h21={eta:Q for eta,Q in eta_to_Q.items() if eta%9 in (0,8)}
assert len(h21)==45_046
assert sum(1 for eta in h21 if eta%9==0)==29_286
assert sum(1 for eta in h21 if eta%9==8)==15_760

# H21-compatible residue reachability: state law contributes eta mod9 in {0,8}.
h21_hits={}
all_reachable={}
for k in range(2,8):
    m=3**k
    invk=pow(1<<(S+34),-1,m)
    reachable={((1<<S)+Q)*invk % m for Q in terminal}
    universe={r for r in range(m) if r%9 in (0,8)}
    hit=reachable & universe
    all_reachable[k]=len(reachable)
    h21_hits[k]=len(hit)
assert h21_hits == {2:2,3:6,4:18,5:54,6:162,7:469}
assert [h21_hits[k] for k in range(2,7)] == [2*(3**(k-2)) for k in range(2,7)]

m7=3**7
inv7=pow(1<<(S+34),-1,m7)
reachable7={((1<<S)+Q)*inv7 % m7 for Q in terminal}
universe7={r for r in range(m7) if r%9 in (0,8)}
forbidden=sorted(universe7-reachable7)
expected_forbidden=[0,53,431,891,917,972,1160,1295,1458,1493,1565,1620,1701,1862,2060,2088,2106]
assert forbidden==expected_forbidden
assert [r for r in forbidden if r%9==0] == [0,891,972,1458,1620,1701,2088,2106]
assert [r for r in forbidden if r%9==8] == [53,431,917,1160,1295,1493,1565,1862,2060]

# The requested compressed automaton: retain only (height,Q mod 3^7).
compressed={(0,1%m7)}
compressed_counts=[len(compressed)]
for i in range(1,16):
    nxt=set()
    for h,Q in compressed:
        Si=bs[i]-h
        for hn in range(h+c[i]):
            nxt.add((hn,(3*Q+(1<<Si))%m7))
    compressed=nxt
    compressed_counts.append(len(compressed))
assert compressed_counts == [1,2,3,7,12,30,85,173,401,586,1071,1912,2308,3416,3655,4950]
assert len({Q for h,Q in compressed if h==1})==1243

# Root p-gap unit filter.  Use exact Q, not a truncated quotient residue.
# Each eta mod 3^16 has exactly one lift mod 3^17 for which both y0 and yp are
# units modulo 3.  The lift leaves eta mod 3^7 unchanged.
lift_counts=Counter()
for eta,Q in h21.items():
    y16=(1<<34)*eta-1-gap
    num=(1<<S)*y16-Q
    assert num%mod16==0
    y0=num//mod16
    valid=[]
    for t in range(3):
        y0t=y0+(1<<(S+34))*t
        ypt=y0t+K0
        if y0t%3 and ypt%3:
            valid.append(t)
    assert len(valid)==1
    lift_counts[valid[0]]+=1
assert sum(lift_counts.values())==45_046

# The ordinary H21 terminal-valuation condition is 2-adic, while the ternary
# holes are modulo 3^7.  CRT coprimality is exact; the terminal filter cannot
# by itself turn a surviving ternary class into an empty arithmetic class.
math_gcd=__import__('math').gcd(m7,1<<22)
assert math_gcd==1
g=pow(3,34,1<<22)
forbidden_s=pow(g,-1,1<<22)
assert forbidden_s & 1
valid_even_eta=[r for r in range(0,1<<22,2) if ((r+21)&((1<<22)-1)) != forbidden_s]
valid_odd_eta=[r for r in range(1,1<<22,2) if r != forbidden_s]
assert valid_even_eta and valid_odd_eta

out={
  "status":"PASS",
  "offset_e":16,
  "root_prefix_count":108950,
  "root_total_exponent":24,
  "h21_compatible_prefix_count":45046,
  "state011_prefix_count":29286,
  "state111_prefix_count":15760,
  "first_informative_ternary_power":7,
  "modulus_3_power_7":2187,
  "h21_universe_mod2187":486,
  "h21_reachable_mod2187":469,
  "forbidden_eta_mod2187":forbidden,
  "forbidden_state011_mod2187":[r for r in forbidden if r%9==0],
  "forbidden_state111_mod2187":[r for r in forbidden if r%9==8],
  "compressed_state_counts_by_phase_1_to_16":compressed_counts,
  "terminal_q_residues_mod2187":1243,
  "root_unit_lift_unique_for_h21_prefixes":True,
  "terminal_valuation_crt_independent":True,
  "new_rank_exclusions":0,
  "frontier":13_415_865_871
}
(ROOT/"certificates/verify_rl212_e16_quotient_residue_output.json").write_text(
    json.dumps(out,indent=2,sort_keys=True)+"\n"
)
print("PASS RL212 exact e=16 quotient-residue certificate")
print("root_prefixes=108950 h21_prefixes=45046 states011_111=29286_15760")
print("ternary_saturation_through=3^6 first_informative=3^7")
print("eta_mod2187_reachable=469/486 forbidden=17")
print("root_unit_lift=unique_mod3 terminal_valuation=CRT_independent")
print("rank_deletions=0 frontier=13415865871")
