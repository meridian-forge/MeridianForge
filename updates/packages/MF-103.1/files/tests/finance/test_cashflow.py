from meridianforge.finance.cashflow import monthly_cash_flow


def test_cashflow():

    result = monthly_cash_flow(
        2000,
        400,
        900,
    )

    assert result == 700
