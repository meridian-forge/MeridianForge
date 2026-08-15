from __future__ import annotations

import base64
from email.message import EmailMessage

from googleapiclient.discovery import build

from meridianforge.connectors.gmail_connector import GmailConnector
from meridianforge.services.monday_execution_orchestrator import (
    MondayExecutionResult,
)


class MorningBriefingService:
    """
    Send a concise MeridianForge morning briefing using the existing Gmail OAuth
    credentials configured for meridianassets.ai@gmail.com.
    """

    def __init__(
        self,
        recipient: str,
        sender: str = "me",
    ) -> None:
        self._recipient = recipient
        self._sender = sender

    def send(
        self,
        execution: MondayExecutionResult,
        dashboard_url: str,
    ) -> None:
        connector = GmailConnector()
        creds = connector._load_credentials()  # reuse existing OAuth token
        service = build("gmail", "v1", credentials=creds)

        opportunities = execution.operations.normalized_opportunities
        top = opportunities[0] if opportunities else None

        subject = "MeridianForge Daily Briefing"

        lines = [
            "MeridianForge Daily Briefing",
            "",
            f"Gmail synchronized: {'Yes' if execution.gmail_synchronized else 'No'}",
            f"Artifacts processed: {execution.operations.artifacts_processed}",
            f"Opportunities: {len(opportunities)}",
        ]

        if top is not None:
            lines.extend(
                [
                    "",
                    f"Top opportunity: {top.city}, {top.state}",
                ]
            )

        lines.extend(
            [
                "",
                f"Dashboard: {dashboard_url}",
            ]
        )

        message = EmailMessage()
        message["To"] = self._recipient
        message["Subject"] = subject
        message.set_content("\n".join(lines))

        raw = base64.urlsafe_b64encode(message.as_bytes()).decode("utf-8")

        service.users().messages().send(
            userId=self._sender,
            body={"raw": raw},
        ).execute()
