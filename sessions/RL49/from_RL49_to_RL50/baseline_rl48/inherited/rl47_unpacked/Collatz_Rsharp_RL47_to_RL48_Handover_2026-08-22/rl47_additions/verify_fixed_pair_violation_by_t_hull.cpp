#include <boost/multiprecision/cpp_int.hpp>
#include <unordered_map>
#include <vector>
#include <iostream>
#include <chrono>
#include <cstdint>
#include <algorithm>
using boost::multiprecision::cpp_int;

struct Key {
    cpp_int T;
    uint16_t z;
    uint8_t d;
    bool operator==(Key const& o) const { return T==o.T && z==o.z && d==o.d; }
};
struct KeyHash {
    size_t operator()(Key const& k) const noexcept {
        auto const& b = k.T.backend();
        size_t h = b.sign() ? 0x9e3779b97f4a7c15ULL : 0x243f6a8885a308d3ULL;
        for (unsigned i=0;i<b.size();++i) {
            uint64_t x = static_cast<uint64_t>(b.limbs()[i]);
            h ^= x + 0x9e3779b97f4a7c15ULL + (h<<6) + (h>>2);
        }
        h ^= (static_cast<size_t>(k.z)<<8) ^ k.d;
        return h;
    }
};
struct Hull { cpp_int lo=0, hi=0; bool ok=false; };

static cpp_int floor_div3(cpp_int const& a) {
    if (a>=0) return a/3;
    return - ((-a + 2)/3);
}
static cpp_int ceil_div3(cpp_int const& a) {
    if (a>=0) return (a+2)/3;
    return - ((-a)/3);
}

struct Result {
    bool hit=false;
    int minH=-1;
    uint64_t total=0, peak=0, hull_prune=0;
    double secs=0;
    bool terminal_cap=false;
    bool relaxed_start=false;
};

