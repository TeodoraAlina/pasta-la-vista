"""
Import libraries to support the application
"""
import re
import sys
import time
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
    Args:
        Request user to input name and strip whitespaces
        If statements validates the input using isalpha()
        Else requests the user to try again
    Returns:
           Confirm statement is valid using print statement
           name_str used within place_order function
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
            print("\nInvalid choice, please enter a number between 1-2.\n")
            continue
    # If user chooses option 1, while loop is used to request user's name
    # If not valid, error message asks the user to try again
    while True:
        name_str = input('Please enter your name:\n').strip()
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
    Args:
        Request user to input address and strip whitespaces
        If statement checks for blank space validation
        and requests the user to try again
    Returns:
           Print statement confirming input is valid
           address used within place_order function
    """
    while True:
        address = input('Please enter your address for delivery:\n').strip()
        if address == '':
            print("It seems like you haven't entered an address,")
            print("please try again.\n")
            continue
        else:
            print("Thank you! We will deliver your order at this address.\n")
        return address


def get_tel_number():
    """
    Request and validate customer telephone number
    Args:
        While True: user must enter 11 digit numbers starting with 07
        validate_tel_number used to validate tel_number variable
        using Re pattern match
    Return:
          Confirm input is valid using print statement
          tel_number used within place_order function
    """
    print("Please enter your telephone number.\n")
    #  While loop to request user inputs valid contact phone number
    #  If not valid, error message asks the user to try again
    while True:
        tel_number = input("Enter your telephone number here (11 digits, "
                           "starting with 07) :\n")
        if validate_tel_num(tel_number):
            print(f"Thank you, we will use {tel_number} to contact you"
                  " when we get at your location.\n")
        else:
            print("Invalid number, plese try again!\n")
            continue
        return tel_number


def validate_tel_num(tel_number):
    """
    Validate user telephone number
    using RE compile method
    """
    telnum_pattern = re.compile(r"^(07\d{9}|447\d{9})$")
    return telnum_pattern.match(tel_number)


def get_menu():
    """
    Provides the menu for the user
    Receives data from external spreadsheet
    Use table rows for this data
    Request user to input a choice between 1-5
    """
    menu = SHEET.worksheet('Menu').get_all_records()
    return menu


def get_order():
    """
    Provides the menu for the user
    Args:
        Receives data from external spreadsheet
        Use table rows for this data
        While loop requests user to input a choice between 1-5
        Else requests the user to try again.
    Returns:
           Print statement confirming input is valid
           dish used within place_order function
    """
    # Print statement to inform the user of what content is displayed
    print("Here are our delicious pasta dishes.")
    print("Which one would you like to enjoy?\n")
    # Printing the menu imported in the get_menu
    # function from external spreadsheet
    menu = get_menu()
    print(tabulate(
        menu, headers='firstrow', tablefmt='fancy_grid'))
    print("Please enter a number between 1-5\n"
          "or enter:\n"
          "(R) to restart order\n"
          "(E) to exit to Main Menu\n")
    # While loop used to request user to input valid dish choice between 1-5,
    # to restart the order or to exit to Main Menu
    # If not valid, error message asks the user to try again
    while True:
        dish = input("Enter your choice here:\n").capitalize()
        if dish == "1":
            print("Nice choice! Cacio e Pepe it is!\n")
            return "Cacio e Pepe"
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
    Args:
        Receive data from external spreadsheet
        Use table rows for this data
        While loop requests user to input a number between 1-5
        Else requests the user to try again.
    Returns:
           Confirm user input using print statement
           pasta_choice used within place_order function
    """
    # Print statement to inform the user of what content is displayed
    print("We have different types of pasta for you to choose from.")
    print("Which one would you like to choose?\n")
    # Printing the pasta menu imported from external spreadsheet
    pasta = SHEET.worksheet("Pasta").get_all_values()
    print(tabulate(
        pasta, headers='firstrow', tablefmt='fancy_grid'))
    # While loop used to request user to input
    # valid types of pasta between 1-5,
    # or to restart the order
    # or to exit to Main Menu
    # If not valid, error message asks the user to try again
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
            print("Invalid choice, please enter a number between 1-5.\n")
            continue
    place_order()


def get_quantity(dish, pasta_choice):
    """
    User can choose how many dishes
    would they like to have.
    Args:
        While loop requests user to input a choice between 1-10
        If valid, order is confirmed using print statement
        Else requests the user to try again
        Variable prompt used for printing repetitive print statement.
    Returns:
            quantity used within place_order function
    """
    prompt = ("Please enter a number between 1-10 below\n"
              "or enter:\n"
              "(R) to restart order\n"
              "(E) to Main Menu.\n")
    # While loop requests user to input valid quantity between 1-10
    # or to restart the order
    # or to exit to Main Menu
    # If not valid, error message asks the user to try again
    print("How many of this yummy dish would you like?\n")
    print(prompt)
    while True:
        quantity_input = input("Enter your choice here:\n").strip()
        try:
            quantity = int(quantity_input)

            if 1 < quantity <= 10:
                print(f"Thank you! You ordered {quantity} {dish} "
                      f"made with {pasta_choice} pasta.\n")
                return quantity
            else:
                print("Invalid choice.")
                print(prompt)
                continue
        except ValueError as err:
            if quantity_input.upper() == "R":
                place_order()
            elif quantity_input.upper() == "E":
                main()
            else:
                print(err)
                print(prompt)
                continue
        place_order()


