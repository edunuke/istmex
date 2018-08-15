import time
from common.config import config
from common.mongodb import client
from common.market import MarketResource

exchange =config["exchange"]
pair =config["pair"]
resource = "orderbook"
market = MarketResource()
starttime=time.time()

#since jan 1st 2018 only

def orderbook():
    try:
        while True:
            repeat = 30.0
            market_db = client[exchange+"_"+resource+"_db"]
            resource_coll = market_db[resource]
            data = market.fetch(exchange,pair,resource)
            resource_coll.insert_one(data)
            time.sleep(repeat - ((time.time() - starttime) % repeat))
    except KeyboardInterrupt:
        print("process stopped")
