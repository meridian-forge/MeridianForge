from abc import ABC, abstractmethod

from meridianforge.domain.source import Source


class FileAdapter(ABC):

    @abstractmethod
    def ingest(self, location: str) -> Source:
        raise NotImplementedError
