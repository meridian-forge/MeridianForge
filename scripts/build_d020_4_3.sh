#!/bin/bash

set -e

echo "======================================"
echo "Meridian Forge D020.4.3"
echo "Property Content Extraction Engine"
echo "======================================"

PACKAGE="updates/packages/D020.4.3"

mkdir -p "$PACKAGE/files/src/meridianforge/models/domain"
mkdir -p "$PACKAGE/files/src/meridianforge/extractors"
mkdir -p "$PACKAGE/files/src/meridianforge/services"
mkdir -p "$PACKAGE/files/tests"


echo "Creating PropertyCandidate model..."

cat > "$PACKAGE/files/src/meridianforge/models/domain/property_candidate.py" <<'PY'
"""
Property candidate model.

Represents extracted investment information
before full underwriting.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class PropertyCandidate:
    """
    Extracted property information.
    """

    purchase_price: float = 0.0

    monthly_rent: float = 0.0

    taxes: float = 0.0

    insurance: float = 0.0

    bedrooms: int = 0

    bathrooms: float = 0.0

    location: str = ""

    confidence: float = 0.0
PY


echo "Creating property content extractor..."

cat > "$PACKAGE/files/src/meridianforge/extractors/property_content_extractor.py" <<'PY'
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
PY


echo "Creating extraction service..."

cat > "$PACKAGE/files/src/meridianforge/services/property_extraction_service.py" <<'PY'
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
PY


echo "Creating tests..."

cat > "$PACKAGE/files/tests/test_property_candidate.py" <<'PY'
from meridianforge.models.domain.property_candidate import (
    PropertyCandidate,
)


def test_property_candidate() -> None:

    candidate = PropertyCandidate(
        purchase_price=200000,
    )

    assert candidate.purchase_price == 200000
PY


cat > "$PACKAGE/files/tests/test_property_content_extractor.py" <<'PY'
from meridianforge.extractors.property_content_extractor import (
    PropertyContentExtractor,
)


def test_property_content_extractor() -> None:

    text = """
    3 bedroom rental.
    Purchase Price: $215,000
    Rent: $1,850
    Taxes: $2,400
    Insurance: $1,200
    """

    result = PropertyContentExtractor.extract(
        text,
    )

    assert result.purchase_price == 215000
    assert result.monthly_rent == 1850
    assert result.bedrooms == 3
PY


cat > "$PACKAGE/files/tests/test_property_extraction_service.py" <<'PY'
from meridianforge.services.property_extraction_service import (
    PropertyExtractionService,
)


def test_property_extraction_service() -> None:

    result = PropertyExtractionService.extract(
        "Price: $100000 Rent: $1200",
    )

    assert result.purchase_price == 100000
PY


echo "Creating manifest..."

cat > "$PACKAGE/manifest.txt" <<EOF
Meridian Forge Update Package

Name:
D020.4.3

Purpose:
Property Content Extraction Engine

Created:
$(date)

EOF


cat > "$PACKAGE/apply.sh" <<'EOF'
#!/bin/bash

echo "D020.4.3 deployment handled by update engine"
EOF


chmod +x "$PACKAGE/apply.sh"


echo
echo "Package created:"
echo "$PACKAGE"

