from dataclasses import dataclass, field
from enum import StrEnum


class Recommendation(StrEnum):
    BUY = "BUY"
    WATCH = "WATCH"
    REJECT = "REJECT"


@dataclass
class AnalysisResult:
    opportunity_file: str
    metrics: dict[str, float] = field(default_factory=dict)
    recommendation: Recommendation = Recommendation.WATCH
    warnings: list[str] = field(default_factory=list)
