"""
Import libraries to support the application
"""
import re
import sys
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


def clear():
    """
    Clear the screen for the next content to be shown
    """
    print('\033c')


def get_name():
    """
    Request and validate customer's name.
    User can choose to whether exit to main menu
    or continue to place the order.
    """
    print("What would you like to do next?\n")
    print("1. Continue to place your order")
    print("2. Exit to Main Menu\n")
    print("Please select an option by entering either 1 or 2\n")
    #  While loop to provide sub-menu options
    #  If not valid, error message asks the user to try again
    while True:
        selection = input("Enter your choice here:\n").strip()
        if selection == "1":
            print("Amazing! We will first need some personal "
                  "details from you.\n")
            break
        elif selection == "2":
            main()
        else:
            print("\nInvalid choice, please enter a number between 1-3\n")
            continue
    while True:
        name_str = input('Please enter your name:\n')
        if name_str.isalpha():
            print(f"Lovely name {name_str.title()}, "
                  "let's keep it going.\n")
        else:
            print("That doesn't look like a name...please, try again.\n")
            continue
        return name_str


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
            print("Thank you! We will deliver your order at this address.\n")
        return address


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
                  " when we get at your location.\n")
        else:
            print("Invalid number. You must enter 11 digits, starting with 07,"
                  " plese try again!\n")
            continue
        return tel_number


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
    print("Please enter a number between 1-5\n"
          "or enter:\n"
          "(R) to restart order\n"
          "(E) to exit to Main Menu\n")
    while True:
        dish = input("Enter your choice here:\n").capitalize()
        if dish == "1":
            print("Nice choice! Cacio e pepe it is!\n")
            return "Cacio e pepe"
        elif dish == "2":
            print("Nice choice! Carbonara it is!\n")
            return "Carbonara"
        elif dish == "3":
            print("Nice choice! Bolognese it is!\n")
            return "Bolognese"
        elif dish == "4":
            print("Nice choice! Al Pomodoro it is!\n")
            return "Al Pomodoro"
        elif dish == "5":
            print("Nice choice! Limone e Pepe it is!\n")
            return "Limone e Pepe"
        elif dish == "R":
            break
        elif dish == "E":
            main()
        else:
            print("Invalid choice, please enter a number between 1-5")
            continue
    place_order()


def get_pasta():
    """
    Provide a table for types of pasta.
    Request user to input a choice between 1-5.
    Use table rows for this data.
    """
    print("We have different types of pasta for you to choose from")
    print("Which one would you like to choose?\n")
    pasta = SHEET.worksheet("Pasta").get_all_values()
    print(tabulate(
        pasta, headers='firstrow', tablefmt='fancy_grid'))
    print("Please enter a number between 1-5\n"
          "or enter:\n"
          "(R) to restart order\n"
          "(E) to exit to Main Menu\n")
    while True:
        pasta_choice = input("Enter your choice here:\n").strip()
        if pasta_choice == "1":
            pasta_choice = "Spaghetti"
            print("Yummy! You chose Spaghetti.\n")
            return pasta_choice
        elif pasta_choice == "2":
            pasta_choice = "Tagliatelle"
            print("Yummy! You chose Tagliatelle.\n")
            return pasta_choice
        elif pasta_choice == "3":
            pasta_choice = "Penne"
            print("Yummy! You chose Penne.\n")
            return pasta_choice
        elif pasta_choice == "4":
            pasta_choice = "Fettuccine"
            print("Yummy! You chose Fettuccine.\n")
            return pasta_choice
        elif pasta_choice == "5":
            pasta_choice = "Rigatoni"
            print("Yummy! You chose Rigatoni.\n")
            return pasta_choice
        elif pasta_choice == "R":
            break
        elif pasta_choice == "E":
            main()
        else:
            print("Invalid choice, please enter a number between 1-5\n")
            continue
    place_order()


