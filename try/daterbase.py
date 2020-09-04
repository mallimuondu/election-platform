import sqlite3
conn = sqlite3.connect('mall.db')
c = conn.cursor()
#c.execute("""CREATE  TABLE moutain( 
#    first text,
#    age interger
#  
#  )""") 
c.execute ("INSERT INTO moutain VALUES('Malli',9)")
c.execute("SELECT * FROM moutain WHERE first = 'Malli'")
print(c.fetchone())
conn.commit()

conn.close()

def uppdate_pay(emp,pay):
    with conn:
        c.execute("""UPDATE from moutain WHERE first = :first AND age = :age""",
                 {'first':emp.first,'age':emp.last})
    pass