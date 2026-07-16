"""
Import learning service.

Coordinates knowledge capture.
"""

from meridianforge.knowledge.mapping_learning import (
    MappingLearning,
)
from meridianforge.knowledge.source_memory import (
    SourceMemory,
)
from meridianforge.models.results.import_decision import (
    ImportDecision,
)


class ImportLearningService:
    """
    Provides import learning operations.
    """

    def __init__(self) -> None:

        self.sources = SourceMemory()

        self.mappings = MappingLearning()

    def record_mapping(
        self,
        source_field: str,
        target_field: str,
    ) -> None:
        """
        Learn a mapping.
        """

        self.mappings.learn(
            source_field,
            target_field,
        )

    def create_decision(
        self,
        source: str,
        asset_type: str,
        confidence: float,
        mappings_used: int,
        warnings: int = 0,
    ) -> ImportDecision:
        """
        Create import decision.
        """

        return ImportDecision(
            source=source,
            asset_type=asset_type,
            confidence=confidence,
            mappings_used=mappings_used,
            warnings=warnings,
        )
