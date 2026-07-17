"""
Attachment type detector.

Identifies common investment document formats.
"""


class AttachmentTypeDetector:
    """
    Detects attachment category.
    """

    @staticmethod
    def detect(
        filename: str,
    ) -> str:
        """
        Determine attachment type.
        """

        name = filename.lower()

        if name.endswith(
            ".xlsx"
        ):
            return "EXCEL"

        if name.endswith(
            ".pdf"
        ):
            return "PDF"

        if name.endswith(
            ".docx"
        ):
            return "DOCUMENT"

        return "UNKNOWN"
