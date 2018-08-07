import falcon
from resources.ohlc import OhlcResource




app = falcon.API()


app.add_route('/{exchange}/{pair}/{after}', OhlcResource())
