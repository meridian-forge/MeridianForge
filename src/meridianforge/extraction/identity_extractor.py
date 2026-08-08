"""
Identity extraction from evidence text.

Provider agnostic.

Converts OCR/source text into canonical
property identity fields.
"""

from __future__ import annotations

from dataclasses import dataclass
import re


@dataclass(frozen=True, slots=True)
class IdentityEvidence:
    """
    Canonical property identity extracted
    from source evidence.
    """

    address: str = ""
    city: str = ""
    state: str = ""
    zip_code: str = ""
    confidence: float = 0.0


class IdentityExtractor:
    """
    Extract property identity from OCR text.
    """

    ADDRESS_PATTERNS = [
        r"Property Address:\s*(.+)",
        r"Address:\s*(.+)",
    ]

    CITY_STATE_PATTERN = re.compile(
        r"([A-Za-z .]+),\s*([A-Z]{2})\s*(\d{5})"
    )

    @classmethod
    def extract(
        cls,
        text: str,
    ) -> IdentityEvidence:
        """
        Extract address components.
        """

        address = ""

        for pattern in cls.ADDRESS_PATTERNS:
            match = re.search(
                pattern,
                text,
                flags=re.IGNORECASE,
            )

            if match:
                address = match.group(1).strip()
                break

        if not address:
            return IdentityEvidence()

        cleaned = (
            address
            .replace(" Financed", "")
            .replace("financed", "")
            .strip()
        )

        match = cls.CITY_STATE_PATTERN.search(
            cleaned,
        )

        if not match:
            return IdentityEvidence(
                address=cleaned,
                confidence=0.70,
            )

        return IdentityEvidence(
            address=cleaned,
            city=match.group(1).strip(),
            state=match.group(2).strip(),
            zip_code=match.group(3).strip(),
            confidence=0.95,
        )
