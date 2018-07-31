from flask import Blueprint
from .markets import MarketsView
from flask_login import login_user, current_user, login_required, logout_user
from flask import redirect, render_template, flash, request, url_for, session



markets_blueprint = Blueprint('markets',__name__)
markets_view_func = MarketsView.as_view('markets')

markets_blueprint.add_url_rule('/<string:exchange>/<string:pair>',
							   view_func=markets_view_func, 
                               methods=['price',
                                        'summary',
                                        'orderbook',
                                        'trades',
                                        'update'])

markets_blueprint.add_url_rule('/<string:exchange>/<string:pair>/<int:after>',
							   view_func=markets_view_func, 
                               methods=['ohlc'])

class Resource:
    def get_blueprint(self):
        return markets_blueprint
