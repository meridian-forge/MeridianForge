from __future__ import annotations

from datetime import datetime

from meridianforge.services.monday_operations_orchestrator_gmail import (
    MondayOperationsOrchestratorGmail,
)


def test_run_gmail_ingestion_returns_extraction_batches() -> None:
    orchestrator = MondayOperationsOrchestratorGmail()

    result = orchestrator.run_gmail_ingestion(
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
    assert result.extraction_batches[0].artifacts[0].provider == "deals@example.com"
