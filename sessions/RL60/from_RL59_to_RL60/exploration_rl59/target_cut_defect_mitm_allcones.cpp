#include <boost/multiprecision/cpp_int.hpp>
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <chrono>
#include <limits>
#include <algorithm>
using boost::multiprecision::cpp_int;
static std::vector<cpp_int>P2{cpp_int(1)},P3{cpp_int(1)};
static inline void e2(int n){while((int)P2.size()<=n)P2.push_back(P2.back()*2);}
static inline void e3(int n){while((int)P3.size()<=n)P3.push_back(P3.back()*3);}
const int IT=73,PT=47,ZT=26,KMIN=25,MEET=55; const long long JT=3;
const cpp_int AA=cpp_int(27)*cpp_int(1000000000000000000LL)+2, AB=cpp_int(2)*cpp_int(1000000000000000000LL);
struct Pots{cpp_int nx,dx,np,dp;};
static Pots pots(int i,int p,int d,long long J){e2(std::max(i,d)+2);e3(p+d+2);cpp_int T=cpp_int(J)-P3[d]+P2[d];cpp_int dx=P3[p+d-1]*P2[d-1];cpp_int nx=P2[i]*((T-1)*P2[d-1]+P3[d-1]);cpp_int dp=2*dx;cpp_int np=P2[i]*(P3[d-1]*P2[d]+(T-1)*P2[d-1]+P3[d-1]);return{nx,dx,np,dp};}
static bool viableKPsiW(int i,int p,int d,long long J){if(d<1||p<0)return false;Pots q=pots(i,p,d,J);cpp_int diff=AA*q.dx-q.nx*AB;if(diff<=0)return false;cpp_int rhs=AA*q.dx;int K=KMIN;while((diff<<K)<=rhs)K+=2;cpp_int two=cpp_int(1)<<K;cpp_int pcn=AA*(two+1),pcd=cpp_int(2)*AB*two;if(q.np*pcd>=pcn*q.dp)return false;e2(i+1);e3(p+d+1);if(cpp_int(3)*AB*P2[i]*J>=AA*P3[p+d]||cpp_int(3)*P2[i]*J<cpp_int(-13)*P3[p+d])return false;return true;}
struct Step{bool ok;int d;long long J;int y;};
static Step step(int d,long long J,int x){e2(d+2);e3(d+2);int y;if(x==0)y=(J&1)?0:1;else{if(J&1)y=1;else if(d>1)y=0;else return{false,0,0,0};}cpp_int jj;int nd=d;if(!x&&!y)jj=(cpp_int(J)+P3[d]-P2[d])/2;else if(x&&y)jj=(cpp_int(3)*J+P2[d]-1)/2;else if(!x&&y){nd=d+1;jj=(cpp_int(3)*J+P3[d+1]-P2[d]-1)/2;}else{nd=d-1;jj=cpp_int(J)/2;}if(jj<std::numeric_limits<long long>::min()||jj>std::numeric_limits<long long>::max())return{false,0,0,0};return{true,nd,jj.convert_to<long long>(),y};}
struct Key{int p,d;long long J;bool operator==(Key const&o)const{return p==o.p&&d==o.d&&J==o.J;}};
struct KH{size_t operator()(Key const&k)const noexcept{uint64_t h=1469598103934665603ULL;auto m=[&](uint64_t x){h^=x;h*=1099511628211ULL;};m(k.p);m(k.d);m((uint64_t)k.J);return(size_t)h;}};
static bool lessK(Key const&a,Key const&b){if(a.p!=b.p)return a.p<b.p;if(a.d!=b.d)return a.d<b.d;return a.J<b.J;}
using Map=std::unordered_map<Key,cpp_int,KH>; using Set=std::unordered_set<Key,KH>;
static void relax(Map& nxt,Key const&k,cpp_int const&D){auto it=nxt.find(k);if(it==nxt.end())nxt.emplace(k,D);else if(D<it->second)it->second=D;}
static void back_add(Set&nxt,int ip,int p,int d,cpp_int const&Jbig,int x){if(p<0||d<1||Jbig<std::numeric_limits<long long>::min()||Jbig>std::numeric_limits<long long>::max())return;long long J=Jbig.convert_to<long long>();int z=ip-p;if(z<0||z>ZT||p>PT)return;int rem=IT-ip;if(p+rem<PT||z+rem<ZT)return;if(x==0){e2(ip+1);e3(p+1);if(cpp_int(30)*P2[ip]>cpp_int(17)*P3[p])return;}if(!viableKPsiW(ip,p,d,J))return;nxt.insert(Key{p,d,J});}
int main(){e2(IT+3);e3(IT+10);auto t0=std::chrono::steady_clock::now();std::vector<std::vector<Key>> cones(IT+1);Set curB,nxtB;curB.reserve(5000000);nxtB.reserve(5000000);curB.insert(Key{PT,1,JT});cones[IT]={{PT,1,JT}};
 for(int i=IT;i>MEET;i--){nxtB.clear();int ip=i-1;for(auto const&k:curB){int p=k.p,d=k.d;cpp_int Jp=k.J;cpp_int J00=2*Jp-P3[d]+P2[d];if((J00&1)!=0)back_add(nxtB,ip,p,d,J00,0);cpp_int num11=2*Jp-P2[d]+1;if(num11%3==0){cpp_int J11=num11/3;if((J11&1)!=0)back_add(nxtB,ip,p-1,d,J11,1);}if(d>=2){cpp_int num01=2*Jp-P3[d]+P2[d-1]+1;if(num01%3==0){cpp_int J01=num01/3;if((J01&1)==0)back_add(nxtB,ip,p,d-1,J01,0);}}back_add(nxtB,ip,p-1,d+1,2*Jp,1);}curB.swap(nxtB);auto &v=cones[ip];v.assign(curB.begin(),curB.end());std::sort(v.begin(),v.end(),lessK);std::cerr<<"back layer="<<ip<<" states="<<v.size()<<"\n";}
 Set().swap(curB);Set().swap(nxtB);
 Map cur,nxt;cur.reserve(3000000);nxt.reserve(3000000);cur.emplace(Key{0,1,-13},cpp_int(0));
 for(int i=0;i<IT;i++){nxt.clear();int remCols=IT-i;for(auto const&kv:cur){int p=kv.first.p,d=kv.first.d;long long J=kv.first.J;cpp_int const&Dnum=kv.second;int z=i-p;if(p>PT||z>ZT||p+remCols<PT||z+remCols<ZT)continue;cpp_int den=P3[p+d-1];int pending=d-1;if(cpp_int(45)*Dnum>=cpp_int(75+17*pending)*den)continue;if(!viableKPsiW(i,p,d,J))continue;
 if(z<ZT&&cpp_int(30)*P2[i]<=cpp_int(17)*P3[p]){auto s=step(d,J,0);if(s.ok){cpp_int nD=s.y==0?Dnum+P2[i]*(P3[d-1]-1):cpp_int(3)*Dnum+P2[i]*P3[d];relax(nxt,Key{p,s.d,s.J},nD);}}
 if(p<PT){auto s=step(d,J,1);if(s.ok){cpp_int nD=s.y==1?cpp_int(3)*Dnum:Dnum-P2[i];relax(nxt,Key{p+1,s.d,s.J},nD);}}
 }
 cur.swap(nxt);int layer=i+1;
 if(layer>=MEET){auto const&v=cones[layer];size_t before=cur.size();for(auto it=cur.begin();it!=cur.end();){if(!std::binary_search(v.begin(),v.end(),it->first,lessK))it=cur.erase(it);else ++it;}std::cerr<<"FILTER layer="<<layer<<" before="<<before<<" kept="<<cur.size()<<"\n";}
 if(layer%5==0||layer>=MEET){double sec=std::chrono::duration<double>(std::chrono::steady_clock::now()-t0).count();std::cerr<<"fwd layer="<<layer<<" states="<<cur.size()<<" sec="<<sec<<"\n";} if(layer==IT){ if(cur.size()!=1){std::cerr<<"unexpected final size\n"; std::_Exit(5);} auto const &D=cur.begin()->second; cpp_int den=P3[PT]; bool good=cpp_int(3)*D<cpp_int(5)*den; long double val=D.convert_to<long double>()/den.convert_to<long double>(); std::cerr<<"FINAL target minDnum="<<D<<" den="<<den<<" defect_lt_5_3="<<good<<" minDefectApprox="<<val<<"\n"; std::cerr.flush(); std::_Exit(good?2:0);} if(cur.empty())break;}
 Key tgt{PT,1,JT};auto it=cur.find(tgt);bool state=it!=cur.end(),good=false;if(state){cpp_int den=P3[PT];good=cpp_int(3)*it->second<cpp_int(5)*den;std::cout<<"target_state=1 minDnum="<<it->second<<" den="<<den<<" defect_lt_5_3="<<good<<"\n";long double val=it->second.convert_to<long double>()/den.convert_to<long double>();std::cout<<"minDefectApprox="<<val<<"\n";}else std::cout<<"target_state=0\n";double sec=std::chrono::duration<double>(std::chrono::steady_clock::now()-t0).count();std::cout<<"MITM_ALLCONES done final_states="<<cur.size()<<" sec="<<sec<<"\n";std::cout.flush(); std::cerr.flush(); std::_Exit(good?2:0);}
