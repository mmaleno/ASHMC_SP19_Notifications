#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: spring19helpers.py

Author: Max Maleno [mmaleno@hmc.edu]

Last Updated: 01-19-2019

-Helper functions to be run in spring19main.py
-This file works for gmail (hmc is a gmail account),
but this can be easily modified for any kind of account.
-You probably need to go into the security settings of
your gmail account, detailed here: https://tinyurl.com/yc6ws9aw

References:
https://tinyurl.com/yblgolpb
https://tinyurl.com/ybqohxvk
https://tinyurl.com/ybqgddzx

"""

# libraries to send email with attachment from any smtp email server
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Create MIME object
msg = MIMEMultipart()

# sender credentials. Hopefully im not dumb and push
# this with my real credentials...
gmail_user =  'notMax@mudd.edu'
gmail_password = 'notMaxsPassword'

# email field variables
sent_from = gmail_user
to = ['maxwellmaleno@hotmail.com', 'mmaleno16@gmail.com']
subject = 'Test message 16'
body = 'my 16 try, back to spring19'

# clean up to[] so that we can put it in msg
polished_to = to[0] + ', ' + to[1]

# fields to be fed into email so that receiver gets info displayed properly
msg['From'] = sent_from
msg['To'] = polished_to
msg['Subject'] = subject

# attach body to msg
msg.attach(MIMEText(body, 'plain'))

# open attachment, convert to base 64, then attach to msg
filename = "Example1.pdf"
attachment = open("PDFs/"+filename, "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= " + filename)
msg.attach(part)

# function to send email based on parameters above
def send_email():
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, msg.as_string())
        server.quit()

        print('Email sent!')

    except:  
        print('Something went wrong...')