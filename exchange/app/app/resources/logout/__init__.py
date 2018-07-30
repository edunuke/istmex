from .Logout import LogoutView
from flask import Blueprint

# login blueprints and views
logout_blueprint = Blueprint('logout',__name__, template_folder='templates')
logout_view_func = LogoutView.as_view('logout')
logout_blueprint.add_url_rule('/logout', view_func=logout_view_func, methods=['GET'])




class Resource:
    def get_blueprint(self):
        return logout_blueprint