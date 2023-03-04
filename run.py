import re
import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate


SCOPE = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive'
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('pasta-la-vista')


def welcome_customer():
    """
    Greet customer
    """
    print('Welcome to Pasta la Vista,')
    print('where all you can eat is delicious pasta!\n')
    print('We will first need some information from you')
    print('then you can proceed to order.\n')
    print('Choose wisely, it is heard that our pasta')
    print('...can become addictive.\n')


welcome_customer()


def get_name():
    """
    Request and validate customer's name
    """
    while True:
        name_str = input('Please enter your name:\n')
        if name_str.isalpha():
            break
        else:
            print("That doesn't look like a name...please, try again.\n")
    print(f"Lovely name {name_str.capitalize()}, let's keep it going.\n")


get_name()


def get_address():
    """
    Request user's address
    """
    while True:
        address = input('Please enter your address for delivery:\n')
        if address == '':
            print("It seems like you haven't entered an address,")
            print("please try again\n")
        else:
            break
    print("Thank you! We will deliver your order at this address.\n")


get_address()


def get_tel_number():
    """
    Request and validate customer telephone number
    User must enter 11 digit numbers starting with 07
    """
    print("Please enter your telephone number.\n")

    def validate_tel_num(tel_number):
        """
        Validate user telephone number
        using RE compile method
        """
        telnum_pattern = re.compile(r"^(07\d{9}|447\d{9})$")
        return telnum_pattern.match(tel_number)
    #  While loop to request user inputs valid contact phone number
    #  If not valid, error message asks the user to try again
    while True:
        tel_number = input("Enter your telephone number here:\n")
        if validate_tel_num(tel_number):
            print(f"Thank you, we will use {tel_number} to contact you"
                  " when we get at you location\n")
        else:
            print("Invalid number. You must enter 11 digits, starting with 07,"
                  " plese try again!\n")
            continue
        return tel_number


get_tel_number()


def get_menu():
    """
    Provides the menu for the user
    Receives data from external spreadsheet
    Use table rows for this data
    Request user to input a choice between 1-5
    """
    print("Here are our delicious pasta dishes.")
    print("Which one would you like to enjoy?\n")
    menu = SHEET.worksheet('Menu').get_all_values()
    print(tabulate(
        menu, headers='firstrow', tablefmt='fancy_grid'))


get_menu()