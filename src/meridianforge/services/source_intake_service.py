"""
Source intake service.

Creates normalized source documents
from external inputs.
"""

from meridianforge.models.domain.source_document import (
    SourceDocument,
)


class SourceIntakeService:
    """
    Handles external source ingestion.
    """

    @staticmethod
    def create(
        source_type: str,
        content: str,
        provider: str | None = None,
        attachments: list[str] | None = None,
    ) -> SourceDocument:
        """
        Create a source document.
        """

        return SourceDocument(
            source_type=source_type,
            content=content,
            provider=provider,
            attachments=attachments or [],
        )
