"""
Extractor learning memory.

Stores learned extractor performance patterns.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class ExtractorLearningProfile:
    """
    Represents learned behavior for an extractor.
    """

    extractor: str
    artifact_type: str
    provider: str | None = None

    runs: int = 0
    successful_runs: int = 0
    corrections: int = 0

    average_confidence: float = 0.0

    def record(
        self,
        confidence: float,
        corrected: bool = False,
    ) -> None:
        """
        Record extraction outcome.
        """

        self.runs += 1

        self.average_confidence = (
            (self.average_confidence * (self.runs - 1)) + confidence
        ) / self.runs

        if confidence >= 0.80:
            self.successful_runs += 1

        if corrected:
            self.corrections += 1

    @property
    def success_rate(self) -> float:
        """
        Return successful extraction ratio.
        """

        if self.runs == 0:
            return 0.0

        return self.successful_runs / self.runs


class ExtractorLearningMemory:
    """
    Stores extractor learning profiles.
    """

    def __init__(self) -> None:
        self._profiles: dict[
            tuple[str, str, str | None],
            ExtractorLearningProfile,
        ] = {}

    def remember(
        self,
        profile: ExtractorLearningProfile,
    ) -> None:
        """
        Store extractor knowledge.
        """

        key = (
            profile.extractor.lower(),
            profile.artifact_type.lower(),
            profile.provider.lower() if profile.provider else None,
        )

        self._profiles[key] = profile

    def find(
        self,
        extractor: str,
        artifact_type: str,
        provider: str | None = None,
    ) -> ExtractorLearningProfile | None:
        """
        Retrieve extractor knowledge.
        """

        return self._profiles.get(
            (
                extractor.lower(),
                artifact_type.lower(),
                provider.lower() if provider else None,
            )
        )

    def count(self) -> int:
        """
        Return learned extractor count.
        """

        return len(self._profiles)
