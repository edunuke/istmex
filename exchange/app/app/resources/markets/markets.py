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
	def __init__(self, *args, **kwargs):
		self.base_url = "https://api.cryptowat.ch/markets"
	
	def ohlc(self,exchange,pair,after):
		if current_user.is_authenticated:
			endpoint = tuple([exchange,pair])
			ohlc = requests.get(self.base_url +"/%s/%s/ohlc" % endpoint, 
								params={"after":after,"periods":"60"}).json()
			return jsonify({"data":ohlc})
		else:
			return redirect('/')

	def price(self,exchange,pair):
		if current_user.is_authenticated:
			endpoint = tuple([exchange,pair])
			price = requests.get(self.base_url +"/%s/%s/price" % endpoint).json()
			return jsonify({"data":price})
		else:
			return redirect('/')
	
	def summary(self,exchange,pair):
		if current_user.is_authenticated:
			endpoint = tuple([exchange,pair])
			summary = requests.get(self.base_url +"/%s/%s/summary" % endpoint).json()
			return jsonify({"data":summary})
		else:
			return redirect('/')
	
	def orderbook(self,exchange,pair):
		if current_user.is_authenticated:
			endpoint = tuple([exchange,pair])
			orderbook = requests.get(self.base_url +"/%s/%s/orderbook" % endpoint).json()
			return jsonify({"data":orderbook})
		else:
			return redirect('/')
	
	def trades(self,exchange,pair):
		if current_user.is_authenticated:
			endpoint = tuple([exchange,pair])
			trades = requests.get(self.base_url +"/%s/%s/trades" % endpoint).json()
			return jsonify({"data":trades})
		else:
			return redirect('/')