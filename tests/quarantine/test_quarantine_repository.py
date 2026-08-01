from pathlib import Path

from meridianforge.quarantine.quarantine_repository import (
    QuarantineRepository,
)


def test_adds_quarantined_artifact() -> None:
    repo = QuarantineRepository()

    artifact = repo.add(
        Path("bad.xlsx"),
        reason="invalid workbook",
        source="email",
        checksum="abc123",
    )

    assert repo.count() == 1
    assert artifact.reason == "invalid workbook"
    assert artifact.source == "email"


def test_deduplicates_by_checksum() -> None:
    repo = QuarantineRepository()

    first = repo.add(
        Path("bad.xlsx"),
        reason="invalid workbook",
        source="email",
        checksum="abc123",
    )

    second = repo.add(
        Path("bad-copy.xlsx"),
        reason="invalid workbook",
        source="email",
        checksum="abc123",
    )

    assert repo.count() == 1
    assert first is second
