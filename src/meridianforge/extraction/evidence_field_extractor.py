from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
import re

from meridianforge.services.extraction_audit_service import (
    ExtractionAuditService,
)


@dataclass(frozen=True, slots=True)
class ExtractedField:
    name: str
    value: Decimal
    source_text: str
    confidence: float


class EvidenceFieldExtractor:
    FIELD_PATTERNS = {
        "purchase_price": [r"Purchase Price\s+\$?([\d,]+)"],
        "cash_investment": [r"Total Cash Investment\s+\$?([\d,]+)"],
        "interest_rate": [r"Interest Rate.*?([\d.]+)%"],
        "monthly_rent": [r"Monthly Rent.*?\$?([\d,]+)"],
        "annual_rent": [r"Gross Scheduled Income.*?\$?([\d,]+)"],
        "property_tax": [
            r"Property Tax.*?\$?([\d,]+)",
            r"Property Taxes.*?\$?\(?([\d,]+)",
        ],
        "insurance": [r"Insurance Premium.*?\$?([\d,]+)"],
        "annual_noi": [r"Net Operating Income\s+\$?([\d,]+)"],
        "annual_cash_flow": [r"Annual Cash Flow\s+\$?([\d,]+)"],
        "monthly_cash_flow": [r"Monthly Cash Flow\s+\$?([\d,]+)"],
        "cap_rate": [r"Cap Rate\s+([\d.]+)%"],
        "cash_on_cash_return": [r"Cash-On-Cash ROI.*?([\d.]+)%"],
        "vacancy_rate": [r"Vacancy Rate.*?([\d.]+)%"],
        "management_rate": [r"Property Mgmt Rate.*?([\d.]+)%"],
    }

    @classmethod
    def extract(
        cls,
        text: str,
        *,
        audit_service: ExtractionAuditService | None = None,
        artifact_id: str | None = None,
        source_file: str | None = None,
    ) -> list[ExtractedField]:

        results: list[ExtractedField] = []

        artifact = artifact_id or source_file or "unknown"
        source = source_file or artifact

        for field_name, patterns in cls.FIELD_PATTERNS.items():
            for pattern in patterns:
                match = re.search(
                    pattern,
                    text,
                    flags=re.IGNORECASE | re.DOTALL,
                )

                if not match:
                    continue

                raw_value = match.group(1).replace(",", "").strip()

                try:
                    value = Decimal(raw_value)
                except Exception:
                    continue

                field = ExtractedField(
                    name=field_name,
                    value=value,
                    source_text=match.group(0),
                    confidence=0.95,
                )

                results.append(field)

                if audit_service is not None:
                    audit_service.record_field(
                        artifact_id=artifact,
                        source_file=source,
                        field_name=field.name,
                        raw_value=field.source_text,
                        normalized_value=str(field.value),
                        confidence=field.confidence,
                        extractor="EvidenceFieldExtractor",
                    )

                break

        return results
