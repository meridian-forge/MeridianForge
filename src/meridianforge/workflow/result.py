from dataclasses import dataclass
from typing import Any


@dataclass
class AnalysisResult:
    """
    Unified output from the Meridian Forge investment analysis workflow.
    """

    property: Any
    underwriting_result: Any
    score: Any
    recommendation: Any
    decision: Any
    confidence: Any
    rationale: Any
