from pathlib import Path


SRC = (
    Path(__file__)
    .resolve()
    .parents[2]
    / "src"
    / "meridianforge"
)


def read_python_files(folder: str) -> list[Path]:
    path = SRC / folder

    return list(
        path.rglob("*.py")
    )


def contains_import(
    file: Path,
    forbidden: str,
) -> bool:

    text = file.read_text(
        encoding="utf-8"
    )

    return forbidden in text


def test_domain_does_not_import_services() -> None:

    for file in read_python_files("models"):

        assert not contains_import(
            file,
            "meridianforge.services",
        )


def test_domain_does_not_import_reporting() -> None:

    for file in read_python_files("models"):

        assert not contains_import(
            file,
            "meridianforge.reporting",
        )


def test_services_do_not_import_cli() -> None:

    for file in read_python_files("services"):

        assert not contains_import(
            file,
            "meridianforge.cli",
        )


def test_engines_do_not_import_workflows() -> None:

    for file in read_python_files("engine"):

        assert not contains_import(
            file,
            "meridianforge.workflow",
        )
