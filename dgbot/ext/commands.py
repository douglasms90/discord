from ext.database import base, engine, session
from models import Act, Vln, Atv
import datetime


def dropdb():
    base.metadata.drop_all(engine)

def createdb():
    base.metadata.create_all(engine)

def insertdb():
    session.add_all([
        Atv(id=35,tp='criptomoedas',nm='beth',pm=1,qt=0.18710108,rc='',pa=0),
    ])
    session.commit()

def deletedb():
    session.query(Atv).filter(Atv.id == 35).delete()
    session.commit()

def updatedb():
    session.query(Vln).filter(Vln.id == 1).update({'olt':'OLT-VALENCA','tfc':'','vln':'1'})
    session.commit()

