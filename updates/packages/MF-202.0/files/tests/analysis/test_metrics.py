from meridianforge.analysis.metrics import (
    cash_on_cash_return,
    roi,
)


def test_cash_on_cash_return() -> None:
    assert cash_on_cash_return(
        4000,
        30000,
    ) == 4000 / 30000


def test_roi() -> None:
    assert roi(
        60000,
        200000,
    ) == 0.30
