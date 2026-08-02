from __future__ import annotations

from meridianforge.services.email_artifact_intake_service import (
    EmailArtifactIntakeService,
)
from meridianforge.services.email_attachment_ingestion_service import (
    EmailAttachmentIngestionRequest,
)
from meridianforge.workflows.email_attachment_intake_workflow import (
    EmailAttachmentIntakeBatch,
)


def test_build_artifact_batch() -> None:
    service = EmailArtifactIntakeService()

    batch = EmailAttachmentIntakeBatch(
        message_id="gmail-123",
        sender="deals@example.com",
        subject="Investment Package",
        requests=[
            EmailAttachmentIngestionRequest(
                message_id="gmail-123",
                sender="deals@example.com",
                subject="Investment Package",
                filename="deal.pdf",
                content_type="application/pdf",
                size_bytes=1024,
            ),
            EmailAttachmentIngestionRequest(
                message_id="gmail-123",
                sender="deals@example.com",
                subject="Investment Package",
                filename="rent_roll.xlsx",
                content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                size_bytes=2048,
            ),
        ],
    )

    artifact_batch = service.build_artifact_batch(batch)

    assert artifact_batch.message_id == "gmail-123"
    assert artifact_batch.sender == "deals@example.com"
    assert artifact_batch.subject == "Investment Package"
    assert len(artifact_batch.artifacts) == 2
    assert artifact_batch.artifacts[0].filename == "deal.pdf"
    assert artifact_batch.artifacts[1].filename == "rent_roll.xlsx"
