# Pasta la Vista
## Project Portofolio Three
Pasta la Vista is a lovely italian restaurant located in Tirol, Austria. As it's so close to the pasta paradise Italy, all their ingredients are freshly coming from the mother country. As the title implies, in this restaurant the only type of dish that you can order is delicious pasta. This command-line application was created so the business can spread their popularity even further through home delivery orders.

You can view the live project here - [Pasta la Vista](https://pasta-la-vista.herokuapp.com/)

You can view the GitHub repository here - [TeodoraAlina/pasta-la-vista](https://github.com/TeodoraAlina/pasta-la-vista)
***

## User Experience (UX)

### Strategy
* The application will provide a way to order from the restaurant.
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
* Find out what types of pasta I can choose for my dish.
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

## Features
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

### Customer details 
* The user is informed that first some details will be needed. The user is asked to provide the name.
![Name](documentation/images/name.png)
The user has to provide only alphabetical input. If this fails, then an error message appears and asks the user to try again.
![Name Error](documentation/images/name-error.png)
* After the name is provided, the user is asked for the address of delivery.
![Address](documentation/images/address.png)
* If the user enters a space instead of the address, then an error message appears and asks the user to try again.
![Address Error](documentation/images/address-error.png)
* A message appears confirming that the address has been received, then the user is asked for the telephone number.
![Telephone Number](documentation/images/telephone-number.png)
* The user has to enter a number with 11 digits and starting with 07, if that fails, an error message appears and asks for the user to try again.
![Telephone Number Error](documentation/images/telephone-number-error.png)
* A confirmation message of the number appears.

### Place Order
* A table presenting the menu of the restaurant is displayed. The user is asked to make a choice or type R to restart order, type E to exit to Main Menu.
![Menu](documentation/images/menu.png)
* If the user enters an invalid input, an error message appears and asks the user to try again, until the user's input is valid. A confirmation message appears.
![Menu Error](documentation/images/Menu-error.png)
* A table presenting the type of pasta that the restaurant has is displayed. The user is asked to mae a choice or type R to restart order, E to exit to Main Menu.
![Pasta Menu](documentation/images/pasta.png)
* If the user enters an invalid input, an error message appears and asks the user to try again, until the user's input is valid. A confirmation message appears.
![Pasta Error](documentation/images/pasta-error.png)
* Then, the user is being asked of how much of the selected dish they would like. If the user enters an invalid input, an error message appears and asks the user to try again, until the user's input is valid. A confirmation message appears.
![Quantity](documentation/images/quantity.png)
* The user is announced with the total cost of the order. The customer can choose whether to send order, restart order or exit to Main Menu.
![Price](documentation/images/price.png)
* If the user chooses to send the order then a confirmation on receiving the order will appear and the user is announced on how long will it take for the order to be delivered.
![Send Order](documentation/images/send-order.png)

### Future Features
* A view order option where customers can see how busy the restaurant is at the moment.
* An online paying option for the customers.
* An application made for smartphones.
***

## Technologies Used
### Languages
[Python v2023.4.0](https://www.python.org/)

### Frameworks, Libraries and Programs
* [Google Spreadsheets](https://en.wikipedia.org/wiki/Google_Sheets): used as the external data store for the Orders and Menu data used by the project.
* [Google Drive API](https://developers.google.com/drive/api/guides/about-sdk): used to generate credentials used in the project to securely access the Google Spreadsheet.
* [Google Sheets API](https://developers.google.com/sheets/api/guides/concepts): used to support interactions (e.g. read/write functionality) between the code and data stored in the Google Spreadsheet.
* [gspread](https://docs.gspread.org/en/latest/): Python API for Google Sheets
* [Google Auth](https://google-auth.readthedocs.io/en/master/): Google authentication library for Python required to use the credentials generated for Google Drive API
* [Git](https://git-scm.com/): was used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
* [GitHub](https://github.com/): is used as the repository for the project's code after being pushed from Git.
* [Heroku](https://dashboard.heroku.com/): is used to deploy the application and provide an enviroment in which the code can execute.
***

## Testing
### Testing User Stories
| Reference  | Description  |
|---|---|
| 01  | Easily determine the purpose of the application  |
| Validation  | The user can easily determine that this is an application where you can order food from Pasta la Vista restaurant.  |
| 02  | Be greeted when entering the application.  |
| Validation  | The customers are being greeted when entering the application.  |
| 03  | Start placing an order with ease.  |
| Validation  | The user can immediately choose to place an order from the main menu.  |
| 04  | Find out what dishes I can order.  |
| Validation  | A menu is being displayed for the user, after all the user's details have been completed.  |
| 05  | Find out what types of pasta I can choose for my dish.  |
| Validation  | The user is being presented with the types of pasta that the restaurant has.  |
| 06  | Order more of the same dish.  |
| Validation  | The user is able to order more of the same dish by entering a number between 1-10.  |
| 07  | Restart the order before placing it, in case I did a mistake during the order.  |
| Validation  | The user can restart the order at any time during ordering process.  |
| 08  | Be informed in how much time the order will be at my place.  |
| Validation  | After the order is confirmed, the user is being informed of how much time will take for the delivery.  |
| 09  | Provide a way for my customers to eat from the restaurant anywhere they like.  |
| Validation  | With the help of this command-line application, the customers can order from anywhere they like.  |
| 10  | Have stored data of orders and customer details so I can improve my business.  |
| Validation  | The orders are being received and stored in the google sheet "pasta-la-vista".  |
***

### Test Cases and Results
| Test Category  | Steps  | Expected Outcome  | Result  |
|---|---|---|---|
| Main Menu  | Run the application.   |  Welcome message. Main menu with option 1. Place order and option 2. Exit Ordering System. Ask the user to input an option. | Pass  |
| Main Menu - data checks  | Run the application, enter a variety of invalid inputs. e.g. cat, empty string, 6. | Error messsage apppears and asks the user to try again.  | Pass  |
| Main Menu - option 2  | Enter a value of 2.  | The application says goodbye and system is being terminated.  | Pass  |
| Main Menu - option 1  | Enter a value of 1.  | User can choose from option 1. Continue to place order and option 2. Exit to Main Menu. Ask the user to input an option.  | Pass   |
| Place Order - option 2  | Enter a value of 2.  | Main Menu is displayed.  | Pass  |
| Place Order - option 1  | Enter a value of 1.  | User is asked to introduce his name.  | Pass   |
| Enter Name - data checks  | Enter invalid inputs, e.g. 12, empty string, @.  | Error message appears and asks the user to try again.  | Pass  |
| Enter Name  | Enter a valid input containing only alphabetical digits.  | A confirmation message of the name appears and the user is asked for the address of delivery.   | Pass  |
| Enter Address - data checks  | Enter invalid input containing empty string.  | Error message appears and asks the user to try again.  | Pass  |
| Enter Address  | Enter a valid input.  | Confirmation message appears and asks the user for the telephone number. The number must begin with 07 and have 11 digits.  | Pass  |
| Enter Telephone Number - data checks  | Enter invalid inputs, e.g. cat, 10 digits, empty string, 11 digits but starting with 06.  | Error message appears and asks the user to try again.  | Pass  |
| Enter Telephone Number  | Enter valid input containing 11 digits and starting with 07.  | Confirmation message of the number appears. A table with the menu is displayed. Ask user to enter their choice (an input between 1 and 5).  | Pass  |
| Choose Pasta Dish - data checks  | Enter invalid inputs, e.g. cat, empty string, 10. | Error message appears and asks the user to try again.  | Pass  |
| Choose Pasta Dish  | Enter a valid input between 1 and 5, 'r' or 'e'.  | If user inputs 'r', he is redirected to place order screen. If user inputs 'e', he is redirected to the Main Menu. A confirmation message appears and a table containing the menu for the types of pasta is displayed. Ask user to enter an input between 1-5. | Pass  |
| Choose Pasta Type - data checks  | Enter invalid inputs, e.g. cat, empty string, 10.  | Error message appears and asks the user to try again.  | Pass  |
| Choose Pasta Type  | Enter a valid input between 1 and 5, 'r' or 'e'.  | If user inputs 'r', he is redirected to place order screen. If user inputs 'e', he is redirected to the Main Menu. A confirmation message appears. The the system asks the user the quantity of the dish that it is to be ordered. The quantity has to be between 1 and 10. | Pass  |
| Choose Quantity - data checks  | Enter invalid inputs, e.g. cat, empty string, 12  | Error message appears and asks the user to try again.  | Pass  |
| Choose Quantity  | Enter valid inputs containing numbers between 1 and 10, "r" or "e".  | If user inputs 'r', he is redirected to place order screen. If user inputs 'e', he is redirected to the Main Menu. If user inputs a number between 1 and 10, a confirmation message with the order apppears and the user is being informed of the total cost of the order. The user is being asked whether to 1. Send order, 2. Restart Order, 3. Exit to Main Menu.  | Pass  |
| Confirm Order - data checks  | Enter invalid inputs, cat, 12, empty string.  | Error message appears and asks the. user to try again.  | Pass  |
| Confirm Order - Restart Order  | Enter valid input 2.  | User is redirected to restart the order, back to place order screen.  | Pass  |
| Confirm Order - Exit to Main Menu | Enter valid input 3.  | User is redirected to the Main Menu.  | Pass  |
| Confirm Order - Send Order  | Enter valid input 1.  | A message appears announcing user that the order has been receive and that it will take a maximum of 30 minutes until it arrives at place of delivery. After that, Main Menu is displayed.  | Pass  |
| Spreadsheet - Orders  | After user sends order, check the spreadsheet if the data has been imported.  | All data has been received.  | Pass  |
***

### Validator Testing
* [Python Validator](https://pep8ci.herokuapp.com)
![Code Validator](documentation/images/validator-testing.png)
***

## Bugs
* There was a problem within the get_price function where the price did not show. Fixed it by putting the index number and the key in separate square brakets.
* While testing the code, it was a bug within the get_quantity function. When entering invalid inputs, an error showed up. Fixed it by changing the except statement from this code:
```
except ValueError():
            if quantity_input.upper() == "R":
                place_order()
            elif quantity_input.upper() == "E":
                main()
            else:
                print("Invalid choice.")
                print(prompt)
                continue
        place_order()
```
To this code:
```
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
```

## Known Bugs
There are no known bugs at the moment.
***

## Deployment

### Delpoying to GitHub Pages
<details>
<summary>The project was deployed with the following steps</summary>

* Log into GitHub;
* Click the "Settings" button in the menu above the Repository;
* Scroll down the Settings page to the "GitHub Pages" Section;
* Under "Source", click the dropdown called "None" and then select "Master Branch";
* The page will automatically refresh, and a link displaced. It may take some time for the link to show the website.
* If the page will not load go down to "template" under the "source" and select a template.
* Scroll back down through the page to locate the now published site link in the "GitHub Pages" section.
</details>

### Forking
<details>
<summary>Forking the GitHub Repository</summary>

By forking the GitHub Repository, you can make a copy of the original repository in your own GitHub account. This means we can view or make changes without making the changes affecting the original.

* Log into GitHub and locate the GitHub Repository;
* At the top of the Repository there is a "Fork" button about the "Settings" button on the menu;
* You should now have a new copy of the original repository in your own GitHub account.
</details>

### Cloning
 <details>
 <summary>Steps on cloning</summary>

Taken from GitHub's documentation on cloning, which can be found [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop)
 
* Once logged into GitHub, navigate to the repository you wish to clone.
* Next to the green Gitpod button there's a button that reads code, click this.
* To clone the repository using HTTPS, copy the link whilst HTTPS is selected.
* Open your local IDE of choice and open the terminal.
* Navigate to the working directory of where you want the cloned directory to be.
* Type ```git clone``` in the terminal and then paste the link that you selected in step 3. Press enter.
* The clone is created in your current working directory (```cwd```).
</details>

### Adding and commiting files
<details>
<summary>Steps to adding and commiting files</summary>
I’ve been using Gitpod to write my code and using the terminal within to add, commit and push code from my workspace to GitHub where it is stored remotely as shown in the course content.

* When I have made a couple of minor additions / changes or one large change or addition I add the file in question to the staging area by typing in the terminal git add . the full stop will add all new files.
* I now want to save my changes to the local repository by typing git commit –m “ ” into the terminal. Between the “ ” I'll write a concise message detailing what this commit has done.
* When I either want to upload all my changes for the day or view on GitHub Pages I push all the commits I’ve previously done to GitHub using the git push command. When GitHub Pages is set up for the repository in question it will automatically pick up these changes and display the most up to date version that has been pushed.
</details>

## Deploying to Heroku
<details>
<summary>Steps on how to deploy to Heroku</summary>
* The requirements.txt file in the project was updated to include details on the project dependencies. Steps to do this are : 
     * Enter the following command at the terminal prompt : 'pip3 freeze > requirements.txt'
     * Commit resulting changes to requirements.txt and push to github
     * Log in to [Heroku](https://id.heroku.com/), create an account if necessary.

* From the Heroku dashboard, click the Create new app button. For a new account an icon will be visible on screen to allow you to Create an app, otherwise a link to this function is located under the New dropdown menu at the top right of the screen.

* On the Create New App page, enter a unique name for the application and select region. Then click Create app.

* You will then be brought to the Application Configuration page for your new app. Changes are needed here on the Settings and Deploy tabs.

* Click on the Settings tab and then scroll down to the Config Vars section to set up the private Environment Variables for the application - i.e. the credentials used by the application to access the spreadsheet data.

* Click on Reveal Config Vars. In the field for key enter 'CREDS' and paste the entire contents of the creds.json file into the VALUE field and click ADD.

* Next, scroll down the Settings page to Buildpacks. Click Add buildpack, select Python from the pop up window and click on Save changes. Click Add buildpack again, select Node.js from the pop up window and click on Save changes. It is important that the buildpacks are listed Python first, then Node.js beneath.

* Click on the Deploy tab on the Application Configuration page.

* Select GitHub as the Deployment Method and if prompted, confirm that you want to connect to GitHub. Enter the name of the github repository (the one used for this project is https://github.com/TeodoraAlina/pasta-la-vista) and click on Connect to link up the Heroku app to the GitHub repository code.

* Scroll down the page and choose to either Automatically Deploy each time changes are pushed to GitHub, or Manually deploy - for this project Automatic Deploy was selected.

* The application can be run from the Application Configuration page by clicking on the Open App button.

* The live link for this project is (https://pasta-la-vista.herokuapp.com/)
</details>

## How to create and configure the Google spreadsheet and APIs
<details>
<summary>Steps to setup and configure access to data</summary>
* Create the Google Spreadsheet : 
    * Log in to your Google account (create one if necessary)
    * Create a Google Spreadsheet called 'ms3-event-scheduler' on Google Drive with 2 pages/sheets, one called 'events' and one called 'bookings'.
    * In row 1 of the events sheet, enter the headings : Event Code, Event Name, Date, Host, Capacity, Status Reason.
    * In row 1 of the bookings sheet, enter the headings : Event Code, Date, Name, Email, Seats
    * The initial sample data used in this project can be seen here, however it is not necessary to use that data : Content
***

* Set up APIs using the Google Cloud Platform
    * Access the [Google Cloud Platform](https://console.cloud.google.com/)
    * Create a new project and give it a unique name, then select the project to go to the project dashboard
    * Setup Google Drive credentials
       * Click on the hamburger menu in the top left of the screen to access the navigation menu
       * On the left hand menu select 'APIs and Services' and then 'Library'
       * Search for Google Drive API
       * Select Google Drive API and click on 'enable' to get to the API and Services Overview page
       * Click on the Create Credentials button near the top left of the screen
       * Select 'Google Drive' API from the dropdown for 'Credential Type'
       * Select the 'Application Data' radio button in the 'What data will you be accessing' area
       * Select the 'No, I'm not using them' for the 'Are you planning to use this API with Compute Engine, Kubernetes Engine, App Engine, or Cloud Functions?' area
       * Cick Next
       * On the Create Service Account page, step 1 is to enter a service account name in the first text box. Any value can be entered here.
       * Click on 'Create and Continue'
       * On step 2, 'Grant this service account access to project', select Basic -> Editor from the 'Select a Role' dropdown.
       * Click on Continue
       * On step 3, 'Grant users access to this service account', simply press Done, no input is necessary
       * On the next page, click on the service account name created (listed under the Service Accounts area) to go to the configuration page for the new service account.
       * Click on the KEYS tab at the top middle of the screen.
       * Click on the Add Key dropdown and select Create New Key.
       * Select the JSON radio button then click Create. The json file with the new API credentials will download your machine.
       * Rename the downloaded file to creds.json. This filename is already listed in the project .gitignore file and so no further action will be needed to prevent it being accidentally uploaded to github
       * Copy the new creds.json file into the local clone
       * In the creds.json file, copy the value for "client email" and then on Google Drive, share the spreadsheet created above with this email address assigning a role of Editor.

    * Enable Google Sheets API
    * Go back to the dashboard for the project on Google Cloud Platform and access the navigation menu as before
    * On the left hand menu select 'APIs and Services' and then 'Library'
    * Search for Google Sheets API
    * Select Google Sheets API and click on 'enable'

* Install gspread and google-auth libraries in the development environment using the command 'pip3 install gspread google-auth'
</details>

***

## Credits
### Code
* Information on how to use Python RegEx came from [this website](https://www.w3schools.com/python/python_regex.asp)
* Code for validating telephone number using RegEx came from [this website](https://stackoverflow.com/questions/16405187/regular-expression-for-uk-mobile-number-python)
* Information on how to create a table in Python came from [this website](https://www.askpython.com/python-modules/tabulate-tables-in-python)
* Information on how to fix the bug on the try except statement came from [this website](https://stackoverflow.com/questions/20057719/how-to-fix-invalid-syntax-error-at-except-valueerror)
* Information on how to clear console came from [this website](https://stackoverflow.com/questions/2084508/clear-terminal-in-python/2084521)
* Information on how to add a pause between functions came from [this website](https://stackoverflow.com/questions/510348/how-do-i-make-a-time-delay)

### Content
* This is the [Google Spreadsheet](https://docs.google.com/spreadsheets/d/1_8mor_TB0ZE-gW2Sxh5LiO3gbOzIasn0HXfoguFOyiQ/edit?usp=sharing) that has been used for this project.

### Acknowledgments
* Tutor support at Code Institute for their help when required.
* My mentor, Brian Macharia, for helping, teaching me various new things and guiding me through this project during the mentor sessions.
