from app import db
from app.models.auth.Group import *
from app.models.auth.Permission import *
from app.models.User import *
from app.models.exchanges.gdax import *

def InitDB():
    
    db.drop_all()
    db.create_all()


    print ("Pre-populating DB")
    p1 = Permission(name=u'read')
    p2 = Permission(name=u'write')
    p3 = Permission(name=u'delete')

    g1 = Group(name=u'Administrator')
    g2 = Group(name=u'Developer')
    g3 = Group(name=u'User')

    u1 = User(username=u'foo_admin', password=u'adminpass',email='admin@example.com', confirmed=True)
    u2 = User(username=u'member1', password=u'test', email='member1@example.com', confirmed=True)
    u3 = User(username=u'member2', password=u'test',email='member2@example.com', confirmed=True)

    g1.permissions = set([p1,p2,p3])
    g2.permissions = set([p1,p2])
    g3.permissions = set([p1])

    u1.groups = set([g1,g2])
    u2.groups = set([g2])
    u3.groups = set([g3])

    #historic = Historic(time_=1415398768, low_=0.32, high_=4.2, open_=0.35,close_=4.2, volume_= 12.3)

    db.session.add_all([u1,u2,u3])
    #db.session.add(historic)
    db.session.commit()

    users = User.query.all()

    for u in users:
        print (u)
        for g in u.in_groups():
            print ('\t%s' % g)
        for p in u.has_permissions():
            print ('\t\t%s' % p)


