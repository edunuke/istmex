import os
from datetime import timedelta


basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'CEYB[zd]kSe$=[/V4.l2@~bPmNek1B&}Sr`.95{(kb?o@PH_LP5dQjhuT?g/0OP'

DEBUG_TB_INTERCEPT_REDIRECTS=True
DEBUG_TB_PROFILER_ENABLED = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_RECORD_QUERIES = True
DEBUG_TB_PANELS = [
    'flask_debugtoolbar.panels.versions.VersionDebugPanel',
    'flask_debugtoolbar.panels.timer.TimerDebugPanel',
    'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
    'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
    'flask_debugtoolbar.panels.template.TemplateDebugPanel',
    'flask_debugtoolbar.panels.logger.LoggingPanel',
    'flask_debugtoolbar.panels.profiler.ProfilerDebugPanel',
    'flask_debugtoolbar.panels.sqlalchemy.SQLAlchemyDebugPanel',
    'flask_debugtoolbar.panels.route_list.RouteListDebugPanel',
    'flask_debugtoolbar.panels.timer.TimerDebugPanel',
    'flask_debugtoolbar.panels.config_vars.ConfigVarsDebugPanel'

    ]


SQLALCHEMY_DATABASE_URI ="postgresql://postgres:test@postgres/postgres"
SQLALCHEMY_TRACK_MODIFICATIONS = False    # Avoids a SQLAlchemy Warning
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'database','migrations')


PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)

# mail server settings
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None

# administrator list
ADMINS = ['eduardo.denadai@gmail.com']

DEBUG = False

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND= 'redis://localhost:6379' 