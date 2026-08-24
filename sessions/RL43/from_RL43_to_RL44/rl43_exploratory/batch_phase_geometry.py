from collections import defaultdict
PAIRS=((0,0),(1,1),(0,1),(1,0))

def batch(a,l,z_target,t,T_target,E_targets):
 p=l-2;h=p+z_target;pa_target=p-1;Emax=max(E_targets);M=(1<<a)-3**l
 assert a==2+h+t
 def nxt(st,x,y,n):
  d,e,T,z,pa=st;pb=pa+d;dd=d+y-x
  if dd<=0:return None
  ee=e+d-x
  if ee>Emax:return None
  num=(3**y)*T+x*3**(d+y-1)-y
  if num&1:return None
  zz=z+1-x; paa=pa+x;pbb=pb+y;rem=(h-1)-(n+1)
  if zz>z_target or zz+rem<z_target:return None
  if paa>pa_target or paa+rem<pa_target:return None
  if pbb>p or pbb+rem<p:return None
  return(dd,ee,num//2,zz,paa)
 f={1:{(1,0,-14,1,0)}}
 for n in range(1,h-1):
  ns=set()
  for st in f[n]:
   for x,y in PAIRS:
    q=nxt(st,x,y,n)
    if q is not None:ns.add(q)
  f[n+1]=ns
 targets={(1,E,T_target,z_target,pa_target) for E in E_targets if (1,E,T_target,z_target,pa_target) in f[h-1]}
 g={h-1:targets}
 for n in range(h-2,0,-1):
  want=g[n+1];cur=set()
  for st in f[n]:
   for x,y in PAIRS:
    if nxt(st,x,y,n) in want:cur.add(st);break
  g[n]=cur
 start=(1,0,-14,1,0)
 initV=(3**(l-1)+2*3**(l-2)+(1<<2)*3**(p-1))%M
 dp={start:{initV}} if start in g[1] else {}
 for n in range(1,h-1):
  ndp=defaultdict(set);allowed=g[n+1]
  for st,vals in dp.items():
   d,e,T,z,pa=st;pb=pa+d
   for x,y in PAIRS:
    q=nxt(st,x,y,n)
    if q not in allowed:continue
    add=0
    if y:
     pbb=pb+y;add=((1<<(2+n))*3**(l-(2+pbb)))%M
    if add:ndp[q].update((v+add)%M for v in vals)
    else:ndp[q].update(vals)
  dp=ndp
 need=(-4*3**l)%M
 out={}
 for E in E_targets:
  vals=dp.get((1,E,T_target,z_target,pa_target),set());out[E]=(len(vals),need in vals)
 return out,sum(map(len,f.values())),sum(map(len,g.values()))

if __name__=='__main__':
 import time
 cases=[(24,0,7,range(26,41)),(22,2,31,range(30,41)),(20,4,127,range(34,41)),(18,6,511,range(35,41))]
 for z,t,T,Es in cases:
  s=time.time();o,fs,gs=batch(65,41,z,t,T,list(Es));print(z,t,o,'f/g',fs,gs,'time',time.time()-s,flush=True)
