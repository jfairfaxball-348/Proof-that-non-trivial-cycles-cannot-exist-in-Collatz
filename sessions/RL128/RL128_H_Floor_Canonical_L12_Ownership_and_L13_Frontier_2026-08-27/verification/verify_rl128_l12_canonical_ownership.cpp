#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>
using u64=std::uint64_t; using u128=__uint128_t;
constexpr int L=12,MAX_Z=40; constexpr u64 THREE_L=531441;
static const u64 p3[]={1,3,9,27,81,243,729,2187,6561,19683,59049,177147,531441};
static void comps(int n,int parts,std::vector<int>&cur,std::vector<std::vector<int>>&out){if(parts==1){cur.push_back(n);out.push_back(cur);cur.pop_back();return;}for(int a=1;a<=n-parts+1;++a){cur.push_back(a);comps(n-a,parts-1,cur,out);cur.pop_back();}}
static u64 one_floor(const std::vector<int>&o){u64 out=0;for(int j=1;j<=L;++j){u64 c=0;for(int x:o)if(x>=j)c+=x-j+1;if(c)out=std::max(out,(c-1)*p3[j]);}return out;}
static bool primitive_pairs(const std::vector<int>&o,const std::vector<int>&z){int t=o.size();for(int d=1;d<t;++d)if(t%d==0){bool same=true;for(int i=d;i<t;++i)if(o[i]!=o[i%d]||z[i]!=z[i%d]){same=false;break;}if(same)return false;}return true;}
static int paircmp(const std::vector<int>&o,const std::vector<int>&z,int a,int b){if(o[a]<o[b])return-1;if(o[a]>o[b])return 1;if(z[a]<z[b])return-1;if(z[a]>z[b])return 1;return 0;}
static bool canonical_pairs(const std::vector<int>&o,const std::vector<int>&z){int n=o.size();if(n<=1)return true;int i=0,j=1,k=0;while(i<n&&j<n&&k<n){int c=paircmp(o,z,(i+k)%n,(j+k)%n);if(c==0){++k;continue;}if(c<0){j=j+k+1;if(j==i)++j;}else{i=i+k+1;if(i==j)++i;}k=0;}return std::min(i,j)==0;}
static bool dq_hit(const std::vector<int>&o,const std::vector<int>&z,u64 D){int seen=0;u64 r=0,pow2=1%D;for(size_t i=0;i<o.size();++i){for(int a=0;a<o[i];++a){u64 term=(u64)(((u128)pow2*p3[L-1-seen])%D);r+=term;if(r>=D)r-=D;++seen;pow2=(u64)(((u128)pow2*2)%D);}for(int a=0;a<z[i];++a)pow2=(u64)(((u128)pow2*2)%D);}return r==0;}
struct Odd{std::vector<int>o;std::array<uint16_t,L+1>mask{};};
struct Scan{int Z,t;u64 U,D;std::vector<Odd> odds;std::array<u64,MAX_Z+1>zw{},zcap{};std::array<int,MAX_Z+1>ncap{};std::array<uint16_t,MAX_Z+1>zmask{};std::vector<int>z;u64 P=0,Per=0,Can=0,W=0,Tests=0,Hits=0;
 Scan(int Z_,int t_,u64 U_,u64 D_):Z(Z_),t(t_),U(U_),D(D_){z.reserve(t);for(int k=1;k<=Z;++k){zcap[k]=(U-1)/(u64(1)<<k)+1;ncap[k]=(int)(U/(3*(u64(1)<<k)))+1;}std::vector<std::vector<int>>os;std::vector<int>cur;comps(L,t,cur,os);for(auto&o:os){if(one_floor(o)>U)continue;Odd c;c.o=o;bool ok=true;for(int j=1;j<=L;++j){uint16_t m=0;for(int i=0;i<t;++i)if(o[i]>=j)m|=(uint16_t(1)<<i);c.mask[j]=m;int cnt=__builtin_popcount((unsigned)m);u64 cap=U/(p3[j]*2)+1;if((u64)cnt>cap){ok=false;break;}}if(ok)odds.push_back(std::move(c));}}
 bool add(int i,int v){for(int k=1;k<=v;++k){zw[k]+=v-k+1;zmask[k]|=(uint16_t(1)<<i);}for(int k=1;k<=v;++k)if(zw[k]>zcap[k]||__builtin_popcount((unsigned)zmask[k])>ncap[k]){undo(i,v);return false;}return true;}
 void undo(int i,int v){for(int k=1;k<=v;++k){zw[k]-=v-k+1;zmask[k]&=~(uint16_t(1)<<i);}}
 bool crt_ok(const Odd&o)const{for(int j=2;j<=L;++j){if(!o.mask[j])break;for(int k=2;k<=Z;++k){if(!zmask[k])break;u64 cap=U/(p3[j]*(u64(1)<<k))+1;if((u64)__builtin_popcount((unsigned)(o.mask[j]&zmask[k]))>cap)return false;}}return true;}
 void leaf(){for(const Odd&oc:odds){if(!crt_ok(oc))continue;++P;if(!primitive_pairs(oc.o,z)){++Per;continue;}if(canonical_pairs(oc.o,z)){++Can;W+=t;++Tests;if(dq_hit(oc.o,z,D))++Hits;}}}
 void dfs(int i,int rem){if(i==t){if(rem==0)leaf();return;}int slots=t-i-1;for(int v=1;v<=rem-slots;++v)if(add(i,v)){z.push_back(v);dfs(i+1,rem-v);z.pop_back();undo(i,v);}}
};
int main(int argc,char**argv){int lo=8,hi=40;if(argc>1)lo=atoi(argv[1]);if(argc>2)hi=atoi(argv[2]);u64 TP=0,TPer=0,TCan=0,TW=0,TT=0,TH=0;for(int Z=lo;Z<=hi;++Z){u64 D=(u64(1)<<(L+Z))-THREE_L,B=((u64(1)<<Z)-1)*(THREE_L-(u64(1)<<L)),U=B/D;u64 P=0,Per=0,Can=0,W=0,Tests=0,Hits=0;for(int t=1;t<=std::min(L,Z);++t){if((u64)6*(t-1)>U)continue;u64 e0=0;for(int k=1;k<=Z;++k){long long c=(long long)Z-(long long)t*(k-1);if(c<=0)break;u64 v=(u64)(c-1)*(u64(1)<<k)+1;e0=std::max(e0,v);}if(e0>U)continue;Scan s(Z,t,U,D);if(s.odds.empty())continue;s.dfs(0,Z);P+=s.P;Per+=s.Per;Can+=s.Can;W+=s.W;Tests+=s.Tests;Hits+=s.Hits;}if(W!=P-Per){std::cerr<<"orbit mismatch Z="<<Z<<"\n";return 2;}std::cout<<"Z="<<Z<<" U="<<U<<" capacity_profiles="<<P<<" periodic="<<Per<<" canonical_primitive_profiles="<<Can<<" orbit_weight="<<W<<" canonical_roots_tested="<<Tests<<" divisibility_hits="<<Hits<<"\n";std::cout.flush();TP+=P;TPer+=Per;TCan+=Can;TW+=W;TT+=Tests;TH+=Hits;}std::cout<<"TOTAL range="<<lo<<".."<<hi<<" capacity_profiles="<<TP<<" periodic="<<TPer<<" canonical_primitive_profiles="<<TCan<<" orbit_weight="<<TW<<" canonical_roots_tested="<<TT<<" divisibility_hits="<<TH<<"\n";}
