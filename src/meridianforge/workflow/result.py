"""
Workflow result models.

MF-332.2

The workflow layer represents orchestration results.

It is intentionally distinct from the canonical underwriting
AnalysisResult located in:

    meridianforge.models.results.analysis_result
"""

from dataclasses import dataclass
from typing import Any


@dataclass
class WorkflowResult:
    """
    Unified output from the MeridianForge workflow layer.
    """

    property: Any
    underwriting_result: Any
    score: Any
    recommendation: Any
    decision: Any
    confidence: Any
    rationale: Any


# ------------------------------------------------------------------
# Temporary compatibility alias.
#
# Remove during MF-333 after all imports migrate.
# ------------------------------------------------------------------

AnalysisResult = WorkflowResult
