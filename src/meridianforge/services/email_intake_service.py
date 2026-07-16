"""
Email intake service.

Application layer wrapper for email extraction.
"""

from meridianforge.extractors.email_extractor import (
    EmailExtractor,
)
from meridianforge.models.domain.source_document import (
    SourceDocument,
)


class EmailIntakeService:
    """
    Handles email ingestion.
    """

    @staticmethod
    def ingest(
        sender: str,
        subject: str,
        body: str,
        attachments: list[str] | None = None,
    ) -> SourceDocument:
        """
        Convert email into source document.
        """

        return EmailExtractor.extract(
            sender,
            subject,
            body,
            attachments,
        )
