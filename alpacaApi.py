import os
from alpaca_trade_api.rest import REST
from localSettings import alpaca_paper


class AlpacaApi():
    def __init__(self):
        os.environ['APCA_API_KEY_ID'] = alpaca_paper['api_key']
        os.environ['APCA_API_SECRET_KEY'] = alpaca_paper['secret_key']
        os.environ['APCA_API_BASE_URL'] = 'https://paper-api.alpaca.markets'
        self.api=REST()

