from __future__ import annotations

from dataclasses import dataclass, field

from meridianforge.services.email_attachment_ingestion_service import (
    EmailAttachmentIngestionRequest,
)
from meridianforge.workflows.email_attachment_intake_workflow import (
    EmailAttachmentIntakeBatch,
)


@dataclass(frozen=True, slots=True)
class EmailArtifactIntakeRequest:
    message_id: str
    sender: str
    subject: str
    filename: str
    content_type: str | None = None
    size_bytes: int | None = None


@dataclass(frozen=True, slots=True)
class EmailArtifactIntakeBatch:
    message_id: str
    sender: str
    subject: str
    artifacts: list[EmailArtifactIntakeRequest] = field(default_factory=list)


class EmailArtifactIntakeService:
    """
    Convert email attachment intake batches into artifact-ready intake batches.
    """

    def build_artifact_batch(
        self,
        batch: EmailAttachmentIntakeBatch,
    ) -> EmailArtifactIntakeBatch:
        artifacts: list[EmailArtifactIntakeRequest] = []

        for request in batch.requests:
            artifacts.append(
                self._to_artifact_request(
                    request,
                )
            )

        return EmailArtifactIntakeBatch(
            message_id=batch.message_id,
            sender=batch.sender,
            subject=batch.subject,
            artifacts=artifacts,
        )

    def _to_artifact_request(
        self,
        request: EmailAttachmentIngestionRequest,
    ) -> EmailArtifactIntakeRequest:
        return EmailArtifactIntakeRequest(
            message_id=request.message_id,
            sender=request.sender,
            subject=request.subject,
            filename=request.filename,
            content_type=request.content_type,
            size_bytes=request.size_bytes,
        )
