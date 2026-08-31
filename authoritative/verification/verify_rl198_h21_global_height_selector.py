#!/usr/bin/env python3

A=217_976_794_617
L=137_528_045_312
B=A-L
R=L-B

DLO=23_369_453_298
DHI=41_775_866_136

D35=7*(2**35)
D34=21*(2**33)
D33=63*(2**32)

def v2(n):
    assert n>0
    k=0
    while n%2==0:
        n//=2
        k+=1
    return k

triples=[
    (0,0,0),(0,1,0),(0,1,1),
    (1,0,0),(1,1,0),(1,1,1)
]
zero_edge={(0,0,0),(1,0,0)}

survivors=[]
for e35,e34,e33 in triples:
    C34=(2**e34)*D34
    C33=(2**e33)*D33
    if v2(C34)>=34 and v2(C33)>=33:
        survivors.append((e35,e34,e33))
assert survivors==[(0,1,1),(1,1,1)]
assert not (set(survivors) & zero_edge)

C34=2*D34
C33=2*D33
assert C34==360_777_252_864 and v2(C34)==34
assert C33==541_165_879_296 and v2(C33)==33

# Positive integer cost saturation: tau terms, each >=1, total=tau.
for tau,total in ((34,v2(C34)),(33,v2(C33))):
    assert total==tau
    assert tau*1==total

C35_011=D35
C35_111=2*D35
assert C35_011==240_518_168_576 and v2(C35_011)==35
assert C35_111==481_036_337_152 and v2(C35_111)==36
assert v2(C35_011)-34==1
assert v2(C35_111)-34==2

pre_lo=(DLO-B)%L
pre_hi=(DHI-B)%L
assert (pre_lo,pre_hi)==(80_448_749_305,98_855_162_143)
assert pre_lo>R and pre_hi>R

Dsum=34
tau=34
h_start=1
H=21
ell=Dsum-tau-h_start+H
assert ell==20
assert ell>=1
pre_twos=ell-1
pre_height=h_start+pre_twos
assert pre_height==20

Cpre=14*(3**34)
T=7*(3**35)
assert Cpre==233_480_543_795_331_966
assert Cpre%8==6
assert T==350_220_815_692_997_949
assert 3*Cpre==2*T

print("PASS RL198 exact H21 global height selector certificate")
print("global_survivor_states=011,111")
print("selector=e34=e33=1")
print("h21_owned_zero_edge_prefix=excluded")
print("tau34_tau33_unit_cost_saturation=yes")
print("leading_cost_011=1 leading_cost_111=2")
print("preterminal_height=20 mechanical_bit=2")
print("preterminal_numerator=14*3^34")
print("terminal_orientation_sign=open")
