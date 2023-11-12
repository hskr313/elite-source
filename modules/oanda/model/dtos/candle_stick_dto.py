from dataclasses import dataclass
from datetime import datetime
from typing import List, Any, Dict

from elite_core.model.entities.elite_candle import EliteCandle


@dataclass
class Price:
    o: str
    h: str
    l: str
    c: str


@dataclass
class CandleStickDTO:
    complete: bool
    volume: int
    time: str
    bid: Price
    mid: Price
    ask: Price

    @staticmethod
    def from_json(json: List[Dict[str, Any]]) -> List['CandleStickDTO']:
        return [CandleStickDTO(**{
            'complete': item['complete'],
            'volume': item['volume'],
            'time': item['time'],
            'bid': Price(**item['bid']),
            'mid': Price(**item['mid']),
            'ask': Price(**item['ask'])
        }) for item in json]

    @staticmethod
    def to_elite_candles(dto: List[Dict[str, Any]]) -> List['EliteCandle']:
        candles = CandleStickDTO.from_json(dto)

        return [
            EliteCandle(
                complete=candle.complete,
                volume=candle.volume,
                time=datetime.strptime(candle.time[:26] + 'Z', '%Y-%m-%dT%H:%M:%S.%fZ'),
                bid_open=float(candle.bid.o),
                bid_high=float(candle.bid.h),
                bid_low=float(candle.bid.l),
                bid_close=float(candle.bid.c),
                mid_open=float(candle.mid.o),
                mid_high=float(candle.mid.h),
                mid_low=float(candle.mid.l),
                mid_close=float(candle.mid.c),
                ask_open=float(candle.ask.o),
                ask_high=float(candle.ask.h),
                ask_low=float(candle.ask.l),
                ask_close=float(candle.ask.c),
            )
            for candle in candles
        ]
