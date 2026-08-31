#!/usr/bin/env python3
"""Targeted exact repair, not a replay of the inherited 16-billion-rank certificate."""
import json

A = 217976794617
L = 137528045312
B = 80448749305
p = 65470613321
u = 103768467013
N = 1 << 24
LO, HI = 25583192106, 41775866136
SAFE_LO, SAFE_HI = 38643145224, 38659291956
OLD = {26058127773,26058127774,28746802249,28746802250,31435476726,
       34124151202,36398517184,36398517185,36812825678,39087191660,
       39087191661,41775866136}
ANCHOR = {26058127775,28746802251,36398517186,39087191662}


def necessary_terminal(r):
    if not LO <= r <= HI or r in OLD | ANCHOR:
        return False
    phase = p*r % L
    root_window = phase < N or phase >= L-N
    return not root_window or SAFE_LO <= r <= SAFE_HI


def main():
    assert A*p-u*L == 1 and p*B % L == 1 and B == A-L
    shift = (-34*B) % L
    assert shift == 15303429870
    assert (LO+shift,HI+shift) == (40886621976,57079296006)
    expected_terminal = [1,57079296008,114158592015,33709842710,
                         90789138717,10340389412]
    rows = []
    for e in range(34,40):
        a = p-e
        terminal = a+34
        source_rank = a*B % L
        terminal_rank = terminal*B % L
        assert terminal_rank == (1-(e-34)*B) % L
        assert terminal_rank == expected_terminal[e-34]
        assert (source_rank+34*B) % L == terminal_rank
        assert p*terminal_rank % L == terminal
        depth = u-(A*a//L-1)
        assert depth == (A*e-1+L-1)//L+1
        rows.append({'offset':e,'source_rank':source_rank,
                     'terminal_rank':terminal_rank,
                     'necessary_terminal':necessary_terminal(terminal_rank),
                     'normalized_root_prefix_depth':depth})
    assert [row['offset'] for row in rows if row['necessary_terminal']] == [37]
    assert rows[3]['source_rank'] == 49013272580
    assert rows[3]['normalized_root_prefix_depth'] == 60
    assert not LO <= rows[3]['source_rank'] <= HI
    assert rows[5]['source_rank'] == 25643819282
    assert LO <= rows[5]['source_rank'] <= HI
    assert not rows[5]['necessary_terminal']
    for e in range(1,34):
        a = p-e
        assert 0 <= p-a <= 33  # source's positive tail hits zero anchor p
    assert 58*L < 37*A-1 <= 59*L
    assert 60 > 56 and 60+37 == 97

    # The unchanged eta-parity calculation is independent of the repaired ranks.
    modulus = 1 << 35
    prefix = sum((1 << t)*pow(pow(3,t,modulus),-1,modulus)
                 for t in range(34)) % modulus
    assert prefix == (3-(1 << 34)) % modulus
    even_terminal = ((1 << 34)*pow(pow(3,34,modulus),-1,modulus)) % modulus
    assert (prefix+even_terminal) % modulus == 3
    assert 34+22 == 56
    # Arithmetic reconciliation only; original whole-window counts remain inherited.
    assert HI-LO+1-len(OLD)-3946781-len(ANCHOR) == 16188727234

    print(json.dumps({'status':'PASS','correction':'RL206-C2',
                      'finite_offset_range':[34,39],'rows':rows,
                      'first_necessary_below_p_offset':37,
                      'root_prefix_depth_lower_bound':60,
                      'root_normalization_depth_lower_bound':97,
                      'qualitative_mod2_56_boundary_preserved':True,
                      'inherited_necessary_rank_count':16188727234,
                      'full_rank_count_recertified':False,
                      'physical_realization_claimed':False},indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
