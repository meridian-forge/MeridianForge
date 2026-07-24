"""
Investor dashboard metrics.

MF-349.1
"""

from dataclasses import dataclass


@dataclass(slots=True)
class DashboardMetrics:
    """
    Core investor dashboard measurements.
    """

    portfolio_score: float

    asset_count: int

    monthly_cash_flow: float

    annual_cash_flow: float

    average_cap_rate: float

    average_dscr: float

    active_alerts: int

    pending_actions: int
