import mysql.connector
import sys
class DBhelper:
    def __init__(self):
        # connect to database
        try:

            self.connection=mysql.connector.connect(host="localhost",user="root",password="",database="db-starting-demo")
            # create cursor-->it can talk to database
            self.mycursor=self.connection.cursor()
            print("Connected to database")
        except Exception as e:
            print("Cannot connect to database.Try after sometime")
            sys.exit(0)

    def register(self,name,email,password):
        try:

            self.mycursor.execute("""INSERT INTO `users` (`id`, `name`, `email`, `password`) VALUES (NULL, '{}', '{}', '{}')""".format(name,email,password))
            self.connection.commit()
        except Exception as e:
            return -1
        else:
            return 1

    def search(self,email,password):
        self.mycursor.execute("""SELECT * FROM users WHERE email LIKE '{}' AND password LIKE '{}'""".format(email,password))
        data=self.mycursor.fetchall()
        return data

    def already_registered(self,email):
        self.mycursor.execute("""SELECT * FROM users WHERE email LIKE '{}'""".format(email))
        data=self.mycursor.fetchall()
        return data


