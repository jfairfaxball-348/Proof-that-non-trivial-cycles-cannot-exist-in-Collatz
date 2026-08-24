#include <bits/stdc++.h>
using namespace std;
static inline bool power2(__uint128_t x,int& k){
    if(!x || (x&(x-1))) return false;
    k=__builtin_ctzll((unsigned long long)x); // safe for encountered <2^64 here
    if(((__uint128_t)1<<k)!=x){ for(k=0;k<127 && (((__uint128_t)1<<k)!=x);++k); }
    return k<127;
}
static inline bool hit(uint64_t n,int KMIN,int& K){
    __uint128_t x=(n&1ULL)?(__uint128_t)n+1:(__uint128_t)3*n+2;
    int k; if(!power2(x,k)) return false;
    if(k>=KMIN && (k&1)){K=k;return true;} return false;
}
int main(int argc,char**argv){
    uint64_t B=stoull(argv[1]); int KMIN=stoi(argv[2]);
    vector<uint8_t> done(B+1); done[1]=1; if(B>=2)done[2]=1;
    uint64_t first=0,hs=0,peak=0;int hk=0;size_t maxpath=0;
    for(uint64_t s=1;s<=B;s++){
        if(done[s])continue;
        vector<uint64_t> path; uint64_t n=s; unordered_set<uint64_t> loc;
        bool found=false;int K=0;
        while(true){
            if(hit(n,KMIN,K)){found=true;hs=n;break;}
            if(n<=B && done[n])break;
            if(n==1||n==2)break;
            if(!loc.insert(n).second)break;
            if(n<=B)path.push_back(n);
            peak=max(peak,n);
            __uint128_t v=(n&1ULL)?((__uint128_t)3*n+1)/2:n/2;
            if(v>numeric_limits<uint64_t>::max()){cerr<<"overflow\n";return 2;}
            n=(uint64_t)v;
        }
        maxpath=max(maxpath,loc.size());
        if(found){first=s;hk=K;break;}
        for(uint64_t v:path)done[v]=1;
    }
    cout<<"B="<<B<<" KMIN="<<KMIN<<" first_start_hit="<<first<<" hit_state="<<hs<<" K="<<hk<<" max_peak="<<peak<<" max_path="<<maxpath<<"\n";
}
