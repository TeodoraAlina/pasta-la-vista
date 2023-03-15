# Pasta la Vista
## Project Portofolio Three
Pasta la Vista is a lovely italian restaurant located in Tirol, Austria. As it's so close to the pasta paradise Italy, all their ingredients are freshly coming from the mother country. As the title implies, in this restaurant the only type of dish that you can order is delicious pasta. This command-line application was created so the business can spread their popularity even further through home delivery orders.

You can view the live project here - [Pasta la Vista](https://pasta-la-vista.herokuapp.com/)

You can view the GitHub repository here - [TeodoraAlina/pasta-la-vista](https://github.com/TeodoraAlina/pasta-la-vista)
***

## User Experience (UX)

### Strategy
* The application will provide a way for ordering from the restaurant.
* The application will collect data for the restaurant about orders and customers details.
* Customers will be greeted when entering the application.
* Customers will have multiple options of dishes and pasta types to order from.
* Customers will be able to order to a maximum of 10 dishes of the same dish.
* Provide the price of the order for the customer.
* Provide the time when the order will arrive at the customer's place.
* The order will be confirmed before being sent to the restaurant.
* The restaurant will be provided with the orders details on a spreadsheet.
***

### User Stories
As a customer I want to be able to:
* Easily determine the purpose of the application.
* Be greeted when entering the application.
* Start placing an order with ease.
* Find out what dishes I can order.
* Find out what types of pasta I can choose from my dish.
* Order more of the same dish.
* Restart the order before placing it, in case I did a mistake during the order.
* Be informed in how much time the order will be at my place.

As the owner I want to be able to:
* Provide a way for my customers to eat from the restaurant anywhere they like.
* Have stored data of orders and customer details so I can improve my business.
***

### Structure
The command-line application will consist of:
* The customer will be welcomed to the CLI (command-line interface) with a message from Pasta la Vista restaurant.
* The customer will be announced about the first step of the order.
* The customer will be asked to provide name, address and telephone number.
* The customer will be provided with the menu.
* The customer has to choose an item from the menu.
* The customer will be provided with the types of pasta that the restaurant has.
* The customer has to choose a type of pasta for his dish.
* Confirmation of the order will be provided, asking the user if they would like to send the order, restart it or exit to the Main Menu.
* If the user chooses to send the order, then the order will be placed and the Google sheet will be updated with the new order for the restaurant.
* A thank you message and the time for the order will appear.
***

### Skeleton
The website will contain a simple interface that immediately greets the customers and takes them through the process with minimal inputs.

If the customer makes an error whilst navigating through the system, a message will appear guiding them on the steps to take, whilst also having the ability to navigate to the Main Menu and exit the system. Furthermore, customers will have the ability to restart the order from within the interface.
***

### Features
### Existing Features 
### Main Menu
* A welcome message greets the customer.
* The user is informed with the next step.
* The main menu is displayed when the application starts. To keep the interface simple to use, the menu divides the functionality into two options: 1. Place Order, 2. Exit Ordering System
![Main Menu](documentation/images/main-menu.png)
* The user has to choose between the two options. If the user's input is invalid then an error message will appear to inform and invite the user to try again.
![Main Menu error message](documentation/images/main-menu-error-message.png)
* The error message appears until the user's input is valid. If the user chooses the option two, then the system is exited.
* If the user chooses option one, then the order process starts.
![Place Order](documentation/images/place-order.png)
* From there, the user can either choose to go back to the Main Menu or continue to place the order.
### Place Order
### Customer details 
* The user is informed that first some details will be needed. The user is asked to provide the name.
![Name](documentation/images/name.png)
The user has to provide only alphabetical input. If this fails, then an error message appears and asks the user to try again.
![Name Error](documentation/images/name-error.png)
* After the name is provided, the user is asked for the address of delivery.
[Address](documentation/images/address.png)
* If the user enters a space instead of the address, then an error message appears and asks the user to try again.
[Address Error](documentation/images/address-error.png)




