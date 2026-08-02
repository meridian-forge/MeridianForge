from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True, slots=True)
class EmailAttachmentRecord:
    filename: str
    content_type: str | None = None
    size_bytes: int | None = None


@dataclass(frozen=True, slots=True)
class EmailIngestionRecord:
    message_id: str
    subject: str
    sender: str
    received_at: datetime | None
    body_preview: str
    attachments: list[EmailAttachmentRecord] = field(default_factory=list)
