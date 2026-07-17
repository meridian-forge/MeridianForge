from tests.fixtures.sample_property_email import (
    sample_email_property,
)

from meridianforge.models.results.acquisition_assessment import (
    AcquisitionAssessment,
)

from meridianforge.services.acquisition_pipeline import (
    AcquisitionPipeline,
)

from meridianforge.services.recommendation_engine import (
    RecommendationEngine,
)


def test_embedded_email_property_workflow() -> None:

    property_data = sample_email_property()

    assessment = AcquisitionAssessment(
        purchase_price=float(
            property_data["purchase_price"]
        ),
        monthly_cash_flow=300,
        dscr=1.25,
        cap_rate=0.065,
    )

    pipeline = AcquisitionPipeline()

    result = pipeline.process(
        assets=[property_data],
        confidence=0.88,
        assessment=assessment,
    )

    recommendation = RecommendationEngine.evaluate(
        assessment
    )

    assert result.assets_analyzed == 1
    assert recommendation.decision == "BUY"
