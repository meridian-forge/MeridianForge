from meridianforge.models.results.acquisition_assessment import (
    AcquisitionAssessment,
)
from meridianforge.reports.acquisition_report import (
    AcquisitionReport,
)
from meridianforge.services.acquisition_pipeline import (
    AcquisitionPipeline,
)
from meridianforge.services.recommendation_engine import (
    RecommendationEngine,
)
from tests.fixtures.real_deal_case import (
    real_deal_property,
)


def test_real_deal_analysis() -> None:

    property_data = real_deal_property()

    assessment = AcquisitionAssessment(
        purchase_price=float(property_data["purchase_price"]),
        monthly_cash_flow=250,
        dscr=1.25,
        cap_rate=0.065,
    )

    pipeline = AcquisitionPipeline()

    result = pipeline.process(
        assets=[property_data],
        confidence=0.90,
        assessment=assessment,
    )

    recommendation = RecommendationEngine.evaluate(assessment)

    report = AcquisitionReport.generate(result)

    assert result.assets_analyzed == 1
    assert recommendation.decision in (
        "BUY",
        "WATCH",
        "PASS",
    )
    assert "MERIDIAN FORGE" in report
