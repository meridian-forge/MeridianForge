from dataclasses import dataclass

from meridianforge.domain.opportunity_status import OpportunityStatus
from meridianforge.domain.source import Source


@dataclass
class Opportunity:
    name: str
    source: Source
    status: OpportunityStatus = OpportunityStatus.NEW

    def validate(self) -> bool:
        if not self.name:
            raise ValueError("Opportunity name required")

        self.source.validate()

        return True
