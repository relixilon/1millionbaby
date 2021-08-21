from stream import GetStream
from order import Order
from alpacaApi import AlpacaApi
from localSettings import alpaca_paper

alpaca = AlpacaApi()

stream1 = GetStream()
stream1.trades('SPY')

buyGme = Order(alpaca.api)

buyGme.marketBuy('GME',100)

x = alpaca.api.list_positions()
 
print(x)
