import sqlite3
conn = sqlite3.connect('try.db')
c = conn.cursor()

def table():
    c.execute('CREATE TABLE IF NOT EXISTS age(age INT)')
table()    
def addinput():
    while True:
        age  = int(input("enter your name: "))
        if not age.isalpha():
            continue
        else:
            c.execute("INSERT INTO malli (name)VALUES(?)",(name,))
                      
            conn.commit()
            print("entereds")
            
            break
addinput()



def read_from_db():
    c.execute("SELECT * FROM malli ")
    
    a = c.fetchall()
    
    print(a)
read_from_db()