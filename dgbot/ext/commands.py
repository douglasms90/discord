from ext.database import base, engine, Session
from models import Act, Atv, Nail
import datetime


def dropdb():
    base.metadata.drop_all(engine)

def createdb():
    base.metadata.create_all(engine)

def insertdb():
    with Session() as session:
        #session.add(Act(id=1,dt=datetime.datetime(2023,1,17,18,2,0,0),usr='269592803602989058',ido='',sn='4D4B5047B4964348',ctr='65628',cto='M08'))
        #session.add(Nail(id=5,dt=datetime.datetime(2024,9,14,11,0,0,0),pr=40))
        session.commit()

def deletedb():
    with Session() as session:
        #session.query(Act).filter(Act.id == 100).delete()
        session.commit()

def updatedb():
    with Session() as session:
        #session.query(Act).filter(Act.id == 1).update({'id':1})
        #session.query(Nail).filter(Nail.id == 9).update({'id':10})
        #session.query(Nail).filter(Nail.id == 5).update({'dt':datetime.datetime(2024,9,13,14,0,0,0)})
        session.commit()
