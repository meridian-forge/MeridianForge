"""
Image evidence extractor.

Extracts textual evidence from image artifacts
without assuming provider-specific formats.

MF-512.4.3-B

Pipeline:

Image
 |
 OCR
 |
 ImageEvidence
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pytesseract
from PIL import Image


@dataclass(frozen=True, slots=True)
class ImageEvidence:
    """
    Raw evidence extracted from an image artifact.

    This layer does not interpret investment meaning.
    It only preserves extracted evidence.
    """

    source_file: Path
    text: str
    confidence: float


class ImageExtractor:
    """
    Extract text evidence from image files.
    """

    SUPPORTED_FORMATS = {
        ".png",
        ".jpg",
        ".jpeg",
        ".webp",
    }

    @classmethod
    def extract(
        cls,
        image_path: Path,
    ) -> ImageEvidence:
        """
        Extract OCR text from an image.
        """

        if image_path.suffix.lower() not in cls.SUPPORTED_FORMATS:
            raise ValueError(f"Unsupported image format: {image_path.suffix}")

        image = Image.open(image_path)

        text = pytesseract.image_to_string(
            image,
        )

        confidence = 0.90 if text.strip() else 0.0

        return ImageEvidence(
            source_file=image_path,
            text=text.strip(),
            confidence=confidence,
        )
