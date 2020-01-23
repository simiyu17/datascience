# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 12:26:59 2020

@author: simiyu
"""

import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# data processing
import pandas as pd 


def get_recipients(file_path):
    names = []
    emails = []
    data = pd.read_excel(file_path)
    for index, row in data.iterrows():
        names.append(row['Name'])
        emails.append(row['Email'])
    return names, emails

def parse_template(file_name):
    with open(file_name, 'r', encoding='utf-8') as msg_template:
        msg_template_content = msg_template.read()
    return Template(msg_template_content)

def main():
    names, emails = get_recipients('recipients.xlsx') # read user details
    message_template = parse_template('email_template.txt')
    
    print ("NOTE: To USE any other email server other than Gmail to sent emails go to line 46 and chnge host name and port, \
           but to run the code as is Gmail Only is allowed and Remember to allow Less secure app access on your gmail")
    # Enter Source 
    FROM_EMAIL = str(input("Enter Email(Note: Gmail Only) : "))
    
    # Enter Source 
    MY_PASSWORD = str(input("Enter password : "))

    # set up the SMTP server
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.ehlo()
    smtp_server.starttls()
    smtp_server.login(FROM_EMAIL, MY_PASSWORD)

    # Get each user detail and send the email:
    for name, email in zip(names, emails):
        multipart_msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
        message = message_template.substitute(NAME=name.title())

        # Prints out the message body for our sake
        print(message)

        # setup the parameters of the message
        multipart_msg['From']=FROM_EMAIL
        multipart_msg['To']=email
        multipart_msg['Subject']="Sample Subject"
        
        # add in the message body
        multipart_msg.attach(MIMEText(message, 'plain'))
        
        # send the message via the server set up earlier.
        smtp_server.send_message(multipart_msg)
        del multipart_msg
        
    # Terminate the SMTP session and close the connection
    smtp_server.quit()
    
if __name__ == '__main__':
    main()