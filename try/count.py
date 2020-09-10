import sqlite3
conn = sqlite3.connect('broS.db')
c = conn.cursor()

def table():
    c.execute('CREATE TABLE IF NOT EXISTS names(names TEXT)')
table()

def insert():
    name = input('enter name:')
    c.execute('INSERT INTO names(names) VALUES(?)', (name,))
    conn.commit()
    
insert()
def read():
    for row in c.execute('select * from names'):
        new_list = list(row)
#        print(new_list)
        
        for a in new_list:
#            print(a)
            empty_list = []
            empty_list.append(a)
            print(empty_list)
        
#        count = new_list.count('malli')
#        print(count)
read()
    
#a = [('malli,'),('Nesh,'),('malli,')]
#listing = list(a)
#
#count = listing.count('malli,')
#print(count)
#
#listing1 = list(a)
#count1 = listing1.count('Nesh,')
#print(count1)

