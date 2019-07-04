from datetime import date
import matplotlib
matplotlib.use('Agg')
import sqlite3


def store_data(vendor, price):
    today = date.today().isoformat()
    item = "grainfather"
    save(today, item, vendor, price)


def init_db():
    conn = sqlite3.connect('../resources/prices.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE items (date TEXT, item TEXT, vendor TEXT, price REAL)''')
    conn.commit()
    conn.close()


def save(date, item, vendor, price):
    query("INSERT INTO items VALUES ('{}', '{}', '{}', '{}')".format(date, item, vendor, price))


def load():
    return query("SELECT * FROM items")


def unique_vendors():
    return [t[0] for t in query("SELECT DISTINCT(vendor) FROM items")]


def query(q):
    conn = sqlite3.connect('../resources/prices.db')
    c = conn.cursor()
    res = c.execute(q)
    conn.commit()
    data = res.fetchall()
    conn.close()
    return data
