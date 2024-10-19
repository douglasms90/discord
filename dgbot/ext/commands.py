from ext.database import databaseConnection
from decouple import config

def dropdb():
    base.metadata.drop_all(engine)

def createdb():
    base.metadata.create_all(engine)

def insertdb():
    with Session() as session:
        #session.add(Act(id=1,dt=datetime.datetime(20023,1,17,18,2,0,0),usr='269592803602989058',ido='',sn='4D4B5047B4964348',ctr='65628',cto='M08'))
        #session.add(Nail(id=5,dt=datetime.datetime(20024,9,14,11,0,0,0),pr=40))
        #session.add(Mkt(id=100,mc='carb',nm='arroz 1',qt='5kg',kc=0,pu=29.90,pd=23.99)),
        session.commit()

def deletedb():
    with Session() as session:
        #session.query(Act).filter(Act.id == 100).delete()
        session.commit()


def updatedb():
    with Session() as session:
        #session.query(Act).filter(Act.id == 1).update(session.add(Mkt(mc='id':1)
        #session.query(Nail).filter(Nail.id == 9).update(session.add(Mkt(mc='id':10)
        #session.query(Nail).filter(Nail.id == 5).update(session.add(Mkt(mc='dt':datetime.datetime(2024,9,13,14,0,0,0))
        session.commit()

def create():
    with databaseConnection(config("hostAdmin")) as db:
        db.create("CREATE DATABASE database")

def createdt():
    with databaseConnection(config("hostMydb")) as db:
        "Tem que ser uma linha de cada vez"
        db.createdt("CREATE TABLE mkt(id SERIAL PRIMARY KEY, mc VARCHAR(5), nm VARCHAR(25), pd FLOAT, pu FLOAT)")
        db.createdt("CREATE TABLE atv(id SERIAL PRIMARY KEY, cl VARCHAR(20), nm VARCHAR(10), pr FLOAT, pm FLOAT, qt FLOAT, dv FLOAT, pl FLOAT, vp FLOAT)")
        db.createdt("CREATE TABLE act(id SERIAL PRIMARY KEY, dt TIMESTAMP, us BIGINT, os INTEGER, sn VARCHAR(20), cr INTEGER, ct VARCHAR(5))")
        db.createdt("CREATE TABLE nails(id SERIAL PRIMARY KEY, dt TIMESTAMP, pr FLOAT)")

def insert():
    with databaseConnection(config("hostMydb")) as db:
        db.insert("INSERT INTO mkt (id, mc, nm,  pd, pu) VALUES(%s, %s, %s, %s, %s)", (101, 'carb', 'arroz', 23.99, 29.9))
        db.insert("INSERT INTO atv (id, cl, nm, pr, pm, qt, dv, pl, vp) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", (101, 'rf', 'firfdi', 1894.08, 1894.08, 1.0, None, None, None))
        db.insert("INSERT INTO act (id, dt, us, os, sn, cr, ct) VALUES(%s, %s, %s, %s, %s, %s, %s)", (1, '2023-01-17 18:02:00.000000', 269592803602989058, 201942, '4D4B5047B4964348', 65628, 'M08'))
        db.insert("INSERT INTO nails (id, dt, pr) VALUES(%s, %s, %s)", (1, '2024-09-11 10:01:20.599270', 20.0))

def update():
    with databaseConnection(config("hostMydb")) as db:
        db.update("UPDATE datacamp_courses SET course_instructor = %s, topic = %s WHERE course_name = %s", ('New Instructor', 'New Topic', 'Introduction to SQL'))

def delete():
    with databaseConnection(config("hostMydb")) as db:
        db.delete("DELETE FROM datacamp_courses WHERE topic = %s", ('Python',))
