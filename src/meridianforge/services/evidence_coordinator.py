"""
Evidence coordinator.

SP-485.2

Provides a single canonical entry point for converting arbitrary artifacts
(images, spreadsheets, PDFs in the future, APIs in the future) into a typed
EvidencePayload.

This layer is intentionally provider agnostic.
"""

from __future__ import annotations

from pathlib import Path

from meridianforge.extraction.evidence_field_extractor import (
    EvidenceFieldExtractor,
)
from meridianforge.extraction.identity_extractor import (
    IdentityExtractor,
)
from meridianforge.extraction.image_extractor import (
    ImageExtractor,
)
from meridianforge.extraction.spreadsheet_extractor import (
    SpreadsheetExtractor,
)
from meridianforge.models.domain.evidence_payload import (
    EvidencePayload,
)
from meridianforge.services.evidence_payload_builder import (
    EvidencePayloadBuilder,
)


class EvidenceCoordinator:
    """
    Canonical artifact-to-evidence entry point.

    Current support:
        - Images (OCR)
        - Excel workbooks (tabular extraction)

    Future support:
        - PDFs
        - Email bodies
        - APIs
        - Cloud storage connectors
    """

    IMAGE_SUFFIXES = {
        ".png",
        ".jpg",
        ".jpeg",
        ".webp",
    }

    SPREADSHEET_SUFFIXES = {
        ".xlsx",
        ".xlsm",
        ".xltx",
        ".xltm",
    }

    @classmethod
    def extract(
        cls,
        artifact_path: Path,
    ) -> EvidencePayload:
        """
        Convert an artifact into a typed EvidencePayload.
        """

        suffix = artifact_path.suffix.lower()

        if suffix in cls.IMAGE_SUFFIXES:
            return cls._from_image(
                artifact_path,
            )

        if suffix in cls.SPREADSHEET_SUFFIXES:
            return cls._from_spreadsheet(
                artifact_path,
            )

        raise ValueError(f"Unsupported artifact type: {artifact_path.suffix}")

    @staticmethod
    def _from_image(
        image_path: Path,
    ) -> EvidencePayload:
        evidence = ImageExtractor.extract(
            image_path,
        )

        fields = EvidenceFieldExtractor.extract(
            evidence.text,
        )

        field_dict: dict[str, object] = {field.name: field.value for field in fields}

        identity = IdentityExtractor.extract(
            evidence.text,
        )

        payload = EvidencePayloadBuilder.build(
            field_dict,
            identity,
            image_path.name,
        )

        payload.source_method = "OCR"
        payload.confidence = evidence.confidence
        payload.raw_text = evidence.text
        payload.image_paths.append(
            image_path,
        )

        return payload

    @staticmethod
    def _from_spreadsheet(
        workbook_path: Path,
    ) -> EvidencePayload:
        artifact = SpreadsheetExtractor.extract(
            workbook_path,
        )

        if not artifact.records:
            return EvidencePayload(
                source_file=workbook_path.name,
                source_method="spreadsheet",
                confidence=0.0,
            )

        first_record = artifact.records[0]

        identity = IdentityExtractor.extract(
            str(
                first_record.get(
                    "Address",
                    first_record.get(
                        "address",
                        "",
                    ),
                )
            )
        )

        payload = EvidencePayloadBuilder.build(
            first_record,
            identity,
            workbook_path.name,
        )

        payload.source_method = "spreadsheet"
        payload.confidence = 0.99

        return payload
