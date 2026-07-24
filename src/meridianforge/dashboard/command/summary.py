"""
Investor command center summary.

MF-349.3
"""

from dataclasses import dataclass


@dataclass(slots=True)
class CommandCenterSummary:
    """
    Executive investor summary.
    """

    health_status: str

    portfolio_score: float

    cash_flow_summary: str

    alert_count: int

    action_count: int
