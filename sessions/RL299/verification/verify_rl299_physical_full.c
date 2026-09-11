#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <inttypes.h>
#include <string.h>

typedef __uint128_t u128;

typedef struct {
    uint64_t steps;
    u128 peak;
} Stat;

static void print_u128(u128 x) {
    char b[64]; int i=0;
    if (!x) { putchar('0'); return; }
    while (x) { b[i++]='0'+(x%10); x/=10; }
    while (i--) putchar(b[i]);
}

static Stat stop_stat(u128 n) {
    Stat s={0,n};
    while (n!=1) {
        if (n&1) n=(3*n+1)/2;
        else n/=2;
        s.steps++;
        if (n>s.peak) s.peak=n;
        if (s.steps>10000000ULL) {
            fprintf(stderr,"step guard exceeded\n"); exit(2);
        }
    }
    return s;
}

static void single(uint64_t h) {
    u128 A=(u128)27*h+22, B=(u128)81*h+80;
    Stat sa=stop_stat(A), sb=stop_stat(B);
    printf("h=%" PRIu64 " A_steps=%" PRIu64 " A_peak=",h,sa.steps); print_u128(sa.peak);
    printf(" B_steps=%" PRIu64 " B_peak=",sb.steps); print_u128(sb.peak); putchar('\n');
}

int main(int argc,char **argv) {
    if (argc==3 && strcmp(argv[1],"--single")==0) {
        single(strtoull(argv[2],0,10)); return 0;
    }
    if (argc!=3) {
        fprintf(stderr,"usage: %s START_H END_H   # half-open h range\n       %s --single H\n",argv[0],argv[0]);
        return 2;
    }
    uint64_t lo=strtoull(argv[1],0,10), hi=strtoull(argv[2],0,10);
    uint64_t maxs=0,maxh=0; char side='?'; u128 maxpeak=0;
    for (uint64_t h=lo; h<hi; ++h) {
        u128 A=(u128)27*h+22, B=(u128)81*h+80;
        Stat sa=stop_stat(A), sb=stop_stat(B);
        if (sa.steps>maxs) { maxs=sa.steps; maxh=h; side='A'; }
        if (sb.steps>maxs) { maxs=sb.steps; maxh=h; side='B'; }
        if (sa.peak>maxpeak) maxpeak=sa.peak;
        if (sb.peak>maxpeak) maxpeak=sb.peak;
    }
    printf("range=[%" PRIu64 ",%" PRIu64 ") max_steps=%" PRIu64 " h=%" PRIu64 " side=%c max_peak=",lo,hi,maxs,maxh,side);
    print_u128(maxpeak); putchar('\n');
    return 0;
}
