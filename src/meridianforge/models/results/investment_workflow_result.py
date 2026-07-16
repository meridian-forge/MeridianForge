"""
Investment workflow result model.

Represents the complete end-to-end
Meridian Forge investment analysis output.
"""

from dataclasses import dataclass

from meridianforge.models.results.investment_pipeline_result import (
    InvestmentPipelineResult,
)
from meridianforge.models.results.investment_report import (
    InvestmentReport,
)


@dataclass(slots=True)
class InvestmentWorkflowResult:
    """
    Complete investor workflow result.
    """

    pipeline_result: InvestmentPipelineResult

    report: InvestmentReport
