from ext.database import db, base


class Act(base):
    __tablename__ = 'act'

    id = db.Column(db.Integer, primary_key=True)
    dt = db.Column(db.DateTime(20))
    usr = db.Column(db.String(20))
    ido = db.Column(db.String(10))
    sn = db.Column(db.String(20))
    ctr = db.Column(db.String(10))
    cto = db.Column(db.String(5))

class Atv(base):
    __tablename__ = 'atv'

    id = db.Column(db.Integer, primary_key=True)
    cl = db.Column(db.String(20))
    nm = db.Column(db.String(10))
    pr = db.Column(db.Float(10))
    pm = db.Column(db.Float(10))
    qt = db.Column(db.Float(10))
    dv = db.Column(db.Float(10))
    pl = db.Column(db.Float(10)) 
    vp = db.Column(db.Float(10)) 

class Nail(base):
    __tablename__ = 'nail'

    id = db.Column(db.Integer, primary_key=True)
    dt = db.Column(db.DateTime(20))
    pr = db.Column(db.Float(10))

class Mkt(base):
    __tablename__ = 'mkt'

    id = db.Column(db.Integer, primary_key=True)
    mc = db.Column(db.String(5))
    nm = db.Column(db.String(20))
    kc = db.Column(db.Float(5))
    pu = db.Column(db.Float(5))
    pd = db.Column(db.Float(5))
