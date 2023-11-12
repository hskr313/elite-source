from enum import Enum


class CandleValues(str, Enum):
    CANDLE_OPEN = 'candle_open'
    CANDLE_CLOSE = 'candle_close'
    CANDLE_HIGH = 'candle_high'
    CANDLE_LOW = 'candle_low'
