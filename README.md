# Flight Deal Finder

The Flight Deals Notifier is a Python program that uses the Tequila Flight API to search for flight deals from your nearest airport to destinations all over the world. When a flight deal is found that is significantly cheaper than average, the program sends an SMS message and email notification to alert you of the deal.
## Setup
Before running the program, you'll need to set up a few things:
* Tequila Flight API Credentials: To access the Tequila Flight API, you'll need to create an account and get your API credentials.
* Sheety API Credentials: The program uses Sheety to store and manage the list of destinations and their IATA codes. You'll need to create a free account and get your API credentials.
* Twilio API Credentials: To send SMS messages, the program uses Twilio. You'll need to create a free account and get your API credentials.
* Gmail account: To get notify via email.
* Add the necessary environment variables to your system or a .env file:
```
TEQUILA_API_KEY=<your_tequila_api_key>
TWILIO_ACCOUNT_SID=<your_twilio_account_sid>
TWILIO_AUTH_TOKEN=<your_twilio_auth_token>
TWILIO_PHONE_NUMBER=<your_twilio_phone_number>
MY_EMAIL=<your_gmail_email>
MY_PASSWORD=<your_gmail_password>
MY_PHONE_NUM=<your_phone_number>
```
## How to Use
Once you've set up everything, you can run the program with ```python main.py```. The program will search for flight deals from airport of choice to all of the destinations listed in the Sheety spreadsheet. If a deal is found that is significantly cheaper than the value stored in the spreadsheet(the lowest price known), the program will send an SMS message and email notification to alert you of the deal.

You can also deploy this application to run the program automatically on a regular basis (e.g. every day at 9am).
## Files
* __main.py__: The main program file that searches for flight deals and sends notifications.
* __flight_search.py__: A helper module that searches the Tequila Flight API for flight deals.
* __data_manager.py__: A helper module that retrieves and updates the list of destinations and customer emails from the Sheety API.
* __notification_manager.py__: A helper module that sends SMS messages and emails using the Twilio API and SMTP protocol.
* __flight_data.py__: A class that represents flight data, used to store flight information retrieved from the Tequila Flight API.
## Limitations
* The program only searches for non-stop flights from your nearest airport to each destination. 
* The program only searches for flight deals on the current date and the following day. It doesn't search for deals on future dates.
* The program uses the Sheety API to store the list of destinations and their IATA codes. If the API is down or the program can't access it for any reason, the program won't be able to run.
* The program uses the Twilio API to send SMS messages. If you don't have a Twilio account or you run out of Twilio credits, you won't be able to receive SMS messages.
* The program uses the SMTP protocol to send email messages. If you're using a free email service like Gmail, you may need to allow less secure apps in your account settings in order for the program to send emails.
## Credits
This project was created as part of the 100 Days of Code - The Complete Python Pro Bootcamp by Dr. Angela Yu on Udemy.
