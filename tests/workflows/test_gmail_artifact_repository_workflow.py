from __future__ import annotations

from datetime import datetime

from meridianforge.workflows.gmail_artifact_repository_workflow import (
    GmailArtifactRepositoryWorkflow,
)


def test_process_gmail_message_to_repository_artifacts() -> None:
    workflow = GmailArtifactRepositoryWorkflow()

    artifacts = workflow.process_message(
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

    assert len(artifacts) == 2
    assert artifacts[0].artifact_id == "email:gmail-123:deal.pdf"
    assert artifacts[0].source == "email"
    assert artifacts[1].artifact_id == "email:gmail-123:rent_roll.xlsx"
