from meridianforge.services.adaptive_extractor_selector import (
    AdaptiveExtractorSelector,
)


def test_selector_returns_explanation() -> None:
    selector = AdaptiveExtractorSelector()

    explanation = selector.select_with_explanation(
        [
            "RentalAcquisitionExtractor",
        ],
        provider="JWB Capital",
    )

    assert explanation is not None
    assert explanation.extractor == "RentalAcquisitionExtractor"
    assert explanation.provider == "JWB Capital"
    assert explanation.reason != ""
