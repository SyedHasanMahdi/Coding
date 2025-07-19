import smtplib, ssl
import string
import pandas as pd

list = open("C:\Coding\Python-Learning\Projects\Emailer\database.csv")
port = 465  # For SSL


# Create a secure SSL context
context = ssl.create_default_context()
message = "Hello, If u are interested in a tech chanell and would like to watch many up and coming videos and tuorials to help u achieve in the tech sector, Visit my youtube chanell at https://www.youtube.com/channel/UCoYWLYIUadcLAPup1iSIJkQ"

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("tgp619@gmail.com", "Akis.123!")
    # TODO: Send email here
    for email in list:
        reciever_email = []
        reciever_email.append(email)
    server.sendmail(sender_email, receiver_email, message)
