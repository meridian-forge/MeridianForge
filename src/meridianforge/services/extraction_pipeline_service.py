"""
Extraction pipeline service.

SP-430.4.1

Connects routed opportunity artifacts to specialized extractors and
normalizes extracted records into MeridianForge opportunity models.
"""

from __future__ import annotations

from pathlib import Path

from meridianforge.extractors.rental_acquisition_extractor import (
    RentalAcquisitionExtractor,
)
from meridianforge.services.extraction_audit_service import (
    ExtractionAuditService,
)
from meridianforge.services.opportunity_intake_service import (
    IntakeArtifact,
)
from meridianforge.services.opportunity_mapper import (
    NormalizedRentalOpportunity,
    OpportunityMapper,
)


class ExtractionPipelineService:
    """
    Execute extraction and normalization for routed artifacts.
    """

    def __init__(
        self,
        audit_service: ExtractionAuditService | None = None,
    ) -> None:
        self._audit = audit_service or ExtractionAuditService()

    def process(
        self,
        artifact: IntakeArtifact,
        extractor_name: str,
    ) -> NormalizedRentalOpportunity | None:
        """
        Execute the selected extractor and normalize the result.
        """

        if extractor_name == "RentalAcquisitionExtractor":
            record = RentalAcquisitionExtractor.extract(
                text=artifact.extracted_text,
                source_file=Path(artifact.path),
            )

            if record is None:
                return None

            return OpportunityMapper.from_rental_record(
                record=record,
                audit_service=self._audit,
            )

        return None
