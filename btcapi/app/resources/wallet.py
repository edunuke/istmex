import falcon
import simplejson as json
from common.auth.rpc import (RsaResource,
                             RpcConnection)


class WalletResource(object):

    def on_get(self, req, resp):
        resp.content_type = 'application/json'

        try:

            credentials = RsaResource().getCredentials()
            rpcconnection = RpcConnection().connect(credentials)
            resp.status = falcon.HTTP_200
            message = rpcconnection.getwalletinfo()
            resp.body = json.dumps({"status": 1,
                                    "message": "Wallet info",
                                    "data": message})
        except BaseException:
            resp.body = json.dumps({"status": 0,
                                    "message": "Something wrong",
                                    "data": None})

            resp.status = falcon.HTTP_404
        pass

    def on_post(self, req, resp, userid):

        resp.content_type = 'application/json'

        pass