# python email sender

# requirements: 
# 1. go over to gmail and enable 2FA in your google account
# 2. generate app password in the section below 2FA, or look up Google app passwords, then type in Python and generate a password. Copy what is givem.
# 3. create a function to send the mail

import ssl
import smtplib
from email.message import EmailMessage
from pass1 import Password
# should be pre-installed

# process flow:
# 1. a variable that has the email SENDER, i.e. the email we generated a pwd for
# 2. then we input the email password that we copied
# 3. input the receiver 
# 4. specify subject, body, create an instance and send the email

email_sender = '' # your email id/sender id
email_password = Password
# created a serparate file called pass1, to store the password for security

email_receiver = '' # whoever you want to send the email to

Subject = 'Dont forget to submit your project!'
# just an example

Body = """
We have to submit your data structures project tomorrow!
"""
# just an example can be anyhting

# instance of the email library package we imported

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = Subject
em.set_content(Body)


# creating a context, after importing the necessary libraries at the top
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
