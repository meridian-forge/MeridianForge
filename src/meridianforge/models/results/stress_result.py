"""
Stress test result model.
"""

from dataclasses import dataclass

from meridianforge.models.results.analysis_result import AnalysisResult


@dataclass(frozen=True)
class StressResult:
    """
    Compares base underwriting against
    a stressed scenario.
    """

    scenario_name: str

    base_result: AnalysisResult

    stressed_result: AnalysisResult

    dscr_change: float

    cash_flow_change: float

    passed: bool
