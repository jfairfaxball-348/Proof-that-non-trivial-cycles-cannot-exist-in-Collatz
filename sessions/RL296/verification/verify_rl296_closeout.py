#!/usr/bin/env python3
"""RL296 self-contained portable closeout verifier."""
from fractions import Fraction
import ast,base64,zlib

DATA=ast.literal_eval(zlib.decompress(base64.b85decode('c-rk;+m0N!5&adt%`Pwxr~1Ms{iav~VnDD0Nrn>yh9B|;c{cR#=_+<NtBT#Tv!kAiV=e5_>`X6NWZh2{`N!eEG#q|-^T*-G_n*Fe=6CeNn*)tM;Qv6hywCqG|MRy{-%<W`e1&|Ke-6ht%{LB6(|Gfv^NTzV(o?mUOf?T!hUs?M0`&-%XQ8O=_um+^_dG|~V<}i3S0ky<rq^kJ{2k`?){M%O4Hr>1G0Xmpqs5CkPiFhnkZD&bC|_gZ+sazTSqXbc#WV?#d4bi<JRe;}LI5{6Dd|u<Uu3BW(V{Oj>yBqR)7@N=J({30Jk%DtiS(~Z-BI|hsL>;9-Yf*p^Ei5z`RBKblIeY~Hmbdz{ncAWZfsP<O!Rd7(xb!$FheLENBMiF7m8O<&rtcTFoFsf)U<1B>>qlKE8<(^XcDkRzO-*FYyA54_~!7RFtou&52N*Z>QX#jN#w?taeEI&yvGQmc^==4GsoCmXJ+VGv-ugP9iAn+d7{wcxSKVybIogPd5xngKeZIYm9|&KDHR!6tVa^!vjj*_q3L&KGg;=U#drO)giB9N7ttMW<FLx;I+(Mj9dJ{qwRw%RagcV3e$_c_rg7crSwgr`rP_#Z-)&8$SqRxZ!4l5db(1m&R8uWvk7V|&7=w`AgmZ;e1!FK%sz?DQT!XTIsMk+R;9!E%b+Rdq8_l8}S)WsgZ8$z=d@+0eCC(^JEWxExXb@~@Xap6cRS+unK*a;Cty>b1Wnfg%p?#JR`l(HA7j`kr8$s<tl@oI132mUSWqR?QFkG6{0c2=$=EAVn^HEJ$6yD?+WL-BvZW0|7tBi_D1g+ymQVE4sc4K2T_jRDXIR3)viOhxJ^3W>Jh3TVnh<MH!40FA0aeEbV3pFXY9^Q_nEs9a1VhNQg*BK3rz1MjSw1p}Wz1d&d-p$eLB~~HM&z`6sTBK%A2Y@9FEkQ2K{+Ow}&$OEcE$P}=s4>hR!<lLrXJj_tSTK|9=sz%6gK=BM)j}ouPUn_{O3$(3EfyAy9wM=WrY5tfNyGjT(S>n8Y}TUFL}U4_RvFuIYUu+DCOzlu@+rlZaNU^H7*!QtIdL@4!o~0=qI2T7sQ8>^udSX}J}P1CpL6=tw>?Sv^Xu>Le){zO$1hU`bjC)g$m2pBY{|q%O8)lom!IFg{q!%MUxbl%iIOLNFcvl?9~6h?Mj{RqIz#zo4;?`Z!~&yDX-eB6K5itZRZjz_I$l^}Em1hmf<hOsrEVV7fpdqF`c6p+HKFM)i|$Q6QBhoi7@=O0z$v3>x<vPuK*d#>V<PIN+@VWdjJrB&?X(EiD=K?tc38zIfQ@UNA1Gm<Lbj9>QT|+KT*8#m4vs5*`}2=~|M=;^a%t9`pJ6>by#MDvM(g<g-T2VIpPt4*vF})jx}4>5wkV%=Ex(O9fr#>H$MPm|(8%?caS-`9ur`37rhzdD{W&C$V?*67&ogk*vJqp?)iv3mO^?gxJaj)k)yU`Lcqs_H(~XK2XdXsBN8r!Lal-g~c>XOTVKGH<1*04I`03qeS?PgyKo%y6JP-d$(O9fJPk)dd6`~t-5*v<$^|!MGu6!^Nm8oJjbfN_m^A?{+l|vQm$a&~7HE%&txH>Mrr{gtiS_+C+07FIDLRvFQ1PggPit0Xy*hP7+b~k`41r(|k*=-i&ky9bu$D5EVm*`C=n|Q$??P^78Nz{v;f#HX{FUggFT_~yO&kGRSBIc5%DAMtkWjTv&ROL2JtlDm5d~#I%n65!?<p<&418c<zLvE&*^OHCPF`ENtFX*ooxwzb=cDzvF>f)bYSj4mnViVX7y+j+4JwX2_3~o*A0*iSm<7=4jaW|FrqExDukVRW@ytKE|=5i&ejcw?opjco(8~&^i)`Hv>y@F5tQGx9m67~7?%ynD6ep&zg{&qtzu}i~YeYhuV0E2=Wz*GTR1#2<oQm6k|6STFxm^Ncv{V=-V6ePBlFt@qGUMLtGR5dE-J@Xj4sc)fzrs%A_u#(YAagkcK&+Q}chA~0vQv;csBF%ZbF>MDY3e+VGSvol2r7k{xj0Owe?gJkiz{e>k8SvOg#1+b{dyJd}+e+_B&TY#=-rXC#v1}C1X1wEkNRml$hDm|;<NRvFUX7=lGKSts*ZxPYoK~Ku%D<xu>@?a8M^C|GO>c^+9auKl4l;s!(g6H*W~(h4oo~xmIM)eUF(iKJ|4%tbsJaMra$2+)<_VkOnj($KMaZ@P!4=dLdsW?M!|R;j+{8MrR#P7_i1$e?Lm1z!?OxVa*Ox0tY>K9+CN@2wC4H!3{}a65Vm*ZQfdP;dsgcBc;{B4#0@yGF8T9L$&~1QzorEwG#(4=Au?e!Zjno|bj5wW{!j^)QLDmHS6wE}rjj&@9588mt80Q#BTIU!jyix*So;6(bSeW20J(pG(O6~W|r;B0Tgsn2_6K5dqX3!>CrCoD-HAKbYN0J?PqmJ}xr!ogji=4I%#xKxXrUutka}H|Na#Y<983=mJTIOQiZ3EnrfqO%)yLMj$I`S?MXW<Mp4mZfb;X-TG6>~!97CX(sRHC7oC~idZTxn!6yHS#+_BF*8szuJl6CP8Xm6y6+>Y<D`59w-<B54O`yr~5kUjh*o*+|oF#^(4y&FU~M_8$21T@*xg0zA!SN-4ng?Npg+>Fzqe2~?MISLh(Z&fO+Af*`Bt4o>iNTail$V2i~Yz+fef1)3+ML9qD*4i6sJEbErJI_)PTxHfUM00ZDUu}U}&+nlP^eXWDrU{?j9wWsk+4Sy{**I1~6>opPrn;L4W4MYatW9k4yXL#od2sV{imAxfQXS8&0;P?_5Iibj^T$4g-M6$W-Al|V|W^iolqoM0Mr&V@JoJbrk4eV=E;vn{Tt5arhNZonmGu2Db4Cp7azqw3&DMJXZ0h^r1TaAviQmD2IX^>&Z*3lhci&GBGhzmj|Eu(0r^3R<R7J$yE8k?GHM3dq|JNmmt%&v*wbo{ES6zs83(&qZCA`O`gH6_W9(+<ry-)whREibuBe`@9Y2^USmJvu3HicCdk>;g^6Xc(^DJLIL_5~Znv7)Wjl8Xl`Ps0u6H8g#SA_```AA4|FF)>^~wzzmH7Sya<UgsM@<W&42Ba$Cs;ok;y?wGAe)a>VY2ZhMQpfbZ}iSHQ5MP=P?^Ks;XFhRGrEDaD9R0<$&;X9q_CULMP|7KLdn!f;EAQvnt_(pUk_;2KOTfS-Ju2~5S#dle_Pw(n=-D3!}wR<cxAzk|70WVJk3KzU4O(m#CsJhdDjq(__4p(qVt41mn%J80r-KIrh&GAJURKA&a1f_5x&I!}xRyUHb~OKS!z*YK#lBa4{P91=@^vMf2}Q+)d@*{RKPct7`UCx$n8vi7Rz6V|9uwG?TvU=rG^pWMPaExN@SbI1Ahn?2x8!fsKgYBthV&y<}_ojw`qEUKME;nGc<(fQCm5DetJ`(g*zJOt57(`J_h(c>s@=pSWa>$MZV3bTwR4pR&5ZCjM>L2Fva7HPvb_X4I4**`x{TX@|8VLMw0)wv$cvenCHs(q;1Tjh|AbQ@AL{B_z}fjS6+!(Lo0b+QeJ7H8JWeHY@j)A71@hSg<t$^k8>YPrUdcBpY|mXQ^%Q`cDpp-l@B?eRLd=&kfd6jp>VPv2Z^52{l^3mqk(k}HV>sBX_MLaq#0VwGN+{`pRY?xM53@Mr7SP7|A{Rh%TE#h82F+~V$`N)I>B|CD$xAN^~mPKrJ}Xb!e=>7QPTinrQ+YP1O5?a!0?Ll&md!n4k_(pR_A>26z`Sa~*NjM%lU9D@q^DA%Drf3hvIrmrT<!-V)4_s=LSM;}&E*B*kZ%PGiKZtR%_b0Zb({cd<UNHWKYVj~bnd<}&0t*s33Es9iKP_pfVts<EyCq=mvPHM}Pj(_Q^A}!4@_tv~FkThpkrgPccg-9K4+oS;3v!E)}@V8OI9ObEQ3)9zU!EY7$zJ8~CdOO{%YWCWsjW*J8*FL=c^8R;&Rne&~<+jPeCSzEfAyfaoTjIXm682)5f(;n-lIX;Rg63Sx5+PI;!xsW=|GxvtXJ=TTak3P`M=0>!THA8FW*VHFQm&T<Ho#m&q5*$`16{Dk{>_C^dYIR2OLam-ZZaT-BO0&<@6qpckBhw?<zyCCuNEVJytRa}0A9(#>X480A%Wv25<Y%s;Y-IoP*b5V$}24lhBOyJDQEO*7J431kaG|GI|C+7gYP`Nl!xx#QP^f1UC<@0G{T<G!-|c4>ZOvzS~!R`#pB$;;?kk&h`oIaW9s~!yWaJiAjI`b!?mHo9A;lXS5+geCPi5JE0tqxhqs^JfBxy+FK<6=#J2tfc)mes$mg(5$$?X5X&!DEe{JNl=xzD&;v?4z@l8=ppPqmF`t^VOvi#c')).decode())

