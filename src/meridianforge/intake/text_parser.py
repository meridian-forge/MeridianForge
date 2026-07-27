"""
Generic text key/value parser.

SP-420

Converts unstructured text artifacts into
the same key/value shape produced by ExcelExtractor.
"""

from __future__ import annotations


def parse_text_fields(
    content: str,
) -> dict[str, str]:
    """
    Extract simple key:value pairs from text.
    """

    fields: dict[str, str] = {}

    for line in content.splitlines():

        if ":" not in line:
            continue

        key, value = line.split(
            ":",
            1,
        )

        key = key.strip()
        value = value.strip()

        if key and value:
            fields[key] = value

    return fields
