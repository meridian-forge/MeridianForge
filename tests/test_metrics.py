from meridianforge.engine import Metrics


def test_noi():

    noi = Metrics.calculate_noi(
        gross_income=24000,
        operating_expenses=9000,
    )

    assert noi == 15000


def test_cap_rate():

    cap_rate = Metrics.calculate_cap_rate(
        annual_noi=15000,
        purchase_price=200000,
    )

    assert round(cap_rate, 2) == 7.50


def test_dscr():

    dscr = Metrics.calculate_dscr(
        annual_noi=18000,
        annual_debt_service=15000,
    )

    assert round(dscr, 2) == 1.20


def test_cash_flow():

    cash_flow = Metrics.calculate_cash_flow(
        annual_noi=18000,
        annual_debt_service=15000,
    )

    assert cash_flow == 3000


def test_cash_on_cash():

    coc = Metrics.calculate_cash_on_cash(
        annual_cash_flow=5000,
        cash_invested=50000,
    )

    assert round(coc, 2) == 10.00
