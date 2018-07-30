from app import db

user_group = db.Table('user_group',
   db.Column('group_id',db.Integer,
                db.ForeignKey('groups.id', onupdate='CASCADE', ondelete='CASCADE'),
                primary_key=True),
   db.Column('user_id',db.Integer,
                db.ForeignKey('users.id', onupdate='CASCADE', ondelete='CASCADE'),
                primary_key=True)
)

group_permission = db.Table('group_permission',
    db.Column('group_id', db.Integer,
           db.ForeignKey('groups.id', onupdate='CASCADE', ondelete='CASCADE'),
           primary_key=True),
    db.Column('permission_id', db.Integer,
           db.ForeignKey('permissions.id', onupdate='CASCADE', ondelete='CASCADE'),
           primary_key=True)
)

class Group(db.Model):
    __tablename__ = 'groups'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique = True)

    permissions = db.relationship('Permission', secondary=group_permission, collection_class=set,
                                    backref=db.backref('groups', collection_class=set, lazy='dynamic'))

    def __repr__(self):
        return '<%s(%r, %r)>' % (self.__class__.__name__, self.id,
                                 self.name)
