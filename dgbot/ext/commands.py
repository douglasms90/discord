from ext.database import base, engine, session
from models import Act, Vln
import datetime


def dropdb():
    base.metadata.drop_all(engine)

def createdb():
    base.metadata.create_all(engine)

def insertdb():
    session.add_all([
        Vln(olt='OLT-SANTANESIA-2',tfc='0/3/0:',vln='783'),
    ])
    session.commit()

def deletedb():
    session.query(Act).filter(Act.id == 964).delete()
    session.commit()

def updatedb():
    session.query(Act).filter(Act.id == 971).update({'cto':'C15'})
    session.query(Act).filter(Act.id == 970).update({'cto':'C10'})
    session.commit()
