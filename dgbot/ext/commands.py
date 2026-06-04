from ext.database import databaseConnection
from decouple import config


def crudIn(self, query):
    with databaseConnection(config("hostMydb")) as db:
        return db.crud(query)

def createdb():
    #crudIn("CREATE DATABASE database")
    pass

def createdt():
    "Tem que ser uma linha de cada vez"
    #crudIn("CREATE TABLE mkt(id SERIAL PRIMARY KEY, mc VARCHAR(5), nm VARCHAR(25), pd FLOAT, pu FLOAT)")
    #crudIn("CREATE TABLE assets(id SERIAL PRIMARY KEY, cl VARCHAR(20), nm VARCHAR(10), pr FLOAT, pm FLOAT, qt FLOAT, dv FLOAT, pl FLOAT, vp FLOAT)")
    #crudIn("CREATE TABLE act(id SERIAL PRIMARY KEY, dt TIMESTAMP, os INTEGER, sn VARCHAR(20), cr INTEGER, ct VARCHAR(5))")
    #crudIn("CREATE TABLE nails(id SERIAL PRIMARY KEY, dt TIMESTAMP, pr FLOAT)")
    pass

def insertdb():
    #crudIn("INSERT INTO assets (id, cl, nm, pr, pm, qt, dv, pl, vp) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", (402, 'rf', 'bonds', 1, 1, 1.0, None, None, None))
    #crudIn("INSERT INTO act (id, dt, us, os, sn, cr, ct) VALUES(%s, %s, %s, %s, %s, %s, %s)", (1, '2023-01-17 18:02:00.000000', 269592803602989058, 201942, '4D4B5047B4964348', 65628, 'M08'))
    #crudIn("INSERT INTO nails (id, dt, pr) VALUES(%s, %s, %s)", (72, '2024-11-08 19:16:00.0', 20.0))
    #crudIn("INSERT INTO assets (id, cl, nm, pr, pm, qt, dv, pl, vp) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", (201, 'fundos-imobiliarios', 'kncr11', 1, 1, 1, None, None, None))
    pass

def updatedb():
    #crudIn("UPDATE %s SET %s = %s WHERE %s = %s", (act, id, id_number, nm, nm_string))
    pass

def deletedb():
    ##crudIn("DELETE FROM act WHERE id = %s", (1000,))
    pass
