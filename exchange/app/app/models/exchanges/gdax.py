"""from app import db

class Historic(db.Model):


    id = db.Column(db.Integer, primary_key = True, unique=True)
    time_ = db.Column(db.Integer, nullable=False)
    low_ = db.Column(db.Float, nullable=False, unique=False)
    high_ = db.Column(db.Float, nullable=False, unique = False)
    open_ = db.Column(db.Float, nullable=False, unique = False)
    close_ = db.Column(db.Float, nullable=False, default=False)
    volume_ = db.Column(db.Float, nullable=False, default=False)"""