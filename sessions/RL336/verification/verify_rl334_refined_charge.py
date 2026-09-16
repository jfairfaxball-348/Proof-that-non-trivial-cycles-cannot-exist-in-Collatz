#!/usr/bin/env python3
import contextlib,io,runpy
from pathlib import Path
from collections import defaultdict,Counter
from functools import lru_cache
with contextlib.redirect_stdout(io.StringIO()):
 B=runpy.run_path(str(Path(__file__).with_name('verify_rl334_self_consistent_ownership.py')))
A=B['A'];ELL=B['ELL'];D=B['D'];LOW=B['LOW'];UP=B['UP'];H=B['H'];CAP=B['CAP'];delta_up=B['delta_up']
factors=B['factors'];residue=B['residue'];reconstruct=B['reconstruct'];realizations=B['realizations']
rows=B['rows'];large=B['large'];by_pair=B['by_pair'];large_pairs=B['large_pairs'];large_pair_links=B['large_pair_links'];pair_links=set(B['pair_links'])
large_t44=set(B['large_t44_pair_links']);t44_large=set(B['t44_large_pair_links']);allowed_large_short=B['allowed_large_short'];allowed_t44_short=B['allowed_t44_short']
HC=20_390_252_058; ZMAX=37; ZS=range(1,ZMAX+1)
Lpairs=sorted(p for p in large_pairs if max(p)<=ZMAX)
Tpairs=sorted(p for p in by_pair if max(p)<=ZMAX)
Lrows=[r for r in large if max(r[:2])<=ZMAX]; Trows=[r for r in rows if max(r[:2])<=ZMAX]
assert len(Lpairs)==141 and len(Tpairs)==31
Lby=defaultdict(list); Tby=defaultdict(list)
for i,r in enumerate(Lrows):Lby[r[:2]].append(i)
for i,r in enumerate(Trows):Tby[r[:2]].append(i)
@lru_cache(None)
def p2_templates(pair):
 left,right=pair;out=[]
 for base in factors(left+right+1):
  for ht in (1,2):
   g=list(base)
   for off,ch in enumerate((ht,1-ht,-1)):g[left-1+off]+=ch
   if min(g[left-1:left+2])<1:continue
   g=tuple(g);q,m=residue(g);out.append((q,m,g))
 return tuple(out)
SHAPES=((1,1,1),(1,2,1),(2,1,1),(2,2,1),(3,2,1))
@lru_cache(None)
def p3_templates(pair):
 left,right=pair;out=[]
 for base in factors(left+right+2):
  for shape in SHAPES:
   qq=(0,)+shape+(0,);g=list(base);ok=True
   for off in range(4):
    pos=left-1+off;g[pos]+=qq[off+1]-qq[off]
    if g[pos]<1:ok=False;break
   if ok:
    g=tuple(g);q,m=residue(g);out.append((q,m,g))
 return tuple(out)
def follows(x,templates,threshold):
 for q,m,g in templates:
  if x%m!=q:continue
  ss=reconstruct(x,g)
  if ss and delta_up*min(ss)>=threshold:return True
 return False
