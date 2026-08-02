from __future__ import annotations

from dataclasses import dataclass

from meridianforge.models.domain.email_ingestion_record import (
    EmailIngestionRecord,
)


@dataclass(frozen=True, slots=True)
class EmailAttachmentIngestionRequest:
    message_id: str
    sender: str
    subject: str
    filename: str
    content_type: str | None = None
    size_bytes: int | None = None


class EmailAttachmentIngestionService:
    """
    Convert normalized email attachments into artifact ingestion requests.
    """

    def build_requests(
        self,
        email: EmailIngestionRecord,
    ) -> list[EmailAttachmentIngestionRequest]:
        requests: list[EmailAttachmentIngestionRequest] = []

        for attachment in email.attachments:
            requests.append(
                EmailAttachmentIngestionRequest(
                    message_id=email.message_id,
                    sender=email.sender,
                    subject=email.subject,
                    filename=attachment.filename,
                    content_type=attachment.content_type,
                    size_bytes=attachment.size_bytes,
                )
            )

        return requests
