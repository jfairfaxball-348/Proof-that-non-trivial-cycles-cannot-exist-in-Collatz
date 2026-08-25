#include <gmp.h>
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    const unsigned long MOD_BITS = 500056UL;
    const unsigned long RMAX = 550000UL;
    const unsigned long TAIL_START = 500001UL;
    const unsigned long SSTAR = 26594276905UL;
    const unsigned long EXPECT_MIN_BITS = 500038UL;
    const unsigned long EXPECT_MIN_R = 298303UL;
    const unsigned long EXPECT_TAIL_BITS = 500041UL;
    const unsigned long EXPECT_TAIL_R = 519699UL;

    mpz_t mod, inv3, residue, alt, balanced;
    mpz_inits(mod, inv3, residue, alt, balanced, NULL);
    mpz_set_ui(mod, 1UL);
    mpz_mul_2exp(mod, mod, MOD_BITS);

    mpz_set_ui(inv3, 3UL);
    if (mpz_invert(inv3, inv3, mod) == 0) {
        fprintf(stderr, "3 unexpectedly noninvertible modulo 2^N\n");
        return 2;
    }

    /* r=0 corresponds to a=s+1=SSTAR+1. Increasing r by one
       reduces a by one, hence multiplies 3^{-a} by 3. */
    mpz_powm_ui(residue, inv3, SSTAR + 1UL, mod);

    unsigned long min_bits = ~0UL, min_r = 0UL;
    unsigned long tail_bits = ~0UL, tail_r = 0UL;

    for (unsigned long r = 0; r <= RMAX; ++r) {
        mpz_sub(alt, mod, residue);
        if (mpz_cmp(residue, alt) <= 0) mpz_set(balanced, residue);
        else mpz_set(balanced, alt);

        unsigned long bits = mpz_sizeinbase(balanced, 2);
        if (bits < min_bits) { min_bits = bits; min_r = r; }
        if (r >= TAIL_START && bits < tail_bits) {
            tail_bits = bits; tail_r = r;
        }

        if (r < RMAX) {
            mpz_mul_ui(residue, residue, 3UL);
            mpz_fdiv_r_2exp(residue, residue, MOD_BITS);
        }
    }

    printf("RL90 band550k 2-adic scan\n");
    printf("modulus_bits=%lu\n", MOD_BITS);
    printf("r_range=0..%lu\n", RMAX);
    printf("global_min_balanced_bitlen=%lu at_r=%lu\n", min_bits, min_r);
    printf("tail_min_balanced_bitlen=%lu at_r=%lu tail_start=%lu\n",
           tail_bits, tail_r, TAIL_START);

    if (min_bits != EXPECT_MIN_BITS || min_r != EXPECT_MIN_R ||
        tail_bits != EXPECT_TAIL_BITS || tail_r != EXPECT_TAIL_R) {
        fprintf(stderr, "unexpected scan result\n");
        return 1;
    }
    if (min_bits < 500038UL) {
        fprintf(stderr, "cofactor covering threshold failed\n");
        return 1;
    }

    printf("certificate: every balanced inverse residue has |mu_r| >= 2^500037\n");
    printf("RL90 band550k 2-adic scan: PASS\n");

    mpz_clears(mod, inv3, residue, alt, balanced, NULL);
    return 0;
}
