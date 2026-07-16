"""
Investment assessment orchestration engine.

Coordinates underwriting, criteria evaluation,
and deal scoring.
"""

from meridianforge.engine.criteria_engine import (
    CriteriaEngine,
)
from meridianforge.engine.deal_scoring import (
    DealScoringEngine,
)
from meridianforge.engine.underwriting_engine import (
    UnderwritingEngine,
)
from meridianforge.models.domain.investor_profile import (
    InvestorProfile,
)
from meridianforge.models.domain.property import (
    Property,
)
from meridianforge.models.results.investment_assessment_result import (
    InvestmentAssessmentResult,
)


class InvestmentAssessmentEngine:
    """
    Performs complete investment assessment.
    """

    @staticmethod
    def assess(
        property_data: Property,
        investor_profile: InvestorProfile,
    ) -> InvestmentAssessmentResult:
        """
        Analyze and score an investment opportunity.
        """

        analysis = UnderwritingEngine.analyze(
            property_data,
        )

        evaluation = CriteriaEngine.evaluate(
            investor_profile,
            analysis,
        )

        scored = DealScoringEngine.evaluate(
            analysis,
            evaluation,
        )

        return InvestmentAssessmentResult(
            analysis=analysis,
            evaluation=scored,
        )
