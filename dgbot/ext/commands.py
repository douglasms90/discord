from ext.database import base, engine, session
from models import Act, Vln, Atv
import datetime


def dropdb():
    base.metadata.drop_all(engine)

def createdb():
    base.metadata.create_all(engine)

def insertdb():
    session.add_all([
        Atv(id=99,tp='fundos-imobiliarios',nm='kncr11',pm=101,qt=1,rc='',pa=101),
    ])
    session.commit()

def deletedb():
    session.query(Atv).filter(Atv.id == 99).delete()
    session.commit()

def updatedb():
    session.query(Atv).filter(Atv.id == 108).update({'id':'208'})
    session.commit()

