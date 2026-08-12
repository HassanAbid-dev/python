from email.message import EmailMessage
import smtplib
import ssl
import os
from dotenv import load_dotenv

load_dotenv()  # reads .env and loads into environment variables

email_sender = os.getenv("EMAIL_ADDRESS")
app_password = os.getenv("EMAIL_APP_PASSWORD")

email_receiver = "keyejo3178@diarshop.com"

subject = "Test Email from Python"
body = "This is a test email sent from a Python script using the smtplib and email libraries."

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, app_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

