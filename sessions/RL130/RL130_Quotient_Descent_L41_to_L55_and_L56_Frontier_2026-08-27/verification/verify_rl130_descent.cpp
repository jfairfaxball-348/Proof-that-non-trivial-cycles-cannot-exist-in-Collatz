#include <cstdint>
#include <iostream>
#include <limits>

using u64 = std::uint64_t;
using u128 = __uint128_t;

static constexpr u64 LIMIT = 6496657853ULL;

int main() {
    u64 starts = 0;
    u64 max_steps = 0, max_steps_start = 1;
    u64 max_excursion = 1, max_excursion_start = 1;
    for (u64 n = 1; n <= LIMIT; n += 2) {
        ++starts;
        u64 x = n, steps = 0, local_max = x;
        while (x != 1) {
            if (x < n) break;
            if (x & 1ULL) {
                u128 y = ((u128)3 * x + 1) >> 1;
                if (y > std::numeric_limits<u64>::max()) {
                    std::cerr << "overflow from start=" << n << "\n";
                    return 2;
                }
                x = (u64)y;
            } else {
                x >>= 1;
            }
            ++steps;
            if (x > local_max) local_max = x;
        }
        if (x == 0) {
            std::cerr << "zero reached from start=" << n << "\n";
            return 3;
        }
        if (steps > max_steps) { max_steps = steps; max_steps_start = n; }
        if (local_max > max_excursion) { max_excursion = local_max; max_excursion_start = n; }
    }
    std::cout << "RL130 quotient descent verifier: PASS\n";
    std::cout << "odd_starts_checked=" << starts << " range=1.." << LIMIT << "\n";
    std::cout << "inductive_max_steps_before_lower=" << max_steps << " start=" << max_steps_start << "\n";
    std::cout << "max_excursion_before_lower=" << max_excursion << " start=" << max_excursion_start << "\n";
}
