#!/usr/bin/env python3
A=217_976_794_617
L=137_528_045_312
B=A-L
R=L-B
p=65_470_613_321
u0=103_768_467_013
t=L-p
N0=43_742_681_439
J00=9_719_139_553
assert A*p-u0*L==1
assert (p*B)%L==1
assert (B,R,t)==(80_448_749_305,57_079_296_007,72_057_431_991)
def I(r): return (p*r)%L
assert I(R-1)==t-1
assert I(L-1)==t
def b(i): return (A*i)//L
def c(i): return b(i+1)-b(i)
assert c(t-1)==1 and c(t-1+p)==2
assert c(t)==2 and c(t+p)==1
for i in range(23): assert c(i+p)==c(i)
assert b(p)-b(0)==u0
assert b(t+p)-b(t)==u0+1
S={0,2}
def count_res_interval(lo,hi,residues,m=5):
    return sum((hi-1-s)//m - (lo-1-s)//m for s in residues)
base_N=(L//5)*2 + sum(1 for x in range(L%5) if x in S)
assert base_N==55_011_218_125
Z_N=base_N
assert B%5==0 and L%5==2
Rwrap=L-B
base_J=count_res_interval(0,Rwrap,{0,2}) + count_res_interval(Rwrap,L,{2})
assert base_J==38_921_468_264
def base_in(r): return r%5 in S
def z_in(r):
    if r==2: return False
    if r==1: return True
    return base_in(r)
def edge(f,r): return f(r) and f((r+B)%L)
affected={1,2,(1-B)%L,(2-B)%L}
delta=sum(int(edge(z_in,r))-int(edge(base_in,r)) for r in affected)
Z_J=base_J+delta
assert delta==-1 and Z_J==38_921_468_263
assert Z_N>N0 and Z_J>J00
assert not base_in(L-1)
assert z_in(0) and z_in(1) and not z_in(2)
for s in range(3,5): assert not (z_in(s) and z_in(s+1))
assert not (z_in(L-1) and z_in(0))
print('PASS RL196 exact p-shift compatibility certificate')
print('seams', t-1, t)
print('placement_relaxation_N', Z_N)
print('placement_relaxation_J00', Z_J)
print('unique_extra_claim=none; anchor_rank_edge=0->1')
