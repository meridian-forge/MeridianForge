"""
Opportunity routing service.

MF-512.2.2

Routes classified investment artifacts to the appropriate extraction
pipeline. This is the bridge between OpportunityIntakeService and the
specialized extractors that normalize opportunities for underwriting.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from meridianforge.extractors.rental_acquisition_extractor import (
    RentalAcquisitionExtractor,
    RentalAcquisitionRecord,
)
from meridianforge.models.opportunity import OpportunityType
from meridianforge.services.opportunity_intake_service import (
    IntakeArtifact,
)


@dataclass(frozen=True)
class RoutedOpportunity:
    """
    Result of routing a classified artifact.
    """

    source_file: Path
    opportunity_type: OpportunityType
    payload: object | None


class OpportunityRouter:
    """
    Route classified artifacts into specialized extraction pipelines.
    """

    def route(
        self,
        artifact: IntakeArtifact,
    ) -> RoutedOpportunity:
        opportunity_type = artifact.classification.opportunity_type

        if opportunity_type == OpportunityType.RENTAL_ACQUISITION:
            payload: RentalAcquisitionRecord | None = (
                RentalAcquisitionExtractor.extract(
                    artifact.extracted_text,
                    artifact.path,
                )
            )

            return RoutedOpportunity(
                source_file=artifact.path,
                opportunity_type=opportunity_type,
                payload=payload,
            )

        # MF-512.2.3
        # Inventory workbook extraction will be connected here.

        if opportunity_type == OpportunityType.INVENTORY_WORKBOOK:
            return RoutedOpportunity(
                source_file=artifact.path,
                opportunity_type=opportunity_type,
                payload=None,
            )

        # MF-512.2.4
        # Private lending extraction will be connected here.

        if opportunity_type == OpportunityType.PRIVATE_LENDING:
            return RoutedOpportunity(
                source_file=artifact.path,
                opportunity_type=opportunity_type,
                payload=None,
            )

        return RoutedOpportunity(
            source_file=artifact.path,
            opportunity_type=opportunity_type,
            payload=None,
        )
