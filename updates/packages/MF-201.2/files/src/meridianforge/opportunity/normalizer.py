from meridianforge.intake.extracted_data import ExtractedData
from meridianforge.opportunity.field_mapper import normalize_field_name
from meridianforge.opportunity.models import (
    Opportunity,
    OpportunityType,
)


def normalize(
    extracted: ExtractedData,
) -> Opportunity:

    fields: dict[str, str] = {}

    for key, value in extracted.fields.items():
        fields[
            normalize_field_name(key)
        ] = value


    opportunity_type = OpportunityType.UNKNOWN

    if "purchase_price" in fields or "rent" in fields:
        opportunity_type = OpportunityType.RENTAL_PROPERTY

    if "irr" in fields or "preferred_return" in fields:
        opportunity_type = OpportunityType.SYNDICATION


    return Opportunity(
        source_file=extracted.source_file,
        opportunity_type=opportunity_type,
        fields=fields,
        confidence=0.80,
    )
