from meridianforge.opportunity.models import Opportunity
from meridianforge.validation.models import ValidationResult

REQUIRED_RENTAL_FIELDS = [
    "purchase_price",
    "rent",
]


def validate_opportunity(
    opportunity: Opportunity,
) -> ValidationResult:

    missing: list[str] = []

    for field in REQUIRED_RENTAL_FIELDS:

        if field not in opportunity.fields:

            missing.append(field)

    notes: list[str] = []

    if missing:

        notes.append("Additional data required for underwriting")

    return ValidationResult(
        opportunity_file=opportunity.source_file,
        missing_fields=missing,
        notes=notes,
    )
