from sqlalchemy import Boolean, Column, Float, DateTime

from elite_core.features.sqlalchemy.model.entities.abstract_entity import AbstractEntity
from elite_core.model.enums.columns.elite_candle_column_names import EliteCandleColumnNames


class EliteCandle(AbstractEntity):
    __tablename__ = 'elite_candle'

    complete = Column(Boolean, name=EliteCandleColumnNames.COMPLETE)
    volume = Column(Float, name=EliteCandleColumnNames.VOLUME)
    time = Column(DateTime, name=EliteCandleColumnNames.TIME)
    bid_open = Column(Float, name=EliteCandleColumnNames.BID_OPEN)
    bid_high = Column(Float, name=EliteCandleColumnNames.BID_HIGH)
    bid_low = Column(Float, name=EliteCandleColumnNames.BID_LOW)
    bid_close = Column(Float, name=EliteCandleColumnNames.BID_CLOSE)
    mid_open = Column(Float, name=EliteCandleColumnNames.MID_OPEN)
    mid_high = Column(Float, name=EliteCandleColumnNames.MID_HIGH)
    mid_low = Column(Float, name=EliteCandleColumnNames.MID_LOW)
    mid_close = Column(Float, name=EliteCandleColumnNames.MID_CLOSE)
    ask_open = Column(Float, name=EliteCandleColumnNames.ASK_OPEN)
    ask_high = Column(Float, name=EliteCandleColumnNames.ASK_HIGH)
    ask_low = Column(Float, name=EliteCandleColumnNames.ASK_LOW)
    ask_close = Column(Float, name=EliteCandleColumnNames.ASK_CLOSE)
