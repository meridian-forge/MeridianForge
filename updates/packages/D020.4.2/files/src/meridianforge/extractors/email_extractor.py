"""
Email extractor.

Converts email content into
Meridian Forge source documents.
"""

from meridianforge.models.domain.source_document import (
    SourceDocument,
)


class EmailExtractor:
    """
    Extracts information from emails.
    """

    @staticmethod
    def extract(
        sender: str,
        subject: str,
        body: str,
        attachments: list[str] | None = None,
    ) -> SourceDocument:
        """
        Create SourceDocument from email.
        """

        return SourceDocument(
            source_type="EMAIL",
            provider=sender,
            content=body,
            attachments=attachments or [],
            metadata={
                "sender": sender,
                "subject": subject,
            },
        )
