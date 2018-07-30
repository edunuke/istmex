import sys
import os
from app import app
from flask_script import Manager, Server
from app.packages.gunicornserver import GunicornServer
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..//')))


manager = Manager(app)

##########################################

#	Manager commands for server management

##########################################


#Start up in non-debug mode


manager.add_command("gunit", GunicornServer())


##########################################

#	Manager commands for database management

##########################################



from database.utils.db_reset import ResetDB
@manager.command
def resetdb():
	"""Reset the user database to defaults"""
	with app.app_context():
		ResetDB()

#Create the user DB
from database.utils.db_create import CreateDB
@manager.command
def createdb():
	"""Create the user database"""
	with app.app_context():
		CreateDB()
from database.utils.db_downgrade import DowngradeDB
@manager.command
def downgradedb():
	"""Downgrade the user DB"""
	with app.app_context():
		DowngradeDB()
from database.utils.db_upgrade import UpgradeDB
@manager.command
def upgradedb():
	"""Upgrade the user database"""
	with app.app_context():
		UpgradeDB()

from database.utils.db_migrate import MigrateDB
@manager.command
def migratedb():
	"""Migrate the user database to the latest version"""

	with app.app_context():
		MigrateDB()

from database.utils.db_init import InitDB
@manager.command
def initdb():
	"""Initialise the user database with test data"""
	with app.app_context():
		InitDB()

if __name__ == "__main__":
	manager.run()
