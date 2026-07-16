"""
Investment report result model.

Represents investor-facing analysis output.
"""

from dataclasses import dataclass, field

from meridianforge.models.results.ranked_deal import (
    RankedDeal,
)


@dataclass(slots=True)
class InvestmentReport:
    """
    Human-readable investment recommendation report.
    """

    title: str

    total_opportunities: int

    ranked_deals: list[RankedDeal] = field(
        default_factory=list,
    )

    summary: str = ""

    recommendations: list[str] = field(
        default_factory=list,
    )

    warnings: list[str] = field(
        default_factory=list,
    )
