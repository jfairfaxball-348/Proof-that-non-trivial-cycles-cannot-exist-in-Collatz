#!/usr/bin/env python3

def half(n):
    return n//2 if n % 2 == 0 else (3*n+1)//2

def audit_rl262_modulus():
    A=1417
    ELL=894
    RHO=ELL-3
    M=(1<<A)-3**ELL
    count=0
    Ns=set()
    for k in range(31,526,2):
        top=237*3**RHO-(1<<(A-k+1))
        for N in range(1,289):
            if N%8 != 3:
                continue
            num=top-(N-2)*M
            if num%12:
                continue
            D=num//12
            if D < 0:
                continue
            count += 1
            Ns.add(N)
            assert N%24 == 19
            m=A-k-1
            C=3**RHO*(9*N+61)//4
            gnum=1+(N-2)*(1<<(k-1))
            assert gnum%3 == 0
            G=gnum//3
            T=(4+(N-2)*(1<<(k+1)))//3
            assert T == 4*G
            assert D == C-(1<<m)*G
            assert (D-C)%(1<<m) == 0
    assert count == 2976
    assert sorted(Ns) == list(range(19,284,24))
    return count, len(Ns)

def audit_physical_gap():
    checks=0
    max_depth=0
    for h in range(64):
        N=19+24*h
        A=(9*N+5)//8
        B=(27*N+127)//8
        assert 8*A == 9*N+5
        assert 8*B == 27*N+127
        X=Y=0
        d=1
        rho=96
        S=0
        C=3**rho*(9*N+61)//4
        assert 3*A-B == -14
        for p in range(48):
            assert d == 1+Y-X
            assert d >= 1
            T=3**d*A-B
            J=T+3**d-2**d
            x=A&1
            y=B&1
            assert (J&1) == int(x==y)
            gap=B-3**(d-1)*A
            assert C-S == (1<<p)*3**(rho-Y)*gap
            A1=half(A)
            B1=half(B)
            d1=d+y-x
            num=3**y*T + (x*3**(d+y-1) if x else 0) - y
            assert num%2 == 0
            if d1 < 1:
                break
            assert 3**d1*A1-B1 == num//2
            if x:
                X += 1
                S += (1<<p)*3**(rho-X)
            if y:
                Y += 1
                S -= (1<<p)*3**(rho-Y)
            A,B,d=A1,B1,d1
            checks += 1
            max_depth=max(max_depth,p+1)
    assert checks == 933
    return checks,max_depth

def audit_endpoint_algebra():
    checks=0
    for k in range(3,40,2):
        for h in range(32):
            N=19+24*h
            Bm=N*(1<<(k-2))
            anum=(N+4)*(1<<(k-2))-1
            assert anum%3 == 0
            Am=anum//3
            assert 3*Am-Bm == (1<<k)-1
            gap=Bm-Am
            gnum=1+(N-2)*(1<<(k-1))
            assert gnum%3 == 0
            assert gap == gnum//3
            checks += 1
    assert checks == 608
    return checks

def main():
    qcount,ncount=audit_rl262_modulus()
    pchecks,maxdepth=audit_physical_gap()
    echecks=audit_endpoint_algebra()
    print("PASS RL263 physical-gap barrier")
    print(f"RL262 odd-k quotient cases checked={qcount}; distinct N={ncount}")
    print("restored exact form: Dcal=C-2^m*G with G=(1+(N-2)*2^(k-1))/3")
    print("therefore Dcal==C mod 2^m in the promoted odd-k scope")
    print(f"physical two-trajectory prefix checks={pchecks}; max legal depth={maxdepth}")
    print("verified T_p=3^d A_p-B_p and C-S_p=2^p*3^(rho-Y_p)*(B_p-3^(d-1)A_p)")
    print(f"endpoint algebra checks={echecks}")
    print("ordered dyadic prefix target is automatic on genuine physical full-phase pairs")

if __name__ == "__main__":
    main()
