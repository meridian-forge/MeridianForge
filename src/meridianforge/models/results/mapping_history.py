"""
Mapping history model.

Stores historical performance of field mappings.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class MappingHistory:
    """
    Historical record for a field mapping.
    """

    source_field: str

    target_field: str

    successful_mappings: int = 0

    failed_mappings: int = 0

    @property
    def total_attempts(self) -> int:
        """
        Total mapping attempts.
        """

        return self.successful_mappings + self.failed_mappings

    @property
    def confidence(self) -> float:
        """
        Historical confidence score.
        """

        if self.total_attempts == 0:
            return 0.0

        return self.successful_mappings / self.total_attempts
