from app import db

class Base(db.Model):
	"""
	Base class that all other classes inherits
	"""

	__abstract__ = True

	created_on = db.Column(db.DateTime,
                            default=db.func.now(), 
                            nullable = False)

	updated_on = db.Column(db.DateTime, 
                            default=db.func.now(),
                            onupdate=db.func.now(),
							nullable = False)