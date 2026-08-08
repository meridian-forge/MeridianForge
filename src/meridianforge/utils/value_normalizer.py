from __future__ import annotations

from decimal import Decimal


class ValueNormalizer:
    """Canonical numeric normalization utilities."""

    @staticmethod
    def clean(value: object) -> str:
        return (
            str(value)
            .replace("$", "")
            .replace(",", "")
            .replace("%", "")
            .strip()
        )

    @classmethod
    def to_decimal(
        cls,
        value: object,
    ) -> Decimal | None:
        if value is None:
            return None

        try:
            return Decimal(cls.clean(value))
        except Exception:
            return None

    @classmethod
    def to_float(
        cls,
        value: object,
        default: float = 0.0,
    ) -> float:
        decimal_value = cls.to_decimal(value)

        if decimal_value is None:
            return default

        return float(decimal_value)
