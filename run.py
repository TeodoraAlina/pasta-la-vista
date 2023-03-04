import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('pasta-la-vista')


def welcome_customer():
    """
    Greet customer
    """
    print("Welcome to Pasta la Vista,")
    print("where all you can eat is delicious pasta!\n")
    print("We will first need some information from you")
    print("then you can proceed to order.\n")
    print("Choose wisely, it is heard that our pasta")
    print("...can become addictive.\n")


welcome_customer()
