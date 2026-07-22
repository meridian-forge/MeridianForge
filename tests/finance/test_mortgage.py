from meridianforge.finance.mortgage import monthly_payment


def test_mortgage():

    payment = monthly_payment(
        200000,
        6.0,
        30,
    )

    assert round(payment, 2) == 1199.10
