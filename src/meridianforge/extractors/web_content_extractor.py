"""
Web content extractor.

Converts webpage content into
Meridian Forge source documents.
"""

from urllib.parse import urlparse

from meridianforge.models.domain.source_document import (
    SourceDocument,
)


class WebContentExtractor:
    """
    Extracts source documents from web content.
    """

    @staticmethod
    def extract(
        url: str,
        content: str,
    ) -> SourceDocument:
        """
        Create SourceDocument from webpage content.
        """

        domain = urlparse(url).netloc

        return SourceDocument(
            source_type="WEB",
            provider=domain,
            content=content,
            metadata={
                "url": url,
            },
        )
