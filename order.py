class Order():
    def __init__(self,api):
        self.api = api
    def marketBuy(self,sym,amount):
        self.api.submit_order(
            symbol=sym,
            qty=amount,
            side='buy',
            type='market',
            time_in_force='gtc'
        )

    def marketSell(self,sym,amount):
        self.api.submit_order(
            symbol=sym,
            qty=amount,
            side='sell',
            type='market',
            time_in_force='gtc'
        )
    

