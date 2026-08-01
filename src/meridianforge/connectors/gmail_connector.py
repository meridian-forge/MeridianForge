from __future__ import annotations

import base64
import json
from pathlib import Path
from typing import Any

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

from meridianforge.connectors.connector import Connector

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


class GmailConnector(Connector):
    """
    Live Gmail connector backed by the Gmail API.

    Synchronizes attachments from a Gmail label into the workspace runtime
    directory and returns only newly downloaded local file paths.
    """

    def __init__(
        self,
        label: str = "MeridianForge",
        destination: Path | None = None,
    ) -> None:
        workspace = Path.home() / "Documents" / "MeridianForge"

        self.label = label
        self.credentials_dir = workspace / "10_Runtime" / "credentials"
        self.state_dir = workspace / "10_Runtime" / "State"

        self.token_file = self.credentials_dir / "gmail_token.json"
        self.state_file = self.state_dir / "gmail_sync_state.json"

        self.destination = (
            destination
            or workspace / "10_Runtime" / "Incoming" / "Email"
        )

    def _load_state(self) -> set[str]:
        if not self.state_file.exists():
            return set()

        try:
            data = json.loads(
                self.state_file.read_text(encoding="utf-8")
            )
            return set(data.get("processed_message_ids", []))
        except Exception:
            return set()

    def _save_state(self, processed: set[str]) -> None:
        self.state_dir.mkdir(parents=True, exist_ok=True)

        payload = {
            "processed_message_ids": sorted(processed),
        }

        self.state_file.write_text(
            json.dumps(payload, indent=2),
            encoding="utf-8",
        )

    def sync(
        self,
        destination: Path | None = None,
    ) -> list[Path]:
        target = destination or self.destination
        target.mkdir(parents=True, exist_ok=True)

        creds = Credentials.from_authorized_user_file(
            str(self.token_file),
            SCOPES,
        )

        if creds.expired and creds.refresh_token:
            creds.refresh(Request())

        service = build(
            "gmail",
            "v1",
            credentials=creds,
        )

        labels = service.users().labels().list(userId="me").execute()
        label_id: str | None = None

        for item in labels.get("labels", []):
            if item.get("name") == self.label:
                label_id = item.get("id")
                break

        if label_id is None:
            return []

        processed = self._load_state()

        messages = (
            service.users()
            .messages()
            .list(
                userId="me",
                labelIds=[label_id],
            )
            .execute()
            .get("messages", [])
        )

        downloaded: list[Path] = []

        for message in messages:
            message_id = message["id"]

            if message_id in processed:
                continue

            full = (
                service.users()
                .messages()
                .get(
                    userId="me",
                    id=message_id,
                )
                .execute()
            )

            payload = full.get("payload", {})
            parts = payload.get("parts", [])

            for part in parts:
                filename = part.get("filename")

                if not filename:
                    continue

                attachment_id = (
                    part.get("body", {})
                    .get("attachmentId")
                )

                if not attachment_id:
                    continue

                attachment = (
                    service.users()
                    .messages()
                    .attachments()
                    .get(
                        userId="me",
                        messageId=message_id,
                        id=attachment_id,
                    )
                    .execute()
                )

                data = attachment.get("data")

                if not data:
                    continue

                content = base64.urlsafe_b64decode(data)

                path = target / filename
                path.write_bytes(content)
                downloaded.append(path)

            processed.add(message_id)

        self._save_state(processed)

        return downloaded


if __name__ == "__main__":
    connector = GmailConnector()
    files = connector.sync()

    print("Connected to Gmail")
    print(f"Label: {connector.label}")
    print(f"New attachments downloaded: {len(files)}")

    for file in files:
        print(file)
