"""
Property content extractor.

Extracts common real estate fields
from unstructured text.
"""

import re

from meridianforge.models.domain.property_candidate import (
    PropertyCandidate,
)


class PropertyContentExtractor:
    """
    Extracts property data from text.
    """

    @staticmethod
    def _money(
        pattern: str,
        text: str,
    ) -> float:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE,
        )

        if not match:
            return 0.0

        value = (
            match.group(1)
            .replace("$", "")
            .replace(",", "")
        )

        return float(value)


    @staticmethod
    def extract(
        content: str,
    ) -> PropertyCandidate:
        """
        Extract property candidate.
        """

        purchase_price = PropertyContentExtractor._money(
            r"(?:purchase price|price)[:\s]+\$?([\d,]+)",
            content,
        )

        rent = PropertyContentExtractor._money(
            r"(?:monthly rent|rent)[:\s]+\$?([\d,]+)",
            content,
        )

        taxes = PropertyContentExtractor._money(
            r"(?:taxes|property tax)[:\s]+\$?([\d,]+)",
            content,
        )

        insurance = PropertyContentExtractor._money(
            r"(?:insurance)[:\s]+\$?([\d,]+)",
            content,
        )

        bedrooms = 0

        bedroom_match = re.search(
            r"(\d+)\s*(?:bed|bedroom)",
            content,
            re.IGNORECASE,
        )

        if bedroom_match:
            bedrooms = int(
                bedroom_match.group(1)
            )

        confidence = 0.0

        fields = [
            purchase_price,
            rent,
            taxes,
            insurance,
        ]

        confidence = (
            sum(
                1 for field in fields if field > 0
            )
            / len(fields)
        )

        return PropertyCandidate(
            purchase_price=purchase_price,
            monthly_rent=rent,
            taxes=taxes,
            insurance=insurance,
            bedrooms=bedrooms,
            confidence=confidence,
        )
