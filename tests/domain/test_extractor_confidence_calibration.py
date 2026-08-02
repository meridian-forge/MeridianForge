from meridianforge.models.domain.extractor_confidence_calibration import (
    ExtractorConfidenceCalibration,
)


def test_extractor_confidence_calibration_defaults() -> None:
    calibration = ExtractorConfidenceCalibration(
        extractor="RentalAcquisitionExtractor",
    )

    assert calibration.extractor == "RentalAcquisitionExtractor"
    assert calibration.provider is None
    assert calibration.raw_confidence == 0.0
    assert calibration.historical_accuracy == 0.0
    assert calibration.calibrated_confidence == 0.0
    assert calibration.sample_size == 0


def test_extractor_confidence_calibration_preserves_values() -> None:
    calibration = ExtractorConfidenceCalibration(
        extractor="RentalAcquisitionExtractor",
        provider="JWB Capital",
        raw_confidence=0.90,
        historical_accuracy=0.95,
        calibrated_confidence=0.925,
        sample_size=20,
    )

    assert calibration.extractor == "RentalAcquisitionExtractor"
    assert calibration.provider == "JWB Capital"
    assert calibration.raw_confidence == 0.90
    assert calibration.historical_accuracy == 0.95
    assert calibration.calibrated_confidence == 0.925
    assert calibration.sample_size == 20
