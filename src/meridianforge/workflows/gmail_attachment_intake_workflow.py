from __future__ import annotations

from meridianforge.services.gmail_email_ingestion_service import (
    GmailEmailIngestionService,
)
from meridianforge.workflows.email_attachment_intake_workflow import (
    EmailAttachmentIntakeBatch,
    EmailAttachmentIntakeWorkflow,
)


class GmailAttachmentIntakeWorkflow:
    """
    End-to-end workflow from Gmail connector message to
    EmailAttachmentIntakeBatch.
    """

    def __init__(
        self,
        gmail_ingestion: GmailEmailIngestionService | None = None,
        attachment_workflow: EmailAttachmentIntakeWorkflow | None = None,
    ) -> None:
        self._gmail_ingestion = gmail_ingestion or GmailEmailIngestionService()
        self._attachment_workflow = (
            attachment_workflow or EmailAttachmentIntakeWorkflow()
        )

    def process_message(
        self,
        gmail_message: dict[str, object],
    ) -> EmailAttachmentIntakeBatch:
        email = self._gmail_ingestion.ingest(
            gmail_message,
        )

        return self._attachment_workflow.build_batch(
            email,
        )
