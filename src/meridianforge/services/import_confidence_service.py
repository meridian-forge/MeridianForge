"""
Import confidence service.

Builds mapping confidence summaries
from detected field mappings.
"""

from meridianforge.models.results.import_mapping_result import (
    ImportMappingResult,
)
from meridianforge.models.results.import_quality_report import (
    ImportQualityReport,
)
from meridianforge.models.results.import_warning import (
    ImportWarning,
)


class ImportConfidenceService:
    """
    Evaluates import quality and confidence.
    """

    @staticmethod
    def generate(
        records_received: int,
        mappings: list[ImportMappingResult],
        unknown_fields: list[str] | None = None,
    ) -> ImportQualityReport:
        """
        Generate import quality report.
        """

        unknown_fields = unknown_fields or []

        confidence = (
            sum(item.confidence for item in mappings) / len(mappings)
            if mappings
            else 0.0
        )

        recognized_fields = [
            item.mapped_field for item in mappings if item.mapped_field is not None
        ]

        warnings: list[ImportWarning] = []

        for field_name in unknown_fields:
            warnings.append(
                ImportWarning(
                    field_name=field_name,
                    message="Field could not be mapped.",
                    confidence=0.0,
                )
            )

        return ImportQualityReport(
            records_received=records_received,
            records_processed=records_received,
            confidence=confidence,
            recognized_fields=recognized_fields,
            unknown_fields=unknown_fields,
            mapping_results=mappings,
            warnings=warnings,
        )
