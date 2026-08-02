from __future__ import annotations

from datetime import datetime

from meridianforge.services.email_ingestion_service import (
    EmailIngestionService,
)


def test_normalize_gmail_message() -> None:
    service = EmailIngestionService()

    record = service.normalize(
        {
            "message_id": "gmail-123",
            "subject": "New Investment Opportunity",
            "sender": "deals@example.com",
            "received_at": datetime(2026, 8, 2, 9, 0, 0),
            "body_preview": "Please review the attached property...",
            "attachments": [
                {
                    "filename": "deal.pdf",
                    "content_type": "application/pdf",
                    "size_bytes": 1024,
                }
            ],
        }
    )

    assert record.message_id == "gmail-123"
    assert record.subject == "New Investment Opportunity"
    assert record.sender == "deals@example.com"
    assert record.received_at is not None
    assert len(record.attachments) == 1
    assert record.attachments[0].filename == "deal.pdf"
