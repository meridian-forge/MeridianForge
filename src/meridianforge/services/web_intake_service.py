"""
Web intake service.

Application wrapper for web ingestion.
"""

from meridianforge.extractors.web_content_extractor import (
    WebContentExtractor,
)
from meridianforge.models.domain.source_document import (
    SourceDocument,
)


class WebIntakeService:
    """
    Handles webpage ingestion.
    """

    @staticmethod
    def ingest(
        url: str,
        content: str,
    ) -> SourceDocument:
        """
        Convert webpage into source document.
        """

        return WebContentExtractor.extract(
            url,
            content,
        )
