from common.config import config
from common.mongodb import client
from common.market import MarketResource
import time

exchange =config["exchange"]
pair =config["pair"]
resource = "ohlc"
starttime=time.time()
market = MarketResource()

#since jan 1st 2018 only 1514764800

def ohlcHist():
    try:
        while True:
            repeat = 1*60*60*24
            market_db = client[exchange+"_"+resource+"_db"]
            resource_coll = market_db[resource]
            data = market.fetch(exchange,pair,resource,
                                after = int(time.time()-repeat),
                                periods = 60)
            resource_coll.insert_one(data)
            time.sleep(repeat - ((time.time() - starttime) % repeat))
    except KeyboardInterrupt:
        print("process stopped")


def updateOhlc():
    try:
        while True:
            repeat = 15.0
            market_db = client[exchange+"_"+resource+"_db"]
            resource_coll = market_db[resource]
            data = market.fetch(exchange,pair,resource,
                                after = int(time.time()-repeat),
                                periods = 60)
            resource_coll.insert_one(data)
            time.sleep(repeat - ((time.time() - starttime) % repeat))
    except KeyboardInterrupt:
        print("process stopped")