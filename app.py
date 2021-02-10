import sys
from dbhelper import DBhelper

class LoginOrRegistration:
    def __init__(self):
        # connect  to database
        self.db=DBhelper()
        self.user_menu()
    def user_menu(self):
        user_input = input("""Hello, how may I help you
                1. Enter 1 to create an account
                2. Enter 2 to login
                3. Press anything else to exit""")

        if user_input == '1':
            self.register()
        elif user_input == '2':
            self.login()
        else:
            sys.exit(0)

    def register(self):
        name=input("Enter your name")
        email=input("Enter your email")
        res = self.db.already_registered(email)
        if len(res) != 0:
            print("Can't register as this email id already registered")
        else:
            password = input("Enter your password")
            response = self.db.register(name, email, password)

            if response == 1:
                print("Registration successful")
            else:
                print("Registration failed")
        self.user_menu()

    def login(self):
        email=input("Enter your email")
        password=input("Enter your password")
        response=self.db.search(email,password)
        if len(response)!=0:
            print("Hello",response[0][1])
        else:
            print("Incorrect email/password")
            self.login()


obj=LoginOrRegistration()
