"""
Acquisition dashboard model.

MF-339.1

Aggregated acquisition intelligence view.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class AcquisitionDashboard:
    """
    Portfolio acquisition summary.
    """

    total_deals: int

    buy_candidates: int

    review_candidates: int

    average_score: float

    average_confidence: float

    high_risk_count: int
