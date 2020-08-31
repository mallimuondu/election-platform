from daterbase import *
def clock():  # This part will great you dipending on time
    now = time.datetime.now()
    hour = now.hour
    if hour < 12:
        print("Good morning")
    elif hour > 12 and hour < 18:
        print("Good afternoon")
    elif hour > 18 and hour < 19:
        print("Good evening")
    else:
        print('Good night.')
clock()
a = input("are you new or not new: ")
if a == 'not new':
    def login(): # this is login for not new people
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
                break
            else:
                print("Username and passwored not recognised")
                again = input("Do u want to try again?(y/n): ")
                if again.lower() == "n":
                    print("Good Bye")
                    time.sleep(1)
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
    elif age > 18:
        print("You are able to vote HURRAY!!")
    
voters()