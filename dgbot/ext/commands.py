from ext.database import base, engine, session
from models import Act, Vln, Atv
import datetime


def dropdb():
    base.metadata.drop_all(engine)

def createdb():
    base.metadata.create_all(engine)

def insertdb():
    #session.add(Act(id=1565,dt=datetime.datetime(2024,2,22,12,10,26,85696),usr='douglasms',olt='OLT-ARROZAL',tfc='0/7/11:',sn='48575443A94F32AC',vln='1219',ctr='69534',cto='L02'))
    session.commit()

def deletedb():
    #session.query(Act).filter(Act.id == 100).delete()
    session.commit()

def updatedb():
    #session.query(Atv).filter(Atv.id == 101).update({'id':101, 'tp':'rf',                  'nm':'inback',  'pm':134.98,    'qt':1.0,       'rc':'',    'pa':137.46})
    session.commit()

