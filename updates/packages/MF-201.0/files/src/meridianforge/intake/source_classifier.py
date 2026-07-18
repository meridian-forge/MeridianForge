from pathlib import Path

from meridianforge.intake.models import (
    SourceCategory,
    SourceDetection,
)


def classify_file(path: Path) -> SourceDetection:
    name = path.name.lower()

    category = SourceCategory.UNKNOWN
    confidence = 0.50

    if "jwb" in name or "turnkey" in name:
        category = SourceCategory.TURNKEY_PROVIDER
        confidence = 0.90

    elif "syndication" in name or "offering" in name or "om" in name:
        category = SourceCategory.SYNDICATION
        confidence = 0.85

    elif "zillow" in name or "realtor" in name or "listing" in name:
        category = SourceCategory.MARKET_LISTING
        confidence = 0.90

    return SourceDetection(
        filename=path.name,
        extension=path.suffix.lower(),
        category=category,
        confidence=confidence,
    )
