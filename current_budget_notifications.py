#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: current_budget_notifications.py

Author: Max Maleno [mmaleno@hmc.edu]

Last Updated: 01-20-2019

Emails each president of every Associated Students of Harvey Mudd College (ASHMC) club,
notifying them how much money their club has remaining this school year.

See example.csv for the format of the data.

Audits of each club should be in PDF form, in the "PDFs" directory.

It is crucial that the first (leftmost) column in example.csv in each row
is the same name as the corresponding PDF.

You probably need to go into the security settings of
your gmail account, detailed here: https://tinyurl.com/yc6ws9aw

References:
https://tinyurl.com/yblgolpb
https://tinyurl.com/ybqohxvk
https://tinyurl.com/ybqgddzx
https://tinyurl.com/ybyo26fk

"""

# libraries to send email with attachment from any smtp email server
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import csv

# sender credentials. Hopefully im not dumb enough
# to push this with my real credentials...
# these fields are constant for the entire script
gmail_user =  'notMax@mudd.edu'
gmail_password = 'notMaxsPassword'
sent_from = gmail_user

# all actions are based on data in example.csv
with open('example.csv') as csvfile:

    readCSV = csv.reader(csvfile, delimiter=',')

    # loop through each row, aka each club
    for club in readCSV:

        # Create MIME object to email
        msg = MIMEMultipart()

        # create empty to list, pack the emails into it
        to = []
        to = club[1].split(',')

        # other email fields
        subject = club[2]
        body = club[3]

        # fields to be fed into email so receiver sees info displayed properly
        # see example.csv to reference location of data fields
        msg['From'] = sent_from
        msg['To'] = club[1]
        msg['Subject'] = subject

        # attach body to msg
        msg.attach(MIMEText(body, 'plain'))

        # open PDF attachment, convert to base 64, then attach to msg
        filename = club[0] + ".pdf"
        attachment = open("PDFs/"+filename, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= " + filename)
        msg.attach(part)

        # attempt to send email!
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, msg.as_string())
            server.quit()

            print('SUCCESS: ' + club[0])

        except:  
            print('FAILURE: ' + club[0])
