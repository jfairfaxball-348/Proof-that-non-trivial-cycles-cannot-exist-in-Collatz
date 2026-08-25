#!/usr/bin/env python3
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parent/'raw_rl95'
pat=re.compile(r'N=(\d+) chunk=(\d+)\.\.(\d+) min_bits=(\d+) at_r=(\d+)')

def load(prefix):
    rows=[]
    for p in sorted(ROOT.glob(prefix+'*.txt')):
        m=pat.fullmatch(p.read_text().strip())
        assert m,p
        N,s,e,b,r=map(int,m.groups())
        assert s<=r<=e,(p.name,s,e,r)
        rows.append((s,e,N,b,r,p.name))
    return sorted(rows)

def check_gap_free(rows,N,start,end):
    assert rows and rows[0][0]==start,(rows[0],start)
    prev=start-1
    for s,e,n,b,r,name in rows:
        assert n==N,(name,n,N)
        assert s==prev+1,(name,prev,s)
        assert e>=s,(name,s,e)
        prev=e
    assert prev==end,(prev,end)

u=load('ultra_rl95_')
m=load('mid_rl95_')
d=load('deep_rl95_')
check_gap_free(u,15000056,335001,605000)
check_gap_free(m,7500056,3675001,3800000)
check_gap_free(d,10000056,2000001,2200000)

umin=min((x[3],x[4]) for x in u)
mmin=min((x[3],x[4]) for x in m)
dmin=min((x[3],x[4]) for x in d)

assert umin==(15000037,575974),umin
assert mmin==(7500039,3785526),mmin
assert dmin==(10000040,2090420),dmin

# Frozen inherited global minima accepted by verification economy.
u_global=min((15000040,2900),umin)
m_global=min((7500034,1635300),mmin)
d_global=min((10000034,378722),dmin)

assert u_global==(15000037,575974)
assert m_global==(7500034,1635300)
assert d_global==(10000034,378722)

# Minimal-reset interface: safe depth D = global bit-length floor B - 2.
assert u_global[0]-2==15000035
assert m_global[0]-2==7500032
assert d_global[0]-2==10000032

print('RL95 scan-certificate aggregation: PASS')
print('ultra records =',len(u),'covered r=335001..605000; new/global min=15000037 at r=575974; D_u=15000035')
print('middle records =',len(m),'covered r=3675001..3800000; new min=7500039 at r=3785526; combined min=7500034 at r=1635300; D_m=7500032')
print('deep records =',len(d),'covered r=2000001..2200000; new min=10000040 at r=2090420; combined min=10000034 at r=378722; D_d=10000032')
