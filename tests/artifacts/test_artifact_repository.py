from pathlib import Path

from meridianforge.repositories.artifact_repository import (
    ArtifactRepository,
)


def test_artifact_repository_registers_and_deduplicates(
    tmp_path: Path,
):

    file = tmp_path / "properties.xlsx"

    file.write_text(
        "sample",
    )

    repository = ArtifactRepository()

    first = repository.register(
        file,
        source="email",
    )

    second = repository.register(
        file,
        source="email",
    )

    assert first.checksum == second.checksum

    assert len(repository.all()) == 1
