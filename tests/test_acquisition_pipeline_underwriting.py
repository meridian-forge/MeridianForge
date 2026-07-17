from meridianforge.models.results.acquisition_assessment import (
    AcquisitionAssessment,
)
from meridianforge.services.acquisition_pipeline import (
    AcquisitionPipeline,
)


def test_pipeline_includes_assessment() -> None:

    pipeline = AcquisitionPipeline()

    assessment = AcquisitionAssessment(
        dscr=1.3,
        cap_rate=0.07,
    )

    result = pipeline.process(
        assets=[{"address": "123 Main"}],
        confidence=0.95,
        assessment=assessment,
    )

    assert "assessment" in result.metadata
