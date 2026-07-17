from meridianforge.services.acquisition_pipeline import (
    AcquisitionPipeline,
)


def test_acquisition_pipeline_returns_result() -> None:

    pipeline = AcquisitionPipeline()

    result = pipeline.process(
        assets=[
            {
                "address": "123 Main St",
            }
        ],
        confidence=0.9,
    )

    assert result.assets_analyzed == 1
    assert result.confidence == 0.9
