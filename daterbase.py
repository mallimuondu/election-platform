import datetime as time
import sqlite3
'''
this page the page for my daterbase
'''
conn = sqlite3.connect('main.db')
cone = sqlite3.connect('name.db')
d = cone.cursor()
c = conn.cursor()