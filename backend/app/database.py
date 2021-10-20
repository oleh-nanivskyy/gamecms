import os

from flask import g
import psycopg2

HOST = os.environ.get('POSTGRES_HOST')
DB_NAME = os.environ.get('POSTGRES_DB')
USER = os.environ.get('POSTGRES_USER')
PASSWORD = os.environ.get('POSTGRES_PASSWORD')

def get_db():
    g.db = psycopg2.connect(dbname=DB_NAME, user=USER, 
                            host=HOST, password=PASSWORD)
    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()