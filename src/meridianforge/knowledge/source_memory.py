"""
Source memory.

Stores recognized providers.
"""

from meridianforge.knowledge.provider_profile import (
    ProviderProfile,
)


class SourceMemory:
    """
    Learns and retrieves known sources.
    """

    def __init__(self) -> None:
        self._providers: dict[str, ProviderProfile] = {}

    def remember(
        self,
        profile: ProviderProfile,
    ) -> None:
        """
        Store provider knowledge.
        """

        self._providers[profile.name.lower()] = profile

    def find(
        self,
        name: str,
    ) -> ProviderProfile | None:
        """
        Retrieve provider knowledge.
        """

        return self._providers.get(name.lower())

    def count(self) -> int:
        """
        Return known provider count.
        """

        return len(self._providers)
