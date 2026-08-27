#include <cerrno>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <string>
#include <vector>

using u64 = std::uint64_t;
using u128 = __uint128_t;

// A deliberately small, self-contained nonnegative integer for the rare
// trajectory that exceeds uint64_t.  Limbs are base 2^32, little-endian.
class Big {
    std::vector<std::uint32_t> a;
    void normalize() { while (a.size() > 1 && a.back() == 0) a.pop_back(); }
public:
    Big(u64 x = 0) : a{static_cast<std::uint32_t>(x), static_cast<std::uint32_t>(x >> 32)} { normalize(); }
    bool is_one() const { return a.size() == 1 && a[0] == 1; }
    bool odd() const { return a[0] & 1U; }
    int compare_u64(u64 x) const {
        if (a.size() > 2) return 1;
        u64 y = a[0];
        if (a.size() == 2) y |= static_cast<u64>(a[1]) << 32;
        return y < x ? -1 : (y > x ? 1 : 0);
    }
    int compare(const Big &b) const {
        if (a.size() != b.a.size()) return a.size() < b.a.size() ? -1 : 1;
        for (std::size_t i = a.size(); i-- > 0;) {
            if (a[i] != b.a[i]) return a[i] < b.a[i] ? -1 : 1;
        }
        return 0;
    }
    void half() {
        std::uint32_t carry = 0;
        for (std::size_t i = a.size(); i-- > 0;) {
            std::uint32_t next = a[i] & 1U;
            a[i] = (a[i] >> 1) | (carry << 31);
            carry = next;
        }
        normalize();
    }
    void odd_step() {
        std::uint64_t carry = 1;
        for (auto &v : a) {
            std::uint64_t t = 3ULL * v + carry;
            v = static_cast<std::uint32_t>(t);
            carry = t >> 32;
        }
        if (carry) a.push_back(static_cast<std::uint32_t>(carry));
        half();
    }
    std::string decimal() const {
        Big t = *this;
        std::vector<std::uint32_t> groups;
        while (!(t.a.size() == 1 && t.a[0] == 0)) {
            std::uint64_t rem = 0;
            for (std::size_t i = t.a.size(); i-- > 0;) {
                std::uint64_t cur = (rem << 32) | t.a[i];
                t.a[i] = static_cast<std::uint32_t>(cur / 1000000000U);
                rem = cur % 1000000000U;
            }
            groups.push_back(static_cast<std::uint32_t>(rem));
            t.normalize();
        }
        std::string out = std::to_string(groups.back());
        for (std::size_t i = groups.size() - 1; i-- > 0;) {
            std::string g = std::to_string(groups[i]);
            out += std::string(9 - g.size(), '0') + g;
        }
        return out;
    }
};

static u64 parse(const char *s) {
    errno = 0;
    char *end = nullptr;
    unsigned long long n = std::strtoull(s, &end, 10);
    if (errno || !end || *end) {
        std::cerr << "invalid endpoint: " << s << "\n";
        std::exit(64);
    }
    return static_cast<u64>(n);
}

int main(int argc, char **argv) {
    if (argc != 3) {
        std::cerr << "usage: verify_rl131_chunk ODD_START ODD_END\n";
        return 64;
    }
    const u64 start = parse(argv[1]), end = parse(argv[2]);
    if (!(start & 1ULL) || !(end & 1ULL) || start > end) {
        std::cerr << "endpoints must be increasing odd integers\n";
        return 64;
    }
    u64 starts = 0, max_steps = 0, max_steps_start = start;
    u64 max_excursion = start, max_excursion_start = start;
    bool saw_big_excursion = false;
    Big big_max_excursion = 0;
    u64 big_max_excursion_start = start;
    // This program certifies a consecutive extension of an already certified
    // prefix ending at start-2.  If x<n, either it belongs to that prefix or
    // it was checked earlier in this increasing odd-start scan.
    for (u64 n = start; n <= end; n += 2) {
        ++starts;
        u64 x = n, steps = 0, local_max = x;
        while (x != 1) {
            if (x < n) break;
            if (x & 1ULL) {
                u128 y = ((u128)3 * x + 1) >> 1;
                if (y > std::numeric_limits<u64>::max()) {
                    // Preserve exactness rather than treating a 64-bit bound
                    // as a mathematical bound.  This rare branch continues
                    // the current trajectory using arbitrary precision.
                    Big bx = x;
                    bx.odd_step();
                    ++steps;
                    if (!saw_big_excursion || bx.compare(big_max_excursion) > 0) {
                        saw_big_excursion = true;
                        big_max_excursion = bx;
                        big_max_excursion_start = n;
                    }
                    while (!bx.is_one() && bx.compare_u64(n) >= 0) {
                        if (bx.odd()) bx.odd_step();
                        else bx.half();
                        ++steps;
                        if (bx.compare(big_max_excursion) > 0) {
                            big_max_excursion = bx;
                            big_max_excursion_start = n;
                        }
                    }
                    x = 1;  // The exact big-integer loop already reached x<n or 1.
                    break;
                }
                x = static_cast<u64>(y);
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
        if (n == end) break;
    }
    std::cout << "RL131 chunk descent verifier: PASS\n";
    std::cout << "odd_starts_checked=" << starts << " range=" << start << ".." << end << "\n";
    std::cout << "inductive_max_steps_before_lower=" << max_steps << " start=" << max_steps_start << "\n";
    if (saw_big_excursion) {
        std::cout << "max_excursion_before_lower=" << big_max_excursion.decimal()
                  << " start=" << big_max_excursion_start << "\n";
    } else {
        std::cout << "max_excursion_before_lower=" << max_excursion
                  << " start=" << max_excursion_start << "\n";
    }
}
