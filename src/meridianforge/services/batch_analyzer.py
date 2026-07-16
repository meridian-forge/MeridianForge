"""
Batch analysis orchestration service.

Coordinates analysis of multiple investment properties.
"""

from meridianforge.engine.criteria_engine import CriteriaEngine
from meridianforge.engine.deal_ranking import DealRankingEngine
from meridianforge.engine.deal_scoring import DealScoringEngine
from meridianforge.engine.underwriting_engine import UnderwritingEngine
from meridianforge.models.domain.investor_profile import InvestorProfile
from meridianforge.models.domain.property import Property
from meridianforge.models.results.deal_evaluation import DealEvaluation
from meridianforge.models.results.ranked_deal import RankedDeal


class BatchAnalyzerService:
    """
    Analyze and rank multiple investment opportunities.
    """

    @staticmethod
    def analyze(
        properties: list[Property],
        investor: InvestorProfile,
    ) -> list[RankedDeal]:
        """
        Analyze a collection of properties and return ranked results.
        """

        evaluated: list[tuple[Property, DealEvaluation]] = []

        for property_data in properties:
            analysis = UnderwritingEngine.analyze(property_data)

            evaluation = CriteriaEngine.evaluate(
                investor,
                analysis,
            )

            evaluation = DealScoringEngine.evaluate(
                analysis,
                evaluation,
            )

            evaluated.append(
                (
                    property_data,
                    evaluation,
                )
            )

        return DealRankingEngine.rank(evaluated)
