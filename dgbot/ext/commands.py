from ext.database import base, engine, session
from models import Act, Vln, Atv
import datetime


def dropdb():
    base.metadata.drop_all(engine)

def createdb():
    base.metadata.create_all(engine)

def insertdb():
    session.add(Act(id=100,dt=datetime.datetime(2023,2,8,14,15),usr='_douglasms_',olt='OLT-PIRAI-AFRODITE',tfc='0/17/2:',sn='4D4B5047B458F4F8',vln='734',ctr='65961',cto='C04'))
    session.commit()

def deletedb():
    session.query(Act).filter(Act.id == 100).delete()
    session.commit()

def updatedb():
    session.query(Atv).filter(Atv.id == 208).update({'id':201})
    session.commit()

