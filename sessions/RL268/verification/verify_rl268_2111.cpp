#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <sstream>
#include <string>
#include <tuple>
#include <vector>
using boost::multiprecision::cpp_int;

struct Pair { int A,L,m,q; };
struct Ev { int k, delta; };
struct Seg { int a,b,level; };

static int egcd_inv(int a,int mod){
    long long t=0,newt=1,r=mod,newr=a;
    while(newr){ long long q=r/newr; auto nt=t-q*newt; t=newt; newt=nt; auto nr=r-q*newr; r=newr; newr=nr; }
    if(r!=1) return -1; t%=mod; if(t<0)t+=mod; return (int)t;
}
static cpp_int pow_small(int base,int exp){ cpp_int r=1,b=base; while(exp){ if(exp&1)r*=b; b*=b; exp>>=1;} return r; }

int main(int argc,char**argv){
    std::string path = argc>1?argv[1]:"rl268_2111_pairs.csv";
    std::ifstream f(path); std::string line; std::getline(f,line);
    std::vector<Pair> pairs;
    while(std::getline(f,line)){
        if(line.empty()) continue; std::replace(line.begin(),line.end(),',',' '); std::istringstream ss(line); Pair p; ss>>p.A>>p.L>>p.m>>p.q; pairs.push_back(p);
    }
    const int lens[4][4]={{2,1,1,1},{2,1,1,1},{2,1,1,1},{2,1,1,1}};
    const int signs[4][4]={{+1,+1,-1,-1},{+1,-1,+1,-1},{+1,-1,-1,+1},{-1,+1,+1,+1}};
    unsigned long long gap_total=0, structural=0, hits=0;
    unsigned long long order_gaps[4]={0}, order_struct[4]={0}, order_hits[4]={0};
    int max_struct_A=0;
    std::vector<std::tuple<int,int,int,int,int,std::array<int,4>>> hitrows;

    for(const auto&p:pairs){
        int A=p.A,L=p.L,m=p.m,q=p.q;
        if(A<9) continue;
        int inv=egcd_inv(m,A); if(inv<0){ std::cerr<<"bad inv\n"; return 2; }
        cpp_int D=(cpp_int(1)<<A)-pow_small(3,L); if(D<=1){std::cerr<<"bad D\n";return 3;}
        if(q*A-m*L!=1){std::cerr<<"bad determinant\n";return 4;}
        std::vector<unsigned short> C((A+1)*(A+1),0);
        for(int j=0;j<A;j++){
            auto prev=&C[j*(A+1)], cur=&C[(j+1)*(A+1)];
            std::copy(prev,prev+A+1,cur);
            int t=(int)((1LL*j*inv)%A);
            for(int k=t+1;k<=A;k++) cur[k]++;
        }
        std::vector<cpp_int> p2(A+1),p3(L+1); p2[0]=1%D; for(int i=1;i<=A;i++)p2[i]=(p2[i-1]*2)%D; p3[0]=1%D; for(int j=1;j<=L;j++)p3[j]=(p3[j-1]*3)%D;
        int Z=A-5;
        for(int ord=0;ord<4;ord++){
          for(int g0=1;g0<=Z-3;g0++) for(int g1=1;g1<=Z-g0-2;g1++) for(int g2=1;g2<=Z-g0-g1-1;g2++){
            int g3=Z-g0-g1-g2; if(g3<1) continue;
            std::array<int,4> gaps={g0,g1,g2,g3};
            gap_total++; order_gaps[ord]++;
            std::array<Ev,8> ev; std::array<int,5> edge_i; std::array<int,5> edge_s; int ec=0,zc=0,pos=0;
            for(int c=0;c<4;c++){
                int s=signs[ord][c], ln=lens[ord][c];
                int start=pos;
                ev[ec++]={int((1LL*start*inv)%A),-s};
                for(int t=0;t<ln;t++){edge_i[zc]=start+t; edge_s[zc]=s; zc++;}
                int endzero=start+ln;
                ev[ec++]={int((1LL*endzero*inv)%A),+s};
                pos += ln+gaps[c];
            }
            if(pos!=A||ec!=8||zc!=5){std::cerr<<"construction\n";return 5;}
            std::sort(ev.begin(),ev.end(),[](const Ev&a,const Ev&b){return a.k<b.k;});
            int level=0,cur=0,mn=0,mx=0; std::vector<Seg> segs; segs.reserve(9);
            for(auto&e:ev){
                if(e.k+1>cur){ segs.push_back({cur,e.k+1,level}); mn=std::min(mn,level); mx=std::max(mx,level); }
                level += e.delta; cur=e.k+1;
            }
            if(cur<A){segs.push_back({cur,A,level});mn=std::min(mn,level);mx=std::max(mx,level);}
            if(level!=0){std::cerr<<"nonzero closure\n";return 6;}
            if(mx-mn>1) continue;
            std::array<int,2> offsets={-mn,1-mx}; int prevc=999;
            for(int off:offsets){
                if(off==prevc) continue; prevc=off;
                bool ok=true; int Lx=0; std::vector<std::pair<int,int>> ones;
                for(auto&s:segs){ int bit=s.level+off; if(bit<0||bit>1){ok=false;break;} if(bit){Lx+=s.b-s.a; if(!ones.empty()&&ones.back().second==s.a)ones.back().second=s.b; else ones.push_back({s.a,s.b});} }
                if(!ok||Lx!=L) continue;
                structural++; order_struct[ord]++; max_struct_A=std::max(max_struct_A,A);
                auto prefixR=[&](int i){
                    int pfx=i+1, ans=0; auto row=&C[pfx*(A+1)];
                    for(auto ab:ones) ans += int(row[ab.second])-int(row[ab.first]);
                    return ans;
                };
                cpp_int rem=0;
                for(int z=0;z<5;z++){
                    int i=edge_i[z], sgn=edge_s[z], R=prefixR(i);
                    int b = (sgn==1)?(L-R):(L-R-1);
                    if(b<0||b>L){std::cerr<<"bad exponent A="<<A<<"\n";return 7;}
                    cpp_int term=(p2[i]*p3[b])%D;
                    if(sgn==1) rem += term; else rem -= term;
                }
                rem%=D; if(rem<0)rem+=D;
                if(rem==0){ hits++;order_hits[ord]++; hitrows.push_back({A,L,m,q,ord,gaps}); }
            }
          }
        }
    }
    std::cout<<"pairs="<<pairs.size()<<"\n";
    std::cout<<"gap_configurations="<<gap_total<<"\n";
    std::cout<<"structural_candidates="<<structural<<"\n";
    std::cout<<"max_structural_A="<<max_struct_A<<"\n";
    std::cout<<"full_D_hits="<<hits<<"\n";
    for(int o=0;o<4;o++) std::cout<<"order"<<o<<": gaps="<<order_gaps[o]<<" structural="<<order_struct[o]<<" hits="<<order_hits[o]<<"\n";
    for(auto &r:hitrows){auto[A,L,m,q,o,g]=r; std::cout<<"HIT "<<A<<","<<L<<","<<m<<","<<q<<" order="<<o<<" gaps="<<g[0]<<","<<g[1]<<","<<g[2]<<","<<g[3]<<"\n";}
}
