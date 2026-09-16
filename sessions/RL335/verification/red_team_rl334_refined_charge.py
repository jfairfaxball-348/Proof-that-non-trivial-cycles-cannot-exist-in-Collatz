#!/usr/bin/env python3
import contextlib, io, runpy
from pathlib import Path
with contextlib.redirect_stdout(io.StringIO()):
    B=runpy.run_path(str(Path(__file__).with_name('verify_rl334_refined_charge.py')))
states=B['states']; edges=B['edges']; low=B['low']
# independent reverse-order density relaxation
pot=[0]*len(states)
for iteration in range(len(states)+1):
    ch=False
    for s,t,z,k in reversed(edges):
        w=2*z-43*k
        if pot[s]+w>pot[t]: pot[t]=pot[s]+w; ch=True
    if not ch: break
else: raise AssertionError('density positive cycle')
assert all(pot[s]+2*z-43*k<=pot[t] for s,t,z,k in edges)
sig=[]
for s,t,z,k in edges:
    sg=pot[t]-pot[s]-(2*z-43*k); assert sg>=0; sig.append((s,t,z,k,sg))
pi=[0]*len(states); q=22
for iteration2 in range(len(states)+1):
    ch=False
    for s,t,z,k,sg in reversed(sig):
        w=q*(k-2*(t in low))-sg
        if pi[s]+w>pi[t]: pi[t]=pi[s]+w; ch=True
    if not ch: break
else: raise AssertionError('q22 positive cycle')
assert all(pi[s]+q*(k-2*(t in low))-sg<=pi[t] for s,t,z,k,sg in sig)
assert min(pi)==0 and max(pi)==44
print('RL334_REFINED_CHARGE_RED_TEAM_GREEN')
print('states_edges',len(states),len(edges))
print('reverse_density_range',min(pot),max(pot))
print('reverse_charge_range',min(pi),max(pi))
