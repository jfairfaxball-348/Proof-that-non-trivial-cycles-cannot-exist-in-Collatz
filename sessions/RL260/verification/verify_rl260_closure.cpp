#include <bits/stdc++.h>
using namespace std;
struct Case {int sd; long long sJ; int budget; int ed; long long eJ;};
struct PairHash { size_t operator()(const pair<int,long long>&p) const noexcept {return std::hash<long long>()((p.second<<4) ^ p.first);} };

bool step_x(int d,long long J,int x,int &d2,long long &J2){
    __int128 val;
    auto p3=[&](int e)->__int128{__int128 v=1; for(int i=0;i<e;i++) v*=3; return v;};
    auto p2=[&](int e)->__int128{return ((__int128)1)<<e;};
    if (J & 1LL){
        d2=d;
        if(x==0) val=((__int128)J+p3(d)-p2(d))/2;
        else val=(3*(__int128)J+p2(d)-1)/2;
    } else {
        if(x==0){ d2=d+1; val=(3*(__int128)J+p3(d+1)-p2(d)-1)/2; }
        else { if(d<=1) return false; d2=d-1; val=J/2; }
    }
    if(val>LLONG_MAX || val<LLONG_MIN){ cerr<<"overflow\n"; exit(3);} J2=(long long)val; return true;
}

int main(int argc,char**argv){
    int LO=1,HI=1000000; if(argc>=2) LO=atoi(argv[1]); if(argc>=3) HI=atoi(argv[2]);
    ifstream in(".rl260_low_cases.tsv"); string hdr; getline(in,hdr);
    vector<Case> cs; Case c; while(in>>c.sd>>c.sJ>>c.budget>>c.ed>>c.eJ) cs.push_back(c);
    map<pair<int,long long>, vector<int>> groups; for(int i=0;i<(int)cs.size();i++) groups[{cs[i].sd,cs[i].sJ}].push_back(i);
    cerr<<"cases="<<cs.size()<<" starts="<<groups.size()<<"\n";
    long long totalStates=0,maxAbs=0; int gi=0; int hits=0;
    for(auto &gg:groups){
        gi++; if(gi<LO || gi>HI) continue; auto start=gg.first; int B=0; for(int ix:gg.second) B=max(B,cs[ix].budget);
        vector<unordered_map<long long,unsigned char>> best(40);
        vector<vector<pair<int,long long>>> buckets(B+1);
        best[start.first][start.second]=0; buckets[0].push_back(start);
        long long states=1;
        for(int cost=0;cost<=B;cost++){
            size_t pos=0;
            while(pos<buckets[cost].size()){
                auto [d,J]=buckets[cost][pos++];
                auto it=best[d].find(J); if(it==best[d].end() || it->second!=cost) continue;
                maxAbs=max(maxAbs,llabs(J));
                int edge=d-1; if(cost+edge>B) continue;
                for(int x=0;x<=1;x++){
                    int d2; long long J2; if(!step_x(d,J,x,d2,J2)) continue;
                    if(d2>=40){cerr<<"d overflow"; return 4;}
                    int nc=cost+edge;
                    auto jt=best[d2].find(J2);
                    if(jt==best[d2].end() || nc<jt->second){
                        if(jt==best[d2].end()) states++;
                        best[d2][J2]=(unsigned char)nc; buckets[nc].push_back({d2,J2});
                    }
                }
            }
        }
        totalStates += states;
        int gh=0;
        for(int ix:gg.second){ auto &q=cs[ix]; auto it=best[q.ed].find(q.eJ); if(it!=best[q.ed].end() && it->second<=q.budget){ gh++; hits++; } }
        cerr<<"start "<<gi<<"/"<<groups.size()<<" ("<<start.first<<","<<start.second<<") B="<<B<<" states="<<states<<" hits="<<gh<<"\n";
        if(gh){cerr<<"FOUND HIT -> fail\n"; return 2;}
    }
    cout<<"PASS RL260 k31 unrestricted minimum-area closure\n";
    cout<<"cases="<<cs.size()<<" starts="<<groups.size()<<" hits="<<hits<<" totalStates="<<totalStates<<" maxAbsJ="<<maxAbs<<"\n";
}
