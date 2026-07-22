"""
Finance mortgage compatibility wrapper.

Canonical mortgage implementation:
meridianforge.engine.mortgage
"""

from meridianforge.engine.mortgage import Mortgage


def monthly_payment(
    loan_amount: float,
    annual_rate: float,
    years: int,
) -> float:
    """
    Calculate monthly mortgage payment.

    annual_rate accepts decimal format.

    Example:
        0.065 = 6.5%
    """

    mortgage = Mortgage(
        loan_amount=loan_amount,
        interest_rate=annual_rate,
        term_years=years,
    )

    return mortgage.monthly_payment
