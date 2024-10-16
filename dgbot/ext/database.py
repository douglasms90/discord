from psycopg2 import connect
import psycopg2.extensions
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)

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

class databaseConnection:
    _db = None

    def __init__(self, host):
        self._db = psycopg2.connect(host)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._db.close()

    def create(self, query):
        try:
            self._db.autocommit = True
            with self._db.cursor() as cur:
                cur.execute(query)
                return print("Creation database successful")
        except Exception as e:
            return print(f"Error during creation: {e}")

    def createdt(self, query):
        try:
            with self._db.cursor() as cur:
                cur.execute(query)
                self._db.commit()
                return print("Creation datatable successful")
        except Exception as e:
            return print(f"Error during creation: {e}")

    def insert(self, query, values):
        try:
            with self._db.cursor() as cur:
                cur.execute(query, values)
                self._db.commit()
            return print("Insert data successful")
        except Exception as e:
            return print(f"Error during insertion: {e}")

    def read(self, query):
        try:
            with self._db.cursor() as cur:
                cur.execute(query)
                dump = cur.fetchall()
                print("Dump data succesful")
            return dump
        except Exception as e:
            return print(f"Error during read: {e}")

    def update(self, query, values):
        try:
            with self._db.cursor() as cur:
                cur.execute(query, values)
                self._db.commit()
            return print("Update data successful")
        except Exception as e:
            return print(f"Error during update: {e}")

    def delete(self, query):
        try:
            with self._db.cursor() as cur:
                cur.execute(query)
                self._db.commit()
            return print("Deletion data successful")
        except Exception as e:
            return print(f"Error during deletion: {e}")
