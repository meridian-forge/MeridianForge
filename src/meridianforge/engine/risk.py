"""
Risk interpretation engine.
"""

from meridianforge.models.results.risk_rating import RiskRating
from meridianforge.models.results.stress_result import StressResult


class RiskEngine:
    """
    Converts stress results into investor risk ratings.
    """

    @staticmethod
    def evaluate(
        result: StressResult,
    ) -> RiskRating:
        """
        Classify investment resilience.
        """

        stressed = result.stressed_result

        if stressed.dscr < 1.10 or stressed.monthly_cash_flow < 0:
            return RiskRating.CRITICAL

        if stressed.dscr < 1.30:
            return RiskRating.WARNING

        return RiskRating.SAFE
