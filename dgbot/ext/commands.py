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
    #session.query(Atv).filter(Atv.id == 102).update({'id':102, 'tp':'rf',                  'nm':'slc-29',  'pm':12874.14,  'qt':1.31,      'rc':'',    'pa':18961.0})
    #session.query(Atv).filter(Atv.id == 103).update({'id':103, 'tp':'rf',                  'nm':'lci-24',  'pm':1000.0,    'qt':20.0,      'rc':'',    'pa':21451.87})
    #session.query(Atv).filter(Atv.id == 104).update({'id':104, 'tp':'rf',                  'nm':'cdb-24',  'pm':1000.0,    'qt':10.0,      'rc':'',    'pa':12452.43})
    #session.query(Atv).filter(Atv.id == 105).update({'id':105, 'tp':'rf',                  'nm':'pre-25',  'pm':738.14,    'qt':3.38,      'rc':'',    'pa':3134.34})
    #session.query(Atv).filter(Atv.id == 106).update({'id':106, 'tp':'rf',                  'nm':'inf-26',  'pm':3146.81,   'qt':0.79,      'rc':'',    'pa':2928.13})
    #session.query(Atv).filter(Atv.id == 107).update({'id':107, 'tp':'rf',                  'nm':'inf-45',  'pm':1291.22,   'qt':17.39,     'rc':'',    'pa':22454.31})
    #session.query(Atv).filter(Atv.id == 201).update({'id':201, 'tp':'fundos-imobiliarios', 'nm':'irdm11',  'pm':107.59,    'qt':37.0,      'rc':'N',   'pa':87.0})
    #session.query(Atv).filter(Atv.id == 202).update({'id':202, 'tp':'fundos-imobiliarios', 'nm':'mcci11',  'pm':97.38,     'qt':20.0,      'rc':'',    'pa':94.0})
    #session.query(Atv).filter(Atv.id == 203).update({'id':203, 'tp':'fundos-imobiliarios', 'nm':'recr11',  'pm':94.62,     'qt':20.0,      'rc':'N',   'pa':94.0})
    #session.query(Atv).filter(Atv.id == 204).update({'id':204, 'tp':'fundos-imobiliarios', 'nm':'vgip11',  'pm':89.59,     'qt':16.0,      'rc':'',    'pa':0.0})
    #session.query(Atv).filter(Atv.id == 205).update({'id':205, 'tp':'fundos-imobiliarios', 'nm':'btlg11',  'pm':102.39,    'qt':17.0,      'rc':'',    'pa':113.0})
    #session.query(Atv).filter(Atv.id == 206).update({'id':206, 'tp':'fundos-imobiliarios', 'nm':'bcff11',  'pm':7.99,      'qt':112.0,     'rc':'N',   'pa':78.0})
    #session.query(Atv).filter(Atv.id == 207).update({'id':207, 'tp':'fundos-imobiliarios', 'nm':'hgru11',  'pm':127.04,    'qt':27.0,      'rc':'',    'pa':136.0})
    #session.query(Atv).filter(Atv.id == 208).update({'id':208, 'tp':'fundos-imobiliarios', 'nm':'mall11',  'pm':91.66,     'qt':14.0,      'rc':'N',   'pa':116.0})
    #session.query(Atv).filter(Atv.id == 209).update({'id':209, 'tp':'fundos-imobiliarios', 'nm':'pvbi11',  'pm':91.79,     'qt':4.0,       'rc':'N',   'pa':106.0})
    #session.query(Atv).filter(Atv.id == 210).update({'id':210, 'tp':'fundos-imobiliarios', 'nm':'rbrp11',  'pm':85.81,     'qt':45.0,      'rc':'N',   'pa':74.0})
    #session.query(Atv).filter(Atv.id == 211).update({'id':211, 'tp':'fundos-imobiliarios', 'nm':'vilg11',  'pm':115.45,    'qt':35.0,      'rc':'N',   'pa':127.0})
    #session.query(Atv).filter(Atv.id == 212).update({'id':212, 'tp':'fundos-imobiliarios', 'nm':'vino11',  'pm':11.91,     'qt':205.0,     'rc':'',    'pa':0.0})
    #session.query(Atv).filter(Atv.id == 301).update({'id':301, 'tp':'acoes',               'nm':'bbse3',   'pm':21.22,     'qt':65.0,      'rc':'N',   'pa':34.0})
    #session.query(Atv).filter(Atv.id == 302).update({'id':302, 'tp':'acoes',               'nm':'b3sA3',   'pm':13.76,     'qt':145.0,     'rc':'N',   'pa':15.0})
    #session.query(Atv).filter(Atv.id == 303).update({'id':303, 'tp':'acoes',               'nm':'egie3',   'pm':39.5,      'qt':10.0,      'rc':'',    'pa':46.0})
    #session.query(Atv).filter(Atv.id == 304).update({'id':304, 'tp':'acoes',               'nm':'eztc3',   'pm':16.86,     'qt':80.0,      'rc':'N',   'pa':22.0})
    #session.query(Atv).filter(Atv.id == 305).update({'id':305, 'tp':'acoes',               'nm':'flry3',   'pm':26.3,      'qt':90.0,      'rc':'N',   'pa':19.0})
    #session.query(Atv).filter(Atv.id == 306).update({'id':306, 'tp':'acoes',               'nm':'itsa4',   'pm':8.78,      'qt':231.0,     'rc':'',    'pa':0.0})
    #session.query(Atv).filter(Atv.id == 307).update({'id':307, 'tp':'acoes',               'nm':'mypk3',   'pm':13.04,     'qt':140.0,     'rc':'N',   'pa':15.0})
    #session.query(Atv).filter(Atv.id == 308).update({'id':308, 'tp':'acoes',               'nm':'sapr4',   'pm':4.09,      'qt':423.0,     'rc':'N',   'pa':26.0})
    #session.query(Atv).filter(Atv.id == 309).update({'id':309, 'tp':'acoes',               'nm':'vale3',   'pm':67.3,      'qt':38.0,      'rc':'N',   'pa':73.0})
    #session.query(Atv).filter(Atv.id == 310).update({'id':310, 'tp':'acoes',               'nm':'vbbr3',   'pm':24.74,     'qt':83.0,      'rc':'',    'pa':0.0})
    #session.query(Atv).filter(Atv.id == 311).update({'id':311, 'tp':'acoes',               'nm':'vivt3',   'pm':44.79,     'qt':33.0,      'rc':'N',   'pa':54.0})
    #session.query(Atv).filter(Atv.id == 312).update({'id':312, 'tp':'acoes',               'nm':'wege3',   'pm':19.52,     'qt':66.0,      'rc':'N',   'pa':40.0})
    #session.query(Atv).filter(Atv.id == 401).update({'id':401, 'tp':'etfs',                'nm':'ivvb11',  'pm':231.95,    'qt':14.0,      'rc':'',    'pa':0.0})
    #session.query(Atv).filter(Atv.id == 402).update({'id':402, 'tp':'bdrs',                'nm':'baba34',  'pm':17.18,     'qt':85.0,      'rc':'',    'pa':23.0})
    #session.query(Atv).filter(Atv.id == 403).update({'id':403, 'tp':'bdrs',                'nm':'disb34',  'pm':37.27,     'qt':33.0,      'rc':'',    'pa':34.0})
    #session.query(Atv).filter(Atv.id == 501).update({'id':501, 'tp':'criptomoedas',        'nm':'btc',     'pm':1,         'qt':0.01350731,'rc':'',    'pa':0.0})
    #session.query(Atv).filter(Atv.id == 502).update({'id':502, 'tp':'criptomoedas',        'nm':'beth',    'pm':1,         'qt':0.18814654,'rc':'',    'pa':0.0})
    session.commit()

