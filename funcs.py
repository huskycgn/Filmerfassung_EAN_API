# from eansearch import EANSearch
import requests
import psycopg2
from cred import *


def ean_lookup(ean):
    header = {"x-rapidapi-key": RAPID_TOKEN}
    url = f"https://big-product-data.p.rapidapi.com/gtin/{ean}"
    request = requests.get(url, headers=header)
    request.close()
    return request.json()["properties"]["title"][0]


def write_db(moviename, ean):
    moviename = moviename.replace("'", "''")
    conn = psycopg2.connect(
        f"host={DB_HOST} dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD}"
    )
    cursor = conn.cursor()
    cursor.execute(
        f"INSERT INTO movies (title, ean) VALUES ('{moviename}', {ean})", (moviename,)
    )
    conn.commit()
    print(f"{moviename, ean} added!")


def remove_movies(ean):
    conn = psycopg2.connect(
        f"host={DB_HOST} dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD}"
    )
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM movies WHERE EAN = {ean}")
    conn.commit()


def read_db():
    conn = psycopg2.connect(
        f"host={DB_HOST} dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD}"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM movies")
    return cursor.fetchall()


def check_duplicate(ean):
    """True means, it is a duplicate of an ean"""
    conn = psycopg2.connect(
        f"host={DB_HOST} dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD}"
    )
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM movies WHERE ean = '{ean}'")
    if not cursor.fetchall():
        return False
    else:
        return True
