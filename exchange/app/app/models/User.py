from flask_login import UserMixin
from app import db
from app.packages.auth.hash_passwords import check_hash, make_hash
from app.models.auth.Group import *
from app.models.auth.Permission import *
from app.models.Base import *
from flask import jsonify

class User(UserMixin ,  Base):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True, unique=True)
    username = db.Column(db.Text, nullable=False, unique=False)
    email = db.Column(db.String(120), nullable=False, unique = True)
    _password = db.Column('password', db.Text, nullable=False)
    confirmed = db.Column(db.Boolean, nullable=False, default=False)

    groups = db.relationship('Group',
                             secondary=user_group,
                             collection_class=set,
                             backref=db.backref('users', collection_class=set, lazy='dynamic'))

    def _set_password(self, password):
        self._password = make_hash(password)

    def _get_password(self):
        return self._password

    password = db.synonym('_password', descriptor=property(_get_password,
                                                        _set_password))
    def is_authenticated(self):
        return True

    def valid_password(self, password):
        """Check if provided password is valid."""
        return check_hash(password, self.password)

    def is_active(self):
        return self.active

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return '<%s(%r, %r)>' % (self.__class__.__name__, self.id,
                                 self.email)

    def in_groups(self):
        """Return set of groups which user belongs to."""
        perms = set(r.name for r in Group.query.join(Group.users).filter(User.id == self.id).all())
        return perms

    def has_permissions(self):
        """Return set of permissions which user has."""
        perms = set(r.name for r in Permission.query.join(Permission.groups, Group.users).filter(User.id == self.id).all())
        return perms

    def get_name(self):
        return jsonify(username = self.username)
