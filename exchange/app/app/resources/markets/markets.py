from flask import redirect, render_template, flash, request, url_for, session, Response
from flask_login import login_user, current_user, login_required, logout_user
from flask.views import MethodView
from flask import jsonify,json
from app import mongo
from bson.json_util import dumps


class MarketsView(MethodView):
	def __init__(self, *args, **kwargs):
		self.base_url = "https://api.cryptowat.ch/markets"
	
	def hist(self,exchange,pair):
		if current_user.is_authenticated:
			db = mongo[exchange+"_"+pair]
			coll = db[request.method.lower()]
			data = coll.find().sort([('_id', -1)]).limit(1)  
			return dumps({"data":data[0]})
		else:
			return redirect('/')

	def summary(self,exchange,pair):
		if current_user.is_authenticated:
			db = mongo[exchange+"_"+pair]
			coll = db[request.method.lower()]
			data = coll.find().sort([('time', -1)]).limit(24)  
			return dumps({"data":data})
		else:
			return redirect('/')