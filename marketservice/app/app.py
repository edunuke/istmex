from resources.ohlc import ohlcHist,updateOhlc
from resources.orderbook import orderbook
from resources.price import price
from resources.summary import summary 
from resources.trades import trades
import threading

#Initialize threads
thread_ohlcHist= threading.Thread(name="ohlcHist", target=ohlcHist)
thread_updateOhlc = threading.Thread(name="updateOhlc", target=updateOhlc)
thread_orderbook = threading.Thread(name="orderbook", target=orderbook)
thread_price = threading.Thread(name="price", target=price)
thread_summary = threading.Thread(name="summary", target=summary)
thread_trades = threading.Thread(name="trades", target=trades)
#start threads
thread_ohlcHist.start()
thread_updateOhlc.start()
thread_orderbook.start()
thread_price.start()
thread_summary.start()
thread_trades.start()
