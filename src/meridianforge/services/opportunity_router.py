"""
Opportunity routing service.

MF-513.6 / MF-440.1 / MF-440.5.3

Routes classified opportunities to extractors.
Provides intelligence context including provider-aware learning.
"""

from __future__ import annotations

from meridianforge.models.domain.extractor_decision_context import (
    ExtractorDecisionContext,
)
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
        provider: str | None = None,
    ) -> str:
        """
        Return extractor name.

        Maintains backward compatibility while allowing
        provider-aware routing.
        """

        return self.route_with_context(
            opportunity_type,
            provider=provider,
        ).selected_extractor

    def route_with_context(
        self,
        opportunity_type: OpportunityType,
        provider: str | None = None,
    ) -> ExtractorDecisionContext:
        """
        Return extractor selection intelligence.
        """

        candidates: list[str]

        if opportunity_type is OpportunityType.RENTAL_ACQUISITION:
            candidates = [
                "RentalAcquisitionExtractor",
                "AlternativeRentalExtractor",
            ]

        elif opportunity_type is OpportunityType.INVENTORY_WORKBOOK:
            candidates = [
                "InventoryWorkbookExtractor",
            ]

        elif opportunity_type is OpportunityType.PRIVATE_LENDING:
            candidates = [
                "PrivateLendingExtractor",
            ]

        else:
            candidates = [
                "GenericDocumentExtractor",
            ]

        selected = self._selector.select(
            candidates,
            provider=provider,
        )

        return ExtractorDecisionContext(
            opportunity_type=opportunity_type.value,
            selected_extractor=(selected or candidates[0]),
            candidate_extractors=candidates,
            historical_confidence=0.0,
            provider=provider,
        )
