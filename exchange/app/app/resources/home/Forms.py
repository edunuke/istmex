from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, validators, SubmitField, HiddenField
from wtforms.validators import InputRequired, Regexp, Email, DataRequired


class RegistrationForm(FlaskForm):

    username = StringField('Username', 
    						validators=[Regexp('^\w+$', message="Only letters allowed"),
    						InputRequired(message="First name required")])

    email = StringField('Email', 
    					validators=[Email(message="Please check the email format"),
    					InputRequired(message="Email required")])

    password = PasswordField('Password', 
    					validators=[InputRequired(message="Password required")])

    accept_tos = BooleanField('I accept the terms of service',
                        validators=[InputRequired(message="Please Accept Terms of Service")])

    submit = SubmitField("register")


class LoginForm(FlaskForm):

    email = StringField('Email', 
                        validators=[Email(message="Please check the email format"),
                        InputRequired(message="Email required")])

    password = PasswordField('Password', [InputRequired(message="Password required")])

    remember_me = BooleanField('remember_me')
    do = HiddenField()
    
    submit = SubmitField("login")