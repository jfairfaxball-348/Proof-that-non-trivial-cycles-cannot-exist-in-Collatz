#!/usr/bin/env python3
import re
from pathlib import Path
root=Path(__file__).resolve().parent/'raw_rl97'
pat=re.compile(r'N=(\d+) chunk=(\d+)\.\.(\d+) min_bits=(\d+) at_r=(\d+)')

def load(name,N,start,end,expected_new_min,expected_r,global_min,global_r,depth):
    rec=[]
    for line in (root/name).read_text().splitlines():
        m=pat.fullmatch(line.strip())
        assert m,line
        n,a,b,mb,mr=map(int,m.groups())
        assert n==N and a<=mr<=b
        rec.append((a,b,mb,mr))
    assert rec and rec[0][0]==start and rec[-1][1]==end,(name,rec[:1],rec[-1:])
    prev=start-1
    for a,b,mb,mr in rec:
        assert a==prev+1,(name,prev,a)
        assert b>=a
        prev=b
    best=min(rec,key=lambda x:(x[2],x[3]))
    assert (best[2],best[3])==(expected_new_min,expected_r),(name,best)
    assert global_min<=expected_new_min
    assert depth==global_min-2
    print(f'{name}: records={len(rec)} covered r={start}..{end}; new min={expected_new_min} at r={expected_r}; global min={global_min} at r={global_r}; D={depth}')
    return rec

u=load('ultra_870001_1680000.txt',15000056,870001,1680000,15000037,905728,15000037,575974,15000035)
m=load('mid_3950001_4350000.txt',7500056,3950001,4350000,7500036,4084218,7500034,1635300,7500032)
d=load('deep_2400001_3000000.txt',10000056,2400001,3000000,10000036,2955163,10000034,378722,10000032)
# Track the second ultra tie explicitly as an audit aid.
assert any(mb==15000037 and mr==1368912 for _,_,mb,mr in u)
print('RL97 scan-certificate aggregation: PASS')
