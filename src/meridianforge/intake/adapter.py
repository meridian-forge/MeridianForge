from abc import ABC, abstractmethod

from meridianforge.domain.source import Source


class SourceAdapter(ABC):

    @abstractmethod
    def ingest(self, location: str) -> Source:
        raise NotImplementedError
