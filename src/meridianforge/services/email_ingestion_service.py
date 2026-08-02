from __future__ import annotations

from datetime import datetime

from meridianforge.models.domain.email_ingestion_record import (
    EmailAttachmentRecord,
    EmailIngestionRecord,
)


class EmailIngestionService:
    """
    Normalize connector-specific email objects into a canonical ingestion record.
    """

    def normalize(
        self,
        message: dict[str, object],
    ) -> EmailIngestionRecord:
        attachments: list[EmailAttachmentRecord] = []

        raw_attachments = message.get("attachments")

        if isinstance(raw_attachments, list):
            for attachment in raw_attachments:
                if not isinstance(attachment, dict):
                    continue

                filename = attachment.get("filename")
                content_type = attachment.get("content_type")
                size_value = attachment.get("size_bytes")

                size_bytes: int | None = (
                    size_value if isinstance(size_value, int) else None
                )

                attachments.append(
                    EmailAttachmentRecord(
                        filename=str(filename or ""),
                        content_type=(
                            str(content_type) if content_type is not None else None
                        ),
                        size_bytes=size_bytes,
                    )
                )

        received = message.get("received_at")
        received_at: datetime | None

        if isinstance(received, datetime):
            received_at = received
        else:
            received_at = None

        return EmailIngestionRecord(
            message_id=str(message.get("message_id", "")),
            subject=str(message.get("subject", "")),
            sender=str(message.get("sender", "")),
            received_at=received_at,
            body_preview=str(message.get("body_preview", "")),
            attachments=attachments,
        )