def step(d,J,x):
    K=J+2**d-1
    if K%2==0:
        if x: d2,K2=d,3*K//2
        else: d2,K2=d,(K+3**d-1)//2
    else:
        if x:
            if d<=1:return None
            d2,K2=d-1,(K-1)//2
        else:d2,K2=d+1,3*(K+3**d)//2
    return d2,K2-2**d2+1,d-1

def replay(start,w):
    d,J=start; H=0
    for ch in w:
        o=step(d,J,int(ch)); assert o is not None,(start,w,d,J,ch)
        d,J,c=o; H+=c
    return (d,J),H

def Kof(d,J): return J+2**d-1

def prefix_complete(words):
    assert len(words)==len(set(words))
    for i,x in enumerate(words):
        for j,y in enumerate(words):
            if i!=j: assert not y.startswith(x),(x,y)
    assert sum(Fraction(1,2**len(w)) for w in words)==1

P=(2,3)

# 1. RL295 scratch frontier reconstructed.
owner={
(4,151):(16,'1111011011111101010000'),
(6,1881):(22,'1111011010111111011011110111011101111010011001011000000'),
(5,752):(20,'11110110101111110110111101110111011110100111000010000'),
(6,1728):(26,'11110110101111110110111101110111011110100111011011111100111110101000111011100111001101000101000000'),
(6,1455):(26,'111101101011111101101111011101110111101001110110111111001111000101010001101000000')}
for s,(c,w) in owner.items(): assert replay(P,w)==(s,c)
cuts=[
((5,191),8,[('0',(5,201),4,None),('100',(6,733),13,None),('1010',(6,949),18,None),('11',(4,151),8,owner[(4,151)]),('1011',(6,1881),18,owner[(6,1881)])]),
((5,201),12,[('0',(5,206),4,None),('10',(5,264),8,None),('110',(5,351),12,None),('111',(5,752),12,owner[(5,752)])]),
((6,733),21,[('0',(6,699),5,None),('10',(6,898),10,None),('11',(6,1728),10,owner[(6,1728)])]),
((6,949),26,[('0',(6,807),5,None),('1',(6,1455),5,owner[(6,1455)])])]
for start,allow,leaves in cuts:
    prefix_complete([r[0] for r in leaves])
    for w,t,sc,ow in leaves:
        assert replay(start,w)==(t,sc)
        if ow:
            oc,pw=ow; assert oc<=sc+allow
