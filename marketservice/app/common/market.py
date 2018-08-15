import requests
#from common.mongodb import client


class MarketResource(object):
    def __init__(self):
        self.base_url = "https://api.cryptowat.ch/markets"
    
    def fetch(self,exchange,pair,resource,**kwargs):
        route ="/%s/%s/%s" % tuple([exchange,pair,resource])
        if bool(kwargs):
            params = kwargs
        else:
            params = None
        
        data = requests.get(self.base_url + route, params=params).json()
        return data
