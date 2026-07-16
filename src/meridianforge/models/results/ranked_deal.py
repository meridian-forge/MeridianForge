"""
Ranked investment opportunity.
"""

from dataclasses import dataclass

from meridianforge.models.domain.property import Property
from meridianforge.models.results.deal_evaluation import (
    DealEvaluation,
)


@dataclass(slots=True, frozen=True)
class RankedDeal:
    """
    Represents a ranked investment opportunity.
    """

    rank: int

    property: Property

    evaluation: DealEvaluation
