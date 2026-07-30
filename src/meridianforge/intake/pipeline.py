from pathlib import Path

from meridianforge.intake.detector import detect_sources
from meridianforge.intake.extractors.registry import get_extractor
from meridianforge.opportunity.models import Opportunity
from meridianforge.opportunity.normalizer import normalize


def process_records(
    extracted_items: list,
) -> list[Opportunity]:
    """
    Normalize multiple extracted records into opportunities.
    """

    return [normalize(item) for item in extracted_items]


def process_file(
    file_path: Path,
) -> Opportunity:
    """
    Backward-compatible single-opportunity loader.
    """

    extractor = get_extractor(file_path)

    extracted = extractor.extract(file_path)

    return normalize(extracted)


def process_folder(
    folder_path: str,
) -> list[Opportunity]:
    """
    Load all opportunities from all supported files in a folder.
    """

    detections = detect_sources(folder_path)

    opportunities: list[Opportunity] = []

    for detection in detections:

        opportunity = process_file(Path(detection.filename))

        opportunities.append(opportunity)

    return opportunities
