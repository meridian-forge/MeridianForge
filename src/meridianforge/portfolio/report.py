from __future__ import annotations

from meridianforge.portfolio.analysis import (
    PortfolioAnalysisResult,
)


class PortfolioReport:
    """
    Portfolio decision report.

    Represents ranked acquisition decisions produced
    from portfolio analysis.
    """

    def __init__(
        self,
        analysis: PortfolioAnalysisResult,
    ) -> None:
        self.analysis = analysis
