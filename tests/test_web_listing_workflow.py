from meridianforge.models.results.acquisition_assessment import (
    AcquisitionAssessment,
)
from meridianforge.services.acquisition_pipeline import (
    AcquisitionPipeline,
)
from meridianforge.services.recommendation_engine import (
    RecommendationEngine,
)
from tests.fixtures.sample_listing_page import (
    sample_listing_property,
)


def test_web_listing_workflow() -> None:

    property_data = sample_listing_property()

    assessment = AcquisitionAssessment(
        purchase_price=float(property_data["purchase_price"]),
        monthly_cash_flow=325,
        dscr=1.28,
        cap_rate=0.068,
    )

    pipeline = AcquisitionPipeline()

    result = pipeline.process(
        assets=[property_data],
        confidence=0.87,
        assessment=assessment,
    )

    recommendation = RecommendationEngine.evaluate(assessment)

    assert result.assets_analyzed == 1
    assert result.confidence == 0.87
    assert recommendation.decision == "BUY"
