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
    c.execute('''CREATE TABLE items (id TEXT PRIMARY KEY , date TEXT, item TEXT, vendor TEXT, price REAL)''')
    conn.commit()
    conn.close()


def save(date, item, vendor, price):
    query("INSERT INTO items VALUES ('{}', '{}', '{}', '{}', '{}')".format(date+item+vendor, date, item, vendor, price))


def load():
    return query("SELECT * FROM items")


def get_vendor_item_price(date, vendor):
    return query("SELECT price FROM items WHERE date=='{}' AND vendor=='{}'".format(date, vendor))


def unique_vendors():
    unique = [t[0] for t in query("SELECT DISTINCT(vendor) FROM items")]
    adds = ["pgw", "hembryggeriet", "koksbryggeriet"]  # TODO: Remove
    return list(set(unique + adds))


def query(q):
    try:
        conn = sqlite3.connect('../resources/prices.db')
        c = conn.cursor()
        res = c.execute(q)
        conn.commit()
        data = res.fetchall()
        conn.close()
        return data
    except Exception as e:
        print(e)
