#include <bits/stdc++.h>
using namespace std;
struct Hash { static uint64_t mix(uint64_t x){x+=0x9e3779b97f4a7c15ULL;x=(x^(x>>30))*0xbf58476d1ce4e5b9ULL;x=(x^(x>>27))*0x94d049bb133111ebULL;return x^(x>>31);} size_t operator()(uint64_t x) const { static const uint64_t seed=0x123456789abcdef0ULL; return mix(x+seed);} };
static inline uint64_t zz(long long j){return (uint64_t(j)<<1) ^ uint64_t(j>>63);} 
static inline long long unzz(uint64_t z){return (long long)((z>>1) ^ (~(z&1)+1));}
static inline uint64_t pack(int d,long long J){uint64_t z=zz(J); if(z >= (1ULL<<56)){cerr<<"pack overflow";exit(3);} return (uint64_t(d)<<56)|z;}
static inline int getd(uint64_t k){return int(k>>56);} static inline long long getj(uint64_t k){return unzz(k&((1ULL<<56)-1));}
int main(){const int HMAX=24; vector<unordered_set<uint64_t,Hash>> seen(HMAX+1); vector<vector<uint64_t>> q(HMAX+1); auto add=[&](int h,int d,long long j){auto k=pack(d,j); if(seen[h].insert(k).second)q[h].push_back(k);}; add(0,1,-13);
 vector<size_t> expected={9,10,9,32,26,49,90,105,172,270,549,859,1768,3578,6906,13642,26624,53758,109744,222460,458460,950914,1987355,4152245};
 for(int H=0;H<=HMAX;H++){ if(H>10)seen[H].reserve(H==24?9000000:(1u<<min(23,H))); size_t pos=0; long long maxabs=0; int maxd=0; int maxmargin=-999; bool bad=false;
  while(pos<q[H].size()) {auto key=q[H][pos++]; int d=getd(key); long long J=getj(key); maxabs=max(maxabs,llabs(J));maxd=max(maxd,d); int K=H+d*(d+1)/2-1; if(J>0){int v=__builtin_ctzll((unsigned long long)J);maxmargin=max(maxmargin,v-K); if(v>K){cout<<"VIOL H="<<H<<" d="<<d<<" J="<<J<<" v="<<v<<" K="<<K<<"\n";bad=true;break;}}
   long long p3=1,p2=1;for(int x=0;x<d;x++){p3*=3;p2*=2;} long long A=p3-p2,B=p2-1,C=3*p3-p2-1; int Hn=H+d-1; if(Hn>HMAX)continue;
   if(J&1){add(Hn,d,(J+A)/2);add(Hn,d,(3*J+B)/2);} else {add(Hn,d+1,(3*J+C)/2);if(d>1)add(Hn,d-1,J/2);} }
  if(H<24 && seen[H].size()!=expected[H]){cerr<<"count mismatch H"<<H<<" got "<<seen[H].size()<<" exp "<<expected[H]<<"\n";return 4;}
  cout<<H<<" "<<seen[H].size()<<" "<<maxd<<" "<<maxabs<<" "<<maxmargin<<"\n"; if(bad)break;
 }
}
