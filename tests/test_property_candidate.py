from meridianforge.models.domain.property_candidate import (
    PropertyCandidate,
)


def test_property_candidate() -> None:

    candidate = PropertyCandidate(
        purchase_price=200000,
    )

    assert candidate.purchase_price == 200000
