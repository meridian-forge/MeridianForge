"""
Mapping memory engine.

Stores and retrieves historical field mappings.
"""

from meridianforge.models.results.mapping_history import (
    MappingHistory,
)


class MappingMemory:
    """
    In-memory knowledge store for field mappings.
    """

    def __init__(self) -> None:
        self._memory: dict[
            str,
            MappingHistory,
        ] = {}

    def record_success(
        self,
        source_field: str,
        target_field: str,
    ) -> None:
        """
        Record a successful mapping.
        """

        key = source_field.lower()

        history = self._memory.get(key)

        if history is None:
            history = MappingHistory(
                source_field=source_field,
                target_field=target_field,
            )
            self._memory[key] = history

        history.successful_mappings += 1

    def record_failure(
        self,
        source_field: str,
        target_field: str,
    ) -> None:
        """
        Record a failed mapping.
        """

        key = source_field.lower()

        history = self._memory.get(key)

        if history is None:
            history = MappingHistory(
                source_field=source_field,
                target_field=target_field,
            )
            self._memory[key] = history

        history.failed_mappings += 1

    def get(
        self,
        source_field: str,
    ) -> MappingHistory | None:
        """
        Retrieve mapping history.
        """

        return self._memory.get(
            source_field.lower(),
        )
