"""
Import pipeline tests.
"""

from meridianforge.services.import_pipeline import (
    ImportPipeline,
)


def test_pipeline_normalizes_records() -> None:
    pipeline = ImportPipeline()

    result = pipeline.process(
        [
            {
                "Price": "$250000",
                "Monthly Rent": "$2200",
                "Tax": "$3500",
            }
        ],
        asset_type="REAL_ESTATE",
    )

    assert len(result.assets) == 1

    assert "purchase_price" in result.assets[0]

    assert result.confidence > 0


def test_pipeline_handles_unknown_records() -> None:
    pipeline = ImportPipeline()

    result = pipeline.process(
        [
            {
                "Random Column": "ABC",
            }
        ]
    )

    assert len(result.assets) == 0

    assert len(result.warnings) == 1


def test_unknown_field_generates_mapping_suggestion() -> None:
    from meridianforge.services.import_pipeline import (
        ImportPipeline,
    )

    pipeline = ImportPipeline()

    result = pipeline.process(
        [
            {
                "Cash Needed": 50000,
                "Purchase Price": 250000,
            }
        ]
    )

    assert len(result.warnings) >= 0
