from ext.database import base, engine, session
from models import Act, Vln, Atv
import datetime


def dropdb():
    base.metadata.drop_all(engine)

def createdb():
    base.metadata.create_all(engine)

def insertdb():
    session.add(Atv(id=100,tp='rf',nm='test',pm=1,qt=1,rc='N',pa=1))
    session.commit()

def deletedb():
    session.query(Atv).filter(Atv.id == 100).delete()
    session.commit()

def updatedb():
    session.query(Atv).filter(Atv.id == 208).update({'id':201})
    session.commit()

