"""
Mapping learning engine.

Learns field relationships.
"""


class MappingLearning:
    """
    Learns source to canonical mappings.
    """

    def __init__(self) -> None:
        self._mappings: dict[str, str] = {}

    def learn(
        self,
        source_field: str,
        target_field: str,
    ) -> None:
        """
        Store a mapping.
        """

        self._mappings[
            source_field.lower()
        ] = target_field

    def lookup(
        self,
        source_field: str,
    ) -> str | None:
        """
        Retrieve learned mapping.
        """

        return self._mappings.get(
            source_field.lower()
        )

    def count(self) -> int:
        """
        Return mapping count.
        """

        return len(self._mappings)
