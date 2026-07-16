"""
Provider profile model.

Represents known data sources.
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class ProviderProfile:
    """
    Represents a known external provider.
    """

    name: str

    category: str = "UNKNOWN"

    mappings: dict[str, str] = field(
        default_factory=dict,
    )

    confidence: float = 0.0
