from tests.fixtures.sample_proforma import (
    sample_proforma_property,
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


def test_excel_proforma_workflow() -> None:

    property_data = sample_proforma_property()

    assessment = AcquisitionAssessment(
        purchase_price=float(
            property_data["purchase_price"]
        ),
        monthly_cash_flow=275,
        dscr=1.22,
        cap_rate=0.065,
    )

    pipeline = AcquisitionPipeline()

    result = pipeline.process(
        assets=[property_data],
        confidence=0.92,
        assessment=assessment,
    )

    recommendation = RecommendationEngine.evaluate(
        assessment
    )

    assert result.assets_analyzed == 1
    assert result.confidence == 0.92
    assert recommendation.decision in (
        "BUY",
        "WATCH",
    )
