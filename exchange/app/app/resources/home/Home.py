
from flask import render_template, flash, redirect, request, session, abort, url_for
from flask_login import current_user
from flask.views import MethodView
from .Forms import LoginForm, RegistrationForm

class HomeView(MethodView):

    def get(self):

    	if current_user.is_authenticated:
    		return redirect(url_for("main.main"))

    	registrationForm = RegistrationForm(prefix = 'register')
    	loginForm = LoginForm(prefix = 'login')
    	return render_template('home.html', loginForm = loginForm, registrationForm=registrationForm)
