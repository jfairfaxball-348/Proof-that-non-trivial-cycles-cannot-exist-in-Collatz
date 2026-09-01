#!/usr/bin/env python3
import json
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

A=217_976_794_617
L=137_528_045_312
p=65_470_613_321
u=103_768_467_013
z=L-p
K0=1<<37
E=16
RANK=34_124_151_203
Q16=43_079_489
K=28_821
EXPECTED_ETA_BASE=94_527_378
EXPECTED_Y0_BASE=632_932_199_441_596_415
EXPECTED_ETA=3_722_043_165_201
EXPECTED_Y0=24_921_895_945_404_894_117_887
HORIZON=51

def b(i): return A*i//L
def v2(n):
    n=abs(n)
    assert n
    return (n & -n).bit_length()-1

assert A*p-u*L==1
assert z==72_057_431_991

# Independently reconstruct the e=16 prefix state machine through h_16=1.
bs=[b(i) for i in range(17)]
assert bs==[0,1,3,4,6,7,9,11,12,14,15,17,19,20,22,23,25]
c=[bs[i+1]-bs[i] for i in range(16)]
states={(0,1)}
for i in range(1,16):
    nxt=set()
    for h,q in states:
        S=bs[i]-h
        for hn in range(h+c[i]):
            a=c[i]+h-hn
            assert a>=1
            nxt.add((hn,3*q+(1<<S)))
    states=nxt
terminal={q for h,q in states if h==1}
assert len(terminal)==108_950
assert Q16 in terminal

# Reconstruct the unique H21-compatible unit-preserving base lift for this prefix.
S=24
gap=3**16 * 2**13
mod16=3**16
mod17=3**17
inv16=pow(1<<(S+34),-1,mod16)
eta0=((1<<S)+Q16)*inv16 % mod16
assert eta0%9 in (0,8)
y16base=(1<<34)*eta0-1-gap
num=(1<<S)*y16base-Q16
assert num%mod16==0
raw_y0=num//mod16
valid=[]
for t in range(3):
    y0=raw_y0+(1<<(S+34))*t
    if y0%3 and (y0+K0)%3:
        valid.append((t,y0))
assert len(valid)==1
t,y0_base=valid[0]
eta_base=eta0+t*mod16
assert eta_base==EXPECTED_ETA_BASE
assert y0_base==EXPECTED_Y0_BASE

# Reconstruct RL215 two-sided k window and terminal-Hensel exclusions.
U=sum(Fraction(2,(2*n+1)*3**(2*n+1)) for n in range(7))
U+=Fraction(1,20*3**14)
W=U+Fraction(z,1<<40)
LB=Fraction(K0)*(L-W)/W
root_lower=LB.numerator//LB.denominator+1
root_upper=(48*L*K0-1)//29
assert root_lower==24_913_843_845_551_577_787_381
assert root_upper==31_285_589_992_934_194_300_574

step=3*(1<<58)
kmax=(48*L*K0-1-29*y0_base)//(29*step)
n=LB.numerator-LB.denominator*y0_base
kmin=0 if n<0 else n//(LB.denominator*step)+1
assert (kmin,kmax)==(28_812,36_180)
assert kmin<=K<=kmax

M=1<<22
hensel_forbidden=pow(pow(3,34,M),-1,M)
r_odd=hensel_forbidden
r_even=(hensel_forbidden-21)%M
invN22=pow(mod17,-1,M)
bad=set()
for rr in (r_odd,r_even):
    kk=((rr-eta_base)*invN22)%M
    if kmin<=kk<=kmax:
        bad.add(kk)
assert bad==set()
assert K not in bad

eta=eta_base+mod17*K
root_y0=y0_base+step*K
assert eta==EXPECTED_ETA
assert root_y0==EXPECTED_Y0
assert root_lower<=root_y0<=root_upper
assert root_y0%4==3
assert v2(3*root_y0+1)==1
assert root_y0%3 and (root_y0+K0)%3

state="011" if eta%9==0 else "111"
assert state=="011"
assert eta%18==9
assert eta%2187==864

# Terminal Hensel/valuation orientation.
s=eta+21 if eta%2==0 else eta
nu=v2(3**34*s-1)
assert s==eta
assert nu==3
assert 1<=nu<=21

# Common phase-16 root/prefix identity and exact forward height replay.
y=(1<<34)*eta-1-gap
y16=y
assert (1<<24)*y16-Q16 == (3**16)*root_y0
h=1
min_h=h
for i in range(16,HORIZON+1):
    ci=b(i+1)-b(i)
    a=v2(3*y+1)
    assert a<=ci+h, (i,h,ci,a)
    h=ci+h-a
    assert h>=0
    min_h=min(min_h,h)
    y=(3*y+1)//(1<<a)
assert min_h==1
assert h==4
assert y==532_778_464_734_508_000_466_137

result={
  "status":"PASS",
  "classification":"exact finite arithmetic witness for nonempty selected inherited candidate intersection",
  "offset_e":16,
  "terminal_rank":RANK,
  "prefix_Q16":Q16,
  "eta_base":eta_base,
  "y0_base":y0_base,
  "k_min":kmin,
  "k_max":kmax,
  "chosen_k":K,
  "eta":eta,
  "root_y0":root_y0,
  "phase16_y":y16,
  "h21_state":state,
  "eta_mod18":eta%18,
  "eta_mod2187":eta%2187,
  "terminal_orientation_s":s,
  "terminal_nu_v2_3pow34s_minus1":nu,
  "root_v2_3y_plus1":v2(3*root_y0+1),
  "minimum_height_phase16_through_51":min_h,
  "phase52_height_after_replay":h,
  "phase52_y_after_replay":y,
  "root_lower_bound":root_lower,
  "root_upper_bound":root_upper,
  "inherited_rl217_phase51_candidates":139_581_280,
  "inherited_rl217_prefixes":45_045,
  "new_candidate_deletions":0,
  "new_prefix_deletions":0,
  "new_rank_exclusions":0
}
expected=json.loads((ROOT/"certificates/verify_rl221_constraint_intersection_output.json").read_text())
assert result==expected
print("PASS RL221 type-safe constraint-intersection witness verifier")
print("Q16=43079489 k=28821 eta=3722043165201")
print("y0=24921895945404894117887 state=011 mod18=9 nu=3")
print("phase51_survives=true minimum_height=1 root_v2=1")
print("selected_constraint_intersection=NONEMPTY candidate_deletions=0 rank_exclusions=0")
