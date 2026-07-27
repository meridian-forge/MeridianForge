from collections.abc import Mapping


FIELD_ALIASES: Mapping[str, list[str]] = {
    "address": [
        "address",
        "property address",
        "street address",
    ],
    "purchase_price": [
        "purchase price",
        "price",
        "list price",
    ],
    "rent": [
        "rent",
        "monthly rent",
        "estimated rent",
    ],
    "taxes": [
        "taxes",
        "property tax",
    ],
    "insurance": [
        "insurance",
    ],
}


def normalize_field_name(field_name: str) -> str:
    """
    Convert external field labels into
    MeridianForge normalized fields.
    """

    normalized = field_name.strip().lower()

    for standard, aliases in FIELD_ALIASES.items():

        if normalized in aliases:
            return standard

    return normalized
