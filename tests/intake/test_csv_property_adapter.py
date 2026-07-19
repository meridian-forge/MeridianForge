from pathlib import Path

from meridianforge.intake.csv_property_adapter import (
    CSVPropertyAdapter,
)


def test_csv_property_import(
    tmp_path: Path,
) -> None:

    file = tmp_path / "properties.csv"

    file.write_text(
        "name,price,rent\n" "Jacksonville A,200000,1800\n",
        encoding="utf-8",
    )

    result = CSVPropertyAdapter().load(file)

    assert len(result) == 1
    assert result[0]["name"] == "Jacksonville A"
    assert result[0]["price"] == 200000
