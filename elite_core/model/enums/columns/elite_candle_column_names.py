from enum import Enum


class EliteCandleColumnNames(str, Enum):
    COMPLETE = 'complete'
    VOLUME = 'volume'
    TIME = 'time'
    BID_OPEN = 'bid_open'
    BID_HIGH = 'bid_high'
    BID_LOW = 'bid_low'
    BID_CLOSE = 'bid_close'
    MID_OPEN = 'mid_open'
    MID_HIGH = 'mid_high'
    MID_LOW = 'mid_low'
    MID_CLOSE = 'mid_close'
    ASK_OPEN = 'ask_open'
    ASK_HIGH = 'ask_high'
    ASK_LOW = 'ask_low'
    ASK_CLOSE = 'ask_close'
