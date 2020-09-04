from daterbase import *
from login import *
def clock():  # This part will great you dipending on time
    now = time.datetime.now()
    hour = now.hour
    if hour < 12:
        print("Good morning")
    elif hour > 11 and hour < 18:
        print("Good afternoon")
    elif hour > 18 and hour < 19:
        print("Good evening")
    else:
        print('Good night.')
clock()
askwho = input('''are you a:
a/avoter
b/candidate
c/staffmember:''')
if askwho == 'a':
    a = input("are you new or not new: ")
    if a == 'not new':
        def login(): # this is login for not new people
            for i in range(3):
                idnumber = input("pls enter your id number: ")
                with sqlite3.connect('main.db') as db:
                    cursour = db.cursor()
                find_user = ('SELECT * FROM login WHERE idnumber = ?')
                cursour.execute(find_user,[(idnumber)])
                results = cursour.fetchall()
                if results:
                    for bla in results:
                        malli = str(bla)
                    break
                else:
                    print("id not recognised")
                    again = input("Do u want to try again?(y/n): ")
                    if again.lower() == "n":
                        print("Good Bye")
                        break
        login()
    elif a == 'new': # this is sign up for new people
        def adding_new_person():
            name1 = input("Enter your first name:  ")
            name2 = input("Enter your second name:  ")
            print(name1 + " welcome")
        adding_new_person()
    def voters(): # cheks is you are over 18
        age  = int(input("pls enter youre age: "))
        if age < 18:
            print("You are not an Eligible voter!!")
            return
        elif age > 18:
            print("You are able to vote HURRAY!!")

    voters()
    def candidets():   
        f.execute("SELECT * FROM candidates")
        print(f.fetchall())
        
        a = input("chose a candidets: ")
        c.execute("INSERT INTO voters VALUES(?)",(a))
        conn.commit()
        
        c.execute("SELECT * FROM  voters")
        print(c.fetchall())
   
    candidets()

elif askwho == 'b':
    def adding_items():
        while True:
            name  = input("enter your name: ")
            if not name.isalpha():
                continue
            else:
                try:
                    age = int(input("enter age: "))
                except ValueError:
                    print("sorry i did'nt understand that")
            
                    
            f.execute("INSERT INTO candidates(name,age) VALUES(?,?)",(name,age))
            fonn.commit()
            print("it works")
            break
                        
        adding_items()

        def age(): # cheks is you are over 18
            print("enter age agin")
            age  = int(input("pls enter youre age: "))
            if age < 18:
                print("You are not an Eligible voter!!")
                exit()
            elif age > 18:
                print("Welcome")
        age()
    adding_items()
else:
    print("sorry don't anderstand you")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
