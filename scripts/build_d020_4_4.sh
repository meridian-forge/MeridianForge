#!/bin/bash

set -e

echo "======================================"
echo "Meridian Forge D020.4.4"
echo "Web Content Analyzer Foundation"
echo "======================================"

PACKAGE="updates/packages/D020.4.4"

mkdir -p "$PACKAGE/files/src/meridianforge/extractors"
mkdir -p "$PACKAGE/files/src/meridianforge/services"
mkdir -p "$PACKAGE/files/tests"


echo "Creating web content extractor..."

cat > "$PACKAGE/files/src/meridianforge/extractors/web_content_extractor.py" <<'PY'
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
PY


echo "Creating web intake service..."

cat > "$PACKAGE/files/src/meridianforge/services/web_intake_service.py" <<'PY'
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
PY


echo "Creating tests..."

cat > "$PACKAGE/files/tests/test_web_content_extractor.py" <<'PY'
from meridianforge.extractors.web_content_extractor import (
    WebContentExtractor,
)


def test_web_content_extractor() -> None:

    document = WebContentExtractor.extract(
        "https://jwb.com/property/123",
        "Jacksonville rental $215000",
    )

    assert document.source_type == "WEB"
    assert document.provider == "jwb.com"
PY


cat > "$PACKAGE/files/tests/test_web_intake_service.py" <<'PY'
from meridianforge.services.web_intake_service import (
    WebIntakeService,
)


def test_web_intake_service() -> None:

    document = WebIntakeService.ingest(
        "https://example.com/listing",
        "Property details",
    )

    assert document.metadata["url"] == (
        "https://example.com/listing"
    )
PY


echo "Creating manifest..."

cat > "$PACKAGE/manifest.txt" <<EOF
Meridian Forge Update Package

Name:
D020.4.4

Purpose:
Web Content Analyzer Foundation

Created:
$(date)

EOF


cat > "$PACKAGE/apply.sh" <<'EOF'
#!/bin/bash

echo "D020.4.4 deployment handled by update engine"
EOF


chmod +x "$PACKAGE/apply.sh"


echo
echo "Package created:"
echo "$PACKAGE"

