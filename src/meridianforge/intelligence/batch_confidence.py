"""
Batch confidence engine.

Calculates confidence at file level.
"""


class BatchConfidence:
    """
    Calculates confidence for batch imports.
    """

    @staticmethod
    def calculate(
        record_confidences: list[float],
        failed_records: int = 0,
        total_records: int = 0,
        unknown_fields: int = 0,
    ) -> float:
        """
        Calculate batch confidence.
        """

        if not record_confidences:
            return 0.0

        confidence = sum(record_confidences) / len(record_confidences)

        if total_records > 0:
            failure_penalty = failed_records / total_records

            confidence -= failure_penalty * 0.25

        unknown_penalty = unknown_fields * 0.01

        confidence -= unknown_penalty

        return max(
            0.0,
            min(
                confidence,
                1.0,
            ),
        )
