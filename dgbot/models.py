from ext.database import db, base


class website(base):
    __tablename__ = 'websites'

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(200))
