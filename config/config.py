from decouple import config


class EnvConfig:
    OANDA_DEMO_ACCOUNT_ID = config('OANDA_DEMO_ACCOUNT_ID')
    OANDA_DEMO_API_KEY = config('OANDA_DEMO_API_KEY')
    OANDA_DEMO_API_URL = config('OANDA_DEMO_API_URL')
    OANDA_CANDLE_COUNT = config('OANDA_CANDLE_COUNT')

    # REGION DB
    DB_NAME = config('DB_NAME')
    DB_URL = config('DB_URL')
    DB_PASSWORD = config('DB_PASSWORD')
    #
