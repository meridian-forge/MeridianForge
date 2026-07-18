from meridianforge.domain.opportunity import Opportunity
from meridianforge.intake.router import IntakeRouter


class IntakeWorkflow:

    def __init__(self) -> None:
        self.router = IntakeRouter()

    def create_opportunity(
        self,
        name: str,
        location: str,
    ) -> Opportunity:

        adapter = self.router.select(location)

        source = adapter.ingest(location)

        return Opportunity(
            name=name,
            source=source,
        )
