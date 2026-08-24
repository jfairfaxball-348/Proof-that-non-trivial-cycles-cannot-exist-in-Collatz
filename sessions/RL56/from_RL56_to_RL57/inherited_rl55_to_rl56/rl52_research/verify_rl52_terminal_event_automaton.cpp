#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <chrono>
#include <cstdlib>
#include <iostream>
#include <vector>

using boost::multiprecision::cpp_int;
using boost::multiprecision::uint256_t;
using boost::multiprecision::uint512_t;

static std::vector<uint256_t> P3;
static unsigned long long calls = 0;
static int max_v_seen = 0;
static int min_precision_seen = 1000000;
static int max_depth_seen = 0;
static bool ambiguous = false;
static int XMAX = 0, YMAX = 0;

static uint256_t mulmod(uint256_t a, uint256_t b, uint256_t m) {
    return uint256_t((uint512_t(a) * uint512_t(b)) % uint512_t(m));
}

static uint256_t powmod2(cpp_int e, uint256_t m) {
    uint256_t a = 2 % m, r = 1 % m;
    while (e > 0) {
        if ((e & 1) != 0) r = mulmod(r, a, m);
        e >>= 1;
        if (e > 0) a = mulmod(a, a, m);
    }
    return r;
}

// Exact zero-event recursion in the retained backward Q_d grammar.
// At a state Q, a run of backward 11 edges can have any length r=0..v3(Q).
// A following 01 consumes one divisibility and therefore requires r<v3(Q).
// Every non-11 event consumes at least one zero budget, so the recursion is finite.
static int dfs(uint256_t q, int precision, int x_used, int y_used, int depth) {
    ++calls;
    min_precision_seen = std::min(min_precision_seen, precision);
    max_depth_seen = std::max(max_depth_seen, depth);

    // q==0 modulo the current modulus would mean the available precision is
    // insufficient to know v3(Q) exactly.  No certified run is allowed to hit it.
    if (q == 0) {
        ambiguous = true;
        return 1000000;
    }

    int v = 0;
    uint256_t tmp = q;
    while (v < precision && tmp % 3 == 0) {
        tmp /= 3;
        ++v;
    }
    if (v == precision) {
        ambiguous = true;
        return 1000000;
    }
    max_v_seen = std::max(max_v_seen, v);

    // If no further zero-event is used, take all remaining legal 11 edges.
    int best = v;

    uint256_t qr = q;
    int pr = precision;
    const int d = 1 + y_used - x_used; // exact invariant d=1+#y0-#x0
    if (d < 1) {
        std::cerr << "height invariant failure\n";
        std::exit(3);
    }

    for (int r = 0; r <= v; ++r) {
        const uint256_t mod = P3[pr];

        // backward 10: Q -> 2Q+1, d -> d+1; consumes one y-zero
        if (y_used < YMAX) {
            const uint256_t nq = (2 * qr + 1) % mod;
            best = std::max(best, r + 1 + dfs(nq, pr, x_used, y_used + 1, depth + r + 1));
        }

        // backward 00: Q -> 2Q-(3^d-1); consumes one x-zero and one y-zero
        if (x_used < XMAX && y_used < YMAX) {
            const uint256_t c = (P3[d] - 1) % mod;
            const uint256_t a = (2 * qr) % mod;
            const uint256_t nq = (a >= c) ? (a - c) : (a + mod - c);
            best = std::max(best, r + 1 + dfs(nq, pr, x_used + 1, y_used + 1, depth + r + 1));
        }

        // backward 01: Q -> 2Q/3-3^(d-1), d -> d-1; consumes one x-zero
        if (x_used < XMAX && d > 1 && r < v) {
            const int np = pr - 1;
            const uint256_t mod2 = P3[np];
            const uint256_t a = (2 * (qr / 3)) % mod2;
            const uint256_t c = P3[d - 1] % mod2;
            const uint256_t nq = (a >= c) ? (a - c) : (a + mod2 - c);
            best = std::max(best, r + 1 + dfs(nq, np, x_used + 1, y_used, depth + r + 1));
        }

        if (r < v) {
            --pr;
            qr = (2 * (qr / 3)) % P3[pr];
        }
    }
    return best;
}

int main(int argc, char **argv) {
    if (argc != 6) {
        std::cerr << "usage: verifier Z XMAX YMAX PRECISION EXPECTED_MAX\n";
        return 2;
    }
    const int Z = std::atoi(argv[1]);
    XMAX = std::atoi(argv[2]);
    YMAX = std::atoi(argv[3]);
    const int PREC = std::atoi(argv[4]);
    const int EXPECTED = std::atoi(argv[5]);
    if (PREC < 2 || PREC > 150) {
        std::cerr << "precision must lie in [2,150] for uint256_t safety\n";
        return 2;
    }

    const cpp_int A("123139092617126647266");
    const cpp_int ELL("77692117359936589403");
    const cpp_int K = A - ELL - Z + 3;

    P3.resize(std::max(PREC + 1, YMAX + 3));
    P3[0] = 1;
    for (size_t i = 1; i < P3.size(); ++i) P3[i] = P3[i - 1] * 3;

    const uint256_t q0 = (powmod2(K, P3[PREC]) + 1) % P3[PREC];
    const auto start = std::chrono::steady_clock::now();
    const int ans = dfs(q0, PREC, 0, 0, 0);
    const double sec = std::chrono::duration<double>(std::chrono::steady_clock::now() - start).count();

    std::cout << "Z=" << Z << " XMAX=" << XMAX << " YMAX=" << YMAX
              << " max_tail=" << ans << " expected=" << EXPECTED
              << " calls=" << calls << " max_v=" << max_v_seen
              << " min_precision=" << min_precision_seen
              << " max_depth=" << max_depth_seen
              << " ambiguous=" << (ambiguous ? 1 : 0)
              << " seconds=" << sec << "\n";

    if (ambiguous) {
        std::cerr << "FAIL: ternary precision exhausted/ambiguous\n";
        return 1;
    }
    if (ans != EXPECTED) {
        std::cerr << "FAIL: unexpected terminal maximum\n";
        return 1;
    }
    std::cout << "PASS\n";
    return 0;
}
