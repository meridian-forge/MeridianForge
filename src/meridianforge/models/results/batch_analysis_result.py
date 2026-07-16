"""
Batch analysis result model.
"""

from dataclasses import dataclass

from meridianforge.models.results.ranked_deal import RankedDeal


@dataclass(frozen=True, slots=True)
class BatchAnalysisResult:
    """
    Summary of a batch property analysis run.
    """

    ranked_deals: list[RankedDeal]

    total_analyzed: int

    qualified_count: int

    rejected_count: int

    average_score: float

    average_dscr: float
