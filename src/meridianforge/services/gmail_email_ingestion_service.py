from __future__ import annotations

from meridianforge.models.domain.email_ingestion_record import (
    EmailIngestionRecord,
)
from meridianforge.services.email_ingestion_service import (
    EmailIngestionService,
)


class GmailEmailIngestionService:
    """
    Adapter that converts Gmail connector messages into canonical
    EmailIngestionRecord objects.
    """

    def __init__(
        self,
        ingestion_service: EmailIngestionService | None = None,
    ) -> None:
        self._ingestion_service = ingestion_service or EmailIngestionService()

    def ingest(
        self,
        gmail_message: dict[str, object],
    ) -> EmailIngestionRecord:
        return self._ingestion_service.normalize(
            gmail_message,
        )
