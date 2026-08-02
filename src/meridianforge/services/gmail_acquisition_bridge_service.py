from __future__ import annotations

from dataclasses import dataclass, field

from meridianforge.workflows.email_artifact_extraction_workflow import (
    EmailExtractionBatch,
)


@dataclass(frozen=True, slots=True)
class GmailAcquisitionOpportunity:
    artifact_id: str
    provider: str | None
    source: str = "gmail"


@dataclass(frozen=True, slots=True)
class GmailAcquisitionBatch:
    opportunities: list[GmailAcquisitionOpportunity] = field(default_factory=list)


class GmailAcquisitionBridgeService:
    """
    Convert Gmail extraction batches into acquisition-ready opportunities.
    This is a bridge layer; the real acquisition pipeline remains unchanged.
    """

    def build_batch(
        self,
        extraction_batch: EmailExtractionBatch,
    ) -> GmailAcquisitionBatch:
        opportunities: list[GmailAcquisitionOpportunity] = []

        for artifact in extraction_batch.artifacts:
            opportunities.append(
                GmailAcquisitionOpportunity(
                    artifact_id=artifact.artifact_id,
                    provider=artifact.provider,
                )
            )

        return GmailAcquisitionBatch(
            opportunities=opportunities,
        )
