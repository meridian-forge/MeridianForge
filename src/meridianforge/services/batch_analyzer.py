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
from meridianforge.models.results.batch_analysis_result import (
    BatchAnalysisResult,
)
from meridianforge.models.results.deal_evaluation import DealEvaluation


class BatchAnalyzerService:
    """
    Analyze and rank multiple investment opportunities.
    """

    @staticmethod
    def analyze(
        properties: list[Property],
        investor: InvestorProfile,
    ) -> BatchAnalysisResult:
        """
        Analyze a collection of properties.
        """

        evaluated: list[tuple[Property, DealEvaluation]] = []

        dscr_values: list[float] = []

        for property_data in properties:
            analysis = UnderwritingEngine.analyze(property_data)

            dscr_values.append(
                analysis.dscr,
            )

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

        ranked_deals = DealRankingEngine.rank(
            evaluated,
        )

        qualified = [deal for deal in ranked_deals if deal.evaluation.qualified]

        average_score = (
            sum(deal.evaluation.score for deal in ranked_deals) / len(ranked_deals)
            if ranked_deals
            else 0.0
        )

        average_dscr = sum(dscr_values) / len(dscr_values) if dscr_values else 0.0

        return BatchAnalysisResult(
            ranked_deals=ranked_deals,
            total_analyzed=len(properties),
            qualified_count=len(qualified),
            rejected_count=(len(ranked_deals) - len(qualified)),
            average_score=average_score,
            average_dscr=average_dscr,
        )
