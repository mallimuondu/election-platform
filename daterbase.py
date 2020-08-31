import datetime as time
import sqlite3
conn = sqlite3.connect('main.db')
cone = sqlite3.connect('name.db')
d = cone.cursor()
c = conn.cursor()