"""
Opportunity routing service.

MF-513.6

Routes classified opportunity artifacts to the preferred extractor,
using adaptive extractor selection when historical performance data is
available.
"""

from __future__ import annotations

from meridianforge.models.opportunity import OpportunityType
from meridianforge.services.adaptive_extractor_selector import (
    AdaptiveExtractorSelector,
)


class OpportunityRouter:
    """
    Route opportunity classifications to extractors.
    """

    def __init__(
        self,
        selector: AdaptiveExtractorSelector | None = None,
    ) -> None:
        self._selector = selector or AdaptiveExtractorSelector()

    def route(
        self,
        opportunity_type: OpportunityType,
    ) -> str:
        """
        Return the preferred extractor for an opportunity type.
        """

        if opportunity_type is OpportunityType.RENTAL_ACQUISITION:
            candidates = [
                "RentalAcquisitionExtractor",
                "AlternativeRentalExtractor",
            ]

            selected = self._selector.select(
                candidates,
            )

            return selected or "RentalAcquisitionExtractor"

        if opportunity_type is OpportunityType.INVENTORY_WORKBOOK:
            return "InventoryWorkbookExtractor"

        if opportunity_type is OpportunityType.PRIVATE_LENDING:
            return "PrivateLendingExtractor"

        return "GenericDocumentExtractor"
