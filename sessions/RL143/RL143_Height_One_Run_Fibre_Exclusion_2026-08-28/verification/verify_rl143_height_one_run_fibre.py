#!/usr/bin/env python3
from fractions import Fraction
A=217_976_794_617; L=137_528_045_312; G=771_316_334_039; T=303_279_262_681
def logi(x,N=260):
 x2=x*x;t=x;s=Fraction()
 for k in range(N): s+=t/(2*k+1);t*=x2
 lo=2*s;return lo,lo+2*t/(2*N+1)/(1-x2)
l2l,l2h=logi(Fraction(1,3));l3l,l3h=logi(Fraction(1,2)); d=A*l2h-L*l3l
def ok(g): return 18*(g*(2*L-A)-1)>Fraction(6*(1<<75),1)/(1-g*d)
assert G*d<1 and ok(T) and not ok(T-1) and ok(G)
print('RL143 height-one run-fibre exclusion: PASS')
