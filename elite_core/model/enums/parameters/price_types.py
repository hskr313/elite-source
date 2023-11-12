from enum import Enum


class PriceTypes(str, Enum):
    MID = 'mid'
    BID = 'bid'
    ASK = 'ask'
