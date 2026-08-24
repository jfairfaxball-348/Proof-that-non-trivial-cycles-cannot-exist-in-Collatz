import sys,time,os
A=int(sys.argv[1]);ELL=int(sys.argv[2]);P=ELL-2;Q=A-ELL;X=1<<A;Y=3**ELL

def cap_ok(n,pa):
    return (1<<(n+2))*Y*Y <= (3**(pa+2))*X*X
# At layer n, pa=n-z. Keep minimum H for each (d,T,z).
cur={(1,-14,1):0}
start_time=time.time();total=len(cur);peak=len(cur);hits=[]
# Preterminal pa=P-1 and z<=Q-2 => n<=P-1+Q-2.
NMAX=(P-1)+(Q-2)
for n in range(1,NMAX+1):
    # inspect terminal prestate at this actual layer
    for (d,T,z),H in cur.items():
        pa=n-z
        if pa==P-1 and d==1 and T&1:
            gout=(T+1)//2
            if gout>=4 and gout&(gout-1)==0:
                t=gout.bit_length()-3
                if z+t==Q and t%2==0 and cap_ok(n,pa):
                    hits.append((H,z,t,T,n))
    if n==NMAX:break
    nxt={}
    for (d,T,z),H in cur.items():
        pa=n-z
        for x,y in ((0,0),(1,1),(0,1),(1,0)):
            nd=d+y-x
            if nd<=0:continue
            nh=H+d-1
            z2=z+1-x; pa2=pa+x
            # A counterexample terminal must have t>=2, hence z_final<=Q-2.
            if z2>Q-2 or pa2>P-1:continue
            if pa2+nd>P:continue  # beta prefix weight
            # Necessary forever for a violation H_final < Q-z_final+3.
            if nh+z2>=Q+3:continue
            num=3**y*T+x*3**(d+y-1)-y
            if num&1:continue
            if x and not cap_ok(n,pa):continue
            st=(nd,num//2,z2)
            old=nxt.get(st)
            if old is None or nh<old:nxt[st]=nh
    cur=nxt;total+=len(cur);peak=max(peak,len(cur))
    if n%10==0:
        print('layer',n+1,'states',len(cur),'total',total,'peak',peak,'secs',time.time()-start_time,flush=True)
    if not cur:break
bad=[h for h in hits if h[0]<h[2]+3]
print('PAIR',(A,ELL,Q),'total',total,'peak',peak,'hits',hits,'violations',bad,'secs',time.time()-start_time)
sys.stdout.flush();os._exit(0)
