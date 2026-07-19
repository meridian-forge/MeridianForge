from typing import Any


def load_sample_opportunities() -> list[dict[str, Any]]:
    """
    Starter opportunity dataset.

    Later replaced by:
    - Zillow imports
    - realtor feeds
    - CSV uploads
    - API integrations
    """

    return [
        {
            "name": "Jacksonville Rental A",
            "status": "BUY",
            "score": 92,
        },
        {
            "name": "Philadelphia Rental B",
            "status": "WATCH",
            "score": 76,
        },
        {
            "name": "Memphis Rental C",
            "status": "BUY",
            "score": 88,
        },
    ]
