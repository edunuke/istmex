from flask import redirect, render_template, flash, request, url_for, session
from flask_login import login_user, current_user, login_required, logout_user
from app import db
from app.models.auth.Group import *
from app.models.auth.Permission import *
from app.models.User import *
from flask.views import MethodView
from app.resources.home.Forms import RegistrationForm
from flask import jsonify

class UserView(MethodView):
	def post(self):
		form = RegistrationForm(request.form, prefix='register')
		if User.query.filter_by(email=form.email.data).first():
    			return jsonify(status = 'error', message ="#register-email")
		print(request.form)
		if form.validate_on_submit():
			new_user = User(username=form.username.data,
						password=form.password.data,
						email= form.email.data,
						confirmed=False)



			db.session.add(new_user)
			db.session.commit()
			login_user(new_user, remember=False)
			session['remember_me'] = False
			session['logged_in'] = True
			
			flash('A confirmation email has been sent via email.', 'success')
			return jsonify(status = 'success', message = url_for("main.main"))

			
		else:
			return jsonify(status='validation', message = form.errors)