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
def main():
    askwho = input('''are you a:
    a/voter
    b/staffmember
    :''')


    if askwho == 'a' or askwho == 'voter':
        def voter():
            def adding_new_person():
                name1 = input("Enter your first name:  ")
                if name1 == '' or name1 == ' ':
                    print('you have inputed nothing try again')
                    adding_new_person()
                elif name1.isdigit():
                    print('pls input leters')
                    adding_new_person()
                def second_name():
                    name2 = input("Enter your second name:  ")
                    if name2 == '' or name2 == ' ':
                        print('you have inputed nothing try again')
                        second_name()
                    elif name1.isdigit():
                        print('pls input leters')
                        second_name()
                second_name()
                def age_of():
                    try:
                        age  = int(input("pls enter youre age: "))
                        if age < 18:
                            print('you are not an elegible voter.come back when you are 18')
                            exit()  
                        elif age == '' or age == ' ':
                            print('you have inputed nothing try again')
                            adding_new_person()
                        elif age > 37:
                            pass
                    except ValueError:
                        print ('That is not a number try again')
                        age_of()
                age_of()
                def idnumbera():
                    try:
                        idnumber = int(input("pls enter your id number(8 digits): "))
                        string_id_number = str(idnumber)
                        if len(string_id_number) < 8:
                            print("an ID number must be 8 digits.That is too low")
                            idnumbera()
                        elif len(string_id_number) >8 or len(string_id_number) <9:
                            pass
                    except ValueError:
                        print ('That is not a number try again')
                        idnumbera()
                idnumbera()
            adding_new_person()
            def candidets():
                a = input('''this are the candidates you can  vote for:
                malli
                nesh
                frank
                :''' )
                if a == '' or a == ' ':
                    print('you have inputed nothing try again')
                    candidets()
                print("Thanks for voting")
                c.execute("INSERT INTO voters VALUES(?)",(a,))
                conn.commit()
                listing = list(a)
            candidets()

        voter()




    elif askwho == 'b' or askwho == 'staffmember':
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

            c.execute('SELECT * FROM voters')
            cal = c.fetchall()
        
            votes = []

            c.execute('SELECT * FROM voters')
            print(c.fetchall())
            which_candidate_find = input("Which candidate are you searching for: ")
            nal = [item for a in cal for item in a]
            find_candidate = nal.count(which_candidate_find)
            print(find_candidate)




    elif askwho == '':
        print("you have inputed nothing try again")
        main()
    else:
        print('you have inputed the wrong thing try again!')
        main()


main()











