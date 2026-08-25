#!/usr/bin/env python3
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parent/'raw_rl96'
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

u=load('ultra_')
m=load('mid_')
d=load('deep_')
check_gap_free(u,15000056,605001,870000)
check_gap_free(m,7500056,3800001,3950000)
check_gap_free(d,10000056,2200001,2400000)

assert len(u)==10,len(u)
assert len(m)==6,len(m)
assert len(d)==8,len(d)

umin=min((x[3],x[4]) for x in u)
mmin=min((x[3],x[4]) for x in m)
dmin=min((x[3],x[4]) for x in d)

assert umin==(15000038,868107),umin
assert mmin==(7500036,3871407),mmin
assert dmin==(10000037,2216053),dmin

u_global=min((15000037,575974),umin)
m_global=min((7500034,1635300),mmin)
d_global=min((10000034,378722),dmin)

assert u_global==(15000037,575974)
assert m_global==(7500034,1635300)
assert d_global==(10000034,378722)

assert u_global[0]-2==15000035
assert m_global[0]-2==7500032
assert d_global[0]-2==10000032

print('RL96 scan-certificate aggregation: PASS')
print('ultra records =',len(u),'covered r=605001..870000; new min=15000038 at r=868107; global min=15000037 at r=575974; D_u=15000035')
print('middle records =',len(m),'covered r=3800001..3950000; new min=7500036 at r=3871407; global min=7500034 at r=1635300; D_m=7500032')
print('deep records =',len(d),'covered r=2200001..2400000; new min=10000037 at r=2216053; global min=10000034 at r=378722; D_d=10000032')
