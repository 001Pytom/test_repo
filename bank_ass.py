import random
details = {}
database_for_known_users = {"user name":"faatihat mohammed",
                             "password":1234567890,
                             "email":"faatihat@gmail.com"}

class Bank_acc:
    def __int__(self, first_name, last_name, email, pass_word):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.pass_word = pass_word

s1 = Bank_acc("faatihat ", "mohammed","faatihat@gmail.com",1234 )
    def initial(self):
        valid_input = True
        while valid_input:
            print("welcome to Faatihat Bank...\n")

            have_acc = int(input("Do you have an account with US?\nIf YES enter '1', if NO enter '2'.\n"))

            if have_acc == 1:
                valid_input = False
                s.login()
            elif have_acc == 2:
                valid_input = False
                s.register()
            else:
                print("You have entered the wrong option.\n")

    def register(self):
        print("Since you don't have an account, you'll REGISTER.")
        print("***REGISTER***")
        s.email = input("enter your email. \n")
        s.first_name = input("what is your first name?\n")
        s.last_name = input("what is your last name?\n")
        s.pass_word = input('enter your desired password.\n')
        print("Wait while we generate an account number")


        s.generate_acc_no()
        print("Please save these details for future purpose....")
        s.acc_number = random.randrange(1111111111, 9999999999)
        s.user_name = s.first_name+" "+s.last_name
        details[s.acc_number] = [s.user_name, s.email]
        print(details)
        print("Now you can proceed to login")

        s.login()


    def generate_acc_no(self):
        print("Generating account number******")
        s.acc_number = random.randrange(1111111111, 9999999999)
        print("Your account number is {}".format(s.acc_number))



    def login(self):
        print("Welcome")
        username = input(" enter user name: ")
        Pass_word = input("enter your pass_word: ")
        # if s.pass_word == Pass_word:
        #     print("you've logged in successfully.")

    def deposit(self):
        print("deposit")

    def withdraw(self):
        print("withdraw")

    def transfer(self):
        print("transfer")

    def available_balance(self):
        print("balance")



# (self,pin,blahblah )
# my_acc_1 = Bank_acc("put in the things you want to compare")
# s.initial()
