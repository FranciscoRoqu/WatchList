import sqlite3

connection = sqlite3.connect('sqlite-database/watchlist.db')

def cursor():
    return connection.cursor()

def commit():
    return connection.commit()

def close():
    return connection.close() 