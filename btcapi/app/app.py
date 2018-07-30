import falcon
from resources.wallet import WalletResource
from resources.account import AddressResource, GiveMoney

app = falcon.API()
app.add_route('/wallet', WalletResource())
app.add_route('/account/{userid}', AddressResource())
app.add_route('/generate/{userid}', GiveMoney())