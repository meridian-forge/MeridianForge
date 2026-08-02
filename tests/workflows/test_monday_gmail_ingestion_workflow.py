from __future__ import annotations

from datetime import datetime

from meridianforge.workflows.monday_gmail_ingestion_workflow import (
    MondayGmailIngestionWorkflow,
)


def test_process_multiple_gmail_messages() -> None:
    workflow = MondayGmailIngestionWorkflow()

    result = workflow.process_messages(
        [
            {
                "message_id": "gmail-1",
                "subject": "Deal One",
                "sender": "jwb@example.com",
                "received_at": datetime(2026, 8, 3, 9, 0, 0),
                "body_preview": "Package attached.",
                "attachments": [
                    {
                        "filename": "deal1.pdf",
                        "content_type": "application/pdf",
                        "size_bytes": 1000,
                    }
                ],
            },
            {
                "message_id": "gmail-2",
                "subject": "Deal Two",
                "sender": "rent@example.com",
                "received_at": datetime(2026, 8, 3, 10, 0, 0),
                "body_preview": "Spreadsheet attached.",
                "attachments": [
                    {
                        "filename": "rent_roll.xlsx",
                        "content_type": (
                            "application/"
                            "vnd.openxmlformats-officedocument."
                            "spreadsheetml.sheet"
                        ),
                        "size_bytes": 2000,
                    }
                ],
            },
        ]
    )

    assert result.processed_messages == 2
    assert len(result.extraction_batches) == 2
    assert (
        result.extraction_batches[0].artifacts[0].artifact_id
        == "email:gmail-1:deal1.pdf"
    )
    assert result.extraction_batches[1].artifacts[0].provider == "rent@example.com"
