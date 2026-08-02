from __future__ import annotations

from dataclasses import dataclass, field

from meridianforge.models.domain.email_ingestion_record import (
    EmailIngestionRecord,
)
from meridianforge.services.email_attachment_ingestion_service import (
    EmailAttachmentIngestionRequest,
    EmailAttachmentIngestionService,
)


@dataclass(frozen=True, slots=True)
class EmailAttachmentIntakeBatch:
    message_id: str
    sender: str
    subject: str
    requests: list[EmailAttachmentIngestionRequest] = field(default_factory=list)


class EmailAttachmentIntakeWorkflow:
    """
    Convert a normalized email into an artifact-ready intake batch.
    """

    def __init__(
        self,
        attachment_service: EmailAttachmentIngestionService | None = None,
    ) -> None:
        self._attachment_service = (
            attachment_service or EmailAttachmentIngestionService()
        )

    def build_batch(
        self,
        email: EmailIngestionRecord,
    ) -> EmailAttachmentIntakeBatch:
        requests = self._attachment_service.build_requests(
            email,
        )

        return EmailAttachmentIntakeBatch(
            message_id=email.message_id,
            sender=email.sender,
            subject=email.subject,
            requests=requests,
        )
