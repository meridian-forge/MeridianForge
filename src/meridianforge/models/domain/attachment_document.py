"""
Attachment document model.

Represents incoming files attached
to external sources.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class AttachmentDocument:
    """
    Attachment representation.
    """

    filename: str

    attachment_type: str

    size_bytes: int = 0
