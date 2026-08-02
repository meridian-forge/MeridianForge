from __future__ import annotations

from meridianforge.services.email_artifact_intake_service import (
    EmailArtifactIntakeService,
)
from meridianforge.services.email_artifact_repository_service import (
    EmailArtifactRepositoryService,
    EmailRepositoryArtifact,
)
from meridianforge.workflows.gmail_attachment_intake_workflow import (
    GmailAttachmentIntakeWorkflow,
)


class GmailArtifactRepositoryWorkflow:
    """
    End-to-end workflow from Gmail connector message to
    repository-managed email artifacts.
    """

    def __init__(
        self,
        gmail_workflow: GmailAttachmentIntakeWorkflow | None = None,
        artifact_intake: EmailArtifactIntakeService | None = None,
        repository_service: EmailArtifactRepositoryService | None = None,
    ) -> None:
        self._gmail_workflow = gmail_workflow or GmailAttachmentIntakeWorkflow()
        self._artifact_intake = artifact_intake or EmailArtifactIntakeService()
        self._repository_service = (
            repository_service or EmailArtifactRepositoryService()
        )

    def process_message(
        self,
        gmail_message: dict[str, object],
    ) -> list[EmailRepositoryArtifact]:
        attachment_batch = self._gmail_workflow.process_message(
            gmail_message,
        )

        artifact_batch = self._artifact_intake.build_artifact_batch(
            attachment_batch,
        )

        return self._repository_service.persist_batch(
            artifact_batch,
        )
