#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <set>
#include <string>
#include <vector>

using U = unsigned __int128;
constexpr uint64_t E = 137528045312ULL;
constexpr uint64_t D = 80448749305ULL;
constexpr U LOW = U(1) << 71;
constexpr U UP = (U(1) << 76) + (U(1) << 36);
constexpr U MIN_OWNED = U(2268974744269304020ULL) * 10000 + 8618;

std::string out(U x) {
    if (!x) return "0";
    std::string s;
    while (x) { s.push_back(char('0' + x % 10)); x /= 10; }
    std::reverse(s.begin(), s.end());
    return s;
}
U power(U x, U n, U m) {
    U y = 1;
    while (n) { if (n & 1) y = y * x % m; x = x * x % m; n >>= 1; }
    return y;
}
std::vector<std::vector<int>> factors(int LEN) {
    std::set<uint64_t> cuts{0, E};
    for (int j = 0; j <= LEN; ++j) cuts.insert((E - U(D) * j % E) % E);
    std::vector<uint64_t> c(cuts.begin(), cuts.end());
    std::set<std::vector<int>> words;
    for (size_t i = 0; i + 1 < c.size(); ++i) {
        for (uint64_t r : {c[i], c[i] + 1}) {
            if (r >= c[i+1]) continue;
            std::vector<int> g;
            uint64_t prev = (r + E - 1) / E;
            for (int j = 1; j <= LEN; ++j) {
                uint64_t next = (r + U(D) * j + E - 1) / E;
                g.push_back(1 + int(next - prev));
                prev = next;
            }
            words.insert(g);
        }
    }
    return {words.begin(), words.end()};
}
std::pair<U,U> residue(const std::vector<int>& g) {
    U m = 1, c = 0, power3 = 1, power2 = 1;
    for (int gap : g) {
        m *= 3;
        c = (U(1) << gap) * c + power3;
        power3 *= 3;
        power2 <<= gap;
    }
    c %= m;
    U phi = 2 * (m / 3);
    U inv = power(power2 % m, phi - 1, m);
    return {c * inv % m, m};
}
U reconstruct_min(U x, const std::vector<int>& g) {
    U mn = x;
    for (int gap : g) {
        U y = (U(1) << gap) * x - 1;
        if (y % 3) { std::cerr << "BAD_CONGRUENCE\n"; std::exit(2); }
        x = y / 3;
        if (!(x & 1)) { std::cerr << "BAD_PARITY\n"; std::exit(2); }
        if (x < mn) mn = x;
    }
    return mn;
}
int escape(U x) {
    constexpr U MAX = ~U(0);
    for (int steps = 0; steps <= 1000; ++steps) {
        if (x < LOW) return steps;
        if (x > (MAX - 1) / 3) { std::cerr << "OVERFLOW\n"; std::exit(3); }
        U y = 3 * x + 1;
        unsigned bits = (uint64_t)y ? __builtin_ctzll((uint64_t)y) : 64 + __builtin_ctzll((uint64_t)(y >> 64));
        x = y >> bits;
    }
    std::cerr << "NO_ESCAPE_1000\n"; std::exit(4);
}
int main(int argc, char** argv) {
    int zero_run = argc > 1 ? std::atoi(argv[1]) : 37;
    if (zero_run < 1 || zero_run > 38) return 2;
    auto words = factors(zero_run - 1);
    if (int(words.size()) != zero_run) { std::cerr << "BAD_FACTOR_COUNT\n"; return 2; }
    int first = 0, last = zero_run;
    if (argc > 2) { first = std::atoi(argv[2]); last = first + 1; }
    for (int i = first; i < last; ++i) {
        auto [r,m] = residue(words[i]);
        U x = r;
        if (x < MIN_OWNED) x += ((MIN_OWNED - x + m - 1) / m) * m;
        if (!(x & 1)) x += m;
        uint64_t candidates = 0;
        int maximum = 0;
        U argmax = 0;
        for (; x < UP; x += 2*m) {
            if (reconstruct_min(x, words[i]) < MIN_OWNED) continue;
            ++candidates;
            int steps = escape(x);
            if (steps > maximum) { maximum = steps; argmax = x; }
        }
        std::cout << "FACTOR " << i << " COUNT " << candidates << " MAX_ESCAPE " << maximum
                  << " ARGMAX " << out(argmax) << " RESIDUE " << out(r) << " MOD " << out(m) << "\n";
    }
}
