from meridianforge.models.domain.extractor_confidence_calibration import (
    ExtractorConfidenceCalibration,
)


def test_extractor_confidence_calibration_defaults() -> None:
    calibration = ExtractorConfidenceCalibration(
        extractor="RentalAcquisitionExtractor",
    )

    assert calibration.extractor == "RentalAcquisitionExtractor"
    assert calibration.raw_confidence == 0.0
    assert calibration.calibrated_confidence == 0.0
