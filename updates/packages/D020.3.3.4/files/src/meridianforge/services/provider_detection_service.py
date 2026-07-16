"""
Provider detection service.

Identifies known external data sources.
"""

from meridianforge.knowledge.provider_profile import (
    ProviderProfile,
)
from meridianforge.knowledge.source_memory import (
    SourceMemory,
)


class ProviderDetectionService:
    """
    Detects provider identity from imported data.
    """

    def __init__(
        self,
        memory: SourceMemory | None = None,
    ) -> None:

        self.memory = memory or SourceMemory()

    def detect(
        self,
        record: dict[str, object],
    ) -> ProviderProfile | None:
        """
        Identify provider from record metadata.
        """

        provider = record.get("provider")

        if provider is None:
            return None

        return self.memory.find(
            str(provider),
        )
