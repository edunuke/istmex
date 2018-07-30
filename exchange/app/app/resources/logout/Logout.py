from flask import redirect, render_template, flash, request, url_for, session
from flask_login import login_user, current_user, login_required, logout_user
from app.models.User import *
from flask.views import MethodView
from app.resources.home.Forms import LoginForm, RegistrationForm
from flask import jsonify

class LogoutView(MethodView):
    def get(self):
	    logout_user()
	    return redirect("/")