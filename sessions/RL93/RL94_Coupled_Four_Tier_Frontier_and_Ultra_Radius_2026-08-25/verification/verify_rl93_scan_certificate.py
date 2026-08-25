#!/usr/bin/env python3
from pathlib import Path
import re
ROOT=Path(__file__).parent
PAT=re.compile(r'N=(\d+) chunk=(\d+)\.\.(\d+) min_bits=(\d+) at_r=(\d+)')

def rows(prefix,N,start,end,count):
    out=[]
    for p in sorted((ROOT/'raw_rl93').glob(prefix+'*.txt')):
        m=PAT.fullmatch(p.read_text().strip())
        assert m,p
        n,a,b,bits,r=map(int,m.groups()); assert n==N,(p,n)
        out.append((a,b,bits,r,p.name))
    out.sort(); assert len(out)==count,(prefix,len(out))
    assert out[0][0]==start and out[-1][1]==end,(prefix,out[0],out[-1])
    for x,y in zip(out,out[1:]): assert y[0]==x[1]+1,(prefix,x,y)
    return out

d=rows('deep_rl93_',10000056,1100001,1775000,27)
m=rows('mid_rl93_',7500056,1250001,3525000,91)
u=rows('ultra_rl93_',15000056,1001,35000,7)
assert min(d,key=lambda x:(x[2],x[3]))[:4]==(1675001,1700000,10000036,1693348)
assert min(m,key=lambda x:(x[2],x[3]))[:4]==(1625001,1650000,7500034,1635300)
assert min(u,key=lambda x:(x[2],x[3]))[:4]==(1001,5000,15000040,2900)

inherited=(ROOT/'inherited_rl92'/'RL92_MULTISCALE_2ADIC_SCAN.txt').read_text()
for s in ['r_range=0..7000000','global_min_balanced_bitlen=5000032 at_r=2595446','r_range=0..1100000','global_min_balanced_bitlen=10000034 at_r=378722']:
    assert s in inherited,s
assert (ROOT/'inherited_rl92'/'ultra_probe_15000056_0_1000.txt').read_text().strip()=='N=15000056 chunk=0..1000 min_bits=15000048 at_r=88'

# Combined minima/consequences.
assert 10000034 < min(x[2] for x in d)
assert min(x[2] for x in m)==7500034
assert min(15000048,min(x[2] for x in u))==15000040
assert 10000034-2==10000032 and 10000056-3==10000053
assert 7500034-2==7500032 and 7500056-3==7500053
assert 15000040-2==15000038 and 15000056-3==15000053
print('RL93 scan-certificate aggregation: PASS')
print('deep new chunks =',len(d),'covered r=1100001..1775000; new min=10000036 at r=1693348; combined min=10000034 at r=378722')
print('middle chunks =',len(m),'covered r=1250001..3525000; min=7500034 at r=1635300')
print('ultra new chunks =',len(u),'covered r=1001..35000; new/combined min=15000040 at r=2900')
