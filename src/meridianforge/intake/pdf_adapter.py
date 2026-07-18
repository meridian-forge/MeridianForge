from pathlib import Path

from meridianforge.domain.source import Source, SourceType
from meridianforge.intake.file_adapter import FileAdapter


class PDFAdapter(FileAdapter):

    def ingest(self, location: str) -> Source:

        if not Path(location).exists():
            raise FileNotFoundError(location)

        return Source(
            source_type=SourceType.PDF,
            location=location,
        )
