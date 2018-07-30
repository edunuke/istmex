import falcon
import simplejson as json
from common.auth.rpc import (RsaResource,
                             RpcConnection)


class AddressResource(object):

    def on_get(self, req, resp, userid):
        resp.content_type = 'application/json'
        try:
            credentials = RsaResource().getCredentials()
            rpcconnection = RpcConnection().connect(credentials)
            resp.status = falcon.HTTP_200
            if userid != "all":
                message = rpcconnection.getbalance(userid)
                resp.body = json.dumps({"status": 1,
                                        "message": "account info",
                                        "data": {"userid": int(userid),
                                                 "address": message}})
            else:
                message = rpcconnection.listaccounts()
                resp.body = json.dumps({"status": 1,
                                        "message": "All accounts balance",
                                        "data": message})
        except BaseException:
            resp.body = json.dumps({"status": 0,
                                    "message": "Something Wrong",
                                    "data": None})
            resp.status = falcon.HTTP_404
        pass

    def on_post(self, req, resp, userid):
        resp.content_type = 'application/json'
        try:
            credentials = RsaResource().getCredentials()
            rpcconnection = RpcConnection().connect(credentials)
            resp.status = falcon.HTTP_200
            message = rpcconnection.getnewaddress(userid)
            resp.body = json.dumps({"status": 1,
                                    "message": "Address key creted",
                                    "data": {"userid": int(userid),
                                             "address": message}})
        except BaseException:
            resp.body = json.dumps({"status": 0,
                                    "message": "Something Wrong",
                                    "data": None})
            resp.status = falcon.HTTP_404
        pass


class GiveMoney (object):

    def on_get(self,  req, resp, userid):
        resp.content_type = 'application/json'
        try:
            credentials = RsaResource().getCredentials()
            rpcconnection = RpcConnection().connect(credentials)
            resp.status = falcon.HTTP_200

            address = rpcconnection.getaccountaddress(userid)
            rpcconnection.generatetoaddress(101, address, 100)

            message = rpcconnection.getbalance(userid)
            resp.body = json.dumps({"status": 1,
                                    "message": "All accounts balance",
                                    "data": message})
        except BaseException:
            resp.body = json.dumps({"status": 0,
                                    "message": "Something Wrong",
                                    "data": None})
            resp.status = falcon.HTTP_404
        pass
        