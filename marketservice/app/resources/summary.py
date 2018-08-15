import time
from common.config import config
from common.mongodb import client
from common.market import MarketResource

exchange =config["exchange"]
pair =config["pair"]
resource = "summary"
market = MarketResource()
starttime=time.time()

def summary():
    try:
        while True:
            repeat = 1*60*60*24
            market_db = client[exchange+"_"+resource+"_db"]
            resource_coll = market_db[resource]
            data = market.fetch(exchange,pair,resource)
            resource_coll.insert_one(data)
            time.sleep(repeat - ((time.time() - starttime) % repeat))
    except KeyboardInterrupt:
        print("process stopped")