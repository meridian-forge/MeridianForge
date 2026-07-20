"""
Investor report archive service.

Stores generated investor artifacts
and associated metadata.
"""

import json
import shutil
from datetime import date
from pathlib import Path


class ReportArchiveService:
    """
    Archive investor report outputs.
    """

    def archive(
        self,
        files: list[Path],
        metadata: dict,
        archive_root: Path,
    ) -> Path:
        """
        Archive report files and metadata.
        """

        today = date.today()

        archive_directory = (
            archive_root
            / str(today.year)
            / f"{today.month:02d}"
            / f"{today.day:02d}"
        )

        archive_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        for file in files:
            shutil.copy2(
                file,
                archive_directory / file.name,
            )

        metadata_file = archive_directory / "metadata.json"

        metadata_file.write_text(
            json.dumps(
                metadata,
                indent=2,
            ),
            encoding="utf-8",
        )

        return archive_directory
