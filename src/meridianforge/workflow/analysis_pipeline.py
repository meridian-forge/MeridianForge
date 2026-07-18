from typing import Any

from meridianforge.workflow.result import AnalysisResult


class InvestmentAnalysisPipeline:
    """
    Orchestrates the complete Meridian Forge investment analysis workflow.

    Flow:

    Property
        |
        v
    Underwriting
        |
        v
    Scoring
        |
        v
    Recommendation
        |
        v
    Decision
        |
        v
    AnalysisResult
    """

    def __init__(
        self,
        underwriting_engine: Any,
        scoring_engine: Any,
        recommendation_engine: Any,
        decision_engine: Any,
    ) -> None:
        self.underwriting_engine = underwriting_engine
        self.scoring_engine = scoring_engine
        self.recommendation_engine = recommendation_engine
        self.decision_engine = decision_engine

    def analyze(self, property_opportunity: Any) -> AnalysisResult:
        underwriting_result = self.underwriting_engine.analyze(property_opportunity)

        score = self.scoring_engine.score(
            property_opportunity,
            underwriting_result,
        )

        recommendation = self.recommendation_engine.recommend(
            property_opportunity,
            score,
        )

        decision = self.decision_engine.decide(
            property_opportunity,
            score,
            recommendation,
        )

        return AnalysisResult(
            property=property_opportunity,
            underwriting_result=underwriting_result,
            score=score,
            recommendation=recommendation,
            decision=decision.action,
            confidence=decision.confidence,
            rationale=decision.rationale,
        )
