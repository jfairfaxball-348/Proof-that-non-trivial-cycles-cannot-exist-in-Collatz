#include <boost/multiprecision/cpp_int.hpp>
#include <iostream>
#include <vector>
#include <unordered_set>
#include <chrono>
#include <limits>
#include <string>
#include <algorithm>
#include <cstdlib>
using boost::multiprecision::cpp_int;
static std::vector<cpp_int>P2{cpp_int(1)},P3{cpp_int(1)};
static inline void e2(int n){while((int)P2.size()<=n)P2.push_back(P2.back()*2);}
static inline void e3(int n){while((int)P3.size()<=n)P3.push_back(P3.back()*3);}
const int IT=73, PT=47, DT=1; const long long JT=3; const int KMIN=25;
const cpp_int AA=cpp_int(27)*cpp_int(1000000000000000000LL)+2;
const cpp_int AB=cpp_int(2)*cpp_int(1000000000000000000LL);
struct Pots{cpp_int nx,dx,np,dp;};
static Pots pots(int i,int p,int d,long long J){
 e2(std::max(i,d)+2); e3(p+d+2);
 cpp_int T=cpp_int(J)-P3[d]+P2[d];
 cpp_int dx=P3[p+d-1]*P2[d-1];
 cpp_int nx=P2[i]*((T-1)*P2[d-1]+P3[d-1]);
 cpp_int dp=2*dx;
 cpp_int np=P2[i]*(P3[d-1]*P2[d]+(T-1)*P2[d-1]+P3[d-1]);
 return {nx,dx,np,dp};
}
struct KSel{bool ok;int K;};
static KSel ksel(Pots const&q){
 cpp_int diff=AA*q.dx-q.nx*AB;
 if(diff<=0)return{false,0};
 cpp_int rhs=AA*q.dx; int K=KMIN;
 while((diff<<K)<=rhs)K+=2;
 cpp_int two=cpp_int(1)<<K;
 cpp_int pcn=AA*(two+1), pcd=cpp_int(2)*AB*two;
 if(q.np*pcd>=pcn*q.dp)return{false,0};
 return{true,K};
}
struct Step{bool ok;int d;long long J;int y;};
static Step step(int d,long long J,int x){
 e2(d+2);e3(d+2);int y;
 if(x==0)y=(J&1)?0:1;
 else { if(J&1)y=1; else if(d>1)y=0; else return{false,0,0,0}; }
 cpp_int jj; int nd=d;
 if(!x&&!y) jj=(cpp_int(J)+P3[d]-P2[d])/2;
 else if(x&&y) jj=(cpp_int(3)*J+P2[d]-1)/2;
 else if(!x&&y){nd=d+1;jj=(cpp_int(3)*J+P3[d+1]-P2[d]-1)/2;}
 else {nd=d-1;jj=cpp_int(J)/2;}
 if(jj<std::numeric_limits<long long>::min()||jj>std::numeric_limits<long long>::max()) return{false,0,0,0};
 return{true,nd,jj.convert_to<long long>(),y};
}
struct Key{int i,p,d;long long J;bool operator==(Key const&o)const{return i==o.i&&p==o.p&&d==o.d&&J==o.J;}};
struct KH{size_t operator()(Key const&k)const noexcept{uint64_t h=1469598103934665603ULL;auto m=[&](uint64_t x){h^=x;h*=1099511628211ULL;};m(k.i);m(k.p);m(k.d);m((uint64_t)k.J);return(size_t)h;}};
static std::unordered_set<Key,KH> dead;
static uint64_t nodes=0,prCount=0,prK=0,prW=0,prMemo=0,prCap=0,prIllegal=0;
static int maxK=0; static std::string path;
static bool rec(int i,int p,int d,long long J){
 ++nodes;
 int z=i-p;
 if(i>IT||p>PT||z>IT-PT){++prCount;return false;}
 if(p+(IT-i)<PT || z+(IT-i)<IT-PT){++prCount;return false;}
 if(i==IT){
   if(p==PT&&d==DT&&J==JT){std::cout<<"HIT path="<<path<<"\n";return true;}
   ++prCount;return false;
 }
 e2(i+2);e3(p+d+3);
 Pots q=pots(i,p,d,J); auto ks=ksel(q);
 if(!ks.ok){++prK;return false;} maxK=std::max(maxK,ks.K);
 // Inherited survivor W-strip condition, exactly as in the audited RL57 search.
 if(cpp_int(3)*AB*P2[i]*J>=AA*P3[p+d] || cpp_int(3)*P2[i]*J<cpp_int(-13)*P3[p+d]){++prW;return false;}
 Key k{i,p,d,J}; if(dead.find(k)!=dead.end()){++prMemo;return false;}
 // Try x=0 if another zero is needed. Sequential zero cap is strict; equality is arithmetically impossible here.
 if(z<IT-PT){
   if(cpp_int(30)*P2[i] <= cpp_int(17)*P3[p]){
     auto s=step(d,J,0);
     if(s.ok){path.push_back('0');if(rec(i+1,p,s.d,s.J))return true;path.pop_back();}
     else ++prIllegal;
   } else ++prCap;
 }
 // Try x=1 if another one is needed.
 if(p<PT){
   auto s=step(d,J,1);
   if(s.ok){path.push_back('1');if(rec(i+1,p+1,s.d,s.J))return true;path.pop_back();}
   else ++prIllegal;
 }
 dead.insert(k); return false;
}
int main(){
 dead.reserve(2000000);
 auto t=std::chrono::steady_clock::now(); bool h=rec(0,0,1,-13);
 double sec=std::chrono::duration<double>(std::chrono::steady_clock::now()-t).count();
 std::cout<<"TARGET (73,47,1,3) hit="<<h<<" nodes="<<nodes<<" sec="<<sec<<" dead="<<dead.size()
          <<" maxK="<<maxK<<" prCount="<<prCount<<" prK="<<prK<<" prW="<<prW<<" prCap="<<prCap<<" prIllegal="<<prIllegal<<" prMemo="<<prMemo<<"\n";
 return h?2:0;
}
