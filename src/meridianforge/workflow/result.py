"""
Workflow result model.

MF-332.2

Represents the complete output of the investment workflow
after underwriting, scoring, recommendation, and decision.
"""

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class WorkflowResult:
    """
    Canonical output of the investment workflow.

    This is intentionally distinct from the underwriting
    AnalysisResult model.
    """

    property: Any
    underwriting_result: Any
    score: Any
    recommendation: Any
    decision: Any
    confidence: Any
    rationale: Any


# ------------------------------------------------------------------
# Backwards compatibility
#
# Existing modules still import:
#
#     from meridianforge.workflow.result import AnalysisResult
#
# During MF-332.x we preserve that API while callers migrate to the
# canonical WorkflowResult name.
# ------------------------------------------------------------------

AnalysisResult = WorkflowResult
