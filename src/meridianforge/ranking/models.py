"""
Ranking domain models.

MF-332.1

Owns the canonical models used by the ranking subsystem.
"""

from dataclasses import dataclass, field
from enum import StrEnum


class Recommendation(StrEnum):
    BUY = "BUY"
    WATCH = "WATCH"
    REJECT = "REJECT"


@dataclass(slots=True)
class RankingInput:
    """
    Canonical input to the ranking engine.

    This replaces the legacy
    meridianforge.analysis.models.AnalysisResult
    for ranking/scoring purposes.
    """

    opportunity_file: str

    metrics: dict[str, float] = field(default_factory=dict)

    recommendation: Recommendation = Recommendation.WATCH

    warnings: list[str] = field(default_factory=list)


@dataclass(slots=True)
class RankingResult:
    """
    Output from the ranking engine.
    """

    opportunity_file: str

    score: float

    rank: int = 0
