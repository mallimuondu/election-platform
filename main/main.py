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
def main():
    askwho = input('''are you a:
    a/voter
    b/candidate
    c/staffmember
    :''')


    if askwho == 'a' or askwho == 'voter':
        def voter():
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
                    else:
                        print('pls input a number!! try again')
                        adding_new_person()
                    idnumber = int(input("pls enter your id number(8 digits): "))
                    string_id_number = str(idnumber)
                    if len(string_id_number) < 8:
                        print("an ID number must be 8 digits.That is too low")
                        adding_new_person()
                    elif len(string_id_number) >8 or len(string_id_number) <9:
                        print(name1 + " welcome")
                    else:
                        print('pls input a number!! try again')
                        adding_new_person()
                adding_new_person()

            elif a == '':
                print("you have inputed nothing try again")
                voter()
            else:
                print('you have inputed the wrong thing! try again!')
                voter()
            def candidets():
                f.execute('SELECT * FROM people')
                print(f.fetchall())
                a = input('''choose a candidets:
                :''' )
                c.execute("INSERT INTO voters VALUES(?)",(a,))
                conn.commit()
                listing = list(a)
                count = listing.count('malli,')
                print(count)
                print("Thanks for voting for "+a)
            candidets()

        voter()


    elif askwho == 'b' or askwho == 'candidate':
        def addinput():
            while True:
                name  = input("enter your first name: ")
                secondname  = input("enter your second name: ")
                idnumber = int(input("pls enter your id number(8 digits): "))
                string_id_number = str(idnumber)
                if len(string_id_number) < 8:
                    print("an ID number must be 8 digits.That is too low")
                    addinput()
                elif len(string_id_number) >8 or len(string_id_number) <9:
                    print(name1 + " welcome")
                else:
                    print('pls input a number!! try again')
                
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

            def read():
                c.execute('SELECT * FROM voters')
                global db
                db = c.fetchall()
                print(db)
            read()
            def count():
                res = []
                for a in db:
                    for item in a:
                        res.append(item)
                print(res)
                print('malli has ')
                occarence = res.count('malli',)
                print(occarence)
                print('votes ')
            count()




    elif askwho == '':
        print("you have inputed nothing try again")
        main()
    else:
        print('you have inputed the wrong thing try again!')
        main()


main()











