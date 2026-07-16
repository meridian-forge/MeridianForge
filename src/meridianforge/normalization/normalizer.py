"""
Normalization engine.

Converts raw external records into normalized
investment asset records.
"""

from meridianforge.models.domain.normalized_asset import (
    NormalizedAsset,
)
from meridianforge.models.results.field_mapping import (
    FieldMapping,
)


class Normalizer:
    """
    Converts mapped raw data into normalized assets.
    """

    @staticmethod
    def normalize(
        record: dict[str, object],
        mappings: list[FieldMapping],
        asset_type: str = "UNKNOWN",
    ) -> NormalizedAsset:
        """
        Normalize a raw record.
        """

        attributes: dict[str, object] = {}

        for mapping in mappings:
            if mapping.source_field in record:
                attributes[mapping.target_field] = record[mapping.source_field]

        return NormalizedAsset(
            asset_type=asset_type,
            attributes=attributes,
        )
