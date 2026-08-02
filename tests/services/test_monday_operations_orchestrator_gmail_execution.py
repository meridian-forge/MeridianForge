from __future__ import annotations

from datetime import datetime

from meridianforge.services.monday_operations_orchestrator import (
    MondayOperationsOrchestrator,
)


def test_execute_gmail_messages_preserves_operations_boundary() -> None:
    orchestrator = MondayOperationsOrchestrator()

    result = orchestrator.execute_gmail_messages(
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

    assert result.artifacts_processed == 1
    assert result.routed_extractors == []
    assert result.extractor_decisions == []
    assert result.normalized_opportunities == []
    assert isinstance(result.audit_report, str)
