from flask import Blueprint
from .Main import MainView
from flask_login import login_user, current_user, login_required, logout_user
from flask import redirect, render_template, flash, request, url_for, session

main_blueprint = Blueprint('main',__name__, template_folder='templates', static_folder='static', static_url_path = '/main/static')
main_view_func = MainView.as_view('main')
main_blueprint.add_url_rule('/main', view_func=main_view_func, methods=['GET','POST',])

class Resource:
    def get_blueprint(self):
        return main_blueprint