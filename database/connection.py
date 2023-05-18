import psycopg2
import os


class Connect:
    def connect_db(self):
        conn = psycopg2.connect(
            database=os.environ.get('DATABASE'),
            user=os.environ.get('POSTGRES_USER'),
            password=os.environ.get('POSTGRES_PASSWORD'),
            host=os.environ.get('HOST'),
            port=os.environ.get('PORT')
        )
        return conn
