from daterbase import *
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
c/staffmember
:''')
if askwho == 'a':
    a = input('''are you:
    a.new voter
    b.old :''' )
    if a == 'b':
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
    elif a == 'a': # this is sign up for new people
        def adding_new_person():
            name1 = input("Enter your first name:  ")
            name2 = input("Enter your second name:  ")
            age  = int(input("pls enter youre age: "))
            if age < 18:
                print("You are not an Eligible voter!!")
                return
            elif age > 18:
                print("You are able to vote HURRAY!!")
            idnumber = input("pls enter your id number: ")
            print(name1 + " welcome")
    def candidets():   
        f.execute("SELECT * FROM people ")
    
        a = f.fetchall()
    
        print(a)
        a = input('''choose a candidets:
        :''' )
        c.execute("INSERT INTO voters VALUES(?)",(a))
        conn.commit()
        
        c.execute("SELECT * FROM  voters")
        print(c.fetchall())
   
    candidets()

elif askwho == 'b':
    def addinput():
        while True:
            name  = input("enter your name: ")
            secondname  = input("enter your secondname: ")
            age  = int(input("enter your age: "))
            idn  = int(input("enter your id: "))
            if not name.isalpha():
                continue
            else:
                f.execute("INSERT INTO people (name)VALUES(?)",(name,))
                      
                fonn.commit()
                
                break
    addinput()


    def age(): # cheks is you are over 18
        age  = int(input("pls enter youre age: "))
        if age < 18:
            print("You are not an Eligible voter!!")
            exit()
        elif age > 18:
            print("Welcome")
    age()
elif askwho == 'c':
    for i in range(3):
        username = input("pls enter your username: ")
        password = input("pls enter pass: ")
        with sqlite3.connect('main.db') as db:
            cursour = db.cursor()
        find_user = ('SELECT * FROM login WHERE username = ? AND password = ?')
        cursour.execute(find_user,[(username), (password)])
        results = cursour.fetchall()
        if results:
            for bla in results:
                malli = str(bla)
                print("Welcome ")
            break
        else:
            print("Username and passwored not recognised")
            again = input("Do u want to try again?(y/n): ")
            if again.lower() == "n":
                print("Good Bye")
                time.sleep(1)
                break

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
