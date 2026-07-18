from typing import Mapping


FIELD_ALIASES: Mapping[str, list[str]] = {
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

    normalized = field_name.strip().lower()

    for standard, aliases in FIELD_ALIASES.items():

        if normalized in aliases:
            return standard

    return normalized
