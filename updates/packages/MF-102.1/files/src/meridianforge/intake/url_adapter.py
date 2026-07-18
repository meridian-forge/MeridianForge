from meridianforge.domain.source import Source, SourceType

from meridianforge.intake.adapter import SourceAdapter


class URLAdapter(SourceAdapter):

    def ingest(self, location: str) -> Source:
        return Source(
            source_type=SourceType.URL,
            location=location,
        )
