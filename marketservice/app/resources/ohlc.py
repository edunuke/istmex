import multiprocessing
import requests
import time
from common.mongodb import client






class MarketResource(object):
	def __init__(self):
		self.base_url = "https://api.cryptowat.ch/markets"
	
	def fetch(self,exchange,pair,resource,**kwargs):
		after=int(time.time())
		route ="/%s/%s/%s" % tuple([exchange,pair,resource])
		
		market = client[exchange+"_db"]
		resource_coll = market [resource]

		while True:
			repeat = 10.0
			if "after" in kwargs :
				after = int(time.time())
				params = {"after":after,"periods":"60"}
			else:
				params = {}
			
			data = requests.get(self.base_url + route,
								params=params).json()
			resource_coll.insert_one(data)
			time.sleep(repeat - ((time.time() - starttime) % repeat))
			return

market = MarketResource()

def ohlc():
	market.fetch("gdax","btcusd","ohlc")
	return


def summary():
	market.fetch("gdax","btcusd","summary")
	return

def trades():
	market.fetch("gdax","btcusd","trades")
	return

def orderbook():
	market.fetch("gdax","btcusd","orderbook")
	return