static Result run_t(int A,int E,int t) {
    int P=E-2, Q=A-E, zt=Q-t, n0=(P-1)+zt, B=t+2;
    Result R;
    if (t<0 || (t&1) || zt<1) return R;
    int DMAX=1;
    while ((DMAX+1)*DMAX/2 <= B) ++DMAX;

    std::vector<cpp_int> p3(DMAX+3), Ad(DMAX+2), Bd(DMAX+2), Cd(DMAX+2);
    p3[0]=1;
    for (int i=1;i<(int)p3.size();++i) p3[i]=p3[i-1]*3;
    for (int d=1;d<=DMAX+1;++d) {
        Ad[d]=p3[d]-(cpp_int(1)<<d);
        Bd[d]=(cpp_int(1)<<d)-1;
        Cd[d]=p3[d+1]-(cpp_int(1)<<d)-1;
    }

    // Exact cap table for every geometry state used by this fixed-t search.
    std::vector<std::vector<char>> cap(n0+1,std::vector<char>(zt+1,0));
    cpp_int X2=cpp_int(1)<<(2*A), Y=1;
    for (int i=0;i<E;++i) Y*=3;
    cpp_int Y2=Y*Y;
    std::vector<cpp_int> pp3(P+3); pp3[0]=1;
    for (int i=1;i<=P+2;++i) pp3[i]=pp3[i-1]*3;
    for (int n=1;n<=n0;++n) for (int z=1;z<=zt;++z) {
        int pa=n-z;
        if (pa<0 || pa>P-1) continue;
        cap[n][z]=((cpp_int(1)<<(n+2))*Y2 <= pp3[pa+2]*X2);
    }
    R.terminal_cap=cap[n0][zt];
    if (!R.terminal_cap) return R;

    // Conservative future J hull.  Parity and /3 divisibility are deliberately
    // relaxed: integer floor/ceil bounds can only ADD possible predecessor J's.
    auto idx=[&](int n,int z,int d){
        return ((size_t)n*(zt+1)+z)*(DMAX+2)+d;
    };
    std::vector<Hull> hull((size_t)(n0+1)*(zt+1)*(DMAX+2));
    cpp_int Jtar=cpp_int(1)<<(t+3);
    hull[idx(n0,zt,1)]={Jtar,Jtar,true};
    for (int n=n0-1;n>=1;--n) {
        for (int z=1;z<=std::min(zt,n);++z) {
            int pa=n-z;
            if (pa<0 || pa>P-1 || !cap[n][z]) continue;
            for (int d=1;d<=DMAX;++d) {
                if (pa+d>P) continue;
                Hull out;
                const int xs[4]={0,1,0,1}, ys[4]={0,1,1,0};
                for (int ii=0;ii<4;++ii) {
                    int x=xs[ii], y=ys[ii], nd=d+y-x;
                    if (nd<=0 || nd>DMAX) continue;
                    int z2=z+1-x, pa2=pa+x;
                    if (z2<1 || z2>zt || pa2>P-1 || pa2+nd>P || !cap[n+1][z2]) continue;
                    Hull const& hn=hull[idx(n+1,z2,nd)];
                    if (!hn.ok) continue;
                    cpp_int lo,hi;
                    if (x==0 && y==0) {
                        lo=2*hn.lo-Ad[d]; hi=2*hn.hi-Ad[d];
                    } else if (x==1 && y==1) {
                        lo=floor_div3(2*hn.lo-Bd[d]); hi=ceil_div3(2*hn.hi-Bd[d]);
                    } else if (x==0 && y==1) {
                        lo=floor_div3(2*hn.lo-Cd[d]); hi=ceil_div3(2*hn.hi-Cd[d]);
                    } else {
                        lo=2*hn.lo; hi=2*hn.hi;
                    }
                    if (!out.ok) out={lo,hi,true};
                    else { if (lo<out.lo) out.lo=lo; if (hi>out.hi) out.hi=hi; }
                }
                hull[idx(n,z,d)]=std::move(out);
            }
        }
    }
    Hull const& hs=hull[idx(1,1,1)];
    cpp_int Jstart=-13;
    R.relaxed_start=hs.ok && Jstart>=hs.lo && Jstart<=hs.hi;
    if (!R.relaxed_start) return R;

    cpp_int Ttarget=Jtar-1;
    std::unordered_map<Key,uint8_t,KeyHash> cur,nxt;
    cur.max_load_factor(.72); nxt.max_load_factor(.72);
    cur.reserve(1024); cur[{cpp_int(-14),1,1}]=0;
    R.total=1; R.peak=1;
    auto start=std::chrono::steady_clock::now();

    for (int n=1;n<n0;++n) {
        nxt.clear(); nxt.reserve(cur.size()*2+16);
        for (auto const& kv:cur) {
            Key const& k=kv.first; int H=kv.second, z=k.z, d=k.d, pa=n-z;
            if (!cap[n][z]) continue;
            Hull const& hc=hull[idx(n,z,d)];
            cpp_int J=k.T+Ad[d];
            if (!hc.ok || J<hc.lo || J>hc.hi) { ++R.hull_prune; continue; }
            const int xs[4]={0,1,0,1}, ys[4]={0,1,1,0};
            for (int ii=0;ii<4;++ii) {
                int x=xs[ii], y=ys[ii], nd=d+y-x;
                if (nd<=0 || nd>DMAX) continue;
                int nh=H+d-1, z2=z+1-x, pa2=pa+x;
                // Fixed-t violation: H_terminal <= t+2.  Also reserve the
                // unavoidable triangular descent area from nd back to height 1.
                if (nh>B || nh+nd*(nd-1)/2>B || z2>zt || pa2>P-1 || pa2+nd>P || !cap[n+1][z2]) continue;
                cpp_int num=(y?3:1)*k.T;
                if (x) num+=p3[d+y-1];
                if (y) num-=1;
                if ((num&1)!=0) continue;
                cpp_int T2=num/2, J2=T2+Ad[nd];
                Hull const& hn=hull[idx(n+1,z2,nd)];
                if (!hn.ok || J2<hn.lo || J2>hn.hi) { ++R.hull_prune; continue; }
                Key kk{T2,(uint16_t)z2,(uint8_t)nd};
                auto it=nxt.find(kk);
                if (it==nxt.end()) nxt.emplace(std::move(kk),(uint8_t)nh);
                else if (nh<it->second) it->second=(uint8_t)nh;
            }
        }
        cur.swap(nxt); R.total+=cur.size(); R.peak=std::max<uint64_t>(R.peak,cur.size());
        if (cur.empty()) break;
    }

    int minH=1000000;
    for (auto const& kv:cur) {
        Key const& k=kv.first;
        if (k.z==zt && k.d==1 && k.T==Ttarget) minH=std::min(minH,(int)kv.second);
    }
    if (minH<1000000) { R.hit=true; R.minH=minH; }
    R.secs=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
    return R;
}

int main(int argc,char**argv) {
    if (argc!=3) { std::cerr<<"usage: verifier A ELL\n"; return 2; }
    int A=std::stoi(argv[1]), E=std::stoi(argv[2]), Q=A-E;
    bool any=false;
    uint64_t grand=0, maxpeak=0, grandprune=0;
    double secs=0;
    for (int t=0;t<Q;t+=2) {
        Result r=run_t(A,E,t);
        if (!r.terminal_cap) {
            std::cout<<"t "<<t<<" terminal_cap_false\n";
            continue;
        }
        if (!r.relaxed_start) {
            std::cout<<"t "<<t<<" relaxed_hull_excludes_start\n";
            continue;
        }
        std::cout<<"t "<<t<<" total "<<r.total<<" peak "<<r.peak<<" hull_prune "<<r.hull_prune
                 <<" hit "<<(r.hit?1:0)<<" minH "<<r.minH<<" secs "<<r.secs<<"\n";
        grand+=r.total; maxpeak=std::max(maxpeak,r.peak); grandprune+=r.hull_prune; secs+=r.secs;
        any = any || r.hit;
    }
    std::cout<<"PAIR ("<<A<<","<<E<<","<<Q<<") any_violation "<<(any?1:0)
             <<" grand_states "<<grand<<" max_peak "<<maxpeak<<" hull_prunes "<<grandprune<<" secs "<<secs<<"\n";
    return any?1:0;
}
