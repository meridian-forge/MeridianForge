from __future__ import annotations

from datetime import datetime

from meridianforge.workflows.monday_operations_gmail_adapter import (
    MondayOperationsGmailAdapter,
)


def test_ingest_gmail_messages_returns_extraction_batches() -> None:
    adapter = MondayOperationsGmailAdapter()

    result = adapter.ingest_gmail_messages(
        [
            {
                "message_id": "gmail-123",
                "subject": "Investment Package",
                "sender": "deals@example.com",
                "received_at": datetime(2026, 8, 3, 9, 0, 0),
                "body_preview": "Please review the attached files.",
                "attachments": [
                    {
                        "filename": "deal.pdf",
                        "content_type": "application/pdf",
                        "size_bytes": 1024,
                    }
                ],
            }
        ]
    )

    assert result.processed_messages == 1
    assert len(result.extraction_batches) == 1
    assert (
        result.extraction_batches[0].artifacts[0].artifact_id
        == "email:gmail-123:deal.pdf"
    )
