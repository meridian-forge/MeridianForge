from __future__ import annotations

from dataclasses import dataclass

from meridianforge.services.gmail_acquisition_bridge_service import (
    GmailAcquisitionBatch,
    GmailAcquisitionBridgeService,
)
from meridianforge.workflows.email_artifact_extraction_workflow import (
    EmailExtractionBatch,
)


@dataclass(frozen=True, slots=True)
class GmailAcquisitionExecutionResult:
    analyzed_opportunities: int
    source: str = "gmail"


class GmailAcquisitionExecutionService:
    """
    Execute acquisition analysis for Gmail-derived opportunities.

    This bridges Gmail extraction batches into the existing acquisition
    execution boundary while preserving the production pipeline.
    """

    def __init__(
        self,
        bridge: GmailAcquisitionBridgeService | None = None,
    ) -> None:
        self._bridge = bridge or GmailAcquisitionBridgeService()

    def execute(
        self,
        extraction_batch: EmailExtractionBatch,
    ) -> GmailAcquisitionExecutionResult:
        acquisition_batch: GmailAcquisitionBatch = self._bridge.build_batch(
            extraction_batch,
        )

        return GmailAcquisitionExecutionResult(
            analyzed_opportunities=len(acquisition_batch.opportunities),
        )
