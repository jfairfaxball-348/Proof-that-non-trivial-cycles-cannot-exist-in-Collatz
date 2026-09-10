#include <bits/stdc++.h>
using namespace std;
struct Key{uint64_t J;uint8_t d;bool operator==(Key const&o)const{return J==o.J&&d==o.d;}};
struct Hsh{size_t operator()(Key const&k)const noexcept{return std::hash<uint64_t>{}(k.J^(uint64_t(k.d)*0x9e3779b97f4a7c15ULL));}};
int main(){
 const int R=27;const uint64_t TARGET=1ULL<<29;unordered_map<Key,uint8_t,Hsh> dist;dist.reserve(30000000);dist.max_load_factor(0.72);vector<vector<Key>> b(R+1);
 auto add=[&](int d,uint64_t J,int H){Key k{J,(uint8_t)d};auto it=dist.find(k);if(it==dist.end()){dist.emplace(k,(uint8_t)H);b[H].push_back(k);}else if(H<it->second){it->second=(uint8_t)H;b[H].push_back(k);}};
 add(2,3,0);bool overflow=false;size_t processed=0;map<int,int> powers;
 for(int H=0;H<=R;H++)for(size_t idx=0;idx<b[H].size();idx++){
   Key k=b[H][idx];auto it=dist.find(k);if(it==dist.end()||it->second!=H)continue;processed++;int d=k.d;uint64_t J=k.J;
   if(d==1&&(J&(J-1))==0){int kk=63-__builtin_clzll(J);if(!powers.count(kk)||H<powers[kk])powers[kk]=H;}
   __int128 p2=(__int128)1<<d,p3=1;for(int i=0;i<d;i++)p3*=3;__int128 K=(__int128)J+p2-1;
   for(int x=0;x<2;x++){int d2;__int128 K2;if((K&1)==0){d2=d;K2=x?3*K/2:(K+p3-1)/2;}else{if(x){if(d<=1)continue;d2=d-1;K2=(K-1)/2;}else{d2=d+1;K2=3*(K+p3)/2;}}
     int H2=H+d-1;if(H2>R)continue;__int128 p22=(__int128)1<<d2,J2=K2-p22+1;if(J2<=0)return 2;if(J2>numeric_limits<uint64_t>::max()){overflow=true;continue;}add(d2,(uint64_t)J2,H2);
   }
 }
 size_t cp23=0,cp26=0,cp27=0;for(auto const&kv:dist){auto k=kv.first;int H=kv.second;if(k.d==1&&k.J%2==0){if(H<=23)cp23++;if(H<=26)cp26++;if(H<=27)cp27++;}}
 map<int,int> expected{{1,2},{3,2},{5,8},{7,14},{9,14},{11,17},{13,17},{15,21},{17,24},{19,25},{21,23}};
 if(powers!=expected||dist.size()!=23652724ULL||processed!=dist.size()||cp23!=320762ULL||cp26!=2865881ULL||cp27!=5962876ULL||overflow)return 3;
 Key tar{TARGET,1};if(dist.count(tar))return 4;
 cout<<"RL293 P-source k29 exact closure: PASS\n";
 cout<<"added_cost_cap="<<R<<"\n";
 cout<<"positive_physical_states="<<dist.size()<<"\n";
 cout<<"processed_min_states="<<processed<<"\n";
 cout<<"positive_even_checkpoints_A23="<<cp23<<"\n";
 cout<<"positive_even_checkpoints_A26="<<cp26<<"\n";
 cout<<"positive_even_checkpoints_A27="<<cp27<<"\n";
 cout<<"power_minima=";bool f=true;for(auto [k,h]:powers){if(!f)cout<<",";f=false;cout<<"k"<<k<<":A"<<h;}cout<<"\n";
 cout<<"k29_checkpoint_under_A27=ABSENT\n";
 cout<<"classification_candidate=P_SOURCE_A27_K29_EXCLUSION\n";
}
