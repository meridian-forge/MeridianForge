from enum import StrEnum


class OpportunityStatus(StrEnum):
    NEW = "NEW"
    ANALYZING = "ANALYZING"
    ANALYZED = "ANALYZED"
    WATCHLIST = "WATCHLIST"
    REJECTED = "REJECTED"
    CLOSED = "CLOSED"
