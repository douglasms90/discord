from ext.database import base, engine, session
from models import Act, Atv, Test
import datetime


def dropdb():
    base.metadata.drop_all(engine)

def createdb():
    base.metadata.create_all(engine)

def insertdb():
    #session.add(Act(id=1,dt=datetime.datetime(2023,1,17,18,2,0,0),usr='269592803602989058',ido='',sn='4D4B5047B4964348',ctr='65628',cto='M08'))
    session.commit()

def deletedb():
    #session.query(Act).filter(Act.id == 100).delete()
    session.commit()

def updatedb():
    #session.query(Act).filter(Act.id == 1).update({'id':1})
    session.commit()
