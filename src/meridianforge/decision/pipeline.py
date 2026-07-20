"""
Acquisition decision pipeline.

Transforms acquisition inputs into investor decisions.
"""

from meridianforge.decision.property_adapter import (
    AcquisitionPropertyAdapter,
)
from meridianforge.engine.underwriting_engine import (
    UnderwritingEngine,
)
from meridianforge.product.weekly_review import (
    WeeklyInvestorReview,
)
from meridianforge.workflows.acquisition_input import (
    AcquisitionInput,
)


class DecisionPipeline:
    """
    Generate investor review decisions.
    """
    
    def __init__(
        self,
        property_adapter=None,
        underwriting_engine=None,
    ):
        self.property_adapter = (
        property_adapter
        or AcquisitionPropertyAdapter()
        )
        self.underwriting_engine = (
        underwriting_engine
        or UnderwritingEngine
        )

    def evaluate(
        self,
        opportunity: AcquisitionInput,
    ) -> WeeklyInvestorReview:
        """
        Evaluate acquisition opportunity.
        """

        property_data = self.property_adapter.build(
            opportunity,
        )

        analysis = self.underwriting_engine.analyze(
            property_data,
        )

        from meridianforge.product.decision_card import (
            InvestorDecisionCard,
        )

        strengths: list[str] = []
        risks: list[str] = []

        if analysis.dscr >= 1.20:
            strengths.append(
                "DSCR meets investment threshold",
            )
        else:
            risks.append(
                "DSCR below target threshold",
            )

        if analysis.cash_on_cash_return > 0:
            strengths.append(
                "Positive cash-on-cash return",
            )
        else:
            risks.append(
                "Negative cash-on-cash return",
            )

        risks.extend(
            analysis.warnings,
        )

        recommendation = (
            "BUY"
            if analysis.passed
            else "REVIEW"
        )

        confidence = min(
            max(
                analysis.dscr / 2,
                0.0,
            ),
            1.0,
        )

        card = InvestorDecisionCard(
            rank=1,
            property_address=(
                property_data.address.display()
            ),
            recommendation=recommendation,
            confidence=confidence,
            strengths=strengths,
            risks=risks,
        )

        return WeeklyInvestorReview(
            cards=[
                card,
            ],
        )

        raise NotImplementedError
