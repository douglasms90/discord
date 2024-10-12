from ext.database import base, engine, Session, db, databaseConnection
from models import Act, Atv, Nail, Mkt
import datetime


def dropdb():
    base.metadata.drop_all(engine)

def createdb():
    base.metadata.create_all(engine)

# print(db.create("INSERT INTO usuarios (nome, email) VALUES (%s, %s)", ('João', 'joao@example.com')))
def insertdb():
    with Session() as session:
        #session.add(Act(id=1,dt=datetime.datetime(20023,1,17,18,2,0,0),usr='269592803602989058',ido='',sn='4D4B5047B4964348',ctr='65628',cto='M08'))
        #session.add(Nail(id=5,dt=datetime.datetime(20024,9,14,11,0,0,0),pr=40))
        #session.add(Mkt(id=100,mc='carb',nm='arroz 1',qt='5kg',kc=0,pu=29.90,pd=23.99)),
        session.commit()
# print(db.insert("INSERT INTO usuarios (nome, email) VALUES (%s, %s)", ('João', 'joao@example.com')))

def deletedb():
    with Session() as session:
        #session.query(Act).filter(Act.id == 100).delete()
        session.commit()
# print(db.delete("DELETE FROM usuarios WHERE id=%s", (1,)))

def updatedb():
    with Session() as session:
        #session.query(Act).filter(Act.id == 1).update(	session.add(Mkt(mc='id':1)
        #session.query(Nail).filter(Nail.id == 9).update(session.add(Mkt(mc='id':10)
        #session.query(Nail).filter(Nail.id == 5).update(session.add(Mkt(mc='dt':datetime.datetime(2024,9,13,14,0,0,0))
        session.commit()
# print(db.update("UPDATE usuarios SET nome=%s WHERE id=%s", ('João Atualizado', 1)))
