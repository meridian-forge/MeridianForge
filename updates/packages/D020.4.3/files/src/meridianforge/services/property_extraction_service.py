"""
Property extraction service.

Application wrapper around content extraction.
"""

from meridianforge.extractors.property_content_extractor import (
    PropertyContentExtractor,
)
from meridianforge.models.domain.property_candidate import (
    PropertyCandidate,
)


class PropertyExtractionService:
    """
    Extracts property candidates.
    """

    @staticmethod
    def extract(
        content: str,
    ) -> PropertyCandidate:
        """
        Extract property information.
        """

        return PropertyContentExtractor.extract(
            content,
        )
