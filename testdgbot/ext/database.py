import sqlalchemy
import sqlalchemy.orm


db = sqlalchemy

dbo = sqlalchemy.orm

base = dbo.declarative_base()

engine = db.create_engine('sqlite:///development.db', echo=True)

Session = dbo.sessionmaker(bind=engine)

session = Session()
<<<<<<< HEAD
=======

class dbConn():
    conn = None
    def __init__(self):
        self.conn = psycopg2.connect("")

    def consult(self, query):
        try:
            cur = self.conn.cursor()
            cur.execute(query)
            dbdump = cur.fetchall()
            return dbdump
        except:
            return "Impossible to connect to the database, check your code."
    
    def close(self):
        self.conn.close()
>>>>>>> 9f2c996b19c25bb968cefe62095ae5b10db00e78
