from decouple import config


class EnvConfig:
    def __init__(self):
        self.OANDA_DEMO_ACCOUNT_ID = config('OANDA_DEMO_ACCOUNT_ID')
        self.OANDA_DEMO_API_KEY = config('OANDA_DEMO_API_KEY')
        self.OANDA_DEMO_API_URL = config('OANDA_DEMO_API_URL')
        self.OANDA_CANDLE_COUNT = config('OANDA_CANDLE_COUNT')

        # REGION DB
        self.DB_NAME = config('DB_NAME')
        self.DB_URL = config('DB_URL')
        self.DB_PASSWORD = config('DB_PASSWORD')
        #
