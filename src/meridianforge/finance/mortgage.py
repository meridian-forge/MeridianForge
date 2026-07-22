"""
Finance mortgage compatibility wrapper.

Canonical mortgage implementation:
meridianforge.engine.mortgage.Mortgage

This module exists temporarily during MF-327 consolidation.
"""

from meridianforge.engine.mortgage import Mortgage


def monthly_payment(
    loan_amount: float,
    annual_rate: float,
    years: int,
) -> float:
    """
    Calculate monthly mortgage payment.

    Supports both:

    annual_rate=6.5
        -> 6.5%

    annual_rate=0.065
        -> 6.5%

    Normalizes into canonical Mortgage engine.
    """

    if loan_amount <= 0:
        raise ValueError(
            "Loan amount must be positive"
        )

    if annual_rate < 0:
        raise ValueError(
            "Interest rate cannot be negative"
        )

    if years <= 0:
        raise ValueError(
            "Loan term must be positive"
        )

    if annual_rate < 1:
        interest_rate = annual_rate * 100
    else:
        interest_rate = annual_rate

    mortgage = Mortgage(
        loan_amount=loan_amount,
        interest_rate=interest_rate,
        term_years=years,
    )

    return mortgage.monthly_payment