print('frontier=PASS')

# 2. Fifteen pre-Q17 side sectors, plus exact first-deviation partition.
S=(6,807); SP='1000000101000101'; ALLOW=31
d,J=S; H=0;sides=[];dev=[]
for i,ch in enumerate(SP):
    alt='1' if ch=='0' else '0'; o=step(d,J,int(alt));assert o
    sides.append(((o[0],o[1]),H+o[2]));dev.append(SP[:i]+alt)
    o=step(d,J,int(ch));assert o;d,J,c=o;H+=c
expected=[((6,736),5),((5,621),10),((6,1462),16),((7,3801),23),((8,10558),31),((9,30471),40),((10,89737),50),((12,530626),61),((11,401454),72),((13,1792803),84),((12,1501654),96),((13,3446175),109),((14,8752393),123),((16,45372670),138),((15,35839500),153),((17,150532452),169)]
assert sides==expected and (d,Kof(d,J),H)==(17,2*3**17,169)
assert sum(Fraction(1,2**len(w)) for w in dev)+Fraction(1,2**len(SP))==1
qcert=DATA['q17']['CERTS']
for idx in range(1,16):
    ep,oc=replay(P,qcert[idx]);target,sc=sides[idx]
    assert ep==target and oc<=sc+31
print('q17_side15=PASS')

