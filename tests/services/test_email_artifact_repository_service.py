from __future__ import annotations

from meridianforge.services.email_artifact_intake_service import (
    EmailArtifactIntakeBatch,
    EmailArtifactIntakeRequest,
)
from meridianforge.services.email_artifact_repository_service import (
    EmailArtifactRepositoryService,
)


def test_persist_batch_creates_repository_artifacts() -> None:
    service = EmailArtifactRepositoryService()

    batch = EmailArtifactIntakeBatch(
        message_id="gmail-123",
        sender="deals@example.com",
        subject="Investment Package",
        artifacts=[
            EmailArtifactIntakeRequest(
                message_id="gmail-123",
                sender="deals@example.com",
                subject="Investment Package",
                filename="deal.pdf",
            ),
            EmailArtifactIntakeRequest(
                message_id="gmail-123",
                sender="deals@example.com",
                subject="Investment Package",
                filename="rent_roll.xlsx",
            ),
        ],
    )

    artifacts = service.persist_batch(batch)

    assert len(artifacts) == 2
    assert artifacts[0].artifact_id == "email:gmail-123:deal.pdf"
    assert artifacts[0].source == "email"
    assert artifacts[0].metadata["sender"] == "deals@example.com"
    assert artifacts[1].artifact_id == "email:gmail-123:rent_roll.xlsx"
