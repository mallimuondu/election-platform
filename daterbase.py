import datetime as time
import sqlite3
'''
this page the page for my daterbase
'''
conn = sqlite3.connect('main.db')
conn = sqlite3.connect('votes.db')
c = conn.cursor()
def table():
    
    conn.execute('CREATE TABLE IF NOT EXISTS malli(pepople)')
    
table()
