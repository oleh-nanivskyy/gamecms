from flask import g
import psycopg2


def get_db():
    g.db = psycopg2.connect(dbname='gamecms', user='oleh')
    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()