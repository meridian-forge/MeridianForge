from __future__ import annotations

import base64
import json
from collections.abc import Iterator
from pathlib import Path
from typing import Any, cast

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]

# Project root: MeridianForge/04_Automation/Mac/MeridianForge
PROJECT_ROOT = Path(__file__).resolve().parents[3]

# Workspace root: ~/Documents/MeridianForge
WORKSPACE_ROOT = PROJECT_ROOT.parents[2]

RUNTIME_ROOT = WORKSPACE_ROOT / "10_Runtime"

CREDENTIALS_PATH = RUNTIME_ROOT / "credentials" / "gmail_client_secret.json"
TOKEN_PATH = RUNTIME_ROOT / "credentials" / "gmail_token.json"
STATE_PATH = RUNTIME_ROOT / "State" / "gmail_sync_state.json"


class GmailConnector:
    def __init__(
        self,
        label: str = "MeridianForge/Intake",
        destination: Path | None = None,
    ) -> None:
        self.credentials_path = CREDENTIALS_PATH
        self.token_path = TOKEN_PATH
        self.state_path = STATE_PATH

        self.label = label
        self.destination = destination or (RUNTIME_ROOT / "Incoming" / "Email")

        self.processed_label = "MeridianForge/Processed"
        self.failed_label = "MeridianForge/Failed"
        self.ignored_label = "MeridianForge/Ignored"

    def _load_credentials(self) -> Credentials:
        creds: Credentials | None = None

        if self.token_path.exists():
            creds = Credentials.from_authorized_user_file(
                str(self.token_path),
                SCOPES,
            )

        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
            self.token_path.write_text(creds.to_json())

        if creds is None or not creds.valid:
            flow = InstalledAppFlow.from_client_secrets_file(
                str(self.credentials_path),
                SCOPES,
            )
            creds = flow.run_local_server(port=0)
            self.token_path.parent.mkdir(parents=True, exist_ok=True)
            self.token_path.write_text(creds.to_json())

        return cast(Credentials, creds)

    def _load_state(self) -> set[str]:
        if not self.state_path.exists():
            return set()

        data = json.loads(self.state_path.read_text())
        return set(data.get("processed_message_ids", []))

    def _save_state(self, processed: set[str]) -> None:
        self.state_path.parent.mkdir(parents=True, exist_ok=True)
        self.state_path.write_text(
            json.dumps(
                {"processed_message_ids": sorted(processed)},
                indent=2,
            )
        )

    def _iter_parts(self, payload: dict[str, Any]) -> Iterator[dict[str, Any]]:
        yield payload
        for part in payload.get("parts", []) or []:
            yield from self._iter_parts(part)

    def _label_id(self, service: Any, label_name: str) -> str | None:
        labels = service.users().labels().list(userId="me").execute().get("labels", [])
        for item in labels:
            if item.get("name") == label_name:
                value = item.get("id")
                return str(value) if value is not None else None
        return None

    def _move_label(
        self,
        service: Any,
        message_id: str,
        destination_label: str,
    ) -> None:
        intake_id = self._label_id(service, self.label)
        destination_id = self._label_id(service, destination_label)

        if not intake_id or not destination_id:
            return

        service.users().messages().modify(
            userId="me",
            id=message_id,
            body={
                "addLabelIds": [destination_id],
                "removeLabelIds": [intake_id],
            },
        ).execute()

    def sync(self, target: Path | None = None) -> list[Path]:
        creds = self._load_credentials()
        service = build("gmail", "v1", credentials=creds)

        target = target or self.destination
        target.mkdir(parents=True, exist_ok=True)

        processed = self._load_state()

        label_id = self._label_id(service, self.label)
        if not label_id:
            return []

        response = (
            service.users()
            .messages()
            .list(
                userId="me",
                labelIds=[label_id],
                maxResults=25,
            )
            .execute()
        )

        messages = response.get("messages", [])
        downloaded: list[Path] = []

        for item in messages:
            message_id = item["id"]
            if message_id in processed:
                continue

            try:
                message = (
                    service.users().messages().get(userId="me", id=message_id).execute()
                )

                payload = message.get("payload", {})
                message_downloads = 0

                for part in self._iter_parts(payload):
                    filename = part.get("filename") or ""
                    if not filename:
                        continue

                    body = part.get("body", {})
                    attachment_id = body.get("attachmentId")
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
                    message_downloads += 1

                processed.add(message_id)

                if message_downloads:
                    self._move_label(
                        service,
                        message_id,
                        self.processed_label,
                    )
                else:
                    self._move_label(
                        service,
                        message_id,
                        self.ignored_label,
                    )

            except Exception:
                self._move_label(
                    service,
                    message_id,
                    self.failed_label,
                )
                raise

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
