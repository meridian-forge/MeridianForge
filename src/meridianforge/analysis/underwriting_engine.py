"""
Legacy underwriting compatibility adapter.

MF-331 consolidation:

The canonical underwriting engine is:

meridianforge.engine.underwriting_engine.UnderwritingEngine

This module preserves the historical analysis API while
the remaining callers migrate.
"""

from meridianforge.analysis.metrics import (
    calculate_cap_rate,
    calculate_cash_on_cash,
    calculate_dscr,
)

from meridianforge.analysis.result import AnalysisResult


class UnderwritingEngine:
    """
    Compatibility layer for the legacy analysis workflow.

    This class intentionally preserves the original API.
    """

    def analyze(
        self,
        purchase_price: float,
        noi: float,
        annual_cash_flow: float,
        cash_invested: float,
        annual_debt: float,
    ) -> AnalysisResult:
        """
        Perform legacy underwriting calculations.

        Migration target:
        meridianforge.engine.underwriting_engine
        """

        cap_rate = calculate_cap_rate(
            noi,
            purchase_price,
        )

        cash_return = calculate_cash_on_cash(
            annual_cash_flow,
            cash_invested,
        )

        dscr = calculate_dscr(
            noi,
            annual_debt,
        )

        score = (
            cap_rate
            + cash_return
            + dscr
        )

        return AnalysisResult(
            cash_flow_monthly=annual_cash_flow / 12,
            cap_rate=cap_rate,
            cash_on_cash_return=cash_return,
            dscr=dscr,
            score=score,
        )
