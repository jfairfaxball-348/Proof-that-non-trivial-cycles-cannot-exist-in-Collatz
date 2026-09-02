#!/usr/bin/env python3
from fractions import Fraction

A=217_976_794_617
L=137_528_045_312
B=A-L
R=L-B
H=17

FAMS={
 "A":{
   "tau":32,
   "T":20_383_222_077_370_251,
   "core":(5_377_348_952,28_746_802_249),
   "start":188_978_561_024,
 },
 "B":{
   "tau":33,
   "T":27_795_302_832_777_615,
   "core":(72_797_034_370,103_818_202_602),
   "start":171_798_691_840,
 },
}
EXPECTED={
 ("A","A"):(13_823,329,8_249_443,(665,28_535_317_275,28_738_140_792,188_978_561_024,1003)),
 ("A","B"):(18_149,383,85_336_126,(582,28_535_317_275,28_746_802_249,171_798_691_840,870)),
 ("B","A"):(18_241,383,77_331_112,(748,90_163_345_248,90_366_168_765,188_978_561_024,1135)),
 ("B","B"):(24_179,437,7_499_467,(665,103_606_717_628,103_809_541_145,171_798_691_840,1002)),
}

def cbit(r): return 1 if r<R else 2

def overlap_core(src_core,tgt_core,sep):
    slo,shi=src_core
    tlo,thi=tgt_core
    sh=(sep*B)%L
    out=[]
    for k in range(-2,3):
        a=max(slo,tlo-sh+k*L)
        b=min(shi,thi-sh+k*L)
        if a<=b:
            out.append((a,b))
    return out

def atom_intervals(lo,hi,n):
    bounds={lo,hi+1}
    for j in range(n):
        shift=(j*B)%L
        for q in (0,R):
            x=(q-shift)%L
            if lo<x<=hi:
                bounds.add(x)
    ss=sorted(bounds)
    return [(a,b-1) for a,b in zip(ss,ss[1:]) if a<=b-1]

def universal_params(word):
    radnum=0
    S=0
    for c in word:
        radnum=3*radnum+2*(1<<S)
        S+=c
    return radnum,S

def scan(src,tgt):
    sf=FAMS[src]; tf=FAMS[tgt]
    atoms=0; nonempty=0; min_margin=None; worst=None
    for sep in range(tf["tau"]+1,1001):
        ovs=overlap_core(sf["core"],tf["core"],sep)
        if ovs: nonempty += 1
        n=sep-tf["tau"]
        p3=3**n
        for a,b in ovs:
            for x,y in atom_intervals(a,b,n):
                word=tuple(cbit((x+j*B)%L) for j in range(n))
                assert tuple(cbit((y+j*B)%L) for j in range(n))==word
                radnum,S=universal_params(word)
                denexp=H+S
                cnum=sf["T"]*p3
                target=tf["start"]
                distnum=abs(cnum-target*(1<<denexp))
                rhs=radnum*(1<<H)
                assert distnum>rhs
                margin=Fraction(distnum-rhs,1<<denexp)
                if min_margin is None or margin<min_margin:
                    min_margin=margin
                    worst=(sep,x,y,target,S)
                atoms += 1
    return atoms,nonempty,min_margin,worst

for edge,exp in EXPECTED.items():
    atoms,nonempty,margin,worst=scan(*edge)
    ea,en,ef,ew=exp
    assert atoms==ea,(edge,atoms,ea)
    assert nonempty==en,(edge,nonempty,en)
    assert margin>ef,(edge,margin,ef)
    assert worst==ew,(edge,worst,ew)
    print(f"{edge[0]}->{edge[1]} atoms={atoms} nonempty={nonempty} margin_gt={ef} worst={worst}")

print("PASS: RL232 exact cross-family H17 return exclusion through separation 1000")
print("combined_H17_spacing_ge=1001")
print("classification=EXACT_FINITE_CERTIFICATE")
