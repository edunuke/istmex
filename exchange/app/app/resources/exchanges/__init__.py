from flask import Blueprint
from .exchanges import Exchanges
from flask_login import login_user, current_user, login_required, logout_user
from flask import redirect, render_template, flash, request, url_for, session

exchanges = Blueprint('exchange',__name__)
exchangeResource = Exchanges.as_view('exchange')

exchanges.add_url_rule('/main/exchange/',
						defaults={'exchangename': None},
						view_func=exchangeResource, methods=['GET',])

exchanges.add_url_rule('/main/exchange/<string:exchangename>', 
						view_func=exchangeResource, methods=['GET',])

class Resource:
    def get_blueprint(self):
        return exchanges
