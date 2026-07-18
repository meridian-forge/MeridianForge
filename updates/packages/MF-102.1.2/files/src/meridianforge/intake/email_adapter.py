from meridianforge.domain.source import Source, SourceType

from meridianforge.intake.file_adapter import FileAdapter


class EmailAdapter(FileAdapter):

    def ingest(self, location: str) -> Source:

        return Source(
            source_type=SourceType.EMAIL,
            location=location,
        )
