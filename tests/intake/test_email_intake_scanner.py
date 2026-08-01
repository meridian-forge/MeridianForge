from pathlib import Path

from meridianforge.artifacts.artifact_classifier import ArtifactType
from meridianforge.intake.email_intake_scanner import EmailIntakeScanner


def test_scans_and_classifies_email_artifacts(tmp_path: Path) -> None:
    inbox = tmp_path / "runtime" / "incoming" / "email"
    inbox.mkdir(parents=True)

    (inbox / "portfolio.xlsx").write_bytes(b"PK")
    (inbox / "offering.pdf").write_bytes(b"%PDF")
    (inbox / "photo.png").write_bytes(b"PNG")
    (inbox / "notes.txt").write_text("ignore me")

    scanner = EmailIntakeScanner()

    result = scanner.scan(inbox)

    assert result.total_files == 4

    types = {
        artifact.path.name: artifact.artifact_type
        for artifact in result.artifacts
    }

    assert types["portfolio.xlsx"] == ArtifactType.PORTFOLIO_WORKBOOK
    assert types["offering.pdf"] == ArtifactType.PDF_DOCUMENT
    assert types["photo.png"] == ArtifactType.IMAGE
    assert types["notes.txt"] == ArtifactType.UNSUPPORTED


def test_scan_missing_directory_returns_empty_result(tmp_path: Path) -> None:
    scanner = EmailIntakeScanner()

    result = scanner.scan(
        tmp_path / "does_not_exist",
    )

    assert result.total_files == 0
