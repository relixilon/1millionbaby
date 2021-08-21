from alpaca_trade_api.rest import URL
from alpaca_trade_api.stream import Stream

class GetStream():
    def __init__(self):
        self.stream = Stream('PK283PDY341ZEJZNMVMC',
            'Sy7aoWwzicwEaqg23RAQ64XRD6bPPT1z5xmHqFRa',
            base_url=URL('https://paper-api.alpaca.markets'),
            data_feed='iex')


    async def callback(self,x):
        print(x)

    def trades(self,ticker):
        self.stream.subscribe_trades(self.callback,ticker)
        self.stream.run()
    def quotes(self,ticker):
        self.stream.subscribe_quotes(self.callback,ticker)
        self.stream.run()