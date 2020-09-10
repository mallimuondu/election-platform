import sqlite3
conn = sqlite3.connect('try.db')
c = conn.cursor()

def table():
    
    c.execute('CREATE TABLE IF NOT EXISTS people(name TEXT)')
    
table()
def addinput():
    while True:
        name  = input("enter your name: ")
        if not name.isalpha():
            continue
        else:
            c.execute("INSERT INTO people (name)VALUES(?)",(name,))
                      
            conn.commit()
            print("Hurray you have been added")
            
            break
addinput()
def read_from_db():
    c.execute("SELECT * FROM people ")
    
    a = c.fetchall()
    
    print(a)
    
read_from_db()