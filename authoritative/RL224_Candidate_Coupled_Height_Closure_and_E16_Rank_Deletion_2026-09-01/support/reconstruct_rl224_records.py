#!/usr/bin/env python3
"""Reconstruct the exact inherited e=16 finite prefix/k-window input used by RL224."""
from fractions import Fraction
from pathlib import Path
import sys

A=217_976_794_617
L=137_528_045_312
p=65_470_613_321
u=103_768_467_013
z=L-p
K0=1<<37
DELETED_Q=43_013_953

def b(i): return A*i//L

def main(out_path: str) -> None:
    bs=[b(i) for i in range(17)]
    assert bs==[0,1,3,4,6,7,9,11,12,14,15,17,19,20,22,23,25]
    c=[bs[i+1]-bs[i] for i in range(16)]
    states={(0,1)}
    for i in range(1,16):
        nxt=set()
        for h,Q in states:
            S=bs[i]-h
            for hn in range(h+c[i]):
                a=c[i]+h-hn
                assert a>=1
                nxt.add((hn,3*Q+(1<<S)))
        states=nxt
    terminal=sorted(Q for h,Q in states if h==1)
    assert len(terminal)==108_950

    S=24
    gap=3**16 * 2**13
    mod16=3**16
    mod17=3**17
    inv16=pow(1<<(S+34),-1,mod16)
    rows=[]
    for Q in terminal:
        eta0=((1<<S)+Q)*inv16 % mod16
        if eta0%9 not in (0,8):
            continue
        y16=(1<<34)*eta0-1-gap
        num=(1<<S)*y16-Q
        assert num%mod16==0
        y0base=num//mod16
        valid=[]
        for t in range(3):
            y0=y0base+(1<<(S+34))*t
            if y0%3 and (y0+K0)%3:
                valid.append((t,y0))
        assert len(valid)==1
        t,y0=valid[0]
        eta=eta0+t*mod16
        rows.append((Q,eta,y0))
    assert len(rows)==45_046 and rows[0][0]==DELETED_Q

    U=sum(Fraction(2,(2*n+1)*3**(2*n+1)) for n in range(7))
    U+=Fraction(1,20*3**14)
    W=U+Fraction(z,1<<40)
    LB=Fraction(K0)*(L-W)/W
    step=3*(1<<58)
    CAPNUM=48*L*K0
    M=1<<22
    forbidden=pow(pow(3,34,M),-1,M)
    r_odd=forbidden
    r_even=(forbidden-21)%M
    invN22=pow(mod17,-1,M)

    records=[]
    pre=post=removed=0
    for Q,eta,y0 in rows:
        kmax=(CAPNUM-1-29*y0)//(29*step)
        num=LB.numerator-LB.denominator*y0
        kmin=0 if num<0 else num//(LB.denominator*step)+1
        n=kmax-kmin+1
        bad=[]
        for rr in (r_odd,r_even):
            k=((rr-eta)*invN22)%M
            if kmin<=k<=kmax:
                bad.append(k)
        bad=sorted(set(bad))
        records.append((Q,eta,y0,kmin,kmax,bad))
        pre+=n; post+=n-len(bad); removed+=len(bad)
    assert pre==331_935_455 and post==331_935_285 and removed==170
    assert records[0][3:5]==(28_812,36_180) and records[0][5]==[]
    assert post-(records[0][4]-records[0][3]+1)==331_927_916

    out=Path(out_path)
    with out.open('w',encoding='utf-8',newline='') as f:
        for Q,eta,y0,lo,hi,bad in records:
            f.write(f"{Q}\t{eta}\t{y0}\t{lo}\t{hi}\t{','.join(map(str,bad))}\n")
    print(out)
    print("records=45046 current_prefixes=45045 current_candidates_pre_height=331927916")

if __name__=='__main__':
    main(sys.argv[1] if len(sys.argv)>1 else 'rl224_records.tsv')
