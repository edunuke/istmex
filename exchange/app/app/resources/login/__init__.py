from .Login import LoginView
from flask import Blueprint

# login blueprints and views
login_blueprint = Blueprint('login',__name__, template_folder='templates')
login_view_func = LoginView.as_view('login')
login_blueprint.add_url_rule('/login', view_func=login_view_func, methods=['POST'])


class Resource:
    def get_blueprint(self):
        return login_blueprint
