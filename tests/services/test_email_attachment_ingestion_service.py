from __future__ import annotations

from meridianforge.models.domain.email_ingestion_record import (
    EmailAttachmentRecord,
    EmailIngestionRecord,
)
from meridianforge.services.email_attachment_ingestion_service import (
    EmailAttachmentIngestionService,
)


def test_build_requests_from_email_attachments() -> None:
    service = EmailAttachmentIngestionService()

    email = EmailIngestionRecord(
        message_id="gmail-123",
        subject="New Deal",
        sender="deals@example.com",
        received_at=None,
        body_preview="See attached files",
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

    requests = service.build_requests(email)

    assert len(requests) == 2

    assert requests[0].filename == "deal.pdf"
    assert requests[0].message_id == "gmail-123"

    assert requests[1].filename == "rent_roll.xlsx"
    assert requests[1].sender == "deals@example.com"
