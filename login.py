import sqlite3
conn = sqlite3.connect('main.db') 
cursour = conn.cursor()

def user_creation():
    '''
    this page is liked to the login  in the main file
    '''
    cursour.execute("CREATE TABLE IF NOT EXISTS login(idnumber VARCHAR)")

    cursour.execute("INSERT INTO login VALUES('190320' )")

    cursour.execute("INSERT INTO login VALUES('64025')")
    conn.commit()
user_creation()
    
cursour.execute("CREATE TABLE IF NOT EXISTS login1(username VARCHAR, password VARCHAR)")

cursour.execute("INSERT INTO login1 VALUES('malli', 'Malli2010')")
                
cursour.execute("INSERT INTO login1 VALUES('nesh', '12')")
conn.commit()