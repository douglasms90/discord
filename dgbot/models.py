from ext.database import db, base


class Act(base):
    __tablename__ = 'act'

    id = db.Column(db.Integer, primary_key=True)
    dt = db.Column(db.DateTime(20))
    usr = db.Column(db.String(20))
    olt = db.Column(db.String(20))
    tfc = db.Column(db.String(10))
    sn = db.Column(db.String(20))
    vln = db.Column(db.String(5))
    ctr = db.Column(db.String(10))
    cto = db.Column(db.String(5))

class Vln(base):
    __tablename__ = 'vln'

    id = db.Column(db.Integer, primary_key=True)
    olt = db.Column(db.String(20))
    tfc = db.Column(db.String(10))
    vln = db.Column(db.String(5))

class Atv(base):
    __tablename__ = 'atv'

    id = db.Column(db.Integer, primary_key=True)
    tp = db.Column(db.String(20))
    nm = db.Column(db.String(10))
    pm = db.Column(db.Float(10))
    qt = db.Column(db.Float(10))
    rc = db.Column(db.String(10))
    pa = db.Column(db.Float(10))