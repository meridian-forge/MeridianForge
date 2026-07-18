from meridianforge.domain.source import SourceType
from meridianforge.intake.workflow import IntakeWorkflow


def test_workflow():

    opportunity = IntakeWorkflow().create_opportunity(
        "Test Property",
        "manual-entry",
    )

    assert opportunity.source.source_type == SourceType.MANUAL
