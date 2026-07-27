"""
Folder intake connector.

SP-410.5

Scans a folder for incoming investment artifacts
and submits them to the Opportunity Inbox.
"""

from pathlib import Path

from meridianforge.intake.file_scanner import scan_directory
from meridianforge.opportunity.inbox_record import OpportunityInboxRecord
from meridianforge.opportunity.inbox_service import OpportunityInboxService


class FolderConnector:
    """
    Connects a filesystem folder to the
    Opportunity Inbox.
    """

    def __init__(
        self,
        inbox: OpportunityInboxService | None = None,
    ) -> None:
        self._inbox = inbox or OpportunityInboxService()

    def import_folder(
        self,
        folder: str | Path,
    ) -> list[OpportunityInboxRecord]:
        """
        Import every supported artifact found
        in the supplied folder.
        """

        records: list[OpportunityInboxRecord] = []

        for file_path in scan_directory(str(folder)):
            record = self._inbox.receive(
                source="FOLDER",
                source_reference=str(file_path),
                metadata={
                    "filename": file_path.name,
                    "extension": file_path.suffix.lower(),
                },
            )

            records.append(record)

        return records
