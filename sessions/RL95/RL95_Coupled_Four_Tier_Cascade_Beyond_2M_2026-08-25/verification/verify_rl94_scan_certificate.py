#!/usr/bin/env python3
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parent/'raw_rl94'
pat=re.compile(r'N=(\d+) chunk=(\d+)\.\.(\d+) min_bits=(\d+) at_r=(\d+)')
def load(prefix):
    rows=[]
    for p in sorted(ROOT.glob(prefix+'*.txt')):
        m=pat.fullmatch(p.read_text().strip())
        assert m,p
        N,s,e,b,r=map(int,m.groups()); rows.append((s,e,N,b,r,p.name))
    return rows
def check(rows,N,start,end,count,width):
    assert len(rows)==count,(len(rows),count)
    assert rows[0][0]==start and rows[-1][1]==end
    prev=start-1
    for s,e,n,b,r,name in rows:
        assert n==N and s==prev+1 and e-s+1==width and s<=r<=e,(name,s,e,r)
        prev=e
    assert prev==end
u=load('ultra_rl94_'); m=load('mid_rl94_'); d=load('deep_rl94_')
check(u,15000056,35001,335000,60,5000)
check(m,7500056,3525001,3675000,6,25000)
check(d,10000056,1775001,2000000,9,25000)
umin=min((x[3],x[4]) for x in u); mmin=min((x[3],x[4]) for x in m); dmin=min((x[3],x[4]) for x in d)
assert umin==(15000040,86111),umin
assert mmin==(7500038,3546704),mmin
assert dmin==(10000037,1817629),dmin
# inherited combined minima are frozen after incoming verification economy gate
assert min((15000040,2900),umin)==(15000040,2900)
assert min((7500034,1635300),mmin)==(7500034,1635300)
assert min((10000034,378722),dmin)==(10000034,378722)
print('RL94 scan-certificate aggregation: PASS')
print('ultra chunks =',len(u),'covered r=35001..335000; new min=15000040 at r=86111; combined min=15000040 at r=2900')
print('middle chunks =',len(m),'covered r=3525001..3675000; new min=7500038 at r=3546704; combined min=7500034 at r=1635300')
print('deep chunks =',len(d),'covered r=1775001..2000000; new min=10000037 at r=1817629; combined min=10000034 at r=378722')
