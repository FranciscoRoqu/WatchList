import sqlite3
def connect():
    connection = sqlite3.connect('sqlite-database/watchlist.db')
    return connection

def cursor():
    return connect().cursor()

def commit():
    return connect().commit()

def close():
    return connect().close() 