import sqlite3
conn = sqlite3.connect('malli.db')
c = conn.cursor()
def table():
    
    c.execute('CREATE TABLE IF NOT EXISTS malli(number INT)')
    
table()