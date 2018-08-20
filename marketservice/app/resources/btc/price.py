import time
from common.config import config
from common.mongodb import client
from common.market import MarketResource

exchange =config["exchange"]
pair =config["pair"]
resource = "price"
market = MarketResource()
starttime=time.time()

def price():
    try:
        while True:
            repeat = 10.0
            market_db = client[exchange+"_"+pair]
            resource_coll = market_db[resource]
            data = {"time":int(time.time()),
                    "data":market.fetch(exchange,pair,resource)
                    }
            resource_coll.insert_one(data)
            time.sleep(repeat - ((time.time() - starttime) % repeat))
    except KeyboardInterrupt:
        print("process stopped")
