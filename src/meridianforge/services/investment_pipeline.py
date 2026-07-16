"""
Investment pipeline orchestration.

Coordinates:
- Import
- Real estate conversion
- Underwriting
- Criteria evaluation
- Scoring
- Ranking
"""

from meridianforge.engine.criteria_engine import (
    CriteriaEngine,
)
from meridianforge.engine.deal_ranking import (
    DealRankingEngine,
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
from meridianforge.models.domain.normalized_asset import (
    NormalizedAsset,
)
from meridianforge.models.domain.property import (
    Property,
)
from meridianforge.models.results.deal_evaluation import (
    DealEvaluation,
)
from meridianforge.models.results.investment_pipeline_result import (
    InvestmentPipelineResult,
)
from meridianforge.normalization.real_estate_adapter import (
    RealEstateAdapter,
)
from meridianforge.services.import_execution_service import (
    ImportExecutionService,
)


class InvestmentPipeline:
    """
    End-to-end investment analysis workflow.
    """

    def __init__(
        self,
        import_service: ImportExecutionService | None = None,
    ) -> None:
        self.import_service = import_service or ImportExecutionService()

    def analyze(
        self,
        records: list[dict[str, object]],
        investor_profile: InvestorProfile,
        asset_type: str = "REAL_ESTATE",
    ) -> InvestmentPipelineResult:
        """
        Analyze investment opportunities.
        """

        import_result = self.import_service.execute(
            records,
            asset_type,
        )

        evaluated_deals: list[tuple[Property, DealEvaluation]] = []

        for asset in import_result.assets:

            normalized_asset = NormalizedAsset(
                asset_type=asset_type,
                attributes=asset,
            )

            property_data = RealEstateAdapter.convert(
                normalized_asset,
            )

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

            evaluated_deals.append(
                (
                    property_data,
                    scored,
                )
            )

        ranked = DealRankingEngine.rank(
            evaluated_deals,
        )

        return InvestmentPipelineResult(
            ranked_deals=ranked,
            import_quality=(import_result.quality_report),
        )
