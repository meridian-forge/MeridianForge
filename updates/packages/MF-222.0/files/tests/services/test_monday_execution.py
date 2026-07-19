from pathlib import Path

from meridianforge.services.monday_execution import (
    MondayExecutionService,
)


def test_monday_execution(
    tmp_path: Path,
) -> None:

    file = tmp_path / "properties.csv"

    file.write_text(
        "name,price,rent\n"
        "Test Property,200000,1800\n",
        encoding="utf-8",
    )

    result = MondayExecutionService().execute(
        file
    )

    assert result is not None
