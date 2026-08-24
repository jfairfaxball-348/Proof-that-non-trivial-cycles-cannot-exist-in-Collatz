#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>

using boost::multiprecision::cpp_int;
using u128 = unsigned __int128;

static std::vector<u128> P3;
static unsigned long long calls=0, trap_hits=0, xfree_calls=0;
static int max_v_seen=0, min_precision_seen=1000000, max_depth_seen=0;
static bool ambiguous=false;
static int XMAX=0,YMAX=0;

static std::string s128(u128 x){ if(!x) return "0"; std::string s; while(x){s.push_back('0'+x%10);x/=10;} reverse(s.begin(),s.end()); return s; }
static u128 mod_cpp(const cpp_int &a, u128 m){ cpp_int mm=0; mm += (uint64_t)(m>>64); mm <<= 64; mm += (uint64_t)m; cpp_int r=a%mm; u128 out=(u128)r.convert_to<uint64_t>(); cpp_int hi=r>>64; out |= (u128)hi.convert_to<uint64_t>()<<64; return out; }
static u128 powmod2_cpp(cpp_int e,u128 m){ cpp_int mm=0; mm+=(uint64_t)(m>>64); mm<<=64; mm+=(uint64_t)m; cpp_int r=boost::multiprecision::powm(cpp_int(2),e,mm); return mod_cpp(r,m); }

static inline int valuation(u128 q,int precision){
    if(q==0){ambiguous=true; return precision;}
    int v=0; while(v<precision && q%3==0){q/=3; ++v;} if(v==precision) ambiguous=true; return v;
}

// Exact x-zero-free suffix solver: only 11 and 10 remain.
// Pair optimization: after a 10 taken at r<v, q' = 2 q_r+1 ==1 mod3,
// so the next step has v3=0 and if continued must be a 10. We can fold
// those two 10 events into one transition consuming 2 y-zeroes.
static int xfree(u128 q,int precision,int yrem){
    ++xfree_calls;
    int v=valuation(q,precision); if(ambiguous) return 1000000;
    max_v_seen=std::max(max_v_seen,v); min_precision_seen=std::min(min_precision_seen,precision);
    int best=v; // stop after all legal 11s
    u128 qr=q; int pr=precision;
    for(int r=0;r<=v;r++){
        if(yrem>=1){
            u128 nq=2*qr+1; // < 2*3^pr, reduce once
            if(nq>=P3[pr]) nq-=P3[pr];
            if(r==v){
                // after exhausting all 11s, valuation of 2*unit+1 can vary
                best=std::max(best,r+1+xfree(nq,pr,yrem-1));
            } else {
                // nq == 1 mod3, so next event (if any) is forced 10; fold it.
                best=std::max(best,r+1); // may stop immediately
                if(yrem>=2){
                    u128 nq2=2*nq+1; if(nq2>=P3[pr]) nq2-=P3[pr];
                    best=std::max(best,r+2+xfree(nq2,pr,yrem-2));
                }
            }
        }
        if(r<v){ --pr; qr=2*(qr/3); if(qr>=P3[pr]) qr-=P3[pr]; }
    }
    return best;
}

static int dfs(u128 q,int precision,int xu,int yu,int depth){
    ++calls; min_precision_seen=std::min(min_precision_seen,precision); max_depth_seen=std::max(max_depth_seen,depth);
    int v=valuation(q,precision); if(ambiguous) return 1000000;
    max_v_seen=std::max(max_v_seen,v);
    if((q%3)==2){ ++trap_hits; return YMAX-yu; }
    if(xu==XMAX){ return xfree(q,precision,YMAX-yu); }
    int best=v;
    u128 qr=q; int pr=precision;
    int d=1+yu-xu; if(d<1){std::cerr<<"height fail\n"; exit(3);}    
    for(int r=0;r<=v;r++){
        // 10
        if(yu<YMAX){
            u128 nq=2*qr+1; if(nq>=P3[pr]) nq-=P3[pr];
            best=std::max(best,r+1+dfs(nq,pr,xu,yu+1,depth+r+1));
        }
        // 00
        if(xu<XMAX && yu<YMAX){
            u128 c=P3[d]-1; u128 a=2*qr; if(a>=P3[pr]) a-=P3[pr];
            u128 nq=(a>=c)?a-c:a+P3[pr]-c;
            best=std::max(best,r+1+dfs(nq,pr,xu+1,yu+1,depth+r+1));
        }
        // 01
        if(xu<XMAX && d>1 && r<v){
            int np=pr-1; u128 a=2*(qr/3); if(a>=P3[np]) a-=P3[np];
            u128 c=P3[d-1]; u128 nq=(a>=c)?a-c:a+P3[np]-c;
            best=std::max(best,r+1+dfs(nq,np,xu+1,yu,depth+r+1));
        }
        if(r<v){ --pr; qr=2*(qr/3); if(qr>=P3[pr]) qr-=P3[pr]; }
    }
    return best;
}

int main(int argc,char**argv){
    if(argc<4||argc>5){std::cerr<<"usage Z XMAX YMAX [PREC=80]\n";return 2;}
    int Z=atoi(argv[1]); XMAX=atoi(argv[2]);YMAX=atoi(argv[3]);int PREC=argc==5?atoi(argv[4]):80;
    if(PREC<2||PREC>80){std::cerr<<"precision 2..80\n";return 2;}
    P3.resize(std::max(PREC+1,YMAX+3)); P3[0]=1; for(size_t i=1;i<P3.size();i++) P3[i]=P3[i-1]*3;
    const cpp_int A("123139092617126647266"), ELL("77692117359936589403"); cpp_int K=A-ELL-Z+3;
    u128 q0=powmod2_cpp(K,P3[PREC]); q0++; if(q0>=P3[PREC]) q0-=P3[PREC];
    auto t=std::chrono::steady_clock::now(); int ans=dfs(q0,PREC,0,0,0); double sec=std::chrono::duration<double>(std::chrono::steady_clock::now()-t).count();
    std::cout<<"Z="<<Z<<" XMAX="<<XMAX<<" YMAX="<<YMAX<<" max_tail="<<ans<<" calls="<<calls<<" xfree_calls="<<xfree_calls<<" trap_hits="<<trap_hits<<" max_v="<<max_v_seen<<" min_precision="<<min_precision_seen<<" max_depth="<<max_depth_seen<<" ambiguous="<<(ambiguous?1:0)<<" seconds="<<sec<<"\n";
    return ambiguous?1:0;
}
