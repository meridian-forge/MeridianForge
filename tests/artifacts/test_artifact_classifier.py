from pathlib import Path

from meridianforge.artifacts.artifact_classifier import (
    ArtifactClassifier,
    ArtifactType,
)


def test_classifies_xlsx_as_portfolio_workbook() -> None:
    classifier = ArtifactClassifier()

    result = classifier.classify(
        Path("portfolio.xlsx"),
    )

    assert result == ArtifactType.PORTFOLIO_WORKBOOK


def test_classifies_csv_as_portfolio_workbook() -> None:
    classifier = ArtifactClassifier()

    result = classifier.classify(
        Path("portfolio.csv"),
    )

    assert result == ArtifactType.PORTFOLIO_WORKBOOK


def test_classifies_pdf() -> None:
    classifier = ArtifactClassifier()

    result = classifier.classify(
        Path("offering.pdf"),
    )

    assert result == ArtifactType.PDF_DOCUMENT


def test_classifies_image() -> None:
    classifier = ArtifactClassifier()

    result = classifier.classify(
        Path("photo.png"),
    )

    assert result == ArtifactType.IMAGE


def test_classifies_unknown_as_unsupported() -> None:
    classifier = ArtifactClassifier()

    result = classifier.classify(
        Path("notes.txt"),
    )

    assert result == ArtifactType.UNSUPPORTED
