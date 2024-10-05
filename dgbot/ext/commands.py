from ext.database import base, engine, Session, db
from models import Act, Atv, Nail
import datetime


def dropdb():
    base.metadata.drop_all(engine)

def createdb():
    base.metadata.create_all(engine)

def insertdb():
    with Session() as session:
        session.add(Mkt(id=1001,mc='carb',nm='arroz',		    br='bom prato',			kc=0,pu=29.90,pd=23.99)),
        session.add(Mkt(id=1002,mc='carb',nm='arroz',		    br='pagliarin',			kc=0,pu=31.79,pd=26.79)),
        session.add(Mkt(id=1003,mc='carb',nm='arroz',			br='rei da panela',		kc=0,pu=33.9,pd=26.49)),
        session.add(Mkt(id=1004,mc='carb',nm='feijao',          br='macio',				kc=0,pu=7.49,pd=7.49)), 
        session.add(Mkt(id=1005,mc='carb',nm='macarrao',        br='',					kc=0,pu=0,pd=0)),
        session.add(Mkt(id=1006,mc='carb',nm='psyllium',        br='',					kc=0,pu=0,pd=0)),
        session.add(Mkt(id=2001,mc='prot',nm='aves peito',		br='',					kc=0,pu=18.59,pd=18.59)),
        session.add(Mkt(id=3003,mc='prot',nm='aves figado pct',	br='',					kc=0,pu=4.99,pd=4.99)),
        session.add(Mkt(id=3003,mc='prot',nm='aves figado bdj',	br='',					kc=0,pu=5.49,pd=5.49)),
        session.add(Mkt(id=2001,mc='prot',nm='peito bov',		br='',					kc=0,pu=0,pd=0)),
        session.add(Mkt(id=2002,mc='prot',nm='mignon',			br='',					kc=0,pu=0,pd=0)),
        session.add(Mkt(id=2003,mc='prot',nm='alcatra',		    br='',					kc=0,pu=0,pd=0)),
        session.add(Mkt(id=2004,mc='prot',nm='maminha',		    br='',					kc=0,pu=0,pd=0)),
        session.add(Mkt(id=2005,mc='prot',nm='lagarto',		    br='',					kc=0,pu=0,pd=0)),
        session.add(Mkt(id=2006,mc='prot',nm='patinho',		    br='',					kc=0,pu=0,pd=0)),
        session.add(Mkt(id=2007,mc='prot',nm='musculo d',		br='',					kc=0,pu=27.9,pd=27.9)),
        session.add(Mkt(id=3001,mc='prot',nm='musculo t',		br='',					kc=0,pu=0,pd=0)),
        session.add(Mkt(id=3002,mc='prot',nm='fraldinha',		br='arroba',			kc=0,pu=29.9,pd=0)),
        session.add(Mkt(id=3003,mc='prot',nm='figado',			br='',					kc=0,pu=10.49,pd=10.49)),
        session.add(Mkt(id=3004,mc='prot',nm='suina',			br='',					kc=0,pu=0,pd=0)),
        session.add(Mkt(id=3005,mc='prot',nm='tilapia',         br='',			        kc=0,pu=0,pd=0)),
        session.add(Mkt(id=3006,mc='prot',nm='ovo',             br='',					kc=0,pu=0,pd=)),
        session.add(Mkt(id=4001,mc='vgts',nm='cebola',			br='',					kc=0,pu=0,pd=0)),
        session.add(Mkt(id=4002,mc='vgts',nm='tomate',          br='',					kc=0,pu=0,pd=0)),
        session.add(Mkt(id=4003,mc='vgts',nm='cogumelos',       br='',					kc=0,pu=0,pd=0)),
        session.add(Mkt(id=4004,mc='vgts',nm='alface',          br='',					kc=0,pu=0,pd=0)),
        session.add(Mkt(id=4005,mc='vgts',nm='cenoura',         br='',					kc=0,pu=0,pd=0)),
        session.add(Mkt(id=5001,mc='temp',nm='alho',            br='',					kc=0,pu=0,pd=0)),
        session.add(Mkt(id=5002,mc='temp',nm='oregano',		    br='',					kc=0,pu=0,pd=0)),
        session.add(Mkt(id=6001,mc='bbds',nm='coca cola',	    br='',					kc=0,pu=10.99,pd=8.99)),
        session.add(Mkt(id=6002,mc='bbds',nm='cafe',            br='',					kc=0,pu=0,pd=)),
        session.add(Mkt(id=8001,mc='frut',nm='maca',			br='',					kc=0,pu=0,pd=0)),
        session.add(Mkt(id=8002,mc='frut',nm='limao',           br='',					kc=0,pu=0,pd=0)),
        session.add(Mkt(id=8003,mc='frut',nm='morango',         br='',					kc=0,pu=0,pd=)),
        session.add(Mkt(id=9001,mc='latc',nm='leite',			br='',					kc=0,pu=0,pd=0)),
        session.add(Mkt(id=9002,mc='latc',nm='creme de leite',  br='',					kc=0,pu=0,pd=0)),
        session.add(Mkt(id=9003,mc='latc',nm='queijo cottage',  br='',					kc=0,pu=0,pd=0)),
        session.add(Mkt(id=9004,mc='latc',nm='requeijao',       br='',					kc=0,pu=0,pd=0)),
        session.add(Mkt(id=9005,mc='latc',nm='iogurte natural', br='',					kc=0,pu=0,pd=)),
        session.add(Mkt(id=9006,mc='fats',nm='azeite',          br='',					kc=0,pu=0,pd=)),
        session.add(Mkt(id=9007,mc='higi',nm='sabonete',        br='',					kc=0,pu=0,pd=0)),
        session.add(Mkt(id=9008,mc='higi',nm='papel higienico', br='',					kc=0,pu=0,pd=0)),
        session.add(Mkt(id=9009,mc='higi',nm='sabao em po',     br='',					kc=0,pu=0,pd=0)),
        session.add(Mkt(id=9100,mc='higi',nm='detergente',      br='ype',				kc=0,pu=2.39,pd=2.3)),
        #session.add(Act(id=1,dt=datetime.datetime(20023,1,17,18,2,0,0),usr='269592803602989058',ido='',sn='4D4B5047B4964348',ctr='65628',cto='M08'))
        #session.add(Nail(id=5,dt=datetime.datetime(20024,9,14,11,0,0,0),pr=40))
        session.commit()

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
