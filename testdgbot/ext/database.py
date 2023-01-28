import sqlalchemy
import sqlalchemy.orm


db = sqlalchemy

dbo = sqlalchemy.orm

base = dbo.declarative_base()

engine = db.create_engine('sqlite:///development.db', echo=True)

Session = dbo.sessionmaker(bind=engine)

session = Session()
