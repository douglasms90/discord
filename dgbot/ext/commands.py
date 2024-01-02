from ext.database import base, engine, session
from models import Act, Vln, Atv
import datetime


def dropdb():
    base.metadata.drop_all(engine)

def createdb():
    base.metadata.create_all(engine)

def insertdb():
    session.add_all([
        Atv(tp='rf',nm='inv',pm=79.18,qt=1,rc='',pa=79.68),#1
    ])
    session.commit()

def deletedb():
    session.query(Act).filter(Act.id == 1).delete()
    session.commit()

def updatedb():
    session.query(Vln).filter(Vln.id == 1).update({'olt':'OLT-VALENCA','tfc':'','vln':'1'})
    session.commit()

