"""
Mapping reuse service.

Retrieves previously learned field mappings.
"""

from meridianforge.knowledge.mapping_learning import (
    MappingLearning,
)


class MappingReuseService:
    """
    Reuses learned mappings.
    """

    def __init__(
        self,
        learning: MappingLearning | None = None,
    ) -> None:

        self.learning = learning or MappingLearning()

    def reuse(
        self,
        fields: list[str],
    ) -> dict[str, str]:
        """
        Return known mappings.
        """

        results: dict[str, str] = {}

        for field in fields:

            target = self.learning.lookup(
                field,
            )

            if target:
                results[field] = target

        return results
