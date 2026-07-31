from __future__ import annotations

from enum import StrEnum
from pathlib import Path


class ArtifactType(StrEnum):
    """
    Classification of incoming investment artifacts.
    """

    PORTFOLIO_WORKBOOK = "portfolio_workbook"
    PDF_DOCUMENT = "pdf_document"
    IMAGE = "image"
    UNSUPPORTED = "unsupported"


class ArtifactClassifier:
    """
    Classifies incoming investment artifacts using filename and extension
    heuristics.

    This preserves the original MF-502 public contract while modernizing
    the enum implementation to StrEnum.
    """

    PORTFOLIO_EXTENSIONS = {
        ".xlsx",
        ".xlsm",
        ".xls",
        ".csv",
    }

    IMAGE_EXTENSIONS = {
        ".png",
        ".jpg",
        ".jpeg",
        ".gif",
        ".webp",
        ".bmp",
        ".tif",
        ".tiff",
    }

    @classmethod
    def classify(
        cls,
        path: Path,
    ) -> ArtifactType:
        suffix = path.suffix.lower()

        if suffix in cls.PORTFOLIO_EXTENSIONS:
            return ArtifactType.PORTFOLIO_WORKBOOK

        if suffix == ".pdf":
            return ArtifactType.PDF_DOCUMENT

        if suffix in cls.IMAGE_EXTENSIONS:
            return ArtifactType.IMAGE

        return ArtifactType.UNSUPPORTED
