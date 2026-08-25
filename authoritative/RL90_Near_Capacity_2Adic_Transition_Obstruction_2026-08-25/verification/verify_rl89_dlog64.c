#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <inttypes.h>
#include <omp.h>

#define MAXCANDS 128

typedef struct { int64_t m; uint64_t a; } cand_t;

static inline uint64_t inv_odd64(uint64_t a){
    uint64_t x=a;
    x = x*(2-a*x); x = x*(2-a*x); x = x*(2-a*x);
    x = x*(2-a*x); x = x*(2-a*x); x = x*(2-a*x);
    return x;
}

static int cmpcand(const void *pa, const void *pb){
    const cand_t *a=(const cand_t*)pa, *b=(const cand_t*)pb;
    if(a->m < b->m) return -1;
    if(a->m > b->m) return 1;
    if(a->a < b->a) return -1;
    if(a->a > b->a) return 1;
    return 0;
}

int main(void){
    const uint64_t AMAX=UINT64_C(42150931629); /* a=s+1, s<=C */
    const uint32_t LIM=(1u<<29);               /* |m| < 2^29 */
    uint64_t g[62]; g[0]=3;
    for(int j=1;j<=61;j++) g[j]=g[j-1]*g[j-1];

    cand_t cands[MAXCANDS];
    int nc=0, err=0;

    #pragma omp parallel for reduction(|:err) schedule(static)
    for(uint32_t mag=1; mag<LIM; mag+=2){
        for(int neg=0; neg<2; neg++){
            uint64_t m = neg ? (uint64_t)(-(int64_t)mag) : (uint64_t)mag;
            uint64_t r8 = m & 7u;
            /* inversion fixes each odd residue mod 8; powers of 3 are 1 or 3 mod 8 */
            if(r8!=1u && r8!=3u) continue;

            uint64_t u=inv_odd64(m); /* target 3^a = m^{-1} mod 2^64 */
            uint64_t a=(u&7u)==3u ? 1u : 0u;
            uint64_t p=a?3u:1u;
            int reject=0;

            for(int j=1;j<=61;j++){
                uint64_t lowmask = (j==61) ? UINT64_MAX : ((UINT64_C(1)<<(j+3))-1);
                if(((p^u)&lowmask)!=0){
                    a += (UINT64_C(1)<<j);
                    if(a>AMAX){ reject=1; break; }
                    p *= g[j];
                    if(((p^u)&lowmask)!=0){ err=1; reject=1; break; }
                }
            }

            if(!reject && p==u && a>=1){
                #pragma omp critical
                {
                    if(nc<MAXCANDS){
                        cands[nc].m = neg ? -(int64_t)mag : (int64_t)mag;
                        cands[nc].a = a;
                    }
                    nc++;
                }
            }
        }
    }

    if(err || nc>MAXCANDS){
        fprintf(stderr,"dlog scan internal error\n");
        return 2;
    }
    qsort(cands,nc,sizeof(cand_t),cmpcand);
    printf("RL89 dlog64 scan |m|<2^29, 1<=a<=42150931629\n");
    printf("candidate_count=%d\n",nc);
    for(int i=0;i<nc;i++)
        printf("candidate m=%" PRId64 " a=%" PRIu64 "\n",cands[i].m,cands[i].a);
    return 0;
}
