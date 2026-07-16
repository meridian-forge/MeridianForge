"""
Confidence engine.

Calculates import confidence using field mappings
and historical mapping performance.
"""

from meridianforge.intelligence.mapping_memory import (
    MappingMemory,
)
from meridianforge.models.results.field_mapping import (
    FieldMapping,
)


class ConfidenceEngine:
    """
    Calculates confidence for normalized imports.
    """

    @staticmethod
    def calculate(
        mappings: list[FieldMapping],
        mapping_memory: MappingMemory,
    ) -> float:
        """
        Calculate combined confidence score.
        """

        if not mappings:
            return 0.0

        scores: list[float] = []

        for mapping in mappings:
            base_confidence = mapping.confidence

            history = mapping_memory.get(mapping.source_field)

            if history is None:
                scores.append(base_confidence)
                continue

            historical_confidence = history.confidence

            combined = (base_confidence + historical_confidence) / 2

            scores.append(combined)

        return sum(scores) / len(scores)
