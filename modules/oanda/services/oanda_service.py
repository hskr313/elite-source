import os

from dateutil import parser
from dotenv import load_dotenv

load_dotenv('config/.env')

from requests import Session

from elite_core.features.exchange.services.abstract_exchange_service import AbstractExchangeService

import pandas as pd
from datetime import datetime as dt

import logging


class OandaService(AbstractExchangeService):
    def __init__(self, base_api_url: str, session):
        self.base_api_url = base_api_url
        self.session = session
        self.session.headers.update({
            "Authorization": f"Bearer {os.environ.get('OANDA_DEMO_API_KEY')}",
            "Content-Type": "application/json"
        })
        print(os.environ.get('OANDA_DEMO_API_KEY'))
        super().__init__(self.base_api_url, self.session)

    def get_session(self) -> Session:
        return self.session

    def get_pairs(self):
        url = self._build_url(f"accounts/{os.environ.get('OANDA_DEMO_ACCOUNT_ID')}/instruments")
        instruments = self._get(url)

        if instruments:
            return instruments['instruments']
        else:
            raise Exception('Instruments empty')

    def get_account_summary(self):
        url = self._build_url(f"accounts/{os.environ.get('OANDA_DEMO_ACCOUNT_ID')}/summary")
        summary = self._get(url)

        if summary:
            return summary['summary']
        else:
            raise Exception('Summary empty')

    def get_candles_dict_by_pair(self, pair_name, granularity: str = 'H1', price: str = 'MBA'
                                 , date_from: dt = None, date_to: dt = None, count: int = 10):
        url = self._build_url(f"instruments/{pair_name}/candles")

        params = dict(
            granularity=granularity,
            price=price
        )

        if date_from is not None and date_to is not None:
            date_format = "%Y-%m-%dT%H:%M:%SZ"
            params["from"] = dt.strftime(date_from, date_format)
            params["to"] = dt.strftime(date_to, date_format)
        else:
            params["count"] = count

        candles = self._get(url, params)

        if candles:
            candles = candles['candles']
            return candles
        else:
            logging.warning(f"Candles for {pair_name} are empty")
            return None

    def get_candles_df_by_pair(self, pair_name, **kwargs):
        data = self.get_candles_dict_by_pair(pair_name, **kwargs)

        if data is None:
            return None
        if len(data) == 0:
            return pd.DataFrame()

        prices = ['mid', 'bid', 'ask']
        ohlc = ['o', 'h', 'l', 'c']

        final_data = []
        for candle in data:
            if not candle['complete']:
                continue
            new_dict = {}
            new_dict['time'] = parser.parse(candle['time'])
            new_dict['volume'] = candle['volume']
            for p in prices:
                if p in candle:
                    for o in ohlc:
                        new_dict[f"{p}_{o}"] = float(candle[p][o])
            final_data.append(new_dict)
        df = pd.DataFrame.from_dict(final_data)
        return df
