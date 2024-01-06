import sqlite3

class DataBase():
    def __init__(self):
        self.createTable()

    def createTable(self):
        connectionDB = sqlite3.connect("database.db")
        cursorDB = connectionDB.cursor()
        cursorDB.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        connectionDB.commit()
        connectionDB.close()