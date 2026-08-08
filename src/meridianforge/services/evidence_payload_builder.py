"""
Evidence payload builder.

Combines extracted financial evidence and
identity evidence into a canonical EvidencePayload.

Provider agnostic.
"""

from __future__ import annotations

from meridianforge.extraction.identity_extractor import (
    IdentityEvidence,
)
from meridianforge.models.domain.evidence_payload import (
    EvidencePayload,
)
from meridianforge.utils.value_normalizer import (
    ValueNormalizer,
)


class EvidencePayloadBuilder:
    """
    Build canonical evidence payloads.
    """

    @staticmethod
    def build(
        fields: dict[str, object],
        identity: IdentityEvidence,
        source_file: str,
    ) -> EvidencePayload:
        financial_fields = {}

        for key, value in fields.items():
            decimal_value = ValueNormalizer.to_decimal(value)

            if decimal_value is not None:
                financial_fields[str(key)] = decimal_value

        return EvidencePayload(
            source_file=source_file,
            identity=identity,
            confidence=identity.confidence,
            financial_fields=financial_fields,
        )
