from ext.database import databaseConnection
from decouple import config


def create():
    with databaseConnection(config("hostAdmin")) as db:
        #db.create("CREATE DATABASE database")
        pass

def createdt():
    with databaseConnection(config("hostMydb")) as db:
        "Tem que ser uma linha de cada vez"
        #db.createdt("CREATE TABLE mkt(id SERIAL PRIMARY KEY, mc VARCHAR(5), nm VARCHAR(25), pd FLOAT, pu FLOAT)")
        #db.createdt("CREATE TABLE atv(id SERIAL PRIMARY KEY, cl VARCHAR(20), nm VARCHAR(10), pr FLOAT, pm FLOAT, qt FLOAT, dv FLOAT, pl FLOAT, vp FLOAT)")
        #db.createdt("CREATE TABLE act(id SERIAL PRIMARY KEY, dt TIMESTAMP, us BIGINT, os INTEGER, sn VARCHAR(20), cr INTEGER, ct VARCHAR(5))")
        #db.createdt("CREATE TABLE nails(id SERIAL PRIMARY KEY, dt TIMESTAMP, pr FLOAT)")
        pass

def insert():
    with databaseConnection(config("hostMydb")) as db:
        #db.insert("INSERT INTO mkt (id, mc, nm,  pd, pu) VALUES(%s, %s, %s, %s, %s)", (101, 'carb', 'arroz', 23.99, 29.9))
        #db.insert("INSERT INTO atv (id, cl, nm, pr, pm, qt, dv, pl, vp) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", (300, 'acoes', 'bbas3', 0, 0, 3.0, None, None, None))
        #db.insert("INSERT INTO act (id, dt, us, os, sn, cr, ct) VALUES(%s, %s, %s, %s, %s, %s, %s)", (1, '2023-01-17 18:02:00.000000', 269592803602989058, 201942, '4D4B5047B4964348', 65628, 'M08'))
        #db.insert("INSERT INTO nails (id, dt, pr) VALUES(%s, %s, %s)", (72, '2024-11-08 19:16:00.0', 20.0))
        pass

def update():
    with databaseConnection(config("hostMydb")) as db:
        #db.update("UPDATE datacamp_courses SET course_instructor = %s, topic = %s WHERE course_name = %s", ('New Instructor', 'New Topic', 'Introduction to SQL'))
        pass

def delete():
    with databaseConnection(config("hostMydb")) as db:
        #db.delete("DELETE FROM datacamp_courses WHERE topic = %s", ('Python',))
        pass
