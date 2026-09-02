#!/usr/bin/env python3
from fractions import Fraction
from collections import defaultdict
from pathlib import Path

A=217_976_794_617
L=137_528_045_312
B=A-L
R=L-B
GAP_LOWER=128_081_997_553
GAP_UPPER=293_591_818_782

def ceil_div(a,b): return (a+b-1)//b
def v2(x): return (x & -x).bit_length()-1
def cbit(r): return 1 if r<R else 2

late_max={j:(0 if j==0 else ceil_div(j*B,L)) for j in range(40)}
height_envelope={j:1+late_max[j] for j in range(40)}
rows=defaultdict(list)
for tau in range(26,40):
    ell0=(tau*B)//L
    ell1=ceil_div(tau*B,L)
    for h0 in (0,1):
        lo=GAP_LOWER*(2**h0)
        hi=GAP_UPPER*(2**h0)
        step=2**tau
        for k in range(lo//step+1,(hi-1)//step+1):
            C0=k*step
            vv=v2(C0)
            odd=C0>>vv
            T=(3**tau)*odd
            for ell in sorted({ell0,ell1}):
                H=h0+tau+ell-vv
                if H<1 or H>height_envelope[tau]: continue
                if not (GAP_LOWER*(2**H)<T<GAP_UPPER*(2**H)): continue
                rlo=max(0,tau*B-ell*L)
                rhi=min(L-1,tau*B-(ell-1)*L-1)
                if rlo<=rhi:
                    rows[(T,H)].append((tau,h0,C0,vv,odd,ell,rlo,rhi))

def word_before_terminal(r_terminal,n):
    return tuple(cbit((r_terminal-(n-j)*B)%L) for j in range(n))

def backward_gaps(word,terminal):
    ds=[None]*(len(word)+1)
    ds[-1]=terminal
    for j in range(len(word)-1,-1,-1):
        ds[j]=ds[j+1]*(2**word[j])/3
    return tuple(ds)

def full_prefix_core(rawlo,rawhi,tau,terminal):
    bounds={rawlo,rawhi+1}
    for j in range(tau):
        shift=(tau-j)*B
        for threshold in (0,R):
            q=(threshold+shift)%L
            if rawlo<q<=rawhi: bounds.add(q)
    bounds=sorted(bounds)
    good=[]
    for x,y in zip(bounds,bounds[1:]):
        lo,hi=x,y-1
        if lo>hi: continue
        w=word_before_terminal(lo,tau)
        assert word_before_terminal(hi,tau)==w
        ds=backward_gaps(w,terminal)
        if all(Fraction(GAP_LOWER)<d<Fraction(GAP_UPPER) for d in ds):
            good.append((lo,hi))
    merged=[]
    for lo,hi in good:
        if merged and merged[-1][1]+1==lo:
            merged[-1]=(merged[-1][0],hi)
        else: merged.append((lo,hi))
    return merged

core_by_key_tau={}
for (T,H),rs in rows.items():
    terminal=Fraction(T,2**H)
    dct=defaultdict(list)
    for rr in rs:
        dct[rr[0]].extend(full_prefix_core(rr[-2],rr[-1],rr[0],terminal))
    md={}
    for tau,cs in dct.items():
        merged=[]
        for a,b in sorted(cs):
            if merged and a<=merged[-1][1]+1:
                merged[-1]=(merged[-1][0],max(merged[-1][1],b))
            else: merged.append((a,b))
        md[tau]=merged
    core_by_key_tau[(T,H)]=md

cells=[]
for (T,H),md in core_by_key_tau.items():
    points={0,L}
    for cs in md.values():
        for a,b in cs:
            points.add(a); points.add(b+1)
    ss=sorted(points)
    for a,b1 in zip(ss,ss[1:]):
        b=b1-1
        if a>b: continue
        owners=tuple(sorted(t for t,cs in md.items() if any(x<=a and b<=y for x,y in cs)))
        if owners:
            cells.append({'T':T,'H':H,'rlo':a,'rhi':b,'owners':list(owners)})
cells=sorted(cells,key=lambda x:(x['H'],x['T'],x['rlo'],x['rhi'],x['owners']))
assert len(cells)==7531
# A rational envelope strictly above the exact repaired charges, proved in the
# companion charging verifier: early < 6.102U, all later < 1.138U.  Therefore
# any cell safe under this envelope is certainly safe under the exact schedule.
AE=Fraction(6102,1000)
BL=Fraction(1138,1000)
over=[]
for c in cells:
    q=sum(AE if t<=34 else BL for t in c['owners'])
    generic=Fraction(2**(24-c['H']),1)
    if q>generic:
        over.append((c['T'],c['H'],c['rlo'],c['rhi'],tuple(c['owners'])))
expected=[
(138976514163888075,20,0,13029063886,(31,32,33)),
(150094635296999121,20,0,18406412838,(31,32,33,34,35,36)),
(150094635296999121,20,18406412839,23369453297,(32,33,34,35,36)),
(161212756430110167,20,5377348952,18406412838,(31,32,33)),
(183448998696332259,20,28746802250,62456644958,(32,33,34)),
(216803362095665397,20,62456644959,96166487667,(32,33,34)),
(250157725494998535,20,96166487668,98855162143,(32,33,34,35)),
(283512088894331673,21,0,13029063886,(33,34)),
(316866452293664811,21,5377348952,36398517184,(33,34)),
(350220815692997949,21,23369453298,41775866136,(33,34,35)),
(450283905890997363,21,72797034370,103818202602,(34,35,36,37)),
(1350851717672992089,23,15717738363,46738906595,(37,38)),
(4052555153018976267,24,96166487668,111884226030,(39,)),
]
assert over==expected
print('PASS: RL235 exact full-prefix cell reconstruction / generic-envelope audit')
print('full_prefix_atomic_cells=7531')
print('generic_envelope_candidate_overages=13')
