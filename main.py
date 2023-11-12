from di.container import Container
from modules.oanda.model.dtos.candle_stick_dto import CandleStickDTO

if __name__ == '__main__':
    container = Container()

    # candles = container.oanda_service().get_candles_dict_by_pair('EUR_USD')
    #
    # candles = CandleStickDTO.to_elite_candles(candles)
    #
    # for candle in candles:
    #     print(candle.mid_open)
    #     print(candle.mid_low)
    #     print(candle.mid_high)
    #     print(candle.mid_close)
    #     print(candle.complete)


