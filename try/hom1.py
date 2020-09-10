import sqlite3
conn = sqlite3.connect('book.db')
c = conn.cursor()

def table():
    c.execute('CREATE TABLE IF NOT EXISTS Malli(names TEXT)')
table()

def isert():
    a = 'malli'
    c.execute('INSERT INTO malli (names) VALUES (?)',(a,))
isert()
def read():
    for row in c.execute('SELECT * FROM Malli'):
        print(row)
        
        new_list = list(row)
        print(new_list)
        for a in new_list:
            print(a)
        user = input("enter name:")
        if a == user:
            print("work")
        else:
            print("does not")
read()