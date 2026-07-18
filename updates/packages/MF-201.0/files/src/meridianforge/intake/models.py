from dataclasses import dataclass
from enum import StrEnum


class SourceCategory(StrEnum):
    UNKNOWN = "UNKNOWN"
    MARKET_LISTING = "MARKET_LISTING"
    TURNKEY_PROVIDER = "TURNKEY_PROVIDER"
    SYNDICATION = "SYNDICATION"
    MANUAL = "MANUAL"


@dataclass
class SourceDetection:
    filename: str
    extension: str
    category: SourceCategory
    confidence: float
