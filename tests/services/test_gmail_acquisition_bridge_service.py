from __future__ import annotations

from meridianforge.services.gmail_acquisition_bridge_service import (
    GmailAcquisitionBridgeService,
)
from meridianforge.workflows.email_artifact_extraction_workflow import (
    EmailExtractionArtifact,
    EmailExtractionBatch,
)


def test_build_batch_from_extraction_batch() -> None:
    service = GmailAcquisitionBridgeService()

    batch = EmailExtractionBatch(
        artifacts=[
            EmailExtractionArtifact(
                artifact_id="email:gmail-123:deal.pdf",
                filename="deal.pdf",
                source="email",
                provider="deals@example.com",
            )
        ]
    )

    acquisition_batch = service.build_batch(batch)

    assert len(acquisition_batch.opportunities) == 1
    assert acquisition_batch.opportunities[0].artifact_id == "email:gmail-123:deal.pdf"
    assert acquisition_batch.opportunities[0].provider == "deals@example.com"
