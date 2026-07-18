from meridianforge.analysis.underwriting_engine import (
    UnderwritingEngine,
)


def test_engine():

    result = UnderwritingEngine().analyze(
        purchase_price=200000,
        noi=12000,
        annual_cash_flow=6000,
        cash_invested=50000,
        annual_debt=8000,
    )

    assert result.cap_rate == 0.06
    assert result.dscr == 1.5
