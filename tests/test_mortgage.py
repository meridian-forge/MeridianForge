from meridianforge.engine import Mortgage


def test_monthly_payment():

    mortgage = Mortgage(
        loan_amount=240000,
        interest_rate=6.5,
        term_years=30,
    )

    payment = mortgage.monthly_payment

    assert round(payment, 2) == 1516.96


def test_total_interest():

    mortgage = Mortgage(
        loan_amount=240000,
        interest_rate=6.5,
        term_years=30,
    )

    assert mortgage.total_interest > 200000


def test_remaining_balance():

    mortgage = Mortgage(
        loan_amount=240000,
        interest_rate=6.5,
        term_years=30,
    )

    balance = mortgage.remaining_balance(5)

    assert balance < 240000
    assert balance > 0