Pall=[]
for total in range(44,99):
 for left in range(max(1,total-ZMAX),min(ZMAX,total-1)+1):
  right=total-left
  if not (1<=right<=ZMAX):continue
  pair=(left,right)
  for q,m,g in p2_templates(pair):
   x=q+max(0,(LOW-q+m-1)//m)*m
   while x<UP:
    if x&1:
     ss=reconstruct(x,g)
     if ss and delta_up*min(ss)>=HC:
      Pall.append((pair,tuple(ss[:left]),tuple(ss[left+2:]),x,min(ss)))
    x+=m
Ppairs=sorted({r[0] for r in Pall});Pby=defaultdict(list)
for i,r in enumerate(Pall):Pby[r[0]].append(i)
assert len(Ppairs)==176
p3pairs=set()
for total in range(44,99):
 for left in range(max(1,total-ZMAX),min(ZMAX,total-1)+1):
  right=total-left
  if not (1<=right<=ZMAX):continue
  pair=(left,right);hit=False
  for q,m,g in p3_templates(pair):
   x=q+max(0,(LOW-q+m-1)//m)*m
   while x<UP:
    if x&1:
     ss=reconstruct(x,g)
     if ss and delta_up*min(ss)>=HC:hit=True;break
    x+=m
   if hit:break
  if hit:p3pairs.add(pair)
Lgroups=defaultdict(list);Tgroups=defaultdict(list)
for r in Lrows:Lgroups[r[:2]].append(r[3])
for r in Trows:Tgroups[r[:2]].append(r[3])
def support_groups(groups):
 p2=set();p3=set()
 for p,xs in groups.items():
  cur=p[1]
  for nz in ZS:
   pr=(cur,nz)
   if any(follows(x,p2_templates(pr),H) for x in xs):p2.add((p,nz))
   if any(follows(x,p3_templates(pr),H) for x in xs):p3.add((p,nz))
 return p2,p3
L_p2,L_p3=support_groups(Lgroups);T_p2,T_p3=support_groups(Tgroups)
pli=defaultdict(list)
for j,r in enumerate(Pall):pli[(r[0][0],r[1][0])].append(j)
PP=set()
for i,r in enumerate(Pall):
 for j in pli[(r[0][1],r[2][0])]:PP.add((r[0],Pall[j][0]))
Lleft=defaultdict(list);Tleft=defaultdict(list)
for j,r in enumerate(Lrows):Lleft[(r[0],r[2])].append(j)
for j,r in enumerate(Trows):Tleft[(r[0],r[2])].append(j)
PL=set();PT=set()
for r in Pall:
 for j in Lleft[(r[0][1],r[2][0])]:PL.add((r[0],Lrows[j][:2]))
 for j in Tleft[(r[0][1],r[2][0])]:PT.add((r[0],Trows[j][:2]))
Pshort=set();P_p2=set();P_p3=set()
for p,inds in Pby.items():
 xs=[Pall[i][2][0] for i in inds];cur=p[1]
 for nz in ZS:
  pr=(cur,nz)
  if cur+nz<=43 and any(B['short_follows'](x,pr) for x in xs):Pshort.add((p,nz))
  if any(follows(x,p2_templates(pr),HC) for x in xs):P_p2.add((p,nz))
  if any(follows(x,p3_templates(pr),HC) for x in xs):P_p3.add((p,nz))
Llinks={(a,b) for a,b in large_pair_links if a in Lpairs and b in Lpairs}
LT={(a,b) for a,b in large_t44 if a in Lpairs and b in Tpairs};TL={(a,b) for a,b in t44_large if a in Tpairs and b in Lpairs};TT={(a,b) for a,b in pair_links if a in Tpairs and b in Tpairs}
states=[('N',z) for z in ZS]+[('L',p) for p in Lpairs]+[('T',p) for p in Tpairs]+[('P',p) for p in Ppairs];ix={s:i for i,s in enumerate(states)}
assert len(states)==385
lpbl=defaultdict(list);tpbl=defaultdict(list)
for p in Lpairs:lpbl[p[0]].append(p)
for p in Tpairs:tpbl[p[0]].append(p)
edges=[]
def posN(s,cur,nz):
 pr=(cur,nz);tot=cur+nz
 if tot<=43:edges.append((s,ix[('N',nz)],nz,2))
 elif pr in Pby:edges.append((s,ix[('P',pr)],nz,2))
 elif pr in p3pairs:edges.append((s,ix[('N',nz)],nz,3))
 else:edges.append((s,ix[('N',nz)],nz,4))
def posLT(s,p,nz,isL):
 cur=p[1];pr=(cur,nz);p2s=L_p2 if isL else T_p2;p3s=L_p3 if isL else T_p3
 if (p,nz) in p2s:
  if cur+nz>=44 and pr in Pby:edges.append((s,ix[('P',pr)],nz,2))
  else:edges.append((s,ix[('N',nz)],nz,2))
 elif (p,nz) in p3s:edges.append((s,ix[('N',nz)],nz,3))
 else:edges.append((s,ix[('N',nz)],nz,4))
def posP(s,p,nz):
 cur=p[1];pr=(cur,nz)
 if (p,nz) in P_p2:
  if cur+nz>=44 and pr in Pby and (p,pr) in PP:edges.append((s,ix[('P',pr)],nz,2))
  else:edges.append((s,ix[('N',nz)],nz,2))
 elif (p,nz) in P_p3:edges.append((s,ix[('N',nz)],nz,3))
 else:edges.append((s,ix[('N',nz)],nz,4))
for z in ZS:
 s=ix[('N',z)]
 for nz in ZS:
  if z+nz<=43:edges.append((s,ix[('N',nz)],nz,1))
  posN(s,z,nz)
 for p in lpbl[z]:edges.append((s,ix[('L',p)],p[1],1))
 for p in tpbl[z]:edges.append((s,ix[('T',p)],p[1],1))
for p in Lpairs:
 s=ix[('L',p)];cur=p[1]
 for nz in ZS:
  if cur+nz<=43 and (p,nz) in allowed_large_short:edges.append((s,ix[('N',nz)],nz,1))
  posLT(s,p,nz,True)
 for q in lpbl[cur]:
  if (p,q) in Llinks:edges.append((s,ix[('L',q)],q[1],1))
 for a,b in LT:
  if a==p:edges.append((s,ix[('T',b)],b[1],1))
for p in Tpairs:
 s=ix[('T',p)];cur=p[1]
 for nz in ZS:
  if cur+nz<=43 and (p,nz) in allowed_t44_short:edges.append((s,ix[('N',nz)],nz,1))
  posLT(s,p,nz,False)
 for a,b in TT:
  if a==p:edges.append((s,ix[('T',b)],b[1],1))
 for a,b in TL:
  if a==p:edges.append((s,ix[('L',b)],b[1],1))
for p in Ppairs:
 s=ix[('P',p)];cur=p[1]
 for nz in ZS:
  if (p,nz) in Pshort:edges.append((s,ix[('N',nz)],nz,1))
  posP(s,p,nz)
 for a,b in PL:
  if a==p:edges.append((s,ix[('L',b)],b[1],1))
 for a,b in PT:
  if a==p:edges.append((s,ix[('T',b)],b[1],1))
print('counts',len(Lpairs),len(Tpairs),len(Ppairs),'edges',len(edges),'pall',len(Pall),'p3pairs',len(p3pairs))
pot=[0]*len(states)
for it in range(len(states)+1):
 ch=False
 for s,t,z,k in edges:
  w=2*z-43*k
  if pot[s]+w>pot[t]:pot[t]=pot[s]+w;ch=True
 if not ch:break
else:raise AssertionError('density positive cycle')
assert all(pot[s]+2*z-43*k<=pot[t] for s,t,z,k in edges)
low={i for i,st in enumerate(states) if st[0]=='N' and st[1]<=21}
sig=[]
for s,t,z,k in edges:
 sg=pot[t]-pot[s]-(2*z-43*k);assert sg>=0;sig.append((s,t,z,k,sg))
q=22;pi=[0]*len(states)
for it2 in range(len(states)+1):
 ch=False
 for s,t,z,k,sg in sig:
  w=q*(k-2*(t in low))-sg
  if pi[s]+w>pi[t]:pi[t]=pi[s]+w;ch=True
 if not ch:break
else:raise AssertionError('q22 positive cycle')
assert all(pi[s]+q*(k-2*(t in low))-sg<=pi[t] for s,t,z,k,sg in sig)
print('RL334_REFINED_CHARGE_GREEN')
print('states_edges',len(states),len(edges))
print('density_potential_range',min(pot),max(pot),'iters',it+1)
print('charge_potential_range',min(pi),max(pi),'iters',it2+1)
print('anchor','22(K-2H)-S<=44')
assert len(edges)==15835
assert min(pi)==0 and max(pi)==44
