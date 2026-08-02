from __future__ import annotations

from meridianforge.models.domain.email_ingestion_record import (
    EmailAttachmentRecord,
    EmailIngestionRecord,
)
from meridianforge.workflows.email_attachment_intake_workflow import (
    EmailAttachmentIntakeWorkflow,
)


def test_build_batch_from_email() -> None:
    workflow = EmailAttachmentIntakeWorkflow()

    email = EmailIngestionRecord(
        message_id="gmail-123",
        subject="Investment Package",
        sender="deals@example.com",
        received_at=None,
        body_preview="Please review the attached package.",
        attachments=[
            EmailAttachmentRecord(
                filename="deal.pdf",
                content_type="application/pdf",
                size_bytes=1024,
            ),
            EmailAttachmentRecord(
                filename="rent_roll.xlsx",
                content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                size_bytes=2048,
            ),
        ],
    )

    batch = workflow.build_batch(email)

    assert batch.message_id == "gmail-123"
    assert batch.sender == "deals@example.com"
    assert batch.subject == "Investment Package"
    assert len(batch.requests) == 2
    assert batch.requests[0].filename == "deal.pdf"
    assert batch.requests[1].filename == "rent_roll.xlsx"