# 3. Complete (6,736) cut.
S=(6,736);ALLOW=36;cert=DATA['c6736']['CERTS'];d,J=S;src=0
for n in range(14):
    o1=step(d,J,1);assert o1;target=(o1[0],o1[1]);sc=src+o1[2]
    bj,wp,wz,pc,lc=cert[n]
    assert replay(P,wp)==((1,bj),pc)
    assert replay((1,bj),wz)==(target,lc)
    assert pc+lc<=sc+ALLOW
    o0=step(d,J,0);assert o0;d,J,c=o0;src+=c
assert (d,Kof(d,J),src)==(11,3**11,116)
assert replay(P,'1'+'0'*9)==((d,J),46)
print('Bcal_6736_le_P_plus_36=PASS')
print('Bcal_6807_le_P_plus_31=PASS_using_inherited_RL295_Q17_tail')

# 4. (5,351).
D=DATA['c5351'];S=(5,351);ALLOW=24;d,J=S;src=0
for n in range(9):
    o1=step(d,J,1);assert o1;target=(o1[0],o1[1]);sc=src+o1[2]
    if n in D['W_DIRECT']: ep,oc=replay(P,D['W_DIRECT'][n]);assert ep==target
    else:
        bj,wp,z=D['BOUNDARY'][n];ep,pc=replay(P,wp);assert ep==(1,bj);ep2,lc=replay((1,bj),'0'*z);assert ep2==target;oc=pc+lc
    assert oc<=sc+ALLOW
    o0=step(d,J,0);assert o0;d,J,c=o0;src+=c
assert ((d,J),src)==((8,6312),47)
bj,wp,z=D['ANCHOR'];ep,pc=replay(P,wp);assert ep==(1,bj);ep2,lc=replay((1,bj),'0'*z);assert ep2==(d,J);assert pc+lc<=src+ALLOW
print('Bcal_5351_le_P_plus_24=PASS')

# 5. Generic complete prefix-record closures.
for label,S,allow,key in [('6898',(6,898),31,'c6898'),('5264',(5,264),20,'c5264')]:
    rec=DATA[key]['RECORDS'];prefix_complete([r[0] for r in rec])
    for pref,target,sc,oc,ow in rec:
        assert replay(S,pref)==(tuple(target),sc)
        assert replay(P,ow)==(tuple(target),oc)
        assert oc<=sc+allow
    print('Bcal_'+label+'_closure=PASS')

# 6. (5,206) exact three-wall reduction.
D=DATA['c5206'];S=(5,206);ALLOW=16
for pref,target,sc,oc,ow in D['CLOSED']:
    assert replay(S,pref)==(tuple(target),sc);assert replay(P,ow)==(tuple(target),oc);assert oc<=sc+ALLOW
for pref,target,sc,budget,oc,ow in D['LATE_CLOSED']:
    assert replay(S,pref)==(tuple(target),sc);assert replay(P,ow)==(tuple(target),oc);assert budget==sc+ALLOW and oc<=budget
for pref,target,sc,budget in D['RESIDUAL']:
    assert replay(S,pref)==(tuple(target),sc);assert budget==sc+ALLOW
# G6 sink and family
assert replay(S,'000')==((6,663),14)
assert replay(P,'00'*4)==((6,663),20)
for dd in range(2,20):
    G=(dd,3**dd-3-2**dd+1);e,c=replay(G,'00')
    assert e==(dd+1,3**(dd+1)-3-2**(dd+1)+1) and c==2*(dd-1)
anchor='11'+'0'*24
ep,sc=replay(S,anchor);assert ep==(15,3**15-2**15+1) and sc==257
assert replay(P,'1'+'0'*13)==(ep,92)
covered=[r[0] for r in D['CLOSED']]+[r[0] for r in D['LATE_CLOSED']]+['000',anchor]+[r[0] for r in D['RESIDUAL']]
prefix_complete(covered)
assert [tuple(r[1]) for r in D['RESIDUAL']]==[(13,2383314),(15,21490604),(15,21490598)]
print('Bcal_5206_three_wall_reduction=PASS')

print('RL296 portable closeout verifier: PASS')
print('final_B439_residual=P+2; B6699-24; B(13,2383314)-187; B(15,21490604)-243; B(15,21490598)-257')
print('Bcal_439_le_Bcal_P_plus_2=NOT_CLAIMED')
print('Bcal_P_le_1=NOT_CLAIMED')
print('gate_A=NOT_CLAIMED')
