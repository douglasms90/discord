from ext.database import base, engine, Session, db
from models import Act, Atv, Nail
import datetime


def dropdb():
    base.metadata.drop_all(engine)

def createdb():
    base.metadata.create_all(engine)

def insertdb():
    with Session() as session:
        session.add(Mkt(mc='carb',nm='arroz',		    br='bom prato',			kc=0,pu=29.90,pd=23.99)),
        session.add(Mkt(mc='carb',nm='arroz',		    br='pagliarin',			kc=0,pu=31.79,pd=26.79)),
        session.add(Mkt(mc='carb',nm='arroz',			br='rei da panela',		kc=0,pu=33.9,pd=26.49)),
        session.add(Mkt(mc='carb',nm='feijao',          br='macio',				kc=0,pu=7.49,pd=7.49)), 
        
        session.add(Mkt(mc='prot',nm='aves peito',		br='',					kc=0,pu=18.59,pd=18.59)),
        session.add(Mkt(mc='prot',nm='aves figado',	    br='pct',				kc=0,pu=4.99,pd=4.99)),
        session.add(Mkt(mc='prot',nm='aves figado',	    br='bdj',				kc=0,pu=5.49,pd=5.49)),
        session.add(Mkt(mc='prot',nm='bov peito',		br='di',				kc=0,pu=33.90,pd=27.90)),
        session.add(Mkt(mc='prot',nm='alcatra', 	    br='tr',				kc=0,pu=45.69,pd=45.69)),
        session.add(Mkt(mc='prot',nm='coxao duro',	    br='',					kc=0,pu=35.99,pd=35.99)),
        session.add(Mkt(mc='prot',nm='patinho',		    br='tr',				kc=0,pu=39.49,pd=39.49)),
        session.add(Mkt(mc='prot',nm='musculo',	        br='2 di',				kc=0,pu=27.9,pd=27.9)),
        session.add(Mkt(mc='prot',nm='musculo',	        br='1 tr',				kc=0,pu=34.90,pd=34.90)),
        session.add(Mkt(mc='prot',nm='fraldinha',		br='arroba',			kc=0,pu=29.9,pd=27.90)),
        session.add(Mkt(mc='prot',nm='figado',			br='',					kc=0,pu=10.49,pd=10.49)),
        session.add(Mkt(mc='prot',nm='lombo suino',	    br='cng',				kc=0,pu=21.99,pd=21.99)),
        session.add(Mkt(mc='prot',nm='tilapia',         br='Copacol 400g',		kc=0,pu=23.90,pd=23.90)),
        session.add(Mkt(mc='prot',nm='ovos',            br='20',	    		kc=0,pu=14.98,pd=14.98)),
        
        session.add(Mkt(mc='vgts',nm='cebola',			br='',					kc=0,pu=0,pd=0)),
        session.add(Mkt(mc='vgts',nm='tomate',          br='',					kc=0,pu=0,pd=0)),
        session.add(Mkt(mc='vgts',nm='alface',          br='',					kc=0,pu=0,pd=0)),
        session.add(Mkt(mc='vgts',nm='cenoura',         br='',					kc=0,pu=0,pd=0)),
        
        session.add(Mkt(mc='temp',nm='alho',            br='',					kc=0,pu=0,pd=0)),
        session.add(Mkt(mc='temp',nm='oregano',		    br='',					kc=0,pu=0,pd=0)),
        
        session.add(Mkt(mc='bbds',nm='refrigerante',	br='coca cola',			kc=0,pu=10.99,pd=8.99)),
        session.add(Mkt(mc='bbds',nm='cafe',            br='',					kc=0,pu=0,pd=)),
        
        session.add(Mkt(mc='frut',nm='maca',			br='',					kc=0,pu=0,pd=0)),
        session.add(Mkt(mc='frut',nm='limao',           br='',					kc=0,pu=0,pd=0)),
        session.add(Mkt(mc='frut',nm='morango',         br='',					kc=0,pu=0,pd=)),
        
        session.add(Mkt(mc='latc',nm='leite',			br='',					kc=0,pu=0,pd=0)),
        session.add(Mkt(mc='latc',nm='creme de leite',  br='piracanjuba 200g',	kc=0,pu=2.99,pd=2.99)),
        session.add(Mkt(mc='latc',nm='requeijao',       br='',					kc=0,pu=0,pd=0)),
        
        session.add(Mkt(mc='higi',nm='sabonete',        br='',					kc=0,pu=0,pd=0)),
        session.add(Mkt(mc='higi',nm='papel higienico', br='',					kc=0,pu=0,pd=0)),
        session.add(Mkt(mc='higi',nm='sabao em po',     br='',					kc=0,pu=0,pd=0)),
        session.add(Mkt(mc='higi',nm='detergente',      br='ype',				kc=0,pu=2.39,pd=1.73)),
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
