from meridianforge.models.results.acquisition_assessment import (
    AcquisitionAssessment,
)


def test_acquisition_assessment_defaults() -> None:

    assessment = AcquisitionAssessment()

    assert assessment.dscr == 0.0
    assert assessment.cap_rate == 0.0
