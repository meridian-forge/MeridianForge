from meridianforge.models.domain.extractor_selection_explanation import (
    ExtractorSelectionExplanation,
)


def test_extractor_selection_explanation_defaults() -> None:
    explanation = ExtractorSelectionExplanation(
        extractor="RentalAcquisitionExtractor",
    )

    assert explanation.extractor == "RentalAcquisitionExtractor"
    assert explanation.provider is None
    assert explanation.decision_accuracy == 0.0
    assert explanation.calibrated_confidence == 0.0
    assert explanation.historical_acceptance == 0.0
    assert explanation.sample_size == 0
    assert explanation.reason == ""
    assert explanation.learning_sources == []


def test_extractor_selection_explanation_preserves_values() -> None:
    explanation = ExtractorSelectionExplanation(
        extractor="RentalAcquisitionExtractor",
        provider="JWB Capital",
        decision_accuracy=0.99,
        calibrated_confidence=0.96,
        historical_acceptance=0.98,
        sample_size=24,
        reason="Highest provider-aware confidence",
        learning_sources=[
            "feedback",
            "calibration",
            "performance",
        ],
    )

    assert explanation.provider == "JWB Capital"
    assert explanation.decision_accuracy == 0.99
    assert explanation.calibrated_confidence == 0.96
    assert explanation.historical_acceptance == 0.98
    assert explanation.sample_size == 24
    assert "feedback" in explanation.learning_sources
