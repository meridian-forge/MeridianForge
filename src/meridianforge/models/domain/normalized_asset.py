"""
Normalized asset model.

Represents standardized investment data independent
of the original source format.
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class NormalizedAsset:
    """
    Generic normalized investment asset.
    """

    asset_type: str

    attributes: dict[str, object] = field(
        default_factory=dict,
    )
