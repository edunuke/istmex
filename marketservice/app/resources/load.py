from resources.btc.ohlc import Historical,Ohlc
from resources.btc.orderbook import orderbook
from resources.btc.price import price
from resources.btc.summary import summary 
from resources.btc.trades import trades
import threading

#Declare threads
thread_Historical= threading.Thread(name="Historical", target=Historical)
#thread_Ohlc = threading.Thread(name="Ohlc", target=Ohlc)
thread_orderbook = threading.Thread(name="orderbook", target=orderbook)
#thread_price = threading.Thread(name="price", target=price)
thread_summary = threading.Thread(name="summary", target=summary)
thread_trades = threading.Thread(name="trades", target=trades)

btc_threads = [thread_Historical,
               #thread_Ohlc,
               thread_orderbook,
               #thread_price,
               thread_summary,
               thread_trades]
