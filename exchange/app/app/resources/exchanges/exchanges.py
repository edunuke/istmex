from flask import redirect, render_template, flash, request, url_for, session, Response
from flask_login import login_user, current_user, login_required, logout_user
from flask.views import MethodView
from flask import jsonify, json
import gdax

public_client = gdax.PublicClient()

"""
if not current_user.is_authenticated:
	pass
"""
class Exchanges(MethodView):

	def get(self,exchangename):

		if exchangename is None:
			#serve all exchanges
			values = public_client.get_product_historic_rates('ETH-USD', granularity=60)
			data= list()
			#time, low, high, open, close, volume
			for point in values:
			    schema = {'time': point[0],
			            'low': point[1],
			            'high': point[2],
			            'open': point[3],
			            'close': point[4],
			            'volume': point[5],
			            }
			    data.append(schema)
			return Response(json.dumps(data),  mimetype='application/json')
		else:
			#serve single exchange
			return jsonify(status="success",
							message = "single gdax")
    
	def post(self):
		pass

	def delete(self, username):
		return 'delete'

	def put(self, username):
		return 'put'
