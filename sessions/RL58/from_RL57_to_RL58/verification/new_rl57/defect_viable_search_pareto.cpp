#include <boost/multiprecision/cpp_int.hpp>
#include <iostream>
#include <vector>
#include <chrono>
#include <limits>
#include <cstdlib>
#include <unordered_map>
#include <utility>
#include <algorithm>
using boost::multiprecision::cpp_int;
static std::vector<cpp_int>P2{cpp_int(1)},P3{cpp_int(1)};
static inline void e2(int n){while((int)P2.size()<=n)P2.push_back(P2.back()*2);} static inline void e3(int n){while((int)P3.size()<=n)P3.push_back(P3.back()*3);}
const int N=26,KMIN=25; long long TA=8,TB=1; const long long REQA=143,REQB=12;
const cpp_int AA=cpp_int(27)*cpp_int(1000000000000000000LL)+2, AB=cpp_int(2)*cpp_int(1000000000000000000LL);
struct Pots{cpp_int nx,dx,np,dp;};
Pots pots(int i,int p,int d,long long J){e2(std::max(i,d)+2);e3(p+d+2);cpp_int T=cpp_int(J)-P3[d]+P2[d];cpp_int dx=P3[p+d-1]*P2[d-1];cpp_int nx=P2[i]*((T-1)*P2[d-1]+P3[d-1]);cpp_int dp=2*dx;cpp_int np=P2[i]*(P3[d-1]*P2[d]+(T-1)*P2[d-1]+P3[d-1]);return{nx,dx,np,dp};}
struct KSel{bool ok;int K;cpp_int pcn,pcd;};
KSel ksel(Pots const&q){cpp_int diff=AA*q.dx-q.nx*AB;if(diff<=0)return{0,0,0,0};cpp_int rhs=AA*q.dx;int K=KMIN;while((diff<<K)<=rhs)K+=2;cpp_int two=cpp_int(1)<<K;cpp_int pcn=AA*(two+1),pcd=cpp_int(2)*AB*two;if(q.np*pcd>=pcn*q.dp)return{0,0,0,0};return{1,K,pcn,pcd};}
struct Step{bool ok;int d;long long J;int y;};
Step step(int d,long long J,int x){e2(d+2);e3(d+2);int y;if(x==0)y=(J&1)?0:1;else{if(J&1)y=1;else if(d>1)y=0;else return{0,0,0,0};}cpp_int jj;int nd=d;if(!x&&!y)jj=(cpp_int(J)+P3[d]-P2[d])/2;else if(x&&y)jj=(cpp_int(3)*J+P2[d]-1)/2;else if(!x&&y){nd=d+1;jj=(cpp_int(3)*J+P3[d+1]-P2[d]-1)/2;}else{nd=d-1;jj=cpp_int(J)/2;}if(jj<std::numeric_limits<long long>::min()||jj>std::numeric_limits<long long>::max()){std::cerr<<"J overflow\n";std::exit(3);}return{1,nd,jj.convert_to<long long>(),y};}

struct Key{int i,p,rem,d; long long J; bool operator==(Key const&o)const{return i==o.i&&p==o.p&&rem==o.rem&&d==o.d&&J==o.J;}};
struct KH{size_t operator()(Key const&k)const noexcept{uint64_t h=1469598103934665603ULL;auto m=[&](uint64_t x){h^=x;h*=1099511628211ULL;};m(k.i);m(k.p);m(k.rem);m(k.d);m((uint64_t)k.J);return(size_t)h;}};
struct Pareto{cpp_int Z,D;};
static std::unordered_map<Key,std::vector<Pareto>,KH> memo;
static uint64_t prMemo=0,paretoMax=0;

