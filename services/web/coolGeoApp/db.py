import psycopg2
import os

from flask import g


def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(os.environ.get('DATABASE_URL'))

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()