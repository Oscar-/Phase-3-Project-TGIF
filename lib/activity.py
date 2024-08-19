import sqlite3
CONN = sqlite3.connect('lib/resources.db', timeout=10)
CURSOR = CONN.cursor()