from ext.database import base, engine, Session, db
from models import Act, Atv, Nail
import datetime


def dropdb():
    base.metadata.drop_all(engine)

def createdb():
    base.metadata.create_all(engine)

def insertdb():
    #with Session() as session:
    #    session.add(Mkt(id=,mc='carb',nm='arroz',			br='bom prato',     kc=0,pu=29.90,pd=23.99)),
    #    session.add(Mkt(id=,mc='carb',nm='arroz',			br='pagliarin',     kc=0,pu=31.79,pd=26.79)),
    #    session.add(Mkt(id=,mc='carb',nm='arroz',			br='rei da panela', kc=0,pu=33.9,pd=26.49)),
    #    session.add(Mkt(id=,mc='carb',nm='feijao',          br='macio',         kc=0,pu=7.49,pd=7.49)), 
    #    session.add(Mkt(id=,mc='carb',nm='macarrao'         br='',  kc=0,pu=0,pd=0)),
    #    session.add(Mkt(id=,mc='carb',nm='batata',          br='',  kc=0,pu=0,pd=0)),
    #    session.add(Mkt(id=,mc='carb',nm='pao',  			br='',  kc=0,pu=0,pd=0)),
    #    session.add(Mkt(id=,mc='carb',nm='psyllium',        br='',  kc=0,pu=0,pd=0)),
    #    session.add(Mkt(id=,mc='prot',nm='peito bov',		br='', kc=0,pu=0,pd=
    #    session.add(Mkt(id=,mc='prot',nm='mignon',			br='',kc=0,pu=0,pd=0)),
    #    session.add(Mkt(id=,mc='prot',nm='alcatra',			br='',kc=0,pu=0,pd=0)),
    #    session.add(Mkt(id=,mc='prot',nm='maminha',			br='',kc=0,pu=0,pd=0)),
    #    session.add(Mkt(id=,mc='prot',nm='lagarto',			br='',kc=0,pu=0,pd=0)),
    #    session.add(Mkt(id=,mc='prot',nm='patinho',			br='',kc=0,pu=0,pd=0)),
    #    session.add(Mkt(id=,mc='prot',nm='musculo d',		br='',kc=0,pu=27.9,pd=27.9)),
    #    session.add(Mkt(id=,mc='prot',nm='musculo t',		br='',kc=0,pu=0,pd=0)),
    #    session.add(Mkt(id=,mc='prot',nm='fraldinha',		br='arroba',kc=0,pu=29.9,pd=0)),
    #    session.add(Mkt(id=,mc='prot',nm='figado',			br='',kc=0,pu=10.49,pd=10.49)),
    #    session.add(Mkt(id=,mc='prot',nm='suina',			br='',kc=0,pu=0,pd=0)),
    #    session.add(Mkt(id=,mc='prot',nm='peixe',           br='tilapia',kc=0,pu=0,pd=0)),
    #    session.add(Mkt(id=,mc='prot',nm='ovo',             br='',kc=0,pu=0,pd=)),
    #    session.add(Mkt(id=,mc='vgts',nm='cebola',			br='',kc=0,pu=0,pd=0)),
    #    session.add(Mkt(id=,mc='vgts',nm='tomate',          br='',kc=0,pu=0,pd=0)),
    #    session.add(Mkt(id=,mc='vgts',nm='cogumelos',       br='',kc=0,pu=0,pd=0)),
    #    session.add(Mkt(id=,mc='vgts',nm='alface',          br='',kc=0,pu=0,pd=)),
    #    session.add(Mkt(id=,mc='vgts',nm='cenoura',         br='',kc=0,pu=0,pd=0)),
    #    session.add(Mkt(id=,mc='temp',nm='alho',            br='',kc=0,pu=0,pd=0)),
    #    session.add(Mkt(id=,mc='temp',nm='oregano',			br='',kc=0,pu=0,pd=0)),
    #    session.add(Mkt(id=,mc='temp',nm='pimenta',         br='',kc=0,pu=0,pd=)),
    #    session.add(Mkt(id=,mc='bbds',nm='coca cola',		br='',kc=0,pu=0,pd=0)),
    #    session.add(Mkt(id=,mc='bbds',nm='cafe',            br='',kc=0,pu=0,pd=)),
    #    session.add(Mkt(id=,mc='frut',nm='maca',			br='',kc=0,pu=0,pd=0)),
    #    session.add(Mkt(id=,mc='frut',nm='limao',           br='',kc=0,pu=0,pd=0)),
    #    session.add(Mkt(id=,mc='frut',nm='morango',         br='',kc=0,pu=0,pd=)),
    #    session.add(Mkt(id=,mc='latc',nm='leite',			br='',kc=0,pu=0,pd=0)),
    #    session.add(Mkt(id=,mc='latc',nm='creme de leite',  br='',kc=0,pu=0,pd=0)),
    #    session.add(Mkt(id=,mc='latc',nm='queijo cottage',  br='',kc=0,pu=0,pd=0)),
    #    session.add(Mkt(id=,mc='latc',nm='requeijao',       br='',kc=0,pu=0,pd=0)),
    #    session.add(Mkt(id=,mc='latc',nm='iogurte natural', br='',kc=0,pu=0,pd=)),
    #    session.add(Mkt(id=,mc='fats',nm='azeite',          br='',kc=0,pu=0,pd=)),
    #    session.add(Mkt(id=,mc='higi',nm='sabonete',		br='',kc=0,pu=0,pd=0)),
    #    session.add(Mkt(id=,mc='higi',nm='papel higienico', br='',kc=0,pu=0,pd=0)),
    #    session.add(Mkt(id=,mc='higi',nm='sabao em po',     br='',kc=0,pu=0,pd=0)),
    #    session.add(Mkt(id=,mc='higi',nm='detergente',      br='ype',kc=0,pu=2.39,pd=2.3)),
    #    session.add(Mkt(id=,mc='desp',nm='chocolate em po',	br='',kc=0,pu=0,pd=0)),
    #    session.add(Mkt(id=,mc='desp',nm='mel',             br='',kc=0,pu=0,pd=0)),
    #    session.add(Mkt(id=,mc='desp',nm='gelatina',        br='',kc=0,pu=0,pd=0)),
    #    session.add(Mkt(id=,mc='desp',nm='filtro de cafe',  br='',kc=0,pu=0,pd=0)),
    #    session.add(Act(id=1,dt=datetime.datetime(2023,1,17,18,2,0,0),usr='269592803602989058',ido='',sn='4D4B5047B4964348',ctr='65628',cto='M08'))
    #    session.add(Nail(id=5,dt=datetime.datetime(2024,9,14,11,0,0,0),pr=40))
    #    session.commit()

def deletedb():
    with Session() as session:
        #session.query(Act).filter(Act.id == 100).delete()
        session.commit()

def updatedb():
    with Session() as session:
        #session.query(Act).filter(Act.id == 1).update(	session.add(Mkt(mc='id':1)
        #session.query(Nail).filter(Nail.id == 9).update(	session.add(Mkt(mc='id':10)
        #session.query(Nail).filter(Nail.id == 5).update(	session.add(Mkt(mc='dt':datetime.datetime(2024,9,13,14,0,0,0))
        session.commit()
