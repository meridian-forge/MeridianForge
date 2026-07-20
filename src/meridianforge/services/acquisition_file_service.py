"""
Acquisition file intake service.

Loads external property files
into normalized opportunities.
"""

from pathlib import Path

from meridianforge.intake.pipeline import (
    process_file,
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
        Load and normalize opportunity file.
        """

        return process_file(
            Path(file_path),
        )
