from meridianforge.opportunity.duplicate_detector import (
    DuplicateDetector,
)


def test_fingerprint_is_stable() -> None:
    first = DuplicateDetector.fingerprint(
        "excel",
        "property.xlsx",
    )

    second = DuplicateDetector.fingerprint(
        "excel",
        "property.xlsx",
    )

    assert first == second


def test_fingerprint_changes() -> None:
    first = DuplicateDetector.fingerprint(
        "excel",
        "a.xlsx",
    )

    second = DuplicateDetector.fingerprint(
        "excel",
        "b.xlsx",
    )

    assert first != second
