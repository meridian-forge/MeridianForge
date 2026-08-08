from pathlib import Path
from unittest.mock import Mock

from meridianforge.connectors.gmail_connector import GmailConnector


def test_gmail_connector_sync_returns_empty_list(
    tmp_path: Path,
    monkeypatch,
) -> None:
    connector = GmailConnector()

    monkeypatch.setattr(
        "meridianforge.connectors.gmail_connector.Credentials.from_authorized_user_file",
        lambda *args, **kwargs: Mock(expired=False, refresh_token=None),
    )

    service = Mock()

    labels_execute = (
        service.users.return_value.labels.return_value.list.return_value.execute
    )
    labels_execute.return_value = {
        "labels": [
            {"name": connector.label, "id": "label-1"},
        ]
    }

    messages_execute = (
        service.users.return_value.messages.return_value.list.return_value.execute
    )
    messages_execute.return_value = {"messages": []}

    monkeypatch.setattr(
        "meridianforge.connectors.gmail_connector.build",
        lambda *args, **kwargs: service,
    )

    files = connector.sync(tmp_path)

    assert files == []


def test_gmail_connector_has_default_label() -> None:
    connector = GmailConnector()

    assert connector.label == "MeridianForge/Intake"
