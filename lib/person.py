import sqlite3
CONN = sqlite3.connect('lib/resources.db', timeout=10)
CURSOR = CONN.cursor()

class Person:

    def __init__(self,name, id=None):
        self.name = name
        self.id = id