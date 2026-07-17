"""
Recommendation engine.

Converts underwriting metrics into
an acquisition decision.
"""

from meridianforge.models.results.acquisition_assessment import (
    AcquisitionAssessment,
)
from meridianforge.models.results.recommendation import (
    Recommendation,
)


class RecommendationEngine:
    """
    Creates BUY/WATCH/PASS recommendations.
    """

    @staticmethod
    def evaluate(
        assessment: AcquisitionAssessment,
    ) -> Recommendation:
        """
        Evaluate investment metrics.
        """

        if (
            assessment.dscr >= 1.20
            and assessment.monthly_cash_flow > 0
            and assessment.cap_rate >= 0.06
        ):
            return Recommendation(
                decision="BUY",
                confidence=0.90,
                reason="Meets core investment criteria.",
            )

        if assessment.monthly_cash_flow > 0:
            return Recommendation(
                decision="WATCH",
                confidence=0.70,
                reason="Positive cash flow but requires review.",
            )

        return Recommendation(
            decision="PASS",
            confidence=0.85,
            reason="Does not meet minimum criteria.",
        )
