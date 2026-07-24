"""
Portfolio metrics model.

MF-341.2

Represents aggregated metrics describing an investor
portfolio. This model is a value object and does not
perform financial calculations.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class PortfolioMetrics:
    """
    Aggregated portfolio metrics.
    """

    total_properties: int

    total_monthly_cash_flow: float

    total_annual_cash_flow: float

    average_cap_rate: float

    average_cash_on_cash: float

    average_dscr: float

    average_score: float

    average_confidence: float

    buy_count: int

    review_count: int

    reject_count: int
