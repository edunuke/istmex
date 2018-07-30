import json
from pathlib import Path
from requests import get
from bitcoinrpc.authproxy import AuthServiceProxy


class RsaResource(object):

    def __init__(self):
        with open(Path.cwd()
                      .joinpath('common')
                      .joinpath('auth')
                      .joinpath('utils')
                      .joinpath('hexkey'), 'rb') as file:
            self.hexkey = file.readlines()[0].decode('utf-8')

    def getCredentials(self):
        yourparams = {'key': self. hexkey}
        host = "btc-core"
        port = "5000"
        route = "validate"
        url = 'http://%s:%s/%s'
        resp = get(url % (host, port, route), params=yourparams)

        return json.loads(resp.json())


class RpcConnection(object):
    """ Connect to RPC server with valid credentials"""
    def connect(self, credentials={}):
        url = 'http://%s:%s@%s:%s'
        return AuthServiceProxy(url % (credentials['rpc_user'],
                                       credentials['rpc_password'],
                                       "btc-core",
                                       credentials['port']))
