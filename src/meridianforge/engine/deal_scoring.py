"""
Deal scoring engine.

Ranks investment opportunities based on
financial attractiveness.
"""

from meridianforge.models.results.analysis_result import (
    AnalysisResult,
)
from meridianforge.models.results.deal_evaluation import (
    DealEvaluation,
)


class DealScoringEngine:
    """
    Calculates investment attractiveness score.
    """

    @staticmethod
    def evaluate(
        analysis: AnalysisResult,
        evaluation: DealEvaluation,
    ) -> DealEvaluation:
        """
        Apply scoring model to a deal evaluation.
        """

        score = 0.0

        reasons = list(evaluation.reasons)

        failed = list(evaluation.failed_criteria)

        # DSCR - 30 points
        if analysis.dscr >= 1.50:
            score += 30
        elif analysis.dscr >= 1.20:
            score += 25
        elif analysis.dscr >= 1.00:
            score += 15

        # Cash Flow - 25 points
        if analysis.monthly_cash_flow >= 500:
            score += 25
        elif analysis.monthly_cash_flow >= 250:
            score += 20
        elif analysis.monthly_cash_flow > 0:
            score += 10

        # Cash-on-Cash - 20 points
        if analysis.cash_on_cash_return >= 12:
            score += 20
        elif analysis.cash_on_cash_return >= 8:
            score += 15
        elif analysis.cash_on_cash_return > 0:
            score += 10

        # Cap Rate - 15 points
        if analysis.cap_rate >= 8:
            score += 15
        elif analysis.cap_rate >= 6:
            score += 10
        elif analysis.cap_rate > 0:
            score += 5

        # Risk adjustment - 10 points
        if evaluation.qualified:
            score += 10

        return DealEvaluation(
            qualified=evaluation.qualified,
            score=score,
            reasons=reasons,
            failed_criteria=failed,
        )
