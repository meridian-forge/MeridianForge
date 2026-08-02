from __future__ import annotations

from meridianforge.services.email_artifact_repository_service import (
    EmailRepositoryArtifact,
)
from meridianforge.workflows.email_artifact_extraction_workflow import (
    EmailArtifactExtractionWorkflow,
)


def test_build_extraction_batch() -> None:
    workflow = EmailArtifactExtractionWorkflow()

    artifacts = [
        EmailRepositoryArtifact(
            artifact_id="email:gmail-123:deal.pdf",
            filename="deal.pdf",
            source="email",
            metadata={
                "message_id": "gmail-123",
                "sender": "deals@example.com",
                "subject": "Investment Package",
            },
        ),
        EmailRepositoryArtifact(
            artifact_id="email:gmail-123:rent_roll.xlsx",
            filename="rent_roll.xlsx",
            source="email",
            metadata={
                "message_id": "gmail-123",
                "sender": "deals@example.com",
                "subject": "Investment Package",
            },
        ),
    ]

    batch = workflow.build_extraction_batch(artifacts)

    assert len(batch.artifacts) == 2
    assert batch.artifacts[0].artifact_id == "email:gmail-123:deal.pdf"
    assert batch.artifacts[0].provider == "deals@example.com"
    assert batch.artifacts[1].filename == "rent_roll.xlsx"
