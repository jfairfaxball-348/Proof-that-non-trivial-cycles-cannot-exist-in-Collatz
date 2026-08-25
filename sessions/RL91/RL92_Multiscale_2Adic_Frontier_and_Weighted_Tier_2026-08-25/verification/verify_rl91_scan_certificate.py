#!/usr/bin/env python3
from pathlib import Path
import re
HERE=Path(__file__).parent
p=HERE/'RL91_MULTISCALE_2ADIC_SCAN.txt'
text=p.read_text()
assert 'sstar=26594276905' in text
pat=re.compile(r'N=(\d+) chunk=(\d+)\.\.(\d+) min_bits=(\d+) at_r=(\d+)')
raw=[]
for fp in sorted((HERE/'raw').glob('*.txt')):
    m=pat.fullmatch(fp.read_text().strip())
    assert m,fp
    raw.append((*map(int,m.groups()),fp.name))
wide=sorted((a,b,bits,r,name) for N,a,b,bits,r,name in raw if N==5_000_056)
deep=sorted((a,b,bits,r,name) for N,a,b,bits,r,name in raw if N==10_000_056)

def audit(rows,end,expected):
    cur=0; g=None
    for a,b,bits,r,name in rows:
        assert a==cur,(cur,a,b,name)
        assert a<=r<=b
        cur=b+1
        x=(bits,r)
        if g is None or x<g:g=x
    assert cur==end+1,(cur,end)
    assert g==expected,(g,expected)
    return len(rows)

nw=audit(wide,7_000_000,(5_000_032,2_595_446))
nd=audit(deep,300_000,(10_000_037,33_524))
for s in [
 'modulus_bits=5000056','r_range=0..7000000',
 'global_min_balanced_bitlen=5000032 at_r=2595446',
 'certificate: every balanced inverse residue has |mu_r| >= 2^5000031',
 'consequence: d<=5000030 and r<=7000000 under minimal reset => n_next<=5000053',
 'modulus_bits=10000056','r_range=0..300000',
 'global_min_balanced_bitlen=10000037 at_r=33524',
 'certificate: every balanced inverse residue has |mu_r| >= 2^10000036',
 'consequence: d<=10000035 and r<=300000 under minimal reset => n_next<=10000053',
 'RL91 multiscale scan certificate: PASS']:
    assert s in text,s
print('RL91 multiscale frozen scan-certificate aggregation: PASS')
print('wide raw chunks =',nw,'covered r=0..7000000; min=5000032 at r=2595446')
print('deep raw chunks =',nd,'covered r=0..300000; min=10000037 at r=33524')
