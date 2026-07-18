from meridianforge.domain.source import Source, SourceType

from meridianforge.intake.adapter import SourceAdapter


class ManualAdapter(SourceAdapter):

    def ingest(self, location: str) -> Source:
        return Source(
            source_type=SourceType.MANUAL,
            location=location,
        )
