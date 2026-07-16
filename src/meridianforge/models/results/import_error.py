"""
Import error model.

Represents recoverable import problems.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class ImportError:
    """
    Structured import error.
    """

    message: str

    file_name: str | None = None

    recoverable: bool = True
