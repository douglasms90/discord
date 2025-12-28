from psycopg2 import connect
import psycopg2.extensions
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)


class databaseConnection:
    def __init__(self, host):
        self.db_ = connect(host)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.db_.close()

    def read(self, query):
        with self.db_.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()

    def crud(self, query):
        with self.db_.cursor() as cur:
            cur.execute(query)
            self.db_.commit()
