"""
Analysis metrics mapper.

MF-512.3.3

Converts underwriting analysis results into
MeridianForge verified investment metrics.
"""

from __future__ import annotations

from decimal import Decimal

from meridianforge.models.domain.opportunity_metrics import (
    VerifiedMetrics,
)
from meridianforge.models.results.analysis_result import (
    AnalysisResult,
)


class AnalysisMetricsMapper:
    """
    Map underwriting outputs into verified metrics.
    """

    @staticmethod
    def from_analysis(
        analysis: AnalysisResult,
    ) -> VerifiedMetrics:
        """
        Convert underwriting analysis into verified metrics.
        """

        return VerifiedMetrics(
            calculated_cashflow=Decimal(str(analysis.monthly_cash_flow)),
            cap_rate=Decimal(str(analysis.cap_rate)),
            cash_on_cash_return=Decimal(
                str(analysis.cash_on_cash_return),
            ),
            dscr=Decimal(str(analysis.dscr)),
        )
