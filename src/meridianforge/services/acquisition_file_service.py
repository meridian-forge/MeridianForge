"""
Acquisition file intake service.

Loads external property files
into normalized opportunities.
"""

from pathlib import Path

from meridianforge.intake.pipeline import (
    process_file,
    process_folder,
)
from meridianforge.opportunity.models import (
    Opportunity,
)


class AcquisitionFileService:
    """
    Converts property files into
    Meridian Forge opportunities.
    """

    def load(
        self,
        file_path: str,
    ) -> Opportunity:
        """
        Load and normalize a single opportunity file.

        Backward compatible with the current CLI.
        """

        return process_file(
            Path(file_path),
        )

    def load_many(
        self,
        folder_path: str,
    ) -> list[Opportunity]:
        """
        Load and normalize every opportunity found
        in a folder of incoming deal files.
        """

        return process_folder(folder_path)
