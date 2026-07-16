"""
Import confidence service tests.
"""

from meridianforge.models.results.import_mapping_result import (
    ImportMappingResult,
)
from meridianforge.services.import_confidence_service import (
    ImportConfidenceService,
)


def test_import_confidence_generation() -> None:

    mappings = [
        ImportMappingResult(
            source_field="Purchase Cost",
            mapped_field="purchase_price",
            confidence=0.98,
        ),
        ImportMappingResult(
            source_field="Rent",
            mapped_field="monthly_rent",
            confidence=0.94,
        ),
    ]

    report = ImportConfidenceService.generate(
        records_received=1,
        mappings=mappings,
    )

    assert report.confidence == 0.96

    assert report.mapped_fields_count == 2

    assert report.unknown_fields == []


def test_unknown_fields_create_warning() -> None:

    report = ImportConfidenceService.generate(
        records_received=1,
        mappings=[],
        unknown_fields=["Solar Lease"],
    )

    assert len(report.warnings) == 1

    assert report.unknown_fields == ["Solar Lease"]
