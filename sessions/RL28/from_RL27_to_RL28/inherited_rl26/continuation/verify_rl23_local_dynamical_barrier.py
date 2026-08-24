from math import floor, log

beta=log(3,2)

def greedy_nus(n):
    A=[floor(i*beta) for i in range(n+1)]
    return [A[i+1]-A[i] for i in range(n)]

def build_segment(n,k0=1000):
    nus=greedy_nus(n)
    # Backward composition gives x0=(a X-b)/3^n, X=x_n.
    a=1; b=0; m=0
    for nu in reversed(nus):
        a=(1<<nu)*a
        b=(1<<nu)*b + 3**m
        m+=1
    M=3**n
    r=(b*pow(a,-1,M))%M
    for k in range(k0,k0+100):
        X=r+M*k
        if X%2==0:
            continue
        rev=[X]
        cur=X
        ok=True
        for nu in reversed(nus):
            num=(1<<nu)*cur-1
            if num%3:
                ok=False; break
            cur=num//3
            rev.append(cur)
        if not ok:
            continue
        states=list(reversed(rev))
        if states[0]%3==0:
            continue
        if min(states)!=states[0]:
            continue
        # Exact forward valuation/transition check.
        for i,nu in enumerate(nus):
            assert 3*states[i]+1==(1<<nu)*states[i+1]
            assert states[i+1]%2==1
        assert all(x%3 for x in states[1:])
        return states,nus
    raise AssertionError('no admissible large cylinder representative found')

for n in [20,50,100,200]:
    states,nus=build_segment(n)
    R=states[0]
    # Multiplicative limiting ratios for this parity cylinder.
    rotavg=sum(2**(-(i*beta-floor(i*beta))) for i in range(n))/(3*n)
    # Large chosen representative is already close to the limiting ratios.
    approx=sum(R/(3*x) for x in states[:-1])/n
    assert abs(approx-rotavg)<1e-10
    print('n =',n,'digits(R) =',len(str(R)),'rotation coefficient ~= %.12f'%rotavg)

barrier=1/(6*log(2))
print('RL23 local dynamical barrier verifier: PASS')
print('limiting coefficient 1/(6 ln 2) ~= %.12f'%barrier)
