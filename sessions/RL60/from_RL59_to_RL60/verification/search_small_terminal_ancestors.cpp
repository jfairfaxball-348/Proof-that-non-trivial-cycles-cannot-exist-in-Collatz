#include <bits/stdc++.h>
using namespace std;

static inline bool ispow2_u128(__uint128_t x, int &k){
    if(x==0 || (x&(x-1))) return false;
    k=0; while(((__uint128_t)1<<k)!=x && k<127) ++k;
    return k<127;
}
static inline bool terminal_hit(unsigned long long n, int &K){
    __uint128_t x;
    if(n&1ULL) x=(__uint128_t)n+1;
    else x=(__uint128_t)3*n+2;
    int k;
    if(!ispow2_u128(x,k)) return false;
    if(k>=25 && (k&1)){ K=k; return true; }
    return false;
}
int main(int argc,char**argv){
    uint64_t B= argc>1? stoull(argv[1]):10000000ULL;
    vector<uint8_t> done(B+1,0); // 1 known no high-terminal hit before reaching 1-cycle
    done[1]=1; done[2]=1;
    uint64_t min_start=0, hit_n=0; int hitK=0;
    uint64_t max_peak=0; size_t max_path=0;
    for(uint64_t s=1;s<=B;s++){
        if(done[s]) continue;
        vector<uint64_t> path;
        uint64_t n=s;
        bool hit=false; int K=0; uint64_t hn=0;
        unordered_set<uint64_t> local; // safety; paths small
        while(true){
            if(terminal_hit(n,K)){ hit=true; hn=n; break; }
            if(n<=B && done[n]) break;
            if(n==1 || n==2) break;
            if(!local.insert(n).second) break;
            if(n<=B) path.push_back(n);
            max_peak=max(max_peak,n);
            if(n&1ULL){
                __uint128_t v=(__uint128_t)3*n+1;
                v/=2;
                if(v>numeric_limits<uint64_t>::max()){ cerr<<"overflow\n"; return 2; }
                n=(uint64_t)v;
            } else n/=2;
            if(local.size()>1000000){ cerr<<"path too long\n"; return 3; }
        }
        max_path=max(max_path,local.size());
        if(hit){ min_start=s; hit_n=hn; hitK=K; break; }
        for(auto v:path) done[v]=1;
    }
    cout<<"B="<<B<<" first_start_hit="<<min_start<<" hit_state="<<hit_n<<" K="<<hitK
        <<" max_peak_seen="<<max_peak<<" max_path="<<max_path<<"\n";
    if(min_start==0) cout<<"CERT: every n<=B avoids any terminal-alternative state with odd K>=25 before entering an already-certified no-hit trajectory.\n";
}
