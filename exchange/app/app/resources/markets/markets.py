from flask import redirect, render_template, flash, request, url_for, session, Response
from flask_login import login_user, current_user, login_required, logout_user
from flask.views import MethodView
from flask import jsonify,json
import requests
"""
if not current_user.is_authenticated:
	redirect("/")
"""

class MarketsView(MethodView):
	def get(self,exchange,pair,command):
		if current_user.is_authenticated:
    
			base_url = "https://api.cryptowat.ch/markets"
			endpoint = tuple([exchange,pair,command])
			if command == "ohlc":
				afterTime = request.args.get("after")
				if afterTime is not None: #need to fix this and main_olhc.js may be compare unixtimstamps less than incoming do something
					ohlc = requests.get(base_url +"/%s/%s/%s" % endpoint, params={"after":1514764800,"periods":"300"}).json()
					return jsonify({"data":ohlc})
				else:
					ohlc = requests.get(base_url +"/%s/%s/%s" % endpoint, params={"after":afterTime,"periods":"300"}).json()
					return jsonify({"data":ohlc})
			elif command == "price":
				price = requests.get(base_url +"/%s/%s/%s" % endpoint).json()
				return jsonify({"data":price})
			elif command == "summary":
				summary = requests.get(base_url +"/%s/%s/%s" % endpoint).json()
				return jsonify({"data":summary})
			elif command == "orderbook":
				orderbook = requests.get(base_url +"/%s/%s/%s" % endpoint).json()
				return jsonify({"data":orderbook})
			elif command == "trades":
				trades = requests.get(base_url +"/%s/%s/%s" % endpoint).json()
				return jsonify({"data":trades})
			else:
				return jsonify({"data":"error"})
		else:
			return redirect("/")