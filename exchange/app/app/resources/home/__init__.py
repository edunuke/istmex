from flask import Blueprint
from .Home import HomeView

home = Blueprint('home',__name__, template_folder='templates', static_folder='static', static_url_path = '/home/static')

home.add_url_rule('/', view_func=HomeView.as_view('home'), methods=['GET'])

class Resource:
    def get_blueprint(self):
        return home