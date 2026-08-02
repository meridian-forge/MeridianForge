from __future__ import annotations

from dataclasses import dataclass, field

from meridianforge.services.email_artifact_intake_service import (
    EmailArtifactIntakeBatch,
    EmailArtifactIntakeRequest,
)


@dataclass(frozen=True, slots=True)
class EmailRepositoryArtifact:
    artifact_id: str
    filename: str
    source: str
    metadata: dict[str, str] = field(default_factory=dict)


class EmailArtifactRepositoryService:
    """
    Bridge email artifact intake batches into repository-managed artifacts.
    """

    def persist_batch(
        self,
        batch: EmailArtifactIntakeBatch,
    ) -> list[EmailRepositoryArtifact]:
        artifacts: list[EmailRepositoryArtifact] = []

        for request in batch.artifacts:
            artifacts.append(self._persist_request(request))

        return artifacts

    def _persist_request(
        self,
        request: EmailArtifactIntakeRequest,
    ) -> EmailRepositoryArtifact:
        artifact_id = f"email:{request.message_id}:{request.filename}"

        return EmailRepositoryArtifact(
            artifact_id=artifact_id,
            filename=request.filename,
            source="email",
            metadata={
                "message_id": request.message_id,
                "sender": request.sender,
                "subject": request.subject,
            },
        )
