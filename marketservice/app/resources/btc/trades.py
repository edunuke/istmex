import time
from common.config import config
from common.mongodb import client
from common.market import MarketResource

exchange =config["exchange"]
pair =config["pair"]
resource = "trades"
market = MarketResource()
starttime=time.time()

def trades():
    try:
        while True:
            repeat = 15.0
            market_db = client[exchange+"_"+pair]
            resource_coll = market_db[resource]
            data = market.fetch(exchange,pair,resource,
                                limit = 20,
                                since = int(time.time()-repeat))
            resource_coll.insert_one(data)
            time.sleep(repeat - ((time.time() - starttime) % repeat))
    except KeyboardInterrupt:
        print("process stopped")
