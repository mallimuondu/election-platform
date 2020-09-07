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
    
    c.execute('CREATE TABLE IF NOT EXISTS voters(people TEXT )')
    
table()

def table():
    
    f.execute('CREATE TABLE IF NOT EXISTS people(name TEXT)')
    
table()