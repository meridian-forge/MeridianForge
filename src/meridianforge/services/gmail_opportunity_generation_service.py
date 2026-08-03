from __future__ import annotations

from dataclasses import dataclass, field

from meridianforge.services.gmail_acquisition_bridge_service import (
    GmailAcquisitionBridgeService,
)
from meridianforge.workflows.email_artifact_extraction_workflow import (
    EmailExtractionBatch,
)


@dataclass(frozen=True, slots=True)
class GmailGeneratedOpportunity:
    artifact_id: str
    provider: str | None
    source: str = "gmail"


@dataclass(frozen=True, slots=True)
class GmailOpportunityGenerationResult:
    opportunities: list[GmailGeneratedOpportunity] = field(default_factory=list)


class GmailOpportunityGenerationService:
    """
    Generate acquisition opportunities from Gmail extraction batches.

    SP-480.2
    """

    def __init__(
        self,
        bridge: GmailAcquisitionBridgeService | None = None,
    ) -> None:
        self._bridge = bridge or GmailAcquisitionBridgeService()

    def generate(
        self,
        extraction_batch: EmailExtractionBatch,
    ) -> GmailOpportunityGenerationResult:
        acquisition_batch = self._bridge.build_batch(
            extraction_batch,
        )

        opportunities = [
            GmailGeneratedOpportunity(
                artifact_id=opportunity.artifact_id,
                provider=opportunity.provider,
                source=opportunity.source,
            )
            for opportunity in acquisition_batch.opportunities
        ]

        return GmailOpportunityGenerationResult(
            opportunities=opportunities,
        )
