import datetime as time
import sqlite3
'''
this page the page for my daterbase
'''
conn = sqlite3.connect('main.db')
c = conn.cursor()
donn = sqlite3.connect('votes.db')
d = donn.cursor()
fonn = sqlite3.connect('candidates.db')
f = fonn.cursor()

def table():
    
    c.execute('CREATE TABLE IF NOT EXISTS malli(people STR)')
    
table()


def candidates():
    
    f.execute('CREATE TABLE IF NOT EXISTS candidates(firstname STR)')
    
candidates()


