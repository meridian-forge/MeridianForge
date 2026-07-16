"""
Source document domain model.

Represents external information entering
Meridian Forge.
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class SourceDocument:
    """
    Universal external source representation.
    """

    source_type: str

    content: str

    provider: str | None = None

    attachments: list[str] = field(
        default_factory=list,
    )

    metadata: dict[str, str] = field(
        default_factory=dict,
    )