def get_quantity(dish, pasta_choice):
    """
    User can choose how many dishes
    would they like.
    """
    print("How many of this yummy dish would you like?\n"
          "Plese enter a number between 1-10 below\n"
          "or enter:\n"
          "(R) to restart order\n"
          "(E) to Main Menu.\n")
    while True:
        quantity = input("Enter your choice here:\n")
        if quantity == "1":
            print(f"Thank you! You ordered {quantity} {dish} "
                  f"made with {pasta_choice} pasta.\n")
            return int(quantity)
        elif quantity == "2":
            print(f"Thank you! You ordered {quantity} {dish} "
                  f"made with {pasta_choice} pasta.\n")
            return int(quantity)
        elif quantity == "3":
            print(f"Thank you! You ordered {quantity} {dish} "
                  f"made with {pasta_choice} pasta.\n")
            return int(quantity)
        elif quantity == "4":
            print(f"Thank you! You ordered {quantity} {dish} "
                  f"made with {pasta_choice} pasta.\n")
            return int(quantity)
        elif quantity == "5":
            print(f"Thank you! You ordered {quantity} {dish} "
                  f"made with {pasta_choice} pasta.\n")
            return int(quantity)
        elif quantity == "6":
            print(f"Thank you! You ordered {quantity} {dish} "
                  f"made with {pasta_choice} pasta.\n")
            return int(quantity)
        elif quantity == "7":
            print(f"Thank you! You ordered {quantity} {dish} "
                  f"made with {pasta_choice} pasta.\n")
            return int(quantity)
        elif quantity == "8":
            print(f"Thank you! You ordered {quantity} {dish} "
                  f"made with {pasta_choice} pasta.\n")
            return int(quantity)
        elif quantity == "9":
            print(f"Thank you! You ordered {quantity} {dish} "
                  f"made with {pasta_choice} pasta.\n")
            return int(quantity)
        elif quantity == "10":
            print(f"Thank you! You ordered {quantity} {dish} "
                  f"made with {pasta_choice} pasta.\n")
            return int(quantity)
        elif quantity == "R":
            break
        elif quantity == "E":
            main()
        else:
            print("Invalid choice, please enter a number between 1-10\n"
                  "or R to restart order\n"
                  "E to exit to Main Menu\n")
            continue
        place_order()


def get_price(dish, quantity):
    """
    Calculate the price of the order.
    """
    order_price = SHEET.worksheet("Menu").get_all_values()
    if dish == ("Cacio e Pepe"):
        price = quantity * order_price.at[0, 'Price']
        print(f"The price of your order is {price}")
        return price
        print(price)


def update_order_worksheet(data):
    """
    Export provided order to external worksheet
    """
    orders_worksheet = SHEET.worksheet("Orders")
    orders_worksheet.append_row(data)
    print("Your order has been received")
    main()


def place_order():
    """
    Provides steps for user to order.
    Functions are called in a logical order.
    User can choose whether to restart order,
    send order or exit to Main Menu.
    """
    name_str = get_name()
    address = get_address()
    tel_number = get_tel_number()
    dish = get_menu()
    pasta_choice = get_pasta()
    quantity = get_quantity(dish, pasta_choice)
    price = get_price(dish, quantity)

    order = [
        name_str.title(),
        address,
        tel_number,
        dish,
        pasta_choice,
        quantity,
        price
    ]
    print(f"Thank you {name_str.title()}! You ordered\n"
          f"{dish} made with {pasta_choice} for {price}\n")
    print("Are you satisfied with your order?\n")
    print("Please enter:\n"
          "1. to send your order\n"
          "2. to restart your order\n"
          "3. to exit to Main Menu\n")
    while True:
        user_confirm = input("Please enter your choice here:\n").strip()
        if user_confirm == "1":
            update_order_worksheet(order)
        if user_confirm == "2":
            place_order()
        if user_confirm == "3":
            main()
        else:
            print("Invalid choice, please enter a number between 1-3")
            continue
        place_order()


def main():
    """
    Execute first fuctionality for the user interface
    Greet customer
    """
    clear()
    print('Welcome to Pasta la Vista,')
    print('where all you can eat is delicious pasta!\n')
    print('We will first need some information from you')
    print('then you can proceed to order.\n')
    print('Choose wisely, it is heard that our pasta')
    print('...can become addictive.\n')
    print("Main Menu")
    print("1. Place an Order")
    print("2.Exit Ordering System\n")
    print("Please select an option by entering a number between 1-2\n")
    while True:
        selection = input("Enter your choice here:\n").strip()
        if selection == "1":
            place_order()
        elif selection == "2":
            sys.exit("Sad to see you go! See you soon though..."
                     "Have a wonderful day!\n")
        else:
            print("Invalid choice, please enter a number between 1-2\n")
            continue


if __name__ == "__main__":
    main()
