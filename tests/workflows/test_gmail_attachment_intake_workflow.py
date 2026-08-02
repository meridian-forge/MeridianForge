from __future__ import annotations

from datetime import datetime

from meridianforge.workflows.gmail_attachment_intake_workflow import (
    GmailAttachmentIntakeWorkflow,
)


def test_process_gmail_message_to_attachment_batch() -> None:
    workflow = GmailAttachmentIntakeWorkflow()

    batch = workflow.process_message(
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
                },
                {
                    "filename": "rent_roll.xlsx",
                    "content_type": (
                        "application/"
                        "vnd.openxmlformats-officedocument."
                        "spreadsheetml.sheet"
                    ),
                    "size_bytes": 2048,
                },
            ],
        }
    )

    assert batch.message_id == "gmail-123"
    assert batch.sender == "deals@example.com"
    assert batch.subject == "Investment Package"
    assert len(batch.requests) == 2
    assert batch.requests[0].filename == "deal.pdf"
    assert batch.requests[1].filename == "rent_roll.xlsx"
