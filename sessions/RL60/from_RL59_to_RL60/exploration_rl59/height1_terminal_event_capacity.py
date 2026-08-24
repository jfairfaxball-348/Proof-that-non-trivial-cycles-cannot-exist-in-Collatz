from functools import lru_cache
QGAP=45446975257190057863

def capacity(z,P=180):
    K=QGAP-z+3
    mod=3**P
    q=(pow(2,K,mod)+1)%mod
    amb=False
    @lru_cache(None)
    def rec(q,p,c):
        nonlocal amb
        # q is residue mod 3^p representing actual positive Q; require v3 exact below p
        if p<=0:
            amb=True; return -10**9
        # valuation
        qq=q; v=0
        while v<p and qq%3==0:
            qq//=3; v+=1
        if v==p:
            amb=True; return -10**9
        # if no zeros left, all remaining 11 backwards can be taken up to exact valuation
        best=v if c==0 else -10**9
        qr=q; pr=p
        # choose r inverse-11s, then one inverse-00 if c>0
        for r in range(v+1):
            if c>0:
                # after r divisions: residue qr mod3^pr; inverse00 Q'=2Q-2
                nq=(2*qr-2)%(3**pr)
                val=rec(nq,pr,c-1)
                if val>-10**8: best=max(best,r+val)
            if r<v:
                # Q <- 2Q/3, modulus drops one power
                qr=(2*(qr//3))%(3**(pr-1)); pr-=1
        return best
    m=rec(q,P,z-27)
    return K,z-27,m,amb,rec.cache_info()

for z in range(41,82,2):
    print(z,capacity(z))
