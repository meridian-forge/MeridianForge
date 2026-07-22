"""
Legacy analysis result model.

MF-332.5

Compatibility model for the legacy analysis underwriting engine.

The canonical underwriting result now lives at:

meridianforge.models.results.analysis_result.AnalysisResult

This model remains temporarily for backward compatibility with:
- analysis.underwriting_engine
- application workflow tests
"""

from dataclasses import dataclass


@dataclass
class AnalysisResult:
    """
    Legacy underwriting output.

    Deprecated:
    Use meridianforge.models.results.AnalysisResult
    for new workflows.
    """

    cash_flow_monthly: float

    cap_rate: float

    cash_on_cash_return: float

    dscr: float

    score: float
