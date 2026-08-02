from __future__ import annotations

from datetime import datetime

from meridianforge.services.gmail_email_ingestion_service import (
    GmailEmailIngestionService,
)


def test_ingest_gmail_message() -> None:
    service = GmailEmailIngestionService()

    record = service.ingest(
        {
            "message_id": "gmail-123",
            "subject": "Investment Opportunity",
            "sender": "deals@example.com",
            "received_at": datetime(2026, 8, 3, 9, 0, 0),
            "body_preview": "Please review the attached deal package.",
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
    assert record.subject == "Investment Opportunity"
    assert record.sender == "deals@example.com"
    assert len(record.attachments) == 1
    assert record.attachments[0].filename == "deal.pdf"
