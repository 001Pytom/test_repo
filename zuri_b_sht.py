# login
# ASK FOR acc number and password
# we will ask for username or email and pass word

# register
# ask for username, pass word and email
# generate user account

# initializing the system
import random

data_base = {}


def initial():
    print("welcome to Faatihat Bank")
    valid_option = True
    while valid_option:

        have_account = int(input("Do You have an account with us? input any of the number: 1(yes),2(no)\n"))

        if have_account == 1:
            valid_option = False
            login()
        elif have_account == 2:
            valid_option = False
            print(register())
        else:
            print("You have selected an invalid option")


def login():
    print("You can Log in to your account")
    bank_operation()


# noinspection PyUnreachableCode
def register():
    print("***REGISTER***")
    email = input("enter your email. \n")
    first_name = input("what is your first name?\n")
    last_name = input("what is your last name?\n")
    pass_word = input('enter your desired password.\n')

    account_number = generate_acc()
    print(account_number)

    data_base[account_number] = [first_name, last_name, email, pass_word]

    print('your account has been created')
    print("=== === === === ===")
    print("your account number is {}".format(account_number))
    print("Do keep it safe.")

    login()


def bank_operation():
    print("welcome ....")
    option = input("what would you like to do?")

def recharge():
    print("recharge")

def transfer():
    print("trans")




def generate_acc():
    print("Generating account number...")
    return random.randrange(1111111111, 9999999999)


initial()
# print(generate_acc())
# print(register())
