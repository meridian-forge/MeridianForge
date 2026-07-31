from pathlib import Path

from meridianforge.connectors.connector import (
    Connector,
)


class DummyConnector:
    def sync(
        self,
        destination: Path,
    ) -> list[Path]:
        file = destination / "sample.xlsx"
        file.write_text("test")
        return [file]


def test_connector_protocol() -> None:
    connector: Connector = DummyConnector()

    tmp = Path("runtime/test-connector")
    tmp.mkdir(parents=True, exist_ok=True)

    files = connector.sync(tmp)

    assert len(files) == 1
    assert files[0].name == "sample.xlsx"
