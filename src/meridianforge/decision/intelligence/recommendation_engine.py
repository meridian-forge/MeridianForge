"""
Recommendation engine.

Converts investment context into
an explainable investor decision.
"""

from meridianforge.decision.intelligence.decision_context import (
    DecisionContext,
)
from meridianforge.decision.intelligence.decision_recommendation import (
    DecisionRecommendation,
    RecommendationAction,
)


class RecommendationEngine:
    """
    Generates investment recommendations.
    """

    def evaluate(
        self,
        context: DecisionContext,
    ) -> DecisionRecommendation:
        """
        Evaluate investment opportunity.
        """

        reasons: list[str] = []
        risks: list[str] = []
        next_steps: list[str] = []

        if context.is_cash_flow_positive:
            reasons.append("Property generates positive monthly cash flow.")
        else:
            risks.append("Property does not generate positive cash flow.")

        if context.cap_rate >= 0.05:
            reasons.append("Cap rate meets minimum yield threshold.")
        else:
            risks.append("Cap rate is below target threshold.")

        if len(context.risk_flags) > 0:
            risks.extend(
                context.risk_flags,
            )

        if (
            context.is_cash_flow_positive
            and context.cap_rate >= 0.05
            and len(risks) <= 2
        ):
            action = RecommendationAction.BUY
            confidence = 0.90

        elif context.is_cash_flow_positive:
            action = RecommendationAction.WATCH
            confidence = 0.70

        else:
            action = RecommendationAction.PASS
            confidence = 0.85

        next_steps.extend(
            [
                "Validate property assumptions.",
                "Confirm financing terms.",
                "Review inspection findings.",
            ]
        )

        return DecisionRecommendation(
            action=action,
            confidence=confidence,
            reasons=reasons,
            risks=risks,
            next_steps=next_steps,
        )
