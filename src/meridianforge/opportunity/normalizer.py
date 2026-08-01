"""
Opportunity normalization.

Converts extracted intake data into the lightweight
Opportunity container used by the intake pipeline.
"""

from meridianforge.intake.extracted_data import ExtractedData
from meridianforge.opportunity.field_mapper import normalize_field_name
from meridianforge.opportunity.models import (
    Opportunity,
    OpportunityType,
)


def normalize(
    extracted: ExtractedData,
) -> Opportunity:
    """
    Normalize extracted property data into
    an intake Opportunity.
    """

    fields: dict[str, str] = {}

    for key, value in extracted.fields.items():

        normalized_key = normalize_field_name(
            str(key),
        )

        fields[normalized_key] = "" if value is None else str(value)

    opportunity_type = OpportunityType.UNKNOWN

    if "purchase_price" in fields:
        opportunity_type = OpportunityType.RENTAL_PROPERTY

    return Opportunity(
        source_file=extracted.source_file,
        opportunity_type=opportunity_type,
        fields=fields,
        confidence=1.0,
    )
