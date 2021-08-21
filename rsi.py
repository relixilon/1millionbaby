import numpy
import talib
from alpacaApi import AlpacaApi

close = numpy.random.random(100)

x = talib.SMA(close)

print(x)