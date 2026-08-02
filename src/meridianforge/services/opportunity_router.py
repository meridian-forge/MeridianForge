"""
Opportunity routing service.

MF-513.6 / MF-440.1 / MF-440.8.4

Routes classified opportunities to extractors.
Provides explainable routing intelligence while preserving backward
compatibility with legacy selector implementations.
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

        Maintains backward compatibility.
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

        candidates = self._candidates_for(
            opportunity_type,
        )

        if hasattr(
            self._selector,
            "select_with_explanation",
        ):
            decision = self._selector.select_with_explanation(
                candidates,
                provider=provider,
            )

            selected = decision.extractor if decision else candidates[0]

            historical_confidence = decision.calibrated_confidence if decision else 0.0

            selection_reason = decision.reason if decision else ""

            learning_sources = decision.learning_sources if decision else []

        else:
            selected = (
                self._selector.select(
                    candidates,
                    provider=provider,
                )
                or candidates[0]
            )

            historical_confidence = 0.0
            selection_reason = "Legacy selector fallback used."
            learning_sources = []

        return ExtractorDecisionContext(
            opportunity_type=opportunity_type.value,
            selected_extractor=(selected or candidates[0]),
            candidate_extractors=candidates,
            historical_confidence=historical_confidence,
            provider=provider,
            selection_reason=selection_reason,
            confidence_score=historical_confidence,
            learning_sources=learning_sources,
        )

    def _candidates_for(
        self,
        opportunity_type: OpportunityType,
    ) -> list[str]:
        if opportunity_type is OpportunityType.RENTAL_ACQUISITION:
            return [
                "RentalAcquisitionExtractor",
                "AlternativeRentalExtractor",
            ]

        if opportunity_type is OpportunityType.INVENTORY_WORKBOOK:
            return [
                "InventoryWorkbookExtractor",
            ]

        if opportunity_type is OpportunityType.PRIVATE_LENDING:
            return [
                "PrivateLendingExtractor",
            ]

        return [
            "GenericDocumentExtractor",
        ]
