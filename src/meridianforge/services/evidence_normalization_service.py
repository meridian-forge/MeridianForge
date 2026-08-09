"""
Evidence normalization service.

Converts extracted evidence fields into canonical
MeridianForge opportunity records.
"""

from __future__ import annotations

from meridianforge.models.evidence.evidence_field import (
    EvidenceRecord,
)


class EvidenceNormalizationService:
    """
    Normalize extracted evidence into canonical fields.
    """

    FIELD_MAP = {
        "purchase_price": "purchase_price",
        "cash_investment": "initial_cash",
        "monthly_rent": "monthly_rent",
        "annual_rent": "annual_rent",
        "property_tax": "property_tax",
        "insurance": "insurance",
        "annual_noi": "annual_noi",
        "annual_cash_flow": "annual_cash_flow",
        "monthly_cash_flow": "monthly_cashflow",
        "cap_rate": "source_cap_rate",
        "cash_on_cash_return": "source_cash_on_cash",
        "interest_rate": "interest_rate",
        "vacancy_rate": "vacancy_rate",
        "management_rate": "management_rate",
    }

    @classmethod
    def normalize(
        cls,
        evidence: EvidenceRecord,
    ) -> dict[str, object]:
        """
        Convert evidence fields into canonical opportunity fields.
        """

        result: dict[str, object] = {
            "source_file": str(evidence.source_file),
            "source_method": "evidence",
            "confidence": evidence.confidence,
        }

        for field in evidence.fields:
            canonical = cls.FIELD_MAP.get(field.name)

            if canonical:
                result[canonical] = field.value

        return result
