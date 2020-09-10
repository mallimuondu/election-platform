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
a/voter
b/candidate
c/staffmember
:''')


if askwho == 'a' or askwho == 'voter':
    a = input('''are you:
    a.new voter
    b.old 
    :''' )
    if a == 'b' or a == 'old':
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
    elif a == 'a' or a == 'new voter': # this is sign up for new people
        def adding_new_person():
            name1 = input("Enter your first name:  ")
            name2 = input("Enter your second name:  ")
            age  = int(input("pls enter youre age: "))
            if age < 18:
                print("You are not an Eligible voter!!")
                exit()
            elif age > 18:
                print("You are able to vote HURRAY!!")
            idnumber = int(input("pls enter your id number: "))
            string_id_number = str(idnumber)
            if len(string_id_number) < 8:
                print("an ID number must be 8 digits.That is too low")
                exit()
            elif len(string_id_number) >8 or len(string_id_number) <9:
                print(name1 + " welcome")
        adding_new_person()
    def candidets():
        f.execute('SELECT * FROM people')
        print(f.fetchall())
        a = input('''choose a candidets:
        :''' )
        c.execute("INSERT INTO voters VALUES(?)",(a,))
        conn.commit()
        print("Thanks for voting for "+a)
        listing = list(a)
        count = listing.count('malli,')
        print(count)
    candidets()
    
    
    
    
elif askwho == 'b' or askwho == 'candidate':
    def addinput():
        while True:
            name  = input("enter your first name: ")
            secondname  = input("enter your second name: ")
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
            print("thanks for signig up as a candidate")
    age()
    
    
    
    
elif askwho == 'c' or askwho == 'staffmember':
    a = {
        "malli" : "Malli2010",
        "nesh" : "1234",
        "sharon": "sharon2008"
                }
    complete = False
    user = {"malli" : "Malli2010", "nesh" : "1234" }
 
    while not complete:
        username = input("Username: ")
        password = input("Password: ")
        if username == user and password == password:
            continue
        elif username not in user:
            print("This is not a valid username, input username again!")
            continue
        elif password != user[username]:
        
            print("Password is not valid for username.")
            continue
        elif password == user[username]:
            print("Welcome username ")
            print("Thank you for logging on. ")
            complete = True
            print ("Username and Password Validated in Python")
        for a in c.execute('SELECT * FROM voters'):
            s = [(''),('')]
            s.append(a)
            listing = list(s)

            count = listing.count('mali,')
            print(count)
 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
