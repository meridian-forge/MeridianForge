"""
Unified opportunity intake service.

MF-512.2.1

Provides a document-level intake boundary for the Family Office OS.
This service classifies incoming artifacts and routes them to the
appropriate extraction pipeline before underwriting occurs.

Current implementation provides classification and routing metadata.
Future milestones (MF-512.2.2+) will connect specialized extractors
and normalize opportunities across multiple asset classes.
"""

from __future__ import annotations

import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from zipfile import ZipFile

from pypdf import PdfReader

from meridianforge.models.opportunity import (
    OpportunityClassification,
)
from meridianforge.services.opportunity_classifier import (
    OpportunityClassifier,
)


@dataclass(frozen=True)
class IntakeArtifact:
    """
    A classified incoming investment artifact.
    """

    path: Path
    classification: OpportunityClassification
    extracted_text: str


class OpportunityIntakeService:
    """
    Classify and prepare incoming investment artifacts for extraction.

    This service intentionally stops at the document boundary.
    It does not perform underwriting or create acquisition opportunities.
    """

    def ingest_file(
        self,
        path: Path,
    ) -> IntakeArtifact:
        text = self._extract_text(path)

        classification = OpportunityClassifier.classify(
            path,
            text,
        )

        return IntakeArtifact(
            path=path,
            classification=classification,
            extracted_text=text,
        )

    def ingest_directory(
        self,
        directory: Path,
    ) -> list[IntakeArtifact]:
        if not directory.exists():
            return []

        artifacts: list[IntakeArtifact] = []

        for path in sorted(directory.iterdir()):
            if not path.is_file():
                continue

            artifacts.append(
                self.ingest_file(
                    path,
                )
            )

        return artifacts

    def _extract_text(
        self,
        path: Path,
    ) -> str:
        suffix = path.suffix.lower()

        if suffix == ".pdf":
            try:
                reader = PdfReader(str(path))

                text = "".join(
                    page.extract_text() or ""
                    for page in reader.pages
                )

                if text.strip():
                    return text

            except Exception:
                pass

            # Fallback for malformed PDFs, text fixtures,
            # or files mislabeled with a PDF extension.
            try:
                return path.read_text()

            except Exception:
                return ""

        if suffix == ".docx":
            try:
                with ZipFile(path) as zf:
                    xml = zf.read("word/document.xml")

                root = ET.fromstring(xml)

                ns = {
                    "w": (
                        "http://schemas.openxmlformats.org/"
                        "wordprocessingml/2006/main"
                    )
                }

                return "\n".join(
                    "".join(t.text or "" for t in p.findall(".//w:t", ns))
                    for p in root.findall(".//w:p", ns)
                )

            except Exception:
                return ""

        try:
            return path.read_text()

        except Exception:
            return ""
