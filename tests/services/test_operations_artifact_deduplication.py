"""
MF-503.2 Operations artifact deduplication tests.
"""

from pathlib import Path

from meridianforge.repositories.artifact_repository import (
    ArtifactRepository,
)


def test_repository_prevents_duplicate_processing(
    tmp_path: Path,
):
    repository = ArtifactRepository()

    artifact = tmp_path / "deal.xlsx"

    artifact.write_text(
        "property data",
    )

    first = repository.register(
        artifact,
        source="operations",
    )

    second = repository.register(
        artifact,
        source="operations",
    )

    assert first.artifact_id == second.artifact_id

    assert len(repository.all()) == 1
