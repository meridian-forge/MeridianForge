"""
MF-503 artifact workflow integration tests.
"""

from pathlib import Path

from meridianforge.repositories.artifact_repository import (
    ArtifactRepository,
)


def test_duplicate_artifacts_are_detected():
    repository = ArtifactRepository()

    artifact_file = Path("property.xlsx")

    artifact_file.write_text(
        "sample",
    )

    first = repository.register(
        artifact_file,
        source="folder",
    )

    second = repository.register(
        artifact_file,
        source="folder",
    )

    assert first.artifact_id == second.artifact_id

    assert len(repository.all()) == 1
