from common.config import config
from common.mongodb import client
from common.market import MarketResource
import time, datetime

exchange =config["exchange"]
pair =config["pair"]
resource = "ohlc"
starttime=time.time()
market = MarketResource()

#since jan 1st 2018 only 1514764800

def Historical():
    try:
        while True:
            repeat = 30.0
            ytd = datetime.date(datetime.datetime.now().year,1,1)
            ytd_unix= int(time.mktime(ytd.timetuple()))
            market_db = client[exchange+"_"+pair]
            resource_coll = market_db["hist"]
            data = market.fetch(exchange,pair,resource,
                                after = ytd_unix,
                                periods = 43200)
            resource_coll.insert_one(data)
            time.sleep(repeat - ((time.time() - starttime) % repeat))
    except KeyboardInterrupt:
        print("process stopped")


def Ohlc():
    try:
        while True:
            repeat = 30.0
            market_db = client[exchange+"_"+pair]
            resource_coll = market_db[resource]
            data = market.fetch(exchange,pair,resource,
                                after = int(time.time()-repeat),
                                periods = 60)
            resource_coll.insert_one(data)
            time.sleep(repeat - ((time.time() - starttime) % repeat))
    except KeyboardInterrupt:
        print("process stopped")