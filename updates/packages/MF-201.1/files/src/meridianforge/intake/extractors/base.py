from abc import ABC, abstractmethod
from pathlib import Path

from meridianforge.intake.extracted_data import ExtractedData


class Extractor(ABC):

    @abstractmethod
    def extract(self, file_path: Path) -> ExtractedData:
        pass
