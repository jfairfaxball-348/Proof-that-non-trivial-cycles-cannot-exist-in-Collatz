#include <bits/stdc++.h>
#include <omp.h>
using namespace std; using i128=__int128_t; using u128=__uint128_t;
const long long A=217976794617LL,L=137528045312LL;
const uint64_t MOD17=129140163ULL; static i128 GAP; static int CI[347];
int v2i(i128 x){ if(x<0)x=-x; u128 u=(u128)x; uint64_t lo=(uint64_t)u; if(lo)return __builtin_ctzll(lo); uint64_t hi=(uint64_t)(u>>64); return hi?64+__builtin_ctzll(hi):200; }
struct Rec{ long long Q; uint64_t eta; int lo,hi,b1,b2; };
struct Node{ int i,h,m; uint32_t r; i128 ac,bc; };
struct Live{ int h,m; uint32_t r; i128 ac,bc; };
struct Stats{
  unsigned long long scanned=0,h51=0,h200=0,resfail=0; long long pref=0,deleted=0,remainpref=0,s011=0,s111=0,mult[4]={0},mod18[18]={0},eta7[2187]={0};
  int maxfail=-1,maxcount=0,lastidx=-1,lastk=-1; long long lastQ=-1;
};
inline int continue_to200(i128 &y,int &h){
  for(int i=52;i<=200;i++){ int a=v2i(3*y+1); if(a>CI[i]+h) return i; h=CI[i]+h-a; y=(3*y+1)/((i128)1<<a); }
  return -1;
}
inline int continue_fail(i128 y,int h){
  for(int i=201;i<=346;i++){ int a=v2i(3*y+1); if(a>CI[i]+h) return i; h=CI[i]+h-a; y=(3*y+1)/((i128)1<<a); }
  return -1;
}
int main(int argc,char**argv){
  if(argc!=2){ cerr<<"usage: verify RECORDS.tsv\n"; return 2; }
  GAP=1; for(int i=0;i<16;i++)GAP*=3; GAP*=((i128)1<<13);
  for(int i=16;i<=346;i++) CI[i]=(int)(((i128)A*(i+1))/L-((i128)A*i)/L);
  ifstream f(argv[1]); if(!f){ cerr<<"cannot open records\n"; return 2; }
  vector<Rec> R; string line; getline(f,line); // header
  while(getline(f,line)){
    vector<string>a; size_t st=0; for(int j=0;j<5;j++){ auto p=line.find('\t',st); if(p==string::npos)return 2; a.push_back(line.substr(st,p-st)); st=p+1; } a.push_back(line.substr(st));
    int b1=INT_MIN,b2=INT_MIN; if(!a[5].empty()){ stringstream ss(a[5]); string z; if(getline(ss,z,',')) b1=stoi(z); if(getline(ss,z,',')) b2=stoi(z); }
    R.push_back({stoll(a[0]),stoull(a[1]),stoi(a[3]),stoi(a[4]),b1,b2});
  }
  if(R.size()!=45045){ cerr<<"record count mismatch "<<R.size()<<"\n"; return 1; }

  // Exact RL217 universal phase-51 automaton, retaining terminal affine states.
  vector<Node> stack; stack.reserve(16000000); stack.push_back({16,1,0,0,(i128)1<<34,-1-GAP});
  vector<Live> live; live.reserve(3200000); unsigned long long processed=0, failures=0;
  while(!stack.empty()){
    Node n=stack.back(); stack.pop_back(); processed++;
    if(n.i>51){ live.push_back({n.h,n.m,n.r,n.ac,n.bc}); continue; }
    int maxa=CI[n.i]+n.h; i128 nc=3*n.bc+1; int va=v2i(n.ac), vb=v2i(nc);
    if(min(va,vb)>maxa){ failures++; continue; }
    if(vb<va){ int a=vb; if(a>maxa){failures++;continue;} i128 den=(i128)1<<a; stack.push_back({n.i+1,CI[n.i]+n.h-a,n.m,n.r,3*n.ac/den,nc/den}); continue; }
    stack.push_back({n.i,n.h,n.m+1,(uint32_t)(n.r+(1u<<n.m)),2*n.ac,n.ac+n.bc});
    stack.push_back({n.i,n.h,n.m+1,n.r,2*n.ac,n.bc});
  }
  if(processed!=14514513ULL || failures!=1705547ULL || live.size()!=3132617ULL){ cerr<<"phase51 automaton mismatch "<<processed<<" "<<failures<<" "<<live.size()<<"\n"; return 1; }
  int maxm=0; for(auto&s:live)maxm=max(maxm,s.m); if(maxm!=25){cerr<<"maxm mismatch\n";return 1;}
  const uint32_t MASK=(1u<<25)-1; vector<int> lut(1u<<25,-1);
  unsigned long long lutfill=0;
  for(int si=0;si<(int)live.size();si++){
    auto&s=live[si]; uint32_t stride=1u<<s.m, reps=1u<<(25-s.m);
    for(uint32_t j=0;j<reps;j++){uint32_t rr=s.r+j*stride; if(lut[rr]!=-1){cerr<<"overlap\n";return 1;} lut[rr]=si; lutfill++;}
  }
  if(lutfill!=14110618ULL){ cerr<<"phase51 lut fill mismatch "<<lutfill<<"\n"; return 1; }
  cerr<<"phase51 built processed="<<processed<<" live="<<live.size()<<" lutfill="<<lutfill<<"\n";

  int nt=max(1,omp_get_max_threads()); vector<Stats> T(nt);
  #pragma omp parallel for schedule(dynamic,32) num_threads(nt)
  for(int j=0;j<(int)R.size();j++){
    int tid=omp_get_thread_num(); Stats &s=T[tid]; const Rec&r=R[j]; long long sv=0,par[2]={0,0}; s.pref++;
    for(int k=r.lo;k<=r.hi;k++){
      if(k==r.b1||k==r.b2) continue; s.scanned++;
      uint64_t x=r.eta+(uint64_t)MOD17*(uint64_t)k; int li=lut[(uint32_t)x&MASK]; if(li<0)continue; s.h51++;
      const Live &q=live[li]; i128 t=((i128)x-q.r)>>q.m; i128 y=q.ac*t+q.bc; int h=q.h;
      if(continue_to200(y,h)!=-1) continue;
      s.h200++; sv++; par[k&1]++; int later=continue_fail(y,h);
      if(later==-1){
        #pragma omp critical
        { cerr<<"survivor beyond 346 idx="<<(j+1)<<" Q="<<r.Q<<" k="<<k<<"\n"; }
        continue;
      }
      s.resfail++; if(later>s.maxfail){s.maxfail=later;s.maxcount=1;s.lastidx=j+1;s.lastQ=r.Q;s.lastk=k;} else if(later==s.maxfail)s.maxcount++;
    }
    if(sv==0)s.deleted++; else {s.remainpref++; if(sv<=3)s.mult[sv]++; if(r.eta%9==0)s.s011+=sv;else s.s111+=sv;}
    int m17=MOD17%18; s.mod18[r.eta%18]+=par[0]; s.mod18[(r.eta+m17)%18]+=par[1]; if(sv)s.eta7[r.eta%2187]+=sv;
  }
  Stats s; for(auto &t:T){
    s.scanned+=t.scanned;s.h51+=t.h51;s.h200+=t.h200;s.resfail+=t.resfail;s.pref+=t.pref;s.deleted+=t.deleted;s.remainpref+=t.remainpref;s.s011+=t.s011;s.s111+=t.s111;
    for(int i=0;i<4;i++)s.mult[i]+=t.mult[i];for(int i=0;i<18;i++)s.mod18[i]+=t.mod18[i];for(int i=0;i<2187;i++)s.eta7[i]+=t.eta7[i];
    if(t.maxfail>s.maxfail){s.maxfail=t.maxfail;s.maxcount=t.maxcount;s.lastidx=t.lastidx;s.lastQ=t.lastQ;s.lastk=t.lastk;} else if(t.maxfail==s.maxfail)s.maxcount+=t.maxcount;
  }
  if(s.pref!=45045 || s.scanned!=331927916ULL || s.h51!=139581280ULL){ cerr<<"coverage mismatch pref="<<s.pref<<" scanned="<<s.scanned<<" h51="<<s.h51<<"\n"; return 1; }
  if(s.h200!=4242 || s.remainpref!=4054 || s.deleted!=40991){ cerr<<"phase200 aggregate mismatch h200="<<s.h200<<" remain="<<s.remainpref<<" deleted="<<s.deleted<<"\n"; return 1; }
  if(s.mult[1]!=3873 || s.mult[2]!=174 || s.mult[3]!=7){ cerr<<"multiplicity mismatch\n"; return 1; }
  if(s.s011!=2782 || s.s111!=1460){ cerr<<"state mismatch\n"; return 1; }
  long long want[18]={0};want[0]=888;want[8]=473;want[9]=1894;want[17]=987;for(int i=0;i<18;i++)if(s.mod18[i]!=want[i]){cerr<<"mod18 mismatch "<<i<<" "<<s.mod18[i]<<"\n";return 1;}
  int nz=0,mn=INT_MAX,mx=0;for(int i=0;i<2187;i++)if(s.eta7[i]){nz++;mn=min(mn,(int)s.eta7[i]);mx=max(mx,(int)s.eta7[i]);} if(nz!=354||mn!=1||mx!=59){cerr<<"eta2187 mismatch\n";return 1;}
  if(s.resfail!=4242 || s.maxfail!=346 || s.maxcount!=1 || s.lastidx!=44955 || s.lastQ!=153134585 || s.lastk!=31480){cerr<<"residual mismatch max="<<s.maxfail<<" count="<<s.maxcount<<" idx="<<s.lastidx<<" Q="<<s.lastQ<<" k="<<s.lastk<<"\n";return 1;}
  cout<<"RL224 FULL E16 RECONSTRUCTIVE HEIGHT CERTIFICATE: PASS\n";
  cout<<"phase51_automaton processed=14514513 live_cylinders=3132617 max_precision=25\n";
  cout<<"coverage prefixes=45045 rl216_targeted_candidates=331927916 phase51_survivors=139581280\n";
  cout<<"phase200 survivors=4242 prefixes_remaining=4054 prefixes_deleted=40991\n";
  cout<<"phase200 state011=2782 state111=1460 eta_mod2187=354\n";
  cout<<"residual failed=4242 remaining=0 last_transition=346 last_idx=44955 last_Q=153134585 last_k=31480\n";
  cout<<"e16_final_candidates=0 e16_final_prefixes=0\n";
}
