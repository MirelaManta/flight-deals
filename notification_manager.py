from twilio.rest import Client
import smtplib
from dotenv import load_dotenv
import os


load_dotenv()
twilio_account_sid = os.environ["TWILIO_ACCOUNT_SID"]
twilio_auth_token = os.environ["TWILIO_AUTH_TOKEN"]
twilio_phone_number = os.environ["TWILIO_PHONE_NUMBER"]
my_email = os.environ["MY_EMAIL"]
my_password = os.environ["MY_PASSWORD"]
my_phone_num = os.environ["MY_PHONE_NUM"]
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"


class NotificationManager:
    def __init__(self):
        self.client = Client(twilio_account_sid, twilio_auth_token)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=twilio_phone_number,
            to=my_phone_num
        )
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(my_email, my_password)
            for email in emails:
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )

