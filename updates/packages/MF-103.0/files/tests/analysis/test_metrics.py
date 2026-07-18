from meridianforge.analysis.metrics import (
    calculate_cap_rate,
    calculate_dscr,
)


def test_cap_rate():

    assert calculate_cap_rate(
        12000,
        200000,
    ) == 0.06



def test_dscr():

    assert calculate_dscr(
        24000,
        12000,
    ) == 2
