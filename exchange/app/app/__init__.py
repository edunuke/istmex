from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_debugtoolbar import DebugToolbarExtension
from app.packages.auth import authorized
from flask_wtf.csrf import CSRFProtect
from flask_socketio import SocketIO
import threading
#from flasgger import Swagger



app = Flask(__name__)
app.config.from_object('config')


db = SQLAlchemy(app)
lm = LoginManager(app)
csrf = CSRFProtect(app)
socketio = SocketIO(app)

#swagger = Swagger(app)


#Register the blueprints from config (ENABLED_VIEWS)

def register_blueprints(app):
    from config_resources import ENABLED_RESOURCES
    for resource in ENABLED_RESOURCES:
        resourceClass_ = __import__(resource, fromlist=['Resource'])
        getResource = resourceClass_.Resource()
        app.register_blueprint(getResource.get_blueprint())


register_blueprints(app)

app.jinja_env.globals['authorized'] = authorized

#if debugging is enabled, add the debug toolbar
if app.debug:
    toolbar = DebugToolbarExtension(app)


#User loader for flask-login
from app.models.User import User
@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


if __name__ == '__main__':
    #app.run()
    socketio.run(app)
