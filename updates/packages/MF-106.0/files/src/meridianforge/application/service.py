from meridianforge.application.models import (
    PropertyInput,
)

from meridianforge.application.workflow import (
    AnalysisWorkflow,
)


class MeridianForgeService:

    def __init__(self) -> None:

        self.workflow = AnalysisWorkflow()


    def analyze_property(
        self,
        property_input: PropertyInput,
    ) -> dict[str, float]:

        return self.workflow.execute(
            property_input
        )
