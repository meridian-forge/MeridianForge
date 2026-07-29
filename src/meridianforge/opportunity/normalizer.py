"""
Opportunity normalization.

Converts extracted intake data into the lightweight
Opportunity container used by the intake pipeline.
"""

from meridianforge.intake.extracted_data import ExtractedData
from meridianforge.opportunity.models import Opportunity


def normalize(extracted: ExtractedData) -> Opportunity:
    """
    Normalize extracted property data into an intake Opportunity.
    """

    fields: dict[str, str] = {
        key: "" if value is None else str(value)
        for key, value in extracted.fields.items()
    }

    return Opportunity(
        source_file=extracted.source_file,
        fields=fields,
        confidence=1.0,
    )
