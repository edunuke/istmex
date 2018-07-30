from flask import redirect, render_template, flash, request, url_for, session
from flask_login import login_user, current_user, login_required, logout_user
from app.models.User import *
from flask.views import MethodView
from app.resources.home.Forms import LoginForm, RegistrationForm
from flask import jsonify

class MainView(MethodView):
	def get(self):

		if not current_user.is_authenticated:
			return redirect("/")
		
		else:

			return render_template('main.html',
								   userdata=current_user.username)


	def post(self):
		return redirect("/")
