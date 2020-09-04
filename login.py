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