# enumerate viable residues depth 30, collect synchronized gap pairs after j>=3
exec(open('/mnt/data/RL27_work/test_three_start_lifts.py').read().split('surv=[27]')[0])
def T(n): return (3*n+1)//2 if n&1 else n//2
K=30
surv=[27]
for k in range(6,K+1):
    old=1<<(k-1); ns=[]
    for r in surv:
      for rr in (r,r+old):
        ok,_=viable(rr,k)
        if ok:ns.append(rr)
    surv=ns
print('survivors',len(surv))
pairs=set(); byj={}
for r in surv:
    xs=[r,r+12,r+4]; ps=[0,0,0]
    for j in range(K+1):
        if j>=3 and ps[0]==ps[1]==ps[2]:
            G=xs[1]-xs[0];H=xs[2]-xs[0]
            pairs.add((G,H));byj.setdefault(j,set()).add((G,H))
        if j==K:break
        for i in range(3):
            b=xs[i]&1;ps[i]+=b;xs[i]=T(xs[i])
print('num sync pairs',len(pairs),'min coords sample',sorted(pairs,key=lambda t:abs(t[0])+abs(t[1]))[:30])
target=(-8,-12)
print('target present',target in pairs)
for m in range(2,101):
    residues={(g%m,h%m) for g,h in pairs}
    if (target[0]%m,target[1]%m) not in residues:
        print('candidate modulus excludes target',m,'residue count',len(residues));break
for j in sorted(byj):
    if j<=20:
      vals=byj[j]
      print('j',j,'n',len(vals),'sample',list(vals)[:8])
