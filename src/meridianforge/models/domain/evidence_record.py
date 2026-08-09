"""
Evidence record.

Aggregates extracted fields from any artifact source.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from meridianforge.models.domain.evidence_field import EvidenceField


@dataclass(slots=True)
class EvidenceRecord:
    """
    Collection of extracted evidence fields.
    """

    fields: list[EvidenceField] = field(default_factory=list)

    def add(
        self,
        evidence: EvidenceField,
    ) -> None:
        self.fields.append(evidence)

    def get(
        self,
        name: str,
    ) -> EvidenceField | None:
        for evidence_field in self.fields:
            if evidence_field.name == name:
                return evidence_field

        return None
