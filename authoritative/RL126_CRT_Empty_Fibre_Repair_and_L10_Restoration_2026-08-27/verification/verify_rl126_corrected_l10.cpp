#include <algorithm>
#include <cstdint>
#include <iostream>
#include <sstream>
#include <vector>

using u64 = std::uint64_t;

static void compositions(int n, int parts, std::vector<int>& current,
                         std::vector<std::vector<int>>& out) {
    if (parts == 1) {
        current.push_back(n); out.push_back(current); current.pop_back(); return;
    }
    for (int a = 1; a <= n - parts + 1; ++a) {
        current.push_back(a); compositions(n - a, parts - 1, current, out); current.pop_back();
    }
}

static bool primitive(const std::vector<int>& o, const std::vector<int>& z) {
    std::vector<int> bits;
    for (size_t i = 0; i < o.size(); ++i) {
        bits.insert(bits.end(), o[i], 1); bits.insert(bits.end(), z[i], 0);
    }
    const int A = static_cast<int>(bits.size());
    for (int d = 1; d < A; ++d) {
        if (A % d) continue;
        bool same = true;
        for (int i = 0; i < A; ++i) if (bits[i] != bits[i % d]) { same = false; break; }
        if (same) return false;
    }
    return true;
}

static u64 side_zero(const std::vector<int>& z) {
    u64 best = 0;
    for (int k = 1; k <= *std::max_element(z.begin(), z.end()); ++k) {
        u64 c = 0; for (int a : z) if (a >= k) c += a - k + 1;
        best = std::max(best, (c - 1) * (u64(1) << k) + 1);
    }
    return best;
}

static u64 side_one(const std::vector<int>& o) {
    static const u64 p3[] = {1,3,9,27,81,243,729,2187,6561,19683,59049};
    u64 best = 0;
    for (int j = 1; j <= *std::max_element(o.begin(), o.end()); ++j) {
        u64 c = 0; for (int a : o) if (a >= j) c += a - j + 1;
        best = std::max(best, (c - 1) * p3[j]);
    }
    return best;
}

static u64 crt(const std::vector<int>& o, const std::vector<int>& z) {
    static const u64 p3[] = {1,3,9,27,81,243,729,2187,6561,19683,59049};
    u64 best = 0;
    for (int j = 1; j <= *std::max_element(o.begin(), o.end()); ++j)
        for (int k = 1; k <= *std::max_element(z.begin(), z.end()); ++k) {
            u64 c = 0;
            for (size_t i = 0; i < o.size(); ++i) if (o[i] >= j && z[i] >= k) ++c;
            if (c) best = std::max(best, (c - 1) * p3[j] * (u64(1) << k));
        }
    return best;
}

static std::vector<int> bits_from_profile(const std::vector<int>& o, const std::vector<int>& z) {
    std::vector<int> bits;
    for (size_t i = 0; i < o.size(); ++i) {
        bits.insert(bits.end(), o[i], 1); bits.insert(bits.end(), z[i], 0);
    }
    return bits;
}

static u64 q_numerator(const std::vector<int>& bits, int shift) {
    static const u64 p3[] = {1,3,9,27,81,243,729,2187,6561,19683,59049};
    const int A = static_cast<int>(bits.size());
    int seen = 0; u64 q = 0;
    for (int p = 0; p < A; ++p) {
        if (bits[(shift + p) % A]) {
            q += (u64(1) << p) * p3[9 - seen];
            ++seen;
        }
    }
    return q;
}

static std::string rotation_string(const std::vector<int>& bits, int shift) {
    std::string s; s.reserve(bits.size());
    for (size_t p = 0; p < bits.size(); ++p) s += bits[(shift + p) % bits.size()] ? '1' : '0';
    return s;
}

int main() {
    constexpr int L = 10; constexpr u64 THREE_L = 59049;
    std::cout << "# L=10 compressed exact ownership certificate\n";
    std::cout << "# Every primitive ordered run profile is capacity-excluded or every cyclic root is tested for D|Q.\n";
    u64 total_primitive_profiles = 0, total_excluded = 0, total_survivors = 0, total_roots = 0, total_hits = 0;
    for (int Z = 6; Z <= 24; ++Z) {
        const int A = L + Z;
        const u64 D = (u64(1) << A) - THREE_L;
        const u64 B = ((u64(1) << Z) - 1) * (THREE_L - (u64(1) << L));
        const u64 U = B / D;
        u64 prim = 0, excluded = 0, survivors = 0, roots = 0, hits = 0;
        for (int t = 1; t <= std::min(L, Z); ++t) {
            std::vector<std::vector<int>> os, zs; std::vector<int> current;
            compositions(L, t, current, os); compositions(Z, t, current, zs);
            for (const auto& o : os) for (const auto& z : zs) {
                if (!primitive(o, z)) continue;
                ++prim;
                const u64 p = std::max({side_one(o), side_zero(z), u64(6 * (t - 1)), crt(o,z)});
                if (p > U) { ++excluded; continue; }
                ++survivors;
                const auto bits = bits_from_profile(o, z);
                for (int s = 0; s < A; ++s) {
                    ++roots;
                    const u64 q = q_numerator(bits, s);
                    if (q % D == 0) {
                        ++hits;
                        std::cout << "HIT Z=" << Z << " shift=" << s << " word=" << rotation_string(bits,s)
                                  << " x=" << (q / D) << "\n";
                    }
                }
            }
        }
        total_primitive_profiles += prim; total_excluded += excluded; total_survivors += survivors;
        total_roots += roots; total_hits += hits;
        std::cout << "Z=" << Z << " D=" << D << " U=" << U << " primitive_profiles=" << prim
                  << " capacity_excluded=" << excluded << " residual_profiles=" << survivors
                  << " roots_tested=" << roots << " divisibility_hits=" << hits << "\n";
    }
    std::cout << "TOTAL primitive_profiles=" << total_primitive_profiles << " capacity_excluded=" << total_excluded
              << " residual_profiles=" << total_survivors << " roots_tested=" << total_roots
              << " divisibility_hits=" << total_hits << "\n";
}
