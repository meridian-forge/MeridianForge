from dataclasses import dataclass, field
from enum import StrEnum


class OpportunityType(StrEnum):
    UNKNOWN = "UNKNOWN"
    RENTAL_PROPERTY = "RENTAL_PROPERTY"
    SYNDICATION = "SYNDICATION"


@dataclass
class Opportunity:
    source_file: str
    opportunity_type: OpportunityType = OpportunityType.UNKNOWN
    fields: dict[str, str] = field(default_factory=dict)
    confidence: float = 0.0
