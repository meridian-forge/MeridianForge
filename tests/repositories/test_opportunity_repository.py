from meridianforge.repositories.opportunity_repository import (
    OpportunityRepository,
)


def test_repository_add_and_get() -> None:

    repository = OpportunityRepository()

    repository.add("Property A")

    opportunities = repository.get_all()

    assert opportunities == ["Property A"]


def test_repository_count() -> None:

    repository = OpportunityRepository(
        [
            "Property A",
            "Property B",
        ]
    )

    assert repository.count() == 2
