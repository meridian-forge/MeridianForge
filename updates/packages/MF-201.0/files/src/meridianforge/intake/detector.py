from meridianforge.intake.file_scanner import scan_directory
from meridianforge.intake.models import SourceDetection
from meridianforge.intake.source_classifier import classify_file


def detect_sources(path: str) -> list[SourceDetection]:
    files = scan_directory(path)

    return [
        classify_file(file)
        for file in files
    ]
