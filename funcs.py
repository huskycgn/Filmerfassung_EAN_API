from eansearch import EANSearch
import psycopg2
from cred import *

def ean_lookup(ean):
    apitoken = EAN_TOKEN
    lookup = EANSearch(apitoken)
    name = lookup.barcodeLookup(ean)
    print(name)
    return name

def write_db(moviename, ean):
    moviename = moviename.replace("'", "''")
    conn = psycopg2.connect(f"host={DB_HOST} dbname=movies user={DB_USER} password={DB_PASSWORD}")
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO movies (title, ean) VALUES ('{moviename}', {ean})", (moviename,))
    conn.commit()


def read_db():
    conn = psycopg2.connect(f"host={DB_HOST} dbname=movies user={DB_USER} password={DB_PASSWORD}")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM movies")
    return cursor.fetchall()


def check_duplicate(ean):
    '''True means, it is a duplicate of an ean'''
    conn = psycopg2.connect(f"host={DB_HOST} dbname=movies user={DB_USER} password={DB_PASSWORD}")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM movies WHERE ean = '{ean}'")
    if cursor.fetchall() == []:
        return False
    else:
        return True