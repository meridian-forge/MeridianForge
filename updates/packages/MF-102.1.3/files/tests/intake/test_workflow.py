from meridianforge.intake.workflow import IntakeWorkflow
from meridianforge.domain.source import SourceType


def test_workflow():

    opportunity = IntakeWorkflow().create_opportunity(
        "Test Property",
        "manual-entry",
    )

    assert opportunity.source.source_type == SourceType.MANUAL
