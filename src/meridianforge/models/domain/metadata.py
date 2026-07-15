"""
Source metadata.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Metadata:
    provider: str
    imported_at: str