uint64_t nodes=0,prK=0,prW=0,prDef=0,prTot=0,prTarget=0;std::string path;
bool rec(int i,int p,int rem,cpp_int const&Z,cpp_int const&Y,int d,long long J){
 ++nodes;e2(i+rem+3);e3(p+d+3);
 // Defect lower bound. Current y-one count is p+d-1, so Zy=Y/3^(p+d-1).
 int pending=d-1;cpp_int denY=P3[p+d-1];cpp_int drawNum=Z*P3[d-1]-Y; // over denY
 if(cpp_int(45)*drawNum >= cpp_int(75+17*pending)*denY){++prDef;return false;}
 // Pareto dominance at identical dynamical state: larger Z and smaller raw defect D dominate.
 Key mk{i,p,rem,d,J}; auto &pv=memo[mk];
 for(auto const&a:pv) if(a.Z>=Z && a.D<=drawNum){++prMemo;return false;}
 pv.erase(std::remove_if(pv.begin(),pv.end(),[&](Pareto const&a){return a.Z<=Z && a.D>=drawNum;}),pv.end());
 pv.push_back({Z,drawNum}); if(pv.size()>paretoMax)paretoMax=pv.size();
 Pots q=pots(i,p,d,J);auto ks=ksel(q);if(!ks.ok){++prK;return false;}
 if(cpp_int(3)*AB*P2[i]*J>=AA*P3[p+d]||cpp_int(3)*P2[i]*J<cpp_int(-13)*P3[p+d]){++prW;return false;}
 cpp_int den=P3[p];
 cpp_int lhs=(Z*q.dp*ks.pcd+ks.pcn*den*q.dp-q.np*den*ks.pcd)*REQB;cpp_int rhs=cpp_int(REQA)*den*q.dp*ks.pcd;if(lhs<=rhs){++prTot;return false;}
 if(cpp_int(TB)*(cpp_int(30)*Z+cpp_int(17)*rem*den)<=cpp_int(TA)*30*den){++prTarget;return false;}
 if(cpp_int(TB)*(Z+(P2[rem]-1)*P2[i])<=cpp_int(TA)*den){++prTarget;return false;}
 cpp_int lhs2=(Z*q.dp*ks.pcd+ks.pcn*den*q.dp-q.np*den*ks.pcd)*TB;cpp_int rhs2=cpp_int(TA)*den*q.dp*ks.pcd;if(lhs2<=rhs2){++prTarget;return false;}
 if(rem==0){std::cout<<"HIT Z="<<Z.convert_to<long double>()/den.convert_to<long double>()<<" i="<<i<<" p="<<p<<" d="<<d<<" J="<<J<<" K="<<ks.K<<" path="<<path<<"\n";return true;}
 // x0
 if(cpp_int(30)*P2[i]<=cpp_int(17)*den){auto s=step(d,J,0);if(s.ok){cpp_int nZ=Z+P2[i];cpp_int nY=(s.y==0?Y+P2[i]:cpp_int(3)*Y);path.push_back('0');if(rec(i+1,p,rem-1,nZ,nY,s.d,s.J))return true;path.pop_back();}}
 auto s=step(d,J,1);if(s.ok){cpp_int nZ=cpp_int(3)*Z;cpp_int nY=(s.y==0?Y+P2[i]:cpp_int(3)*Y);path.push_back('1');if(rec(i+1,p+1,rem,nZ,nY,s.d,s.J))return true;path.pop_back();}
 return false;
}
int main(int argc,char**argv){memo.reserve(900000);if(argc>1){std::string s=argv[1];auto pos=s.find('/');if(pos==std::string::npos){TA=std::stoll(s);TB=1;}else{TA=std::stoll(s.substr(0,pos));TB=std::stoll(s.substr(pos+1));}}auto t=std::chrono::steady_clock::now();bool h=rec(0,0,N,cpp_int(0),cpp_int(0),1,-13);double sec=std::chrono::duration<double>(std::chrono::steady_clock::now()-t).count();std::cout<<"DEFECT_NOMEMO target="<<TA<<"/"<<TB<<" hit="<<h<<" nodes="<<nodes<<" sec="<<sec<<" prDef="<<prDef<<" prTot="<<prTot<<" prTarget="<<prTarget<<" prK="<<prK<<" prW="<<prW<<" prMemo="<<prMemo<<" memoKeys="<<memo.size()<<" paretoMax="<<paretoMax<<"\n";return h?2:0;}
