from meridianforge.engine.mortgage import Mortgage
from meridianforge.finance.mortgage import monthly_payment


def test_finance_wrapper_matches_engine() -> None:
    engine_value = Mortgage(
        loan_amount=300000,
        interest_rate=6.5,
        term_years=30,
    ).monthly_payment

    finance_value = monthly_payment(
        loan_amount=300000,
        annual_rate=6.5,
        years=30,
    )

    assert finance_value == engine_value
