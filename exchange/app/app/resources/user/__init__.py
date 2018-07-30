from .User import UserView
from flask import Blueprint


# user blueprints
user_blueprint = Blueprint('user',__name__, template_folder='templates')
user_view_func = UserView.as_view('user')
user_blueprint.add_url_rule('/user', defaults={'username': None}, view_func=user_view_func, methods=['GET',])
user_blueprint.add_url_rule('/user', view_func=user_view_func, methods=['POST',])
user_blueprint.add_url_rule('/user/<string:username>', view_func=user_view_func, methods=['GET', 'PUT', 'DELETE'])




class Resource:
    def get_blueprint(self):
        return user_blueprint
