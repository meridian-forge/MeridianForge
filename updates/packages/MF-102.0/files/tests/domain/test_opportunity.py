from meridianforge.domain.opportunity import Opportunity
from meridianforge.domain.source import Source, SourceType


def test_opportunity():

    opportunity = Opportunity(
        "Test Property",
        Source(
            SourceType.MANUAL,
            "manual"
        )
    )

    assert opportunity.validate()
