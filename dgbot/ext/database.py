import sqlalchemy
import sqlalchemy.orm

from psycopg2 import connect
import psycopg2.extensions
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)


db = sqlalchemy

dbo = sqlalchemy.orm

base = dbo.declarative_base()

engine = db.create_engine('sqlite:///development.db', echo=True)

Session = dbo.sessionmaker(bind=engine)

class dbc():
    db_ = None
    def __init__(self, host):
        self.db_ = psycopg2.connect(host)

    def consult(self, query):
        try:
            cur = self.db_.cursor()
            cur.execute(query)
            dump = cur.fetchall()
            return dump
        except:
            return "Impossible to connect to the database, check your code."

    def close(self):
        self.db_.close()

class databaseConnection():
    _db = None

    def __init__(self, pslhost):
        self._db = psycopg2.connect(pslhost)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._db.close()

    def create(self, pslquery, values):
        try:
            with self._db.cursor() as cur:
                cur.execute(pslquery, values)
                self._db.commit()
            return "Creation successful"
        except Exception as e:
            return f"Error during creation: {e}"

    def read(self, pslquery):
        try:
            with self._db.cursor() as cur:
                cur.execute(pslquery)
                dump = cur.fetchall()
            return dump
        except Exception as e:
            return f"Impossible to connect to the database, check your code. Error: {e}"

    def update(self, pslquery, values):
        try:
            with self._db.cursor() as cur:
                cur.execute(pslquery, values)
                self._db.commit()
            return "Update successful"
        except Exception as e:
            return f"Error during update: {e}"

    def delete(self, pslquery, values):
        try:
            with self._db.cursor() as cur:
                cur.execute(pslquery, values)
                self._db.commit()
            return "Deletion successful"
        except Exception as e:
            return f"Error during deletion: {e}"
