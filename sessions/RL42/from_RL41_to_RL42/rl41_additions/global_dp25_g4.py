from fractions import Fraction
from collections import defaultdict
from functools import lru_cache
import time
N=25;G=4;BUD=Fraction(31,4)
# E exact from fast sweep
Evals='''1 1/4
2 16/27
3 13/16
4 188/135
5 53/32
6 560/243
7 377/135
8 401/128
9 5068/1215
10 1321/270
11 1369/256
12 13552/2187
13 8713/1215
14 8929/1080
15 9121/1024
16 22300/2187
17 28361/2430
18 28793/2160
19 466832/32805
20 59083/4096
21 179297/10935
22 181241/9720
23 182969/8640
24 147604/6561
25 185963/8192'''
E={int(a):Fraction(b) for a,b in (ln.split() for ln in Evals.splitlines())}
F=[Fraction(0)]*(N+1)
for n in range(1,N+1):F[n]=max(E[r]+F[n-r] for r in range(1,n+1))
# dedup small physical types <=17
sb=defaultdict(dict)
with open('/mnt/data/rl41_work/small_types_18_fast_raw.tsv') as f:
 next(f)
 for ln in f:
  r,D,h,p,sn,sd=map(int,ln.split());k=(D,h,p);s=Fraction(sn,sd)
  if k not in sb[r] or s>sb[r][k]:sb[r][k]=s
small={r:[(D,h,p,s) for (D,h,p),s in d.items()] for r,d in sb.items()}
cb=defaultdict(dict)
with open('/mnt/data/rl41_work/cross_types_25_fast_raw.tsv') as f:
 next(f)
 for ln in f:
  r,D,h,p,sn,sd,g,om=map(int,ln.split());k=(D,h,p,om);s=Fraction(sn,sd)
  if k not in cb[(r,g)] or s>cb[(r,g)][k]:cb[(r,g)][k]=s
cross={(r,g):[(om,h,p,s,D) for (D,h,p,om),s in d.items()] for (r,g),d in cb.items()}

def v2(n):
 s=0
 while n%2==0:n//=2;s+=1
 return s,n
@lru_cache(None)
def noncross(g,r):
 best={}
 for D,h,p,S in small.get(r,()):
  base=3**p*g;den=1<<h
  for sig in (1,-1):
   n=base-sig*D
   if n<=0 or n%den:continue
   out=n//den;k=(out,h,p)
   if k not in best or S>best[k]:best[k]=S
 return tuple((out,h,p,S) for (out,h,p),S in best.items())
def term(m):
 if m%G:return False
 q=m//G;return q>0 and q&(q-1)==0
def near(A,B):
 x=1<<A;y=3**B;return x>y and 15*x*x<16*y*y
# K=P/g=2^A/3^B, start g=9 -> B=2
states=[{} for _ in range(N+1)]; states[0][(9,0,2,0)]=Fraction(0)
hits=[]; trans=0;st=time.time()
for area in range(N):
 if states[area]: print('area',area,'states',len(states[area]),flush=True)
 for (g,A,B,cnt),S in list(states[area].items()):
  remtot=N-area
  if S+F[remtot]<=BUD:continue
  # noncross r <=17, and need room for a crossing if cnt even? terminal must odd; if cnt=0 or2 need >=7 left eventually.
  needcross = (cnt%2==0)
  maxr=min(18, remtot-(7 if needcross else 0))
  for r in range(1,maxr+1):
   rem=N-area-r
   if S+E[r]+F[rem]<=BUD:continue
   for out,h,p,Sx in noncross(g,r):
    trans+=1;S2=S+Sx
    if S2+F[rem]<=BUD:continue
    sv,odd=v2(out)
    if rem==0:
     if cnt in (1,3) and S2>BUD and term(out):
      AA=A+h+sv;BB=B+p
      if near(AA,BB):hits.append(('Nfinal',area,(g,A,B,cnt),r,(out,h,p,Sx),AA,BB,S2))
     continue
    for c in range(sv+1):
     k=(odd*3**c,A+h+sv,B+p+c,cnt)
     old=states[area+r].get(k)
     if old is None or S2>old:states[area+r][k]=S2
  # crossing if cnt<3
  if cnt<3:
   for r in range(7,remtot+1):
    rem=N-area-r
    # after crossing count cnt+1; if now even and <3, need room for another crossing
    cnt2=cnt+1
    if cnt2%2==0 and rem<7:continue
    for out,h,p,Sx,D in cross.get((r,g),()):
     trans+=1;S2=S+Sx
     if S2+F[rem]<=BUD:continue
     sv,odd=v2(out)
     if rem==0:
      if cnt2 in (1,3) and S2>BUD and term(out):
       AA=A+h+sv;BB=B+p
       if near(AA,BB):hits.append(('Cfinal',area,(g,A,B,cnt),r,(out,h,p,Sx,D),AA,BB,S2))
      continue
     for c in range(sv+1):
      k=(odd*3**c,A+h+sv,B+p+c,cnt2)
      old=states[area+r].get(k)
      if old is None or S2>old:states[area+r][k]=S2
print('DONE',time.time()-st,'trans',trans,'hits',len(hits),'cache',noncross.cache_info())
print('hit tuples')
for h in hits:print(h)