def get_price(dish, quantity):
    """
    Calculate the price of the order.
    Args:
        dish: user choice of dish from menu
        quantity: user choice of number of dishes between 1-10
        If statement used to multiply the price of the dish * quantity
    Returns:
           f string with calculated price used within place_order function
           price used within place_order function
    """
    order_price = SHEET.worksheet("Menu").get_all_records()
    if dish == "Cacio e Pepe":
        price = quantity * order_price[0]['Price(€)']
        return price
    if dish == "Carbonara":
        price = quantity * order_price[1]['Price(€)']
        return price
    if dish == "Bolognese":
        price = quantity * order_price[2]['Price(€)']
        return price
    if dish == "Al Pomodoro":
        price = quantity * order_price[3]['Price(€)']
        return price
    if dish == "Limone e Pepe":
        price = quantity * order_price[4]['Price(€)']
        return price


def update_order_worksheet(data):
    """
    Export provided order to external worksheet
    """
    #  Identifies the applicable worksheet from the external spreadsheet
    #  Appends the users order to the last row of that worksheet
    #  Print statement confirms the order has been sent to the kitchen
    #  Returns user back to the Main Menu
    orders_worksheet = SHEET.worksheet("Orders")
    orders_worksheet.append_row(data)
    print("We got your order!\n"
          "Now relax and we'll be there with your delicious pasta "
          "in maximum 30 minutes!\n")
    # Sets a delay to allow time for user to read
    time.sleep(4.5)
    main()


def place_order():
    """
    Provides steps for user to order.
    Functions are called in a logical order.
    User can choose whether to restart order,
    send order or exit to Main Menu.
    """
    # Clear screen for next functions
    clear()
    # Request the user name, address and telephone number
    name_str = get_name()
    address = get_address()
    tel_number = get_tel_number()
    # Sets a delay to allow time for user to read
    time.sleep(3)
    # Clear screen for next functions
    clear()
    # Request and return user choice of dish
    dish = get_order()
    # Sets a delay to allow time for user to read
    time.sleep(2)
    # Clear screen for next functions
    clear()
    # Request and return user choice of pasta
    pasta_choice = get_pasta()
    # Sets a delay to allow time for user to read
    time.sleep(2)
    # Clear screen for next functions
    clear()
    # Request and return user choice of quantity
    quantity = get_quantity(dish, pasta_choice)
    # Sets a delay to allow time for user to read
    time.sleep(2)
    # Clear screen for next functions
    clear()
    # Request and return the price of the order
    price = get_price(dish, quantity)
    # Sets a delay to allow time for user to read
    time.sleep(2)
    # Clear screen for next functions
    clear()

    # List containing the returned values from functions to confirm order
    order = [
        name_str.title(),
        address,
        tel_number,
        dish,
        pasta_choice,
        quantity,
        price
    ]

    # Confirm order for the customer and provide order reference
    print(f"Thank you {name_str.title()}! You ordered "
          f"{quantity} {dish} made with {pasta_choice} for €{price}.\n")
    # While loop used to request user to either
    # send the confirmed order
    # restart the order
    # or exit to Main Menu
    # If input is not valid, error message asks the user to try again
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
            print("Invalid choice, please enter a number between 1-3.\n")
            continue
        place_order()


def main():
    """
    Execute first fuctionality for the user interface
    Greet customer and provide a Main Menu with 2 choices.
    Args:
        Request user to input a number between 1-2
        If statement executes a function depending on input choice
        1. place_order function
        2. exit system using sys.exit()
        Else requests the user to try again.
    """
    # Clear previous content to print welcome message and Main Menu
    clear()
    print('Welcome to Pasta la Vista,')
    print('where all you can eat is delicious pasta!\n')
    print('We will first need some information from you')
    print('then you can proceed to order.\n')
    print('Choose wisely, it is heard that our pasta')
    print('...can become addictive.\n')
    print("Main Menu")
    print("1. Place an Order")
    print("2. Exit Ordering System\n")
    print("Please select an option by entering a number between 1-2.\n")
    # While loop used to request user to enter valid inputs between 1-2
    # If not valid, error message asks the user to try again
    while True:
        selection = input("Enter your choice here:\n").strip()
        if selection == "1":
            place_order()
        elif selection == "2":
            sys.exit("Sad to see you go! See you soon though..."
                     "Have a wonderful day!\n")
        else:
            print("Invalid choice, please enter a number between 1-2.\n")
            continue


if __name__ == "__main__":
    # Execute main Python function
    main()
